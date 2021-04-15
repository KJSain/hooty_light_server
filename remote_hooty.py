#!/usr/bin/python3

import json
import time
import sys
sys.path.append(".")
from hooty_lights import OwlLight
from flask import Flask
from flask import request
from threading import Thread
from neopixel import *
import datetime

APP = Flask(__name__)
HOOTY = OwlLight()

@APP.route("/api/v1/light/", methods=['POST'])
def api_light():
    data = request.json
    mic_state = data['mic_state']
    vid_state = data['vid_state']
    light_state = dict()

    # Handle the Mic & Eye state
    if mic_state is True:
        HOOTY.update_time(datetime.datetime.now())
        eye_thread = Thread(target = HOOTY.eyes, args=(True,))
        eye_thread.start()
        light_state['eyes'] = True
    else:
        eye_thread = Thread(target = HOOTY.eyes, args=(False,))
        eye_thread.start()
        light_state['eyes'] = False

    # Handle the Vid & Beak + Head state
    if vid_state is True:
        HOOTY.update_time(datetime.datetime.now())
        beak_thread = Thread(target = HOOTY.beak, args=(True,))
        head_thread = Thread(target = HOOTY.head, args=(True,))
        beak_thread.start()
        head_thread.start()
        light_state['beak'] = True
        light_state['head'] = True
    else:
        beak_thread = Thread(target = HOOTY.beak, args=(False,))
        head_thread = Thread(target = HOOTY.head, args=(False,))
        beak_thread.start()
        head_thread.start()
        light_state['beak'] = False
        light_state['head'] = False

    return json.dumps(light_state)

if __name__ == '__main__':
    HOOTY.clear()
    APP.run(host='0.0.0.0', port=5000)
