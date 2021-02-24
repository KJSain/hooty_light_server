# hooty_light_server

Simple python web server to control some LEDs for my 'busy box' hooty project. There are hopes to make this more sophisticated but for now it's good enough to give Hooty some demon eyes when I'm in a call :)
Code is tested on the raspberry pi 3

## Usage (for now)


### Running it
```bash
sudo ./remote_hooty.py
```

### Web call
Expects a json request with bool as the values:
```json
{
    "mic_state": true,
    "vid_state": false
}
```