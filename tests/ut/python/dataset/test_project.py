# Copyright 2019 Huawei Technologies Co., Ltd
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
# ==============================================================================
import mindspore.dataset.transforms.vision.c_transforms as vision
import mindspore._c_dataengine as de_map
from util import ordered_save_and_check

import mindspore.dataset as ds

DATA_DIR_TF = ["../data/dataset/testTFTestAllTypes/test.data"]
SCHEMA_DIR_TF = "../data/dataset/testTFTestAllTypes/datasetSchema.json"
GENERATE_GOLDEN = False


def test_case_project_single_column():
    columns = ["col_sint32"]
    parameters = {"params": {'columns': columns}}

    data1 = ds.TFRecordDataset(DATA_DIR_TF, SCHEMA_DIR_TF, shuffle=False)
    data1 = data1.project(columns=columns)

    filename = "project_single_column_result.npz"
    ordered_save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)


def test_case_project_multiple_columns_in_order():
    columns = ["col_sint16", "col_float", "col_2d"]
    parameters = {"params": {'columns': columns}}

    data1 = ds.TFRecordDataset(DATA_DIR_TF, SCHEMA_DIR_TF, shuffle=False)
    data1 = data1.project(columns=columns)

    filename = "project_multiple_columns_in_order_result.npz"
    ordered_save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)


def test_case_project_multiple_columns_out_of_order():
    columns = ["col_3d", "col_sint64", "col_2d"]
    parameters = {"params": {'columns': columns}}

    data1 = ds.TFRecordDataset(DATA_DIR_TF, SCHEMA_DIR_TF, shuffle=False)
    data1 = data1.project(columns=columns)

    filename = "project_multiple_columns_out_of_order_result.npz"
    ordered_save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)


def test_case_project_map():
    columns = ["col_3d", "col_sint64", "col_2d"]
    parameters = {"params": {'columns': columns}}

    data1 = ds.TFRecordDataset(DATA_DIR_TF, SCHEMA_DIR_TF, shuffle=False)
    data1 = data1.project(columns=columns)

    no_op = de_map.NoOp()

    data1 = data1.map(input_columns=["col_3d"], operations=no_op)

    filename = "project_map_after_result.npz"
    ordered_save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)


def test_case_map_project():
    columns = ["col_3d", "col_sint64", "col_2d"]
    parameters = {"params": {'columns': columns}}

    data1 = ds.TFRecordDataset(DATA_DIR_TF, SCHEMA_DIR_TF, shuffle=False)

    no_op = de_map.NoOp()
    data1 = data1.map(input_columns=["col_sint64"], operations=no_op)

    data1 = data1.project(columns=columns)

    filename = "project_map_before_result.npz"
    ordered_save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)


def test_case_project_between_maps():
    columns = ["col_3d", "col_sint64", "col_2d"]
    parameters = {"params": {'columns': columns}}

    data1 = ds.TFRecordDataset(DATA_DIR_TF, SCHEMA_DIR_TF, shuffle=False)

    no_op = de_map.NoOp()
    data1 = data1.map(input_columns=["col_3d"], operations=no_op)
    data1 = data1.map(input_columns=["col_3d"], operations=no_op)
    data1 = data1.map(input_columns=["col_3d"], operations=no_op)
    data1 = data1.map(input_columns=["col_3d"], operations=no_op)

    data1 = data1.project(columns=columns)

    data1 = data1.map(input_columns=["col_3d"], operations=no_op)
    data1 = data1.map(input_columns=["col_3d"], operations=no_op)
    data1 = data1.map(input_columns=["col_3d"], operations=no_op)
    data1 = data1.map(input_columns=["col_3d"], operations=no_op)
    data1 = data1.map(input_columns=["col_3d"], operations=no_op)

    filename = "project_between_maps_result.npz"
    ordered_save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)


def test_case_project_repeat():
    columns = ["col_3d", "col_sint64", "col_2d"]
    parameters = {"params": {'columns': columns}}

    data1 = ds.TFRecordDataset(DATA_DIR_TF, SCHEMA_DIR_TF, shuffle=False)
    data1 = data1.project(columns=columns)

    repeat_count = 3
    data1 = data1.repeat(repeat_count)

    filename = "project_before_repeat_result.npz"
    ordered_save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)


def test_case_repeat_project():
    columns = ["col_3d", "col_sint64", "col_2d"]
    parameters = {"params": {'columns': columns}}

    data1 = ds.TFRecordDataset(DATA_DIR_TF, SCHEMA_DIR_TF, shuffle=False)

    repeat_count = 3
    data1 = data1.repeat(repeat_count)

    data1 = data1.project(columns=columns)

    filename = "project_after_repeat_result.npz"
    ordered_save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)


def test_case_map_project_map_project():
    columns = ["col_3d", "col_sint64", "col_2d"]
    parameters = {"params": {'columns': columns}}

    data1 = ds.TFRecordDataset(DATA_DIR_TF, SCHEMA_DIR_TF, shuffle=False)

    no_op = de_map.NoOp()
    data1 = data1.map(input_columns=["col_sint64"], operations=no_op)

    data1 = data1.project(columns=columns)

    data1 = data1.map(input_columns=["col_2d"], operations=no_op)

    data1 = data1.project(columns=columns)

    filename = "project_alternate_parallel_inline_result.npz"
    ordered_save_and_check(data1, parameters, filename, generate_golden=GENERATE_GOLDEN)
