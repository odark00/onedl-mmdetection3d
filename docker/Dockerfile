ARG CU_VERSION="129"
ARG TORCH_VERSION="2100"
ARG ONEDL_MMDET_VERSION="latest"

FROM vbti/onedl-mmdetection-cu${CU_VERSION}-torch${TORCH_VERSION}:${ONEDL_MMDET_VERSION}

# Install OneDL-MMDetection3D
COPY . /onedl/onedl-mmdetection3d

WORKDIR /onedl/onedl-mmdetection3d
RUN mim install --no-cache-dir -e .[optional] \
    && python -m compileall -q /onedl/onedl-mmdetection3d

# Verify installation
RUN python -c "import mmdet3d; print('mmdet3d version:', mmdet3d.__version__)"
