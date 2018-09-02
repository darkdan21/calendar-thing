#!/bin/python
from modules import eventmanager

def main():
    e = eventmanager.eventmanager()
    e.getevents("%Name %date %Duration")

if __name__ == "__main__":
    main()
