
import logging
import inspect
from itertools import chain
from tqdm import tqdm

import rospy
import rosbag

import sensors

def sorted_with_index(L):
    print(type(L))
    L_with_index = [(L[i], i) for i in range(len(L))]
    sorted_L_with_index = sorted(L_with_index, key=lambda t: t[0])
    sorted_L, indices  = zip(*sorted_L_with_index)
    return sorted_L, indices


class Converter:
    def __init__(self, data_dir):
        logging.debug('data_dir=%s' % data_dir)

        self.sensors = []
        for class_name, _class in inspect.getmembers(sensors, inspect.isclass):
            logging.debug('Sensor found: %s' % class_name)
            self.sensors.append(_class(data_dir))

    def run(self,  out_file):
        logging.debug('out_file=%s' % out_file)

        timestamps_list = [(ts, sid) for sid, sensor in enumerate(self.sensors) for ts in sensor.get_timestamps()]
        sorted_timestamps_list = sorted(timestamps_list, key=lambda elem: elem[0])

        bag = rosbag.Bag(out_file, 'w')

        for ts, sid in tqdm(sorted_timestamps_list):
            msg = self.sensors[sid].read_message(ts)
            t = rospy.Time(ts // 1000000, (ts % 1000000) * 1000)
            # logging.info("Writing %s (%f) to %s" % (type(msg), t.to_sec(), self.sensors[sid].topic_name))
            bag.write(self.sensors[sid].topic_name, msg, t)
        bag.close()

