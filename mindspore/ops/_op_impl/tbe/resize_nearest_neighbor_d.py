# Copyright 2020 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================

"""ResizeNearestNeighbor op"""
from mindspore.ops.op_info_register import op_info_register


@op_info_register("""{
    "op_name": "ResizeNearestNeighbor",
    "imply_type": "TBE",
    "fusion_type": "OPAQUE",
    "async_flag": false,
    "binfile_name": "resize_nearest_neighbor_d.so",
    "compute_cost": 10,
    "kernel_name": "resize_nearest_neighbor_d",
    "partial_flag": true,
    "attr": [
        {
            "name": "size",
            "param_type": "required",
            "type": "listInt",
            "value": "all"
        },
        {
            "name": "align_corners",
            "param_type": "optional",
            "type": "bool",
            "value": "all"
        }
    ],
    "inputs": [
        {
            "index": 0,
            "dtype": [
                "float16","float","int32","int8","uint8"
            ],
            "format": [
                "NC1HWC0","NC1HWC0","NC1HWC0","NC1HWC0","NC1HWC0"
            ],
            "name": "images",
            "need_compile": false,
            "param_type": "required",
            "shape": "all"
        }
    ],
    "outputs": [
        {
            "index": 0,
            "dtype": [
                "float16","float","int32","int8","uint8"
            ],
            "format": [
                "NC1HWC0","NC1HWC0","NC1HWC0","NC1HWC0","NC1HWC0"
            ],
            "name": "y",
            "need_compile": true,
            "param_type": "required",
            "shape": "all"
        }
    ]
}""")
def _resize_nearest_neighbor_d_tbe():
    """ResizeNearestNeighbor TBE register"""
    return
