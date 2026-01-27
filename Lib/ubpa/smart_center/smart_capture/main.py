# CI-FLAG-NOT-COMPILE

# from ubpa.smart_capture import smart_cap
from ubpa.smart_center.smart_capture import smart_cap

if __name__ == '__main__':
    smart_capture = smart_cap.SmartCapture()
    smart_capture.listen()
