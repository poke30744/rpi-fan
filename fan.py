#!/usr/bin/env python
import argparse
import time
from gpiozero import OutputDevice, CPUTemperature

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Python script to control fan on Raspberry Pi')
    parser.add_argument('--gpio', '-g', required=True, help='GPIO pin name (e.g.: GPIO17, BCM17, BOARD11, WPI0, J8:11)')
    parser.add_argument('--on', '-n', required=True, type=float, help='ON threshold to start (in Celsius)')
    parser.add_argument('--off', '-f', required=True, type=float, help='OFF threshold to stop (in Celsius)')
    parser.add_argument('--interval', '-i', default=5, type=int, help='How often we check CPU temperature (seconds)')
    args = parser.parse_args()

    fan = OutputDevice(args.gpio)
    cpu = CPUTemperature()

    while True:
        if cpu.temperature > args.on:
            fan.on()
        elif cpu.temperature < args.off:
            fan.off()
        time.sleep(args.interval)
