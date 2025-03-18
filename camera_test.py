import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("无法打开摄像头")
    exit()

ret, frame = cap.read()

if not ret:
    print("摄像头抽帧失败")
else:
    cv2.imwrite("captured_image.jpg", frame)
    print("照片已保存为 'captured_image.jpg'")

cap.release()
