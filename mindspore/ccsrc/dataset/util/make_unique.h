/**
 * Copyright 2019 Huawei Technologies Co., Ltd
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef DATASET_UTIL_MAKE_UNIQUE_H_
#define DATASET_UTIL_MAKE_UNIQUE_H_

#ifdef DEBUG
#include <cassert>
#define DS_ASSERT(f) assert(f)
#else
#define DS_ASSERT(f) ((void)0)
#endif

#include <memory>
#include <type_traits>
#include <utility>
#include "dataset/util/de_error.h"
#include "utils/log_adapter.h"

namespace mindspore {
using std::make_unique;
}  // namespace mindspore

#endif  // DATASET_UTIL_MAKE_UNIQUE_H_
