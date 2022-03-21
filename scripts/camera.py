import cv2

cam = cv2.VideoCapture(0, cv2.CAP_V4L2)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 3000)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 3000)
cam.set(cv2.CAP_PROP_EXPOSURE, 2000)

while True:
    ret, frame = cam.read()
    if not ret:
        break
    cv2.imwrite("/home/poop/frinks/skh/camera_backend/images/upload.bmp", frame)
    break

cam.release()
