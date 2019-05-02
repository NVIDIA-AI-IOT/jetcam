from .camera import Camera
import atexit
import cv2
import numpy as np
import threading
import traitlets


class webcam_usb(Camera):
    
    capture_fps = traitlets.Integer(default_value=30)
    capture_width = traitlets.Integer(default_value=640)
    capture_height = traitlets.Integer(default_value=480)   
    capture_device = traitlets.Integer(default_value=1)
    def __init__(self, *args, **kwargs):
        super(IMX219, self).__init__(*args, **kwargs)
        try:
            self.cap = cv2.VideoCapture(self._gst_str(), cv2.CAP_GSTREAMER)

            re, image = self.cap.read()

            if not re:
                raise RuntimeError('Could not read image from camera.')
        except:
            raise RuntimeError(
                'Could not initialize camera.  Please see error trace.')

        atexit.register(self.cap.release)
                
    def _gst_str(self):
        return 'v4l2src device=/dev/video{} ! '
               'video/x-raw, width=%d, height=%d, framerate=(fraction)%d/1 ! '
               'videoconvert !  video/x-raw, width=(int)%d, height=(int)%d, format=(string)BGR ! appsink'% (
                self.capture_device, self.capture_width, self.capture_height, self.capture_fps, self.width, self.height)
    
    def _read(self):
        re, image = self.cap.read()
        if re:
            return image
        else:
            raise RuntimeError('Could not read image from camera')
