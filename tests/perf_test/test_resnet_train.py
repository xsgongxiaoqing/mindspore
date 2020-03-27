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

"""Resnet test."""

import numpy as np

from mindspore.common.api import _executor
import mindspore.context as context
from mindspore import Tensor
from ..train_step_wrap import train_step_with_loss_warp
from .resnet_example import resnet50
context.set_context(mode=context.GRAPH_MODE)

def test_train_step():
    net = train_step_with_loss_warp(resnet50())
    net.set_train()
    inp = Tensor(np.ones([1, 3, 224, 224], np.float32))
    label = Tensor(np.zeros([1, 10], np.float32))
    _executor.compile(net, inp, label)
