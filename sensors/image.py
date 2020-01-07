
import os
import cv_bridge
import logging

try:
    from sdk.python.image import load_image
    from sdk.python.camera_model import CameraModel
except ImportError:
    logging.error(
        """Robotcar SDK module not found. 
        Please create __init__.py under the root directory of SDK. 
        Will be fixed in the future."""
        )
    exit(-1)

from base_sensor import BaseSensor

class Image(BaseSensor):
    def __init__(self, name, topic_name, root_dir, sensor_subdir=None, timestamps_file=None):
        super(Image, self).__init__(name, topic_name, root_dir, sensor_subdir, timestamps_file)
        self.name = name
        self.bridge = cv_bridge.CvBridge()
        self.model = self.load_camera_model()

    def read_message(self, timestamp):
        img = load_image("%s/%d.png" % (self.sensor_dir, timestamp), self.model)
        assert(not(img is None))
        msg = self.bridge.cv2_to_imgmsg(img, encoding="rgb8")
        return msg

    def load_camera_model(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        models_dir = "%s/../sdk/models" % base_dir
        images_dir = self.name
        model = CameraModel(models_dir, images_dir)
        return model
