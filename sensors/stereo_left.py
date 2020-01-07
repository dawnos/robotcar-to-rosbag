
from stereo import Stereo

class StereoLeft(Stereo):
    def __init__(self, root_dir):
        super(StereoLeft, self).__init__("left", root_dir)
    