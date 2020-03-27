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
from mindspore import Tensor
from mindspore.ops import operations as P
import mindspore.nn as nn
from mindspore.common.api import ms_function
import numpy as np
import mindspore.context as context
from mindspore.common.initializer import initializer
from mindspore.common.parameter import Parameter

class Net(nn.Cell):
    def __init__(self):
        super(Net, self).__init__()
        self.add = P.TensorAdd()

    def construct(self, x, y):
        return self.add(x, y)

x = np.random.randn(1,3,3,4).astype(np.float32)
y = np.random.randn(1,3,3,4).astype(np.float32)


def test_net():
    context.set_context(mode=context.GRAPH_MODE, device_target="Ascend")
    add = Net()
    output = add(Tensor(x), Tensor(y))
    print(x)
    print(y)
    print(output.asnumpy())

    context.set_context(mode=context.PYNATIVE_MODE, device_target="Ascend")
    add = Net()
    output = add(Tensor(x), Tensor(y))
    print(x)
    print(y)
    print(output.asnumpy())
