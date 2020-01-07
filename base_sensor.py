
class BaseSensor(object):
    def __init__(self, name, topic_name, root_dir, sensor_subdir=None, timestamps_file=None):
        self.sensor_dir = "%s/%s" % (root_dir, name if sensor_subdir is None else sensor_subdir)
        self.topic_name = topic_name
        if timestamps_file is None:
            timestamps_file = "%s.timestamps" % name
        with open("%s/%s" % (root_dir, timestamps_file)) as f:
            self.timestamps = [int(line.split()[0]) for line in f.readlines()]

    def get_timestamps(self):
        return self.timestamps

    def read_message(self, timestamp):
        raise NotImplementedError