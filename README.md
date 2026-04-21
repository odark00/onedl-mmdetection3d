<div align="center">

<picture>
    <!-- User prefers dark mode: -->
  <source srcset="https://raw.githubusercontent.com/vbti-development/onedl-mmdetection3d/main/docs/en/_static/image/onedl-mmdetection3d-banner_dark.png"  media="(prefers-color-scheme: dark)"/>

<img src="https://raw.githubusercontent.com/vbti-development/onedl-mmdetection3d/main/docs/en/_static/image/onedl-mmdetection3d-banner.png" alt="OneDL-MMDetection3D logo" height="200"/>
  </picture>

<div>&nbsp;</div>
  <div align="center">
    <a href="https://vbti.nl">
      <b><font size="5">VBTI Website</font></b>
    </a>
    &nbsp;&nbsp;&nbsp;&nbsp;
    <a href="https://onedl.ai">
      <b><font size="5">OneDL platform</font></b>
    </a>
  </div>
<div>&nbsp;</div>

[VBTI Website](https://vbti.nl/)
[OneDL platform](https://onedl.ai/)

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/onedl-mmdetection3d)](https://pypi.org/project/onedl-mmdetection3d/)
[![PyPI](https://img.shields.io/pypi/v/onedl-mmdetection3d)](https://pypi.org/project/onedl-mmdetection3d)
[![docs](https://img.shields.io/badge/docs-latest-blue)](https://onedl-mmdetection3d.readthedocs.io/en/latest/)
[![Build Status](https://github.com/VBTI-development/onedl-mmdetection3d/actions/workflows/merge_stage_test.yml/badge.svg)](https://github.com/VBTI-development/onedl-mmdetection3d/actions)
[![license](https://img.shields.io/github/license/VBTI-development/onedl-mmdetection3d.svg)](https://github.com/VBTI-development/onedl-mmdetection3d/blob/main/LICENSE)
[![open issues](https://isitmaintained.com/badge/open/VBTI-development/onedl-mmdetection3d.svg)](https://github.com/VBTI-development/onedl-mmdetection3d/issues)
[![issue resolution](https://isitmaintained.com/badge/resolution/VBTI-development/onedl-mmdetection3d.svg)](https://github.com/VBTI-development/onedl-mmdetection3d/issues)

[📘Documentation](https://onedl-mmdetection3d.readthedocs.io/en/latest/) |
[🛠️Installation](https://onedl-mmdetection3d.readthedocs.io/en/latest/get_started.html) |
[👀Model Zoo](https://onedl-mmdetection3d.readthedocs.io/en/latest/model_zoo.html) |
[🆕Update News](https://onedl-mmdetection3d.readthedocs.io/en/latest/notes/changelog.html) |
[🚀Ongoing Projects](https://github.com/VBTI-development/onedl-mmdetection3d/projects) |
[🤔Reporting Issues](https://github.com/VBTI-development/onedl-mmdetection3d/issues/new/choose)

[Discord](https://discord.gg/8DvcVRs5Pm)

</div>

## Introduction

MMDetection3D is an open source object detection toolbox based on PyTorch, towards the next-generation platform for general 3D detection. This is the OneDL fork maintained by the [VBTI](https://vbti.nl/) development team, reviving MMLabs code to work with newer PyTorch versions and fixing bugs.

The main branch works with **PyTorch 2.0+**.

![demo image](resources/mmdet3d_outdoor_demo.gif)

<details open>
<summary>Major features</summary>

- **Support multi-modality/single-modality detectors out of box**

  It directly supports multi-modality/single-modality detectors including MVXNet, VoteNet, PointPillars, etc.

- **Support indoor/outdoor 3D detection out of box**

  It directly supports popular indoor and outdoor 3D detection datasets, including ScanNet, SUNRGB-D, Waymo, nuScenes, Lyft, and KITTI. For nuScenes dataset, we also support [nuImages dataset](https://github.com/open-mmlab/mmdetection3d/tree/main/configs/nuimages).

- **Natural integration with 2D detection**

  All the about **300+ models, methods of 40+ papers**, and modules supported in [MMDetection](https://github.com/open-mmlab/mmdetection/blob/3.x/docs/en/model_zoo.md) can be trained or used in this codebase.

- **High efficiency**

  It trains faster than other codebases. The main results are as below. Details can be found in [benchmark.md](./docs/en/notes/benchmarks.md). We compare the number of samples trained per second (the higher, the better). The models that are not supported by other codebases are marked by `✗`.

  |       Methods       | MMDetection3D | [OpenPCDet](https://github.com/open-mmlab/OpenPCDet) | [votenet](https://github.com/facebookresearch/votenet) | [Det3D](https://github.com/poodarchu/Det3D) |
  | :-----------------: | :-----------: | :--------------------------------------------------: | :----------------------------------------------------: | :-----------------------------------------: |
  |       VoteNet       |      358      |                          ✗                           |                           77                           |                      ✗                      |
  |  PointPillars-car   |      141      |                          ✗                           |                           ✗                            |                     140                     |
  | PointPillars-3class |      107      |                          44                          |                           ✗                            |                      ✗                      |
  |       SECOND        |      40       |                          30                          |                           ✗                            |                      ✗                      |
  |       Part-A2       |      17       |                          14                          |                           ✗                            |                      ✗                      |

</details>

Like [OneDL-MMDetection](https://github.com/vbti-development/onedl-mmdetection) and [OneDL-MMCV](https://github.com/vbti-development/onedl-mmcv), MMDetection3D can also be used as a library to support different projects on top of it.

## What's New

### Highlight

In version 1.4, MMDetecion3D refactors the Waymo dataset and accelerates the preprocessing, training/testing setup, and evaluation of Waymo dataset. We also extends the support for camera-based, such as Monocular and BEV, 3D object detection models on Waymo. A detailed description of the Waymo data information is provided [here](https://mmdetection3d.readthedocs.io/en/latest/advanced_guides/datasets/waymo.html).

Besides, in version 1.4, MMDetection3D provides [Waymo-mini](https://mmassets.onedl.ai/mmdetection3d/data/waymo_mmdet3d_after_1x4/waymo_mini.tar.gz) to help community users get started with Waymo and use it for quick iterative development.

**v1.5.0** was released in 17/4/2026:

- Update to join OneDL ecosystem.
- Support python 3.12 and torch 2.10.
- Removed lyft-dataset-sdk and nuscene-devkit dependencies (for now) because of incompatibilities.

**v1.4.0** was released in 8/1/2024：

- Support the training of [DSVT](<(https://arxiv.org/abs/2301.06051)>) in `projects`
- Support [Nerf-Det](https://arxiv.org/abs/2307.14620) in `projects`
- Refactor Waymo dataset

**v1.3.0** was released in 18/10/2023:

- Support [CENet](https://arxiv.org/abs/2207.12691) in `projects`
- Enhance demos with new 3D inferencers

**v1.2.0** was released in 4/7/2023

- Support [New Config Type](https://mmengine.readthedocs.io/en/latest/advanced_tutorials/config.html#a-pure-python-style-configuration-file-beta) in `mmdet3d/configs`
- Support the inference of [DSVT](<(https://arxiv.org/abs/2301.06051)>) in `projects`
- Support downloading datasets from [OpenDataLab](https://opendatalab.com/) using `mim`

**v1.1.1** was released in 30/5/2023:

- Support [TPVFormer](https://arxiv.org/pdf/2302.07817.pdf) in `projects`
- Support the training of BEVFusion in `projects`
- Support lidar-based 3D semantic segmentation benchmark

## Installation

Please refer to [Installation](https://onedl-mmdetection3d.readthedocs.io/en/latest/get_started.html) for installation instructions.

## Getting Started

For detailed user guides and advanced guides, please refer to our [documentation](https://onedl-mmdetection3d.readthedocs.io/en/latest/):

<details>
<summary>User Guides</summary>

- [Train & Test](https://onedl-mmdetection3d.readthedocs.io/en/latest/user_guides/index.html#train-test)
  - [Learn about Configs](https://onedl-mmdetection3d.readthedocs.io/en/latest/user_guides/config.html)
  - [Coordinate System](https://onedl-mmdetection3d.readthedocs.io/en/latest/user_guides/coord_sys_tutorial.html)
  - [Dataset Preparation](https://onedl-mmdetection3d.readthedocs.io/en/latest/user_guides/dataset_prepare.html)
  - [Customize Data Pipelines](https://onedl-mmdetection3d.readthedocs.io/en/latest/user_guides/data_pipeline.html)
  - [Test and Train on Standard Datasets](https://onedl-mmdetection3d.readthedocs.io/en/latest/user_guides/train_test.html)
  - [Inference](https://onedl-mmdetection3d.readthedocs.io/en/latest/user_guides/inference.html)
  - [Train with Customized Datasets](https://onedl-mmdetection3d.readthedocs.io/en/latest/user_guides/new_data_model.html)
- [Useful Tools](https://onedl-mmdetection3d.readthedocs.io/en/latest/user_guides/index.html#useful-tools)

</details>

<details>
<summary>Advanced Guides</summary>

- [Datasets](https://onedl-mmdetection3d.readthedocs.io/en/latest/advanced_guides/index.html#datasets)
  - [KITTI Dataset](https://onedl-mmdetection3d.readthedocs.io/en/latest/advanced_guides/datasets/kitti.html)
  - [NuScenes Dataset](https://onedl-mmdetection3d.readthedocs.io/en/latest/advanced_guides/datasets/nuscenes.html)
  - [Lyft Dataset](https://onedl-mmdetection3d.readthedocs.io/en/latest/advanced_guides/datasets/lyft.html)
  - [Waymo Dataset](https://onedl-mmdetection3d.readthedocs.io/en/latest/advanced_guides/datasets/waymo.html)
  - [SUN RGB-D Dataset](https://onedl-mmdetection3d.readthedocs.io/en/latest/advanced_guides/datasets/sunrgbd.html)
  - [ScanNet Dataset](https://onedl-mmdetection3d.readthedocs.io/en/latest/advanced_guides/datasets/scannet.html)
  - [S3DIS Dataset](https://onedl-mmdetection3d.readthedocs.io/en/latest/advanced_guides/datasets/s3dis.html)
  - [SemanticKITTI Dataset](https://onedl-mmdetection3d.readthedocs.io/en/latest/advanced_guides/datasets/semantickitti.html)
- [Supported Tasks](https://onedl-mmdetection3d.readthedocs.io/en/latest/advanced_guides/index.html#supported-tasks)
  - [LiDAR-Based 3D Detection](https://onedl-mmdetection3d.readthedocs.io/en/latest/advanced_guides/supported_tasks/lidar_det3d.html)
  - [Vision-Based 3D Detection](https://onedl-mmdetection3d.readthedocs.io/en/latest/advanced_guides/supported_tasks/vision_det3d.html)
  - [LiDAR-Based 3D Semantic Segmentation](https://onedl-mmdetection3d.readthedocs.io/en/latest/advanced_guides/supported_tasks/lidar_sem_seg3d.html)
- [Customization](https://onedl-mmdetection3d.readthedocs.io/en/latest/advanced_guides/index.html#customization)
  - [Customize Datasets](https://onedl-mmdetection3d.readthedocs.io/en/latest/advanced_guides/customize_dataset.html)
  - [Customize Models](https://onedl-mmdetection3d.readthedocs.io/en/latest/advanced_guides/customize_models.html)
  - [Customize Runtime Settings](https://onedl-mmdetection3d.readthedocs.io/en/latest/advanced_guides/customize_runtime.html)

</details>

## Overview of Benchmark and Model Zoo

Results and models are available in the [model zoo](docs/en/model_zoo.md).

<div align="center">
  <b>Components</b>
</div>
<table align="center">
  <tbody>
    <tr align="center" valign="bottom">
      <td>
        <b>Backbones</b>
      </td>
      <td>
        <b>Heads</b>
      </td>
      <td>
        <b>Features</b>
      </td>
    </tr>
    <tr valign="top">
      <td>
      <ul>
        <li><a href="configs/pointnet2">PointNet (CVPR'2017)</a></li>
        <li><a href="configs/pointnet2">PointNet++ (NeurIPS'2017)</a></li>
        <li><a href="configs/regnet">RegNet (CVPR'2020)</a></li>
        <li><a href="configs/dgcnn">DGCNN (TOG'2019)</a></li>
        <li>DLA (CVPR'2018)</li>
        <li>MinkResNet (CVPR'2019)</li>
        <li><a href="configs/minkunet">MinkUNet (CVPR'2019)</a></li>
        <li><a href="configs/cylinder3d">Cylinder3D (CVPR'2021)</a></li>
      </ul>
      </td>
      <td>
      <ul>
        <li><a href="configs/free_anchor">FreeAnchor (NeurIPS'2019)</a></li>
      </ul>
      </td>
      <td>
      <ul>
        <li><a href="configs/dynamic_voxelization">Dynamic Voxelization (CoRL'2019)</a></li>
      </ul>
      </td>
    </tr>
</td>
    </tr>
  </tbody>
</table>

<div align="center">
  <b>Architectures</b>
</div>
<table align="center">
  <tbody>
    <tr align="center" valign="middle">
      <td>
        <b>LiDAR-based 3D Object Detection</b>
      </td>
      <td>
        <b>Camera-based 3D Object Detection</b>
      </td>
      <td>
        <b>Multi-modal 3D Object Detection</b>
      </td>
      <td>
        <b>3D Semantic Segmentation</b>
      </td>
    </tr>
    <tr valign="top">
      <td>
        <li><b>Outdoor</b></li>
        <ul>
            <li><a href="configs/second">SECOND (Sensor'2018)</a></li>
            <li><a href="configs/pointpillars">PointPillars (CVPR'2019)</a></li>
            <li><a href="configs/ssn">SSN (ECCV'2020)</a></li>
            <li><a href="configs/3dssd">3DSSD (CVPR'2020)</a></li>
            <li><a href="configs/sassd">SA-SSD (CVPR'2020)</a></li>
            <li><a href="configs/point_rcnn">PointRCNN (CVPR'2019)</a></li>
            <li><a href="configs/parta2">Part-A2 (TPAMI'2020)</a></li>
            <li><a href="configs/centerpoint">CenterPoint (CVPR'2021)</a></li>
            <li><a href="configs/pv_rcnn">PV-RCNN (CVPR'2020)</a></li>
            <li><a href="projects/CenterFormer">CenterFormer (ECCV'2022)</a></li>
        </ul>
        <li><b>Indoor</b></li>
        <ul>
            <li><a href="configs/votenet">VoteNet (ICCV'2019)</a></li>
            <li><a href="configs/h3dnet">H3DNet (ECCV'2020)</a></li>
            <li><a href="configs/groupfree3d">Group-Free-3D (ICCV'2021)</a></li>
            <li><a href="configs/fcaf3d">FCAF3D (ECCV'2022)</a></li>
            <li><a href="projects/TR3D">TR3D (ArXiv'2023)</a></li>
      </ul>
      </td>
      <td>
        <li><b>Outdoor</b></li>
        <ul>
          <li><a href="configs/imvoxelnet">ImVoxelNet (WACV'2022)</a></li>
          <li><a href="configs/smoke">SMOKE (CVPRW'2020)</a></li>
          <li><a href="configs/fcos3d">FCOS3D (ICCVW'2021)</a></li>
          <li><a href="configs/pgd">PGD (CoRL'2021)</a></li>
          <li><a href="configs/monoflex">MonoFlex (CVPR'2021)</a></li>
          <li><a href="projects/DETR3D">DETR3D (CoRL'2021)</a></li>
          <li><a href="projects/PETR">PETR (ECCV'2022)</a></li>
        </ul>
        <li><b>Indoor</b></li>
        <ul>
          <li><a href="configs/imvoxelnet">ImVoxelNet (WACV'2022)</a></li>
        </ul>
      </td>
      <td>
        <li><b>Outdoor</b></li>
        <ul>
          <li><a href="configs/mvxnet">MVXNet (ICRA'2019)</a></li>
          <li><a href="projects/BEVFusion">BEVFusion (ICRA'2023)</a></li>
        </ul>
        <li><b>Indoor</b></li>
        <ul>
          <li><a href="configs/imvotenet">ImVoteNet (CVPR'2020)</a></li>
        </ul>
      </td>
      <td>
        <li><b>Outdoor</b></li>
        <ul>
          <li><a href="configs/minkunet">MinkUNet (CVPR'2019)</a></li>
          <li><a href="configs/spvcnn">SPVCNN (ECCV'2020)</a></li>
          <li><a href="configs/cylinder3d">Cylinder3D (CVPR'2021)</a></li>
          <li><a href="projects/TPVFormer">TPVFormer (CVPR'2023)</a></li>
        </ul>
        <li><b>Indoor</b></li>
        <ul>
          <li><a href="configs/pointnet2">PointNet++ (NeurIPS'2017)</a></li>
          <li><a href="configs/paconv">PAConv (CVPR'2021)</a></li>
          <li><a href="configs/dgcnn">DGCNN (TOG'2019)</a></li>
        </ul>
      </ul>
      </td>
    </tr>
</td>
    </tr>
  </tbody>
</table>

|               | ResNet | VoVNet | Swin-T | PointNet++ | SECOND | DGCNN | RegNetX | DLA | MinkResNet | Cylinder3D | MinkUNet |
| :-----------: | :----: | :----: | :----: | :--------: | :----: | :---: | :-----: | :-: | :--------: | :--------: | :------: |
|    SECOND     |   ✗    |   ✗    |   ✗    |     ✗      |   ✓    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
| PointPillars  |   ✗    |   ✗    |   ✗    |     ✗      |   ✓    |   ✗   |    ✓    |  ✗  |     ✗      |     ✗      |    ✗     |
|  FreeAnchor   |   ✗    |   ✗    |   ✗    |     ✗      |   ✗    |   ✗   |    ✓    |  ✗  |     ✗      |     ✗      |    ✗     |
|    VoteNet    |   ✗    |   ✗    |   ✗    |     ✓      |   ✗    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
|    H3DNet     |   ✗    |   ✗    |   ✗    |     ✓      |   ✗    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
|     3DSSD     |   ✗    |   ✗    |   ✗    |     ✓      |   ✗    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
|    Part-A2    |   ✗    |   ✗    |   ✗    |     ✗      |   ✓    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
|    MVXNet     |   ✓    |   ✗    |   ✗    |     ✗      |   ✓    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
|  CenterPoint  |   ✗    |   ✗    |   ✗    |     ✗      |   ✓    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
|      SSN      |   ✗    |   ✗    |   ✗    |     ✗      |   ✗    |   ✗   |    ✓    |  ✗  |     ✗      |     ✗      |    ✗     |
|   ImVoteNet   |   ✓    |   ✗    |   ✗    |     ✓      |   ✗    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
|    FCOS3D     |   ✓    |   ✗    |   ✗    |     ✗      |   ✗    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
|  PointNet++   |   ✗    |   ✗    |   ✗    |     ✓      |   ✗    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
| Group-Free-3D |   ✗    |   ✗    |   ✗    |     ✓      |   ✗    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
|  ImVoxelNet   |   ✓    |   ✗    |   ✗    |     ✗      |   ✗    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
|    PAConv     |   ✗    |   ✗    |   ✗    |     ✓      |   ✗    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
|     DGCNN     |   ✗    |   ✗    |   ✗    |     ✗      |   ✗    |   ✓   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
|     SMOKE     |   ✗    |   ✗    |   ✗    |     ✗      |   ✗    |   ✗   |    ✗    |  ✓  |     ✗      |     ✗      |    ✗     |
|      PGD      |   ✓    |   ✗    |   ✗    |     ✗      |   ✗    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
|   MonoFlex    |   ✗    |   ✗    |   ✗    |     ✗      |   ✗    |   ✗   |    ✗    |  ✓  |     ✗      |     ✗      |    ✗     |
|    SA-SSD     |   ✗    |   ✗    |   ✗    |     ✗      |   ✓    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
|    FCAF3D     |   ✗    |   ✗    |   ✗    |     ✗      |   ✗    |   ✗   |    ✗    |  ✗  |     ✓      |     ✗      |    ✗     |
|    PV-RCNN    |   ✗    |   ✗    |   ✗    |     ✗      |   ✓    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
|  Cylinder3D   |   ✗    |   ✗    |   ✗    |     ✗      |   ✗    |   ✗   |    ✗    |  ✗  |     ✗      |     ✓      |    ✗     |
|   MinkUNet    |   ✗    |   ✗    |   ✗    |     ✗      |   ✗    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✓     |
|    SPVCNN     |   ✗    |   ✗    |   ✗    |     ✗      |   ✗    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✓     |
|   BEVFusion   |   ✗    |   ✗    |   ✓    |     ✗      |   ✓    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
| CenterFormer  |   ✗    |   ✗    |   ✗    |     ✗      |   ✓    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
|     TR3D      |   ✗    |   ✗    |   ✗    |     ✗      |   ✗    |   ✗   |    ✗    |  ✗  |     ✓      |     ✗      |    ✗     |
|    DETR3D     |   ✓    |   ✓    |   ✗    |     ✗      |   ✗    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
|     PETR      |   ✗    |   ✓    |   ✗    |     ✗      |   ✗    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |
|   TPVFormer   |   ✓    |   ✗    |   ✗    |     ✗      |   ✗    |   ✗   |    ✗    |  ✗  |     ✗      |     ✗      |    ✗     |

**Note:** All the about **500+ models, methods of 90+ papers** in 2D detection supported by [MMDetection](https://github.com/open-mmlab/mmdetection/blob/3.x/docs/en/model_zoo.md) can be trained or used in this codebase.

## FAQ

Please refer to [FAQ](docs/en/notes/faq.md) for frequently asked questions.

## Contributing

We appreciate all contributions to improve MMDetection3D. Please refer to [CONTRIBUTING.md](.github/CONTRIBUTING.md) for the contributing guideline.

## Acknowledgement

MMDetection3D is an open source project that is contributed by researchers and engineers from various colleges and companies. We appreciate all the contributors as well as users who give valuable feedbacks. We wish that the toolbox and benchmark could serve the growing research community by providing a flexible toolkit to reimplement existing methods and develop their own new 3D detectors.

The VBTI development team is reviving MMLabs code, making it work with newer PyTorch versions and fixing bugs. We are only a small team, so your help is appreciated.

## Citation

If you find this project useful in your research, please consider cite:

```latex
@misc{mmdet3d2020,
    title={{OneDL-MMDetection3D: OneDL Lab} next-generation platform for general {3D} object detection},
    author={OneDL-MMDetection3D Contributors},
    howpublished = {\url{https://github.com/vbti-development/onedl-mmdetection3d}},
    year={2026}
}
```

## License

This project is released under the [Apache 2.0 license](LICENSE).

## Projects in VBTI-development

- [OneDL-MMEngine](https://github.com/vbti-development/onedl-mmengine): Foundational library for training deep learning models.
- [OneDL-MMCV](https://github.com/vbti-development/onedl-mmcv): Foundational library for computer vision.
- [OneDL-MMPreTrain](https://github.com/vbti-development/onedl-mmpretrain): Pre-training toolbox and benchmark.
- [OneDL-MMDetection](https://github.com/vbti-development/onedl-mmdetection): Detection toolbox and benchmark.
- [OneDL-MMDetection3D](https://github.com/vbti-development/onedl-mmdetection3d): 3D Object Detection toolbox and benchmark.
- [OneDL-MMRotate](https://github.com/vbti-development/onedl-mmrotate): Rotated object detection toolbox and benchmark.
- [OneDL-MMSegmentation](https://github.com/vbti-development/onedl-mmsegmentation): Semantic segmentation toolbox and benchmark.
- [OneDL-MMDeploy](https://github.com/vbti-development/onedl-mmdeploy): Model deployment framework.
- [OneDL-MIM](https://github.com/vbti-development/onedl-mim): MIM installs VBTI packages.
