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
from mindspore.ops import operations as P
from mindspore.ops import Primitive

mul = P.Mul()
reduce_sum = P.ReduceSum()
sub = P.Sub()
confusion_softmax_grad = Primitive('ConfusionSoftmaxGrad')
make_tuple = Primitive('make_tuple')
tuple_getitem = Primitive('tuple_getitem')
axis = 2


class FnDict:
    def __init__(self):
        self.fnDict = {}

    def __call__(self, fn):
        self.fnDict[fn.__name__] = fn

    def __getitem__(self, name):
        return self.fnDict[name]


def test_confusion_softmax_grad_rule(tag):
    """ test_confusion_softmax_grad_rule """
    fns = FnDict()

    @fns
    def before(input0, input1):
        res = mul(input0, input1)
        # input axis will be convert to attr in ConstructKernelGraph step
        res = reduce_sum(res, axis)
        res = sub(input0, res)
        return res

    @fns
    def after(input0, input1):
        res = confusion_softmax_grad(input0, input1)
        return make_tuple(res)

    return fns[tag]
