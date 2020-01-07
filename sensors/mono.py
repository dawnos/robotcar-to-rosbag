
from image import Image

class Mono(Image):
    def __init__(self, name, root_dir):
        super(Mono, self).__init__("mono_%s" % name, "/mono/%s" % name, root_dir)
    