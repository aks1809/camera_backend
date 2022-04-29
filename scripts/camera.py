import cv2

cam = cv2.VideoCapture(0)

cam.set(cv2.CAP_PROP_FRAME_WIDTH, 3000)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 3000)
cam.set(cv2.CAP_PROP_EXPOSURE, 250)

BASE_PATH = "/home/user/frinks/camera_backend"

# cv2.namedWindow('test', cv2.WINDOW_NORMAL)

while True:
    ret, frame = cam.read()
    # print(frame.max())
    if not ret:
        break
    if frame.max() == 0:
        continue
    # cv2.imshow('test', frame)
    # k = cv2.waitKey(20)
    # if k % 256 == 27:
    #     # ESC pressed
    #     print("Escape hit, closing...")
    #     break
    # elif k % 256 == 32:
        # SPACE pressed
    cv2.imwrite(f"{BASE_PATH}/images/upload.bmp", frame)
    break

cam.release()
