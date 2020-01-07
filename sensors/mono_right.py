
from image import _Image

class MonoRight(_Image):
    def __init__(self, root_dir):
        super(MonoRight, self).__init__("mono_right", "/mono/right", root_dir)
