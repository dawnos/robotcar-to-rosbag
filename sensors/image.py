
import os
# import cv2
import cv_bridge
from sdk.python.image import load_image
from sdk.python.camera_model import CameraModel
# from sensor_msgs.msg import Image as Msg

from base_sensor import BaseSensor

class _Image(BaseSensor):
    def __init__(self, name, topic_name, root_dir):
        super(_Image, self).__init__(name, topic_name, root_dir, name)
        self.name = name
        self.bridge = cv_bridge.CvBridge()
        self.model = self.load_camera_model()

    def read_message(self, timestamp):
        # img = cv2.imread("%s/%d.png" % (self.sensor_dir, timestamp))
        img = load_image("%s/%d.png" % (self.sensor_dir, timestamp), self.model)
        assert(not(img is None))
        msg = self.bridge.cv2_to_imgmsg(img, encoding="passthrough")
        return msg

    def load_camera_model(self):
        base_dir = os.path.dirname(os.path.abspath(__file__))
        models_dir = "%s/../sdk/models" % base_dir
        images_dir = self.name
        model = CameraModel(models_dir, images_dir)
        return model
