# Copyright (c) OpenMMLab. All rights reserved.
# flake8: noqa: F405
from mmengine import read_base

with read_base():
    from .._base_.datasets.semantickitti import *  # noqa: F403
    from .._base_.default_runtime import *  # noqa: F403
    from .._base_.models.cylinder3d import *  # noqa: F403
    from .._base_.schedules.schedule_3x import *  # noqa: F403

from mmcv.transforms.wrappers import RandomChoice

from mmdet3d.datasets.transforms.transforms_3d import LaserMix, PolarMix

train_pipeline = [
    dict(
        type=LoadPointsFromFile,
        coord_type='LIDAR',
        load_dim=4,  # noqa: F405, E501
        use_dim=4),
    dict(
        type=LoadAnnotations3D,  # noqa: F405
        with_bbox_3d=False,
        with_label_3d=False,
        with_seg_3d=True,
        seg_3d_dtype='np.int32',
        seg_offset=2**16,
        dataset_type='semantickitti'),
    dict(type=PointSegClassMapping),  # noqa: F405
    dict(
        type=RandomChoice,  # noqa: F405
        transforms=[
            [
                dict(
                    type=LaserMix,  # noqa: F405
                    num_areas=[3, 4, 5, 6],
                    pitch_angles=[-25, 3],
                    pre_transform=[
                        dict(
                            type=LoadPointsFromFile,  # noqa: F405
                            coord_type='LIDAR',
                            load_dim=4,
                            use_dim=4),
                        dict(
                            type=LoadAnnotations3D,  # noqa: F405
                            with_bbox_3d=False,
                            with_label_3d=False,
                            with_seg_3d=True,
                            seg_3d_dtype='np.int32',
                            seg_offset=2**16,
                            dataset_type='semantickitti'),
                        dict(type=PointSegClassMapping)  # noqa: F405
                    ],
                    prob=1)
            ],
            [
                dict(
                    type=PolarMix,  # noqa: F405
                    instance_classes=[0, 1, 2, 3, 4, 5, 6, 7],
                    swap_ratio=0.5,
                    rotate_paste_ratio=1.0,
                    pre_transform=[
                        dict(
                            type=LoadPointsFromFile,  # noqa: F405
                            coord_type='LIDAR',
                            load_dim=4,
                            use_dim=4),
                        dict(
                            type=LoadAnnotations3D,  # noqa: F405
                            with_bbox_3d=False,
                            with_label_3d=False,
                            with_seg_3d=True,
                            seg_3d_dtype='np.int32',
                            seg_offset=2**16,
                            dataset_type='semantickitti'),
                        dict(type=PointSegClassMapping)  # noqa: F405
                    ],
                    prob=1)
            ],
        ],
        prob=[0.5, 0.5]),
    dict(
        type=GlobalRotScaleTrans,  # noqa: F405
        rot_range=[0., 6.28318531],
        scale_ratio_range=[0.95, 1.05],
        translation_std=[0, 0, 0],
    ),
    dict(type=Pack3DDetInputs, keys=['points',
                                     'pts_semantic_mask'])  # noqa: F405
]

train_dataloader.update(  # noqa: F405
    dict(dataset=dict(pipeline=train_pipeline)))  # noqa: F405

default_hooks.update(  # noqa: F405
    dict(checkpoint=dict(type=CheckpointHook, interval=1)))  # noqa: F405
