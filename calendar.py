#!/bin/python
from modules import eventmanager
from modules import event

def main():
    e = eventmanager.eventmanager()
    e.getevents("%hello %date %it's the man %duration")
    parameters = {"hello":"there","it's the man":"who"}

if __name__ == "__main__":
    main()
