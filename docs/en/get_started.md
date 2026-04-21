# Get Started

## Prerequisites

In this section, we demonstrate how to prepare an environment with PyTorch.

MMDetection3D works on Linux, Windows (experimental support) and macOS. It requires Python 3.10+, CUDA 11.8+, and PyTorch 2.0+.

```{note}
If you are experienced with PyTorch and have already installed it, just skip this part and jump to the [next section](#installation). Otherwise, you can follow these steps for the preparation.
```

**Step 0.** Install [uv](https://docs.astral.sh/uv/) — a fast Python package manager.

```shell
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Step 1.** Create a virtual environment and activate it.

```shell
uv venv --python 3.12
source .venv/bin/activate
```

**Step 2.** Install PyTorch following [official instructions](https://pytorch.org/get-started/locally/), e.g.

On GPU platforms:

```shell
uv pip install torch torchvision --torch-backend=auto
```

On CPU platforms:

```shell
uv pip install --torch-backend=cpu torch torchvision
```

## Installation

We recommend that users follow our best practices to install MMDetection3D. However, the whole process is highly customizable. See [Customize Installation](#customize-installation) section for more information.

### Best Practices

**Step 0.** Install [OneDL-MMEngine](https://github.com/vbti-development/onedl-mmengine), [OneDL-MMCV](https://github.com/vbti-development/onedl-mmcv) and [OneDL-MMDetection](https://github.com/vbti-development/onedl-mmdetection) using [OneDL-MIM](https://github.com/vbti-development/onedl-mim).

```shell
uv pip install onedl-mim
mim install onedl-mmengine
mim install onedl-mmcv --only-binary=onedl-mmcv
mim install 'onedl-mmdetection>=v3.4.0-rc1'
```

**Step 1.** Install MMDetection3D.

Case a: If you develop and run mmdet3d directly, install it from source:

```shell
git clone https://github.com/vbti-development/onedl-mmdetection3d.git
cd onedl-mmdetection3d
uv pip install -e .
```

Case b: If you use mmdet3d as a dependency or third-party package, install it with MIM:

```shell
mim install "onedl-mmdetection3d>=1.1.0"
```

Note:

1. If you would like to use `opencv-python-headless` instead of `opencv-python`,
   you can install it before installing MMCV.

2. Some dependencies are optional. Simply running `uv pip install -e .` will only install the minimum runtime requirements. To use optional dependencies specify desired extras when calling `uv pip` (e.g. `uv pip install -e .[optional]`). Valid keys for the extras field are: `optional`, `mminstall`, and `torch`.

   We have supported `spconv 2.0`. If the user has installed `spconv 2.0`, the code will use `spconv 2.0` first, which will take up less GPU memory than using the default `mmcv spconv`. Users can use the following commands to install `spconv 2.0`:

   ```shell
   pip install cumm-cuxxx
   pip install spconv-cuxxx
   ```

   Where `xxx` is the CUDA version in the environment.

   For example, using CUDA 10.2, the command will be `pip install cumm-cu102 && pip install spconv-cu102`.

   Supported CUDA versions include 10.2, 11.1, 11.3, and 11.4. Users can also install it by building from the source. For more details please refer to [spconv v2.x](https://github.com/traveller59/spconv).

   We also support `Minkowski Engine` as a sparse convolution backend. If necessary please follow original [installation guide](https://github.com/NVIDIA/MinkowskiEngine#installation) or use `pip` to install it:

   ```shell
   conda install openblas-devel -c anaconda
   export CPLUS_INCLUDE_PATH=CPLUS_INCLUDE_PATH:${YOUR_CONDA_ENVS_DIR}/include
   # replace ${YOUR_CONDA_ENVS_DIR} to your anaconda environment path e.g. `/home/username/anaconda3/envs/openmmlab`.
   pip install -U git+https://github.com/NVIDIA/MinkowskiEngine -v --no-deps --install-option="--blas_include_dirs=/opt/conda/include" --install-option="--blas=openblas"
   ```

   We also support `Torchsparse` as a sparse convolution backend. If necessary please follow original [installation guide](https://github.com/mit-han-lab/torchsparse#installation) or use `pip` to install it:

   ```shell
   sudo apt-get install libsparsehash-dev
   pip install --upgrade git+https://github.com/mit-han-lab/torchsparse.git@v1.4.0
   ```

   or omit sudo install by following command:

   ```shell
   conda install -c bioconda sparsehash
   export CPLUS_INCLUDE_PATH=CPLUS_INCLUDE_PATH:${YOUR_CONDA_ENVS_DIR}/include
   # replace ${YOUR_CONDA_ENVS_DIR} to your anaconda environment path e.g. `/home/username/anaconda3/envs/openmmlab`.
   pip install --upgrade git+https://github.com/mit-han-lab/torchsparse.git@v1.4.0
   ```

3. The code can not be built for CPU only environment (where CUDA isn't available) for now.

### Verify the Installation

To verify whether MMDetection3D is installed correctly, we provide some sample codes to run an inference demo.

**Step 1.** We need to download config and checkpoint files.

```shell
mim download onedl-mmdetection3d --config pointpillars_hv_secfpn_8xb6-160e_kitti-3d-car --dest .
```

The downloading will take several seconds or more, depending on your network environment. When it is done, you will find two files `pointpillars_hv_secfpn_8xb6-160e_kitti-3d-car.py` and `hv_pointpillars_secfpn_6x8_160e_kitti-3d-car_20220331_134606-d42d15ed.pth` in your current folder.

**Step 2.** Verify the inference demo.

Case a: If you install MMDetection3D from source, just run the following command.

```shell
python demo/pcd_demo.py demo/data/kitti/000008.bin pointpillars_hv_secfpn_8xb6-160e_kitti-3d-car.py hv_pointpillars_secfpn_6x8_160e_kitti-3d-car_20220331_134606-d42d15ed.pth --show
```

You will see a visualizer interface with point cloud, where bounding boxes are plotted on cars.

**Note**:

If you install MMDetection3D on a remote server without display device, you can leave out the `--show` argument. Demo will still save the predictions to  `outputs/pred/000008.json` file.

**Note**:

If you want to input a `.ply` file, you can use the following function and convert it to `.bin` format. Then you can use the converted `.bin` file to run demo.
Note that you need to install `pandas` and `plyfile` before using this script. This function can also be used for data preprocessing for training `ply data`.

```python
import numpy as np
import pandas as pd
from plyfile import PlyData

def convert_ply(input_path, output_path):
    plydata = PlyData.read(input_path)  # read file
    data = plydata.elements[0].data  # read data
    data_pd = pd.DataFrame(data)  # convert to DataFrame
    data_np = np.zeros(data_pd.shape, dtype=np.float)  # initialize array to store data
    property_names = data[0].dtype.names  # read names of properties
    for i, name in enumerate(
            property_names):  # read data by property
        data_np[:, i] = data_pd[name]
    data_np.astype(np.float32).tofile(output_path)
```

Examples:

```python
convert_ply('./test.ply', './test.bin')
```

If you have point clouds in other format (`.off`, `.obj`, etc.), you can use `trimesh` to convert them into `.ply`.

```python
import trimesh

def to_ply(input_path, output_path, original_type):
    mesh = trimesh.load(input_path, file_type=original_type)  # read file
    mesh.export(output_path, file_type='ply')  # convert to ply
```

Examples:

```python
to_ply('./test.obj', './test.ply', 'obj')
```

Case b: If you install MMDetection3D with MIM, open your python interpreter and copy&paste the following codes.

```python
from mmdet3d.apis import init_model, inference_detector

config_file = 'pointpillars_hv_secfpn_8xb6-160e_kitti-3d-car.py'
checkpoint_file = 'hv_pointpillars_secfpn_6x8_160e_kitti-3d-car_20220331_134606-d42d15ed.pth'
model = init_model(config_file, checkpoint_file)
inference_detector(model, 'demo/data/kitti/000008.bin')
```

You will see a list of `Det3DDataSample`, and the predictions are in the `pred_instances_3d`, indicating the detected bounding boxes, labels, and scores.

### Customize Installation

#### CUDA Versions

When installing PyTorch, you need to specify the version of CUDA. If you are not clear on which to choose, follow our recommendations:

- For Ampere-based NVIDIA GPUs, such as GeForce 30 series and NVIDIA A100, CUDA 11 is a must.
- For older NVIDIA GPUs, CUDA 11 is backward compatible, but CUDA 10.2 offers better compatibility and is more lightweight.

Please make sure the GPU driver satisfies the minimum version requirements. See [this table](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#cuda-major-component-versions__table-cuda-toolkit-driver-versions) for more information.

```{note}
Installing CUDA runtime libraries is enough if you follow our best practices, because no CUDA code will be compiled locally. However if you hope to compile MMCV from source or develop other CUDA operators, you need to install the complete CUDA toolkit from NVIDIA's [website](https://developer.nvidia.com/cuda-downloads), and its version should match the CUDA version of PyTorch. i.e., the specified version of cudatoolkit in `conda install` command.
```

#### Install OneDL-MMEngine without MIM

To install OneDL-MMEngine with pip instead of MIM, you can use:

```shell
uv pip install onedl-mmengine
```

#### Install OneDL-MMCV without MIM

OneDL-MMCV provides pre-built wheels. We strongly recommend using MIM which handles CUDA/PyTorch version matching automatically:

```shell
mim install onedl-mmcv --only-binary=onedl-mmcv
```

Alternatively, wheels are available from our mmwheels index. For example, for PyTorch 2.10 and CUDA 12.4:

```shell
uv pip install onedl-mmcv -f https://vbti-development.github.io/mmwheels/
```

#### Install on Google Colab

[Google Colab](https://colab.research.google.com/) usually has PyTorch installed, thus we only need to install MMEngine, MMCV, MMDetection, and MMDetection3D with the following commands.

**Step 1.** Install [OneDL-MMEngine](https://github.com/vbti-development/onedl-mmengine), [OneDL-MMCV](https://github.com/vbti-development/onedl-mmcv) and [OneDL-MMDetection](https://github.com/vbti-development/onedl-mmdetection) using [OneDL-MIM](https://github.com/vbti-development/onedl-mim).

```shell
!pip3 install onedl-mim
!mim install onedl-mmengine
!mim install onedl-mmcv --only-binary=onedl-mmcv
!mim install "onedl-mmdetection>=v3.4.0-rc1"
```

**Step 2.** Install MMDetection3D from source.

```shell
!git clone https://github.com/VBTI-development/onedl-mmdetection3d.git -b dev-1.x
%cd mmdetection3d
!pip install -e .
```

**Step 3.** Verification.

```python
import mmdet3d
print(mmdet3d.__version__)
# Example output: 1.1.0, or an another version.
```

```{note}
Within Jupyter, the exclamation mark `!` is used to call external executables and `%cd` is a [magic command](https://ipython.readthedocs.io/en/stable/interactive/magics.html#magic-cd) to change the current working directory of Python.
```

#### Using MMDetection3D with Docker

We provide a [Dockerfile](https://github.com/VBTI-development/onedl-mmdetection3d/blob/main/docker/Dockerfile) to build an image. Ensure that your [docker version](https://docs.docker.com/engine/install/) >= 19.03.

```shell
# build an image with PyTorch 1.9, CUDA 11.1
# If you prefer other versions, just modified the Dockerfile
docker build -t mmdetection3d docker/
```

Run it with:

```shell
docker run --gpus all --shm-size=8g -it -v {DATA_DIR}:/mmdetection3d/data mmdetection3d
```

### Troubleshooting

If you have some issues during the installation, please first view the [FAQ](notes/faq.md) page.
You may [open an issue](https://github.com/VBTI-development/onedl-mmdetection3d/issues/new/choose) on GitHub if no solution is found.

### Use Multiple Versions of MMDetection3D in Development

Training and testing scripts have already been modified in `PYTHONPATH` in order to make sure the scripts are using their own versions of MMDetection3D.

To install the default version of MMDetection3D in your environment, you can exclude the following code in the related scripts:

```shell
PYTHONPATH="$(dirname $0)/..":$PYTHONPATH
```
