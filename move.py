import os
import shutil
import time
import subprocess
import cv2
from shapely.geometry import Polygon, box

def move_files():
    # 获取 lier_workload_path 的值
    lier_workload_path = os.getenv('lier_workload_path')

    if lier_workload_path is not None:
        # 定义源目录和目标目录
        source_dir = os.path.join(lier_workload_path, 'out')
        target_dir = os.path.join(lier_workload_path, 'ascend-yolov8-sample', 'data')

        # 检查源目录是否存在
        if os.path.exists(source_dir) and os.path.isdir(source_dir):
            while True:
                # 获取源目录中的文件列表
                files = os.listdir(source_dir)
                if files:  # 如果有文件
                    # 确保目标目录存在，如果不存在则创建
                    os.makedirs(target_dir, exist_ok=True)

                    # 清空目标目录中的所有文件
                    for filename in os.listdir(target_dir):
                        file_path = os.path.join(target_dir, filename)
                        try:
                            if os.path.isfile(file_path) or os.path.islink(file_path):
                                os.unlink(file_path)
                                print(f"Removed {file_path}")
                            elif os.path.isdir(file_path):
                                shutil.rmtree(file_path)
                                print(f"Removed directory {file_path}")
                        except Exception as e:
                            print(f'Failed to delete {file_path}. Reason: {e}')

                    # 遍历源目录中的所有文件
                    for filename in files:
                        source_file = os.path.join(source_dir, filename)
                        
                        # 检查路径是否是文件
                        if os.path.isfile(source_file):
                            # 生成目标文件路径
                            target_file = os.path.join(target_dir, filename)
                            # 移动文件
                            shutil.move(source_file, target_file)
                            print(f"Moved {source_file} to {target_file}")
                    break
                else:
                    print("No files in the source directory, waiting for files...")
                    ##
                    cap = cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    target_file = os.path.join(source_dir, "captured_image.jpg")
                    cv2.imwrite(target_file, frame)
                    cap.release()
                    ##
                    time.sleep(1)  # 如果没有文件，等待1秒钟

            # 进入 ascend-yolov8-sample/out 目录并运行 main 文件
            out_dir = os.path.join(lier_workload_path, 'ascend-yolov8-sample', 'out')
            if os.path.exists(out_dir) and os.path.isdir(out_dir):
                # 使用 subprocess.run 来执行主程序
                try:
                    subprocess.run(['./main'], cwd=out_dir, check=True)
                    print(f"Executed main in {out_dir}")
                except subprocess.CalledProcessError as e:
                    print(f"Failed to execute main: {e}")
            else:
                print(f"The directory {out_dir} does not exist or is not a directory.")
        else:
            print(f"The source directory {source_dir} does not exist or is not a directory.")
    else:
        print("The environment variable 'lier_workload_path' is not set.")

# def move_files():
#     lier_workload_path = os.getenv('lier_workload_path')

#     if lier_workload_path is not None:
#         target_dir = os.path.join(lier_workload_path, 'ascend-yolov8-sample', 'data')
#         os.makedirs(target_dir, exist_ok=True)
#         cap = cv2.VideoCapture(0)
#         if not cap.isOpened():
#             print("无法打开摄像头")
#             return
#         ret, frame = cap.read()
        
#         if not ret:
#             print("无法读取摄像头中的帧")
#         else:
#             target_file = os.path.join(target_dir, "captured_image.jpg")
#             cv2.imwrite(target_file, frame)
#             print(f"照片已保存为 '{target_file}'")
        
#         cap.release()
        
#         out_dir = os.path.join(lier_workload_path, 'ascend-yolov8-sample', 'out')
#         if os.path.exists(out_dir) and os.path.isdir(out_dir):
#             try:
#                 subprocess.run(['./main'], cwd=out_dir, check=True)
#                 print(f"Executed main in {out_dir}")
#             except subprocess.CalledProcessError as e:
#                 print(f"Failed to execute main: {e}")
#         else:
#             print(f"The directory {out_dir} does not exist or is not a directory.")
#     else:
#         print("The environment variable 'lier_workload_path' is not set.")



def calculate_distance():
    # 获取 lier_workload_path 的值
    lier_workload_path = os.getenv('lier_workload_path')

    if lier_workload_path is not None:
        ans_file_path = os.path.join(lier_workload_path, 'ascend-yolov8-sample', 'out', 'ans.txt')

        # 检查 ans.txt 文件是否存在
        if os.path.exists(ans_file_path) and os.path.isfile(ans_file_path):
            with open(ans_file_path, 'r') as file:
                lines = file.readlines()

            # 对每一行进行处理，非空行添加 ",distance: 3m"
            with open(ans_file_path, 'w') as file:
                for line in lines:
                    stripped_line = line.strip()
                    if stripped_line:  # 确保不是空行
                        line = stripped_line + ",distance: 3m\n"
                    else:
                        line = "\n"
                    file.write(line)
            print(f"Processed ans.txt in {os.path.dirname(ans_file_path)}")
        else:
            print(f"The file {ans_file_path} does not exist.")
    else:
        print("The environment variable 'lier_workload_path' is not set.")

def give_broadcast():
    # 获取环境变量 lier_workload_path 的值
    lier_workload_path = os.getenv('lier_workload_path')
    
    if lier_workload_path is not None:
        ans_file_path = os.path.join(lier_workload_path, 'ascend-yolov8-sample', 'out', 'ans.txt')
        final_ans_file_path = os.path.join(lier_workload_path, 'ascend-yolov8-sample', 'out', 'final_ans.txt')
        
        # 检查 ans.txt 是否存在
        if os.path.exists(ans_file_path) and os.path.isfile(ans_file_path):
            with open(ans_file_path, 'r') as file:
                lines = file.readlines()
            
            # 准备写入 final_ans.txt
            with open(final_ans_file_path, 'w') as outFile:
                data = []
                for line in lines:
                    if line.strip():  # 非空行，解析并添加到当前图片的数据
                        parts = line.strip().split(',')
                        name = parts[0].split(':')[1].strip()
                        box_name = parts[1].split(':')[1].strip()
                        original_width = float(parts[2].split(':')[1].strip())
                        original_height = float(parts[3].split(':')[1].strip())
                        
                        x = float(parts[4].split(':')[1].strip())
                        y = float(parts[5].split(':')[1].strip())
                        width = float(parts[6].split(':')[1].strip())
                        height = float(parts[7].split(':')[1].strip())

                        data.append({
                            "name": name,
                            "original_width": original_width,
                            "original_height": original_height,
                            "box_name": box_name,
                            "x": x,
                            "y": y,
                            "width": width,
                            "height": height
                        })
                    else:
                        # 遇到空行，处理当前图片的数据
                        if data:
                            process_image_data(data, outFile)
                            data = []  # 清空数据以便处理下一个图片
                
                # 处理最后一组数据（如果最后没有空行）
                if data:
                    process_image_data(data, outFile)
        
        else:
            print(f"文件 {ans_file_path} 不存在。")
    else:
        print("环境变量 'lier_workload_path' 未设置。")

def process_image_data(data, outFile):
    # 提取图片的宽度信息，假设每个图片的宽度是一致的
    if not data:
        return
    
    original_width = data[0]['original_width']
    original_height = data[0]['original_height']
    max_height = original_height * 0.5 #最远播报距离

    bottom_left1_X = original_width * 0.1 #最左侧和偏左侧分界
    bottom_left2_X = original_width * 0.4 #偏左侧和中间分界
    bottom_right1_X = original_width * 0.6 #中间和偏右侧分界
    bottom_right2_X = original_width * 0.9 #偏右侧和最右侧分界
    top_left1_X = original_width * 0.15
    top_left2_X = original_width * 0.45
    top_right1_X = original_width * 0.55
    top_right2_X = original_width * 0.85

    left_boxes = []
    little_left_boxes = []
    middle_boxes = []
    little_right_boxes = []
    right_boxes = []

    left_polygon = Polygon([(0, original_height), (0, max_height), (bottom_left1_X, original_height), (top_left1_X, max_height)])
    little_left_polygon = Polygon([(bottom_left1_X, original_height), (top_left1_X, max_height), (bottom_left2_X, original_height), (top_left2_X, max_height)])
    center_polygon = Polygon([(bottom_left2_X, original_height), (top_left2_X, max_height), (bottom_right1_X, original_height), (top_right1_X, max_height)])
    little_right_polygon = Polygon([(bottom_right1_X, original_height), (top_right1_X, max_height), (bottom_right2_X, original_height), (top_right2_X, max_height)])
    right_polygon = Polygon([(bottom_right2_X, original_height), (top_right2_X, max_height), (original_width, original_height), (original_width, max_height)])
    
    people_num = 0
    is_crosswalk = False
    is_green_light = False
    is_red_light = False

    for box_now in data:
        # 生成框的矩形
        rect = box(box_now['x'], box_now['y'], box_now['x'] + box_now['width'], box_now['y'] + box_now['height'])
        
        if box_now['box_name'] == 'person':
            people_num += 1
        if box_now['box_name'] == 'crosswalk':
            is_crosswalk = True
        if box_now['box_name'] == 'green_light':
            is_green_light = True
        if box_now['box_name'] == 'red_light':
            is_red_light = True

        if rect.intersects(left_polygon):
            left_boxes.append(box_now)
        if rect.intersects(little_left_polygon):
            little_left_boxes.append(box_now)
        if rect.intersects(center_polygon):
            middle_boxes.append(box_now)
        if rect.intersects(little_right_polygon):
            little_right_boxes.append(box_now)
        if rect.intersects(right_polygon):
            right_boxes.append(box_now)

    # 找到每类中 y 最大（最下面）的矩形框
    def find_lowest_box(boxes):
        if not boxes:
            return None
        return max(boxes, key=lambda b: b['y'] + b['height'])
    
    lowest_left_box = find_lowest_box(left_boxes)
    lowest_little_left_box = find_lowest_box(little_left_boxes)
    lowest_middle_box = find_lowest_box(middle_boxes)
    lowest_little_right_box = find_lowest_box(little_right_boxes)
    lowest_right_box = find_lowest_box(right_boxes)

    output_sign = "empty"
    English_to_Chinese = {}
    English_to_Chinese["Left"] = "前方左侧"
    English_to_Chinese["Right"] = "前方右侧"
    English_to_Chinese["Middle"] = "正前方"
    English_to_Chinese["little_left"] = "前方偏左侧"
    English_to_Chinese["little_right"] = "前方偏右侧"
    English_to_Chinese["stop_sign"] = "警示牌"
    English_to_Chinese["bicycle"] = "自行车"
    English_to_Chinese["bus"] = "公交车"
    English_to_Chinese["truck"] = "卡车"
    English_to_Chinese["car"] = "汽车"
    English_to_Chinese["motorbike"] = "摩托车"
    English_to_Chinese["reflective_cone"] = "反光路障"
    English_to_Chinese["warning_column"] = "警示牌"
    English_to_Chinese["spherical_roadblock"] = "球形路障"
    English_to_Chinese["pole"] = "电线杆"
    English_to_Chinese["dog"] = "狗"
    English_to_Chinese["tricycle"] = "三轮车"
    English_to_Chinese["fire_hydrant"] = "消防栓"
    English_to_Chinese["red_light"] = "红灯"
    English_to_Chinese["green_light"] = "绿灯"

    if is_crosswalk:
        if is_green_light:
            output_sign = "前方注意斑马线，当前为绿灯，请谨慎通行"
        else:
            if is_red_light:
                output_sign = "当前为红灯，请等待"
            else:
                output_sign = "前方注意斑马线，请谨慎通行"
    else:
        if people_num >= 5:
            output_sign = "前方注意有较多行人"
        else:
            cross_area = ""
            bottom_Y = 0
            nearest_obstacle = ""
            nearest_obstacle_area = ""
            for region, box_now in [("Left", lowest_left_box), ("Right", lowest_right_box), ("little_left", lowest_little_left_box), ("little_right", lowest_little_right_box), ("Middle", lowest_middle_box)]:
                if box_now and box_now['box_name'] != "person" and box_now['box_name'] != "guide_arrows":
                    if box_now['y'] + box_now['height'] > bottom_Y:
                        nearest_obstacle = box_now['box_name']
                        nearest_obstacle_area = region
                        bottom_Y = box_now['y'] + box_now['height']
                else:
                    cross_area = region
            if nearest_obstacle_area:
                if cross_area:
                    output_sign = (f"{English_to_Chinese[nearest_obstacle_area]}有{English_to_Chinese[nearest_obstacle]},请从{English_to_Chinese[cross_area]}通行")
                else:
                    output_sign = "前方障碍物过多，请向左或向右走几步绕行"
            else:
                output_sign = "前方无障碍物，请直行"
    print(output_sign)
    subprocess.run(['espeak-ng', '-s', '200', '-p', '70', '-v', 'zh', output_sign], capture_output=True, text=True)

    # 输出每类选中的矩形框信息到文件
    for region, box_now in [("Left", lowest_left_box), ("little_left", lowest_little_left_box), ("Middle", lowest_middle_box), ("little_right", lowest_little_right_box), ("Right", lowest_right_box)]:
        if box_now:
            output_str = (f"图片: {box_now['name']}, 区域: {region}, 类别: {box_now['box_name']}, X: {box_now['x']}, Y: {box_now['y']}, 宽度: {box_now['width']}, 高度: {box_now['height']}\n")
            outFile.write(output_str)
            print(output_str)

    outFile.write("\n")  # 每个图片输出完成后，空一行

def main():
    while True:
        move_files()  # 等待并处理文件
        calculate_distance()
        give_broadcast()
        # 每隔2秒执行一次
        # time.sleep(2)

if __name__ == "__main__":
    main()
