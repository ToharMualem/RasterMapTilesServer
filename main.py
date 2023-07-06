#!/usr/bin/env python
"""
Author: Tohar Mualem <toharm7@gmail.com>
Date: 4-07-2023
Purpose: main script, runs the flask application.
"""

import tile_serving_application
from tiling import tiling_obj
import argparse


def get_args():
    """ Arguments for maptiles web server"""

    parser = argparse.ArgumentParser(
        description='Arguments for running maptiles web server',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-ho',
                        '--host',
                        help='Server Address',
                        metavar='str',
                        type=str,
                        default='localhost')

    parser.add_argument('-p',
                        '--port',
                        help='Server port',
                        metavar='int',
                        type=int,
                        default=8080)

    return parser.parse_args()


if __name__ == '__main__':
    args = get_args()
    host = args.host
    port = args.port

    serving_app = tile_serving_application.create_application(tiling_obj.file_name, r"/", host, port)
    serving_app.run_server()
