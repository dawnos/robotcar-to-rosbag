
from image import _Image

class MonoLeft(_Image):
    def __init__(self, root_dir):
        super(MonoLeft, self).__init__("mono_left", "/mono/left", root_dir)
    