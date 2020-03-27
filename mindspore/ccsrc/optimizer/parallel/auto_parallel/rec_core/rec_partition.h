/**
 * Copyright 2020 Huawei Technologies Co., Ltd
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

#ifndef OPTIMIZER_PARALLEL_AUTO_PARALLEL_REC_PARTITION_H_
#define OPTIMIZER_PARALLEL_AUTO_PARALLEL_REC_PARTITION_H_

#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <utility>
#include <cmath>
#include <memory>

#include "optimizer/parallel/auto_parallel/rec_core/rec_graph.h"
#include "optimizer/parallel/auto_parallel/rec_core/rec_strategy.h"
#include "optimizer/parallel/auto_parallel/rec_core/rec_cost.h"
#include "optimizer/parallel/status.h"

namespace mindspore {
namespace parallel {
std::vector<size_t> SortByWeight(const std::shared_ptr<Graph> graph);

double GetWeights(const Graph::NodeType &node);

StrategyRec PartitionNode(const Graph::NodeType &node,
                          const std::vector<std::pair<std::string, StrategyRec>> &node_name_to_strategy,
                          std::shared_ptr<Graph> graph);

Status PartitionForAllDevices(const size_t num_device, std::shared_ptr<Graph> graph);

Graph::NodeType ApplyStrToTensor(Graph::NodeType Node);

void InferUndecideStrategy(std::shared_ptr<Graph> graph);

void ApplyLastStrategy(const uint64_t node_index, std::shared_ptr<Graph> graph);

void ApplyNextStrategy(const uint64_t node_index, std::shared_ptr<Graph> graph);

Status DevicesMemoryControl(std::shared_ptr<Graph> graph);

size_t GetDataTypeSize(const TensorType &type);
}  // namespace parallel
}  // namespace mindspore

#endif  // OPTIMIZER_PARALLEL_AUTO_PARALLEL_REC_PARTITION_H_
