/**
* Copyright (c) Huawei Technologies Co., Ltd. 2020-2022. All rights reserved.
*
* Licensed under the Apache License, Version 2.0 (the "License");
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at

* http://www.apache.org/licenses/LICENSE-2.0

* Unless required by applicable law or agreed to in writing, software
* distributed under the License is distributed on an "AS IS" BASIS,
* WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
* See the License for the specific language governing permissions and
* limitations under the License.

* File label.h
* Description: label result
*/
#ifndef modelInference_label_H
#define modelInference_label_H
using namespace std;
//ver1
// const string label[] = {"stop_sign", "person", "bicycle", "bus", 
// 			"truck", "car", "motorbike", "reflective_cone", 
// 			"ashcan", "warning_column", "spherical_roadblock", "pole", 
// 			"dog", "tricycle", "fire_hydrant", "red", "green"};

//ver2
const string label[] = {"stop_sign", "person", "bicycle", "bus", 
			"truck", "car", "motorbike", "reflective_cone", 
			"ashcan", "warning_column", "spherical_roadblock", "pole", 
			"dog", "tricycle", "fire_hydrant", "red_light", "green_light", 
			"crosswalk", "guide_arrows"};


#endif //modelInference_label_H
