import cv2

def open_cam_onboard(width, height):
   # On versions of L4T previous to L4T 28.1, flip-method=2
   # Use Jetson onboard camera
   gst_str = ("nvarguscamerasrc ! video/x-raw(memory:NVMM)," \
              "width=(int)1920, height=(int)1080, format=(string)NV12, " \
              "framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, " \
              "width=(int){}, height=(int){}, format=(string)BGRx ! " \
              "videoconvert ! video/x-raw, format=(string)BGR !" \
              "appsink").format(width, height)

   return cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)

cap = open_cam_onboard(1280, 720)

#cap = cv2.VideoCapture("nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)1280, height=(int)720,format=(string)I420, framerate=(fraction)30/1 ! nvvidconv flip-method=0 ! video/x-raw, format=(string)$

#cap = cv2.VideoCapture(0)

#cap = cv2.VideoCapture(“nvcamerasrc”)

if cap is None:
   print("No Cam")

while True:
    _, frame = cap.read()

    cv2.imshow("frame", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

cap.stop()
cv2.destroyAllWindows()
