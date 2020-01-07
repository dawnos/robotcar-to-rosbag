
from stereo import Stereo

class StereoRight(Stereo):
    def __init__(self, root_dir):
        super(StereoRight, self).__init__("right", root_dir)
    