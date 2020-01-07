
import argparse

from converter import Converter

import logging
logging.basicConfig(level=logging.INFO)


def main():
    args = parse_argument()
    cvt = Converter(args.data_dir)
    cvt.run(args.out_file)


def parse_argument():
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('data_dir', metavar='data_dir', type=str,
                        help='data folder')
    parser.add_argument('out_file', metavar='out.bag', type=str,
                        help='output filename')

    args = parser.parse_args()

    return args


if __name__ == "__main__":
    main()
