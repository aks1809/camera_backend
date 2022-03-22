import cv2

cam = cv2.VideoCapture(2)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 3000)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 3000)
cam.set(cv2.CAP_PROP_EXPOSURE, 250)

while True:
    ret, frame = cam.read()
    if not ret:
        break
    if frame.max() == 0:
        continue
    cv2.imwrite("/home/poop/frinks/skh/camera_backend/images/upload.bmp", frame)
    break

cam.release()
