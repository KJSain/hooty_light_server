#!/usr/bin/python3

import json
import time
import sys
sys.path.append(".")
from hooty_lights import OwlLight
from flask import Flask 
from flask import request
from neopixel import *
#import argparse


APP = Flask(__name__)
HOOTY = OwlLight()


@APP.route("/api/v1/light/", methods=['POST'])
def api_light():
    data = request.json
    mic_state = data['mic_state']
    vid_state = data['vid_state']
    light_state = dict()

    if mic_state is True: 
        HOOTY.eyes(True)
        light_state['eyes'] = True
    else: 
        HOOTY.eyes(False)
        light_state['eyes'] = False
    if vid_state is True:
        HOOTY.beak(True)
        HOOTY.head(True)
        light_state['beak'] = True
    else: 
        HOOTY.beak(False)
        HOOTY.head(False)
        light_state['beak'] = False

    return json.dumps(light_state)

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=5000)
