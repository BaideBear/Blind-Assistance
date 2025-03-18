#!/bin/bash

# 检查环境变量 lier_workload_path 是否为空
if [ -z "$lier_workload_path" ]; then
    # 获取当前目录的绝对路径
    WORKLOAD_PATH="$(pwd)"

    # 将 lier_workload_path 设置为当前目录路径
    export lier_workload_path="$WORKLOAD_PATH"
    echo "环境变量 'lier_workload_path' 设置为: $lier_workload_path"
else
    echo "环境变量 'lier_workload_path' 已设置为: $lier_workload_path"
fi

# 保存当前目录
CURRENT_DIR="$(pwd)"

# 进入 ascend-yolov8-sample/src 目录
cd "$CURRENT_DIR/ascend-yolov8-sample/src"

# 执行 cmake 和 make 命令
cmake .
make

# 返回到原来的目录
cd "$CURRENT_DIR"

# 运行 move.py 脚本
python move.py
