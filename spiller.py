import sys

class Spiller:
    def __init__(self):
        self.spilled = []


    def report(self):
        return self.spilled

    def trace(self, frame, event, args):
        self.accumulate(frame, event, args)


    def start(self):
        sys.settrace(self.trace)

    def stop(self):
        sys.settrace(None)


    def accumulate(self, frame, event, args):
        self.spilled.append([frame, event, args])