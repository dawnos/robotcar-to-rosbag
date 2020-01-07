
from image import Image

class Stereo(Image):
    def __init__(self, name, root_dir):
        super(Stereo, self).__init__(
            "stereo_%s" % name, "/stereo/%s" % name, root_dir, "stereo/%s" % name, "stereo.timestamps")
    