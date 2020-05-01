# rpi-fan
## Usage
```
fan.py -h
usage: fan.py [-h] --gpio GPIO --on ON --off OFF [--interval INTERVAL]

Python script to control fan on Raspberry Pi

optional arguments:
  -h, --help            show this help message and exit
  --gpio GPIO, -g GPIO  GPIO pin name (e.g.: GPIO17, BCM17, BOARD11, WPI0,
                        J8:11)
  --on ON, -n ON        ON threshold to start (in Celsius)
  --off OFF, -f OFF     OFF threshold to stop (in Celsius)
  --interval INTERVAL, -i INTERVAL
                        How often we check CPU temperature (seconds)
```
