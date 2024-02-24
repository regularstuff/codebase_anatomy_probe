import copy
import dis
import sys
import pickle
import itertools
import datetime
import time

class Spiller:

    def __init__(self, include_code=True):
        self.spilled = []
        self.include_code = include_code
        self.event_number = itertools.count()


    def report(self):
        return self.spilled

    def analysis_items(self):
        for x in self.spilled:
            yield x
    def trace(self, frame, event, args):
        frame.f_trace_opcodes = self.include_code
        self.accumulate(frame, event, args)
        return self.trace


    def start(self):
        sys.settrace(self.trace)

    def stop(self):
        sys.settrace(None)

    def accumulate(self, frame, event, args):

        thing = { "number":  next(self.event_number),
                  "code": frame.f_code,
                 "line": frame.f_lineno,
                 "event": event,
                 "time": time.perf_counter_ns()
                 }
        if event == "opcode":
            thing["opcode"] = frame.f_code.co_code[frame.f_lasti]
        self.spilled.append(thing)

    def save_spillfile(self, save_name):
        savable = []
        for trace_item in self.spilled:
            pickleable = copy.deepcopy(trace_item)
            del pickleable["code"]
            pickleable["function_name"] = trace_item["code"].co_name
            pickleable["file_name"] = trace_item["code"].co_filename
            if trace_item["event"] == "opcode":
                pickleable["opcode"] = dis.opname[trace_item["opcode"]]

            savable.append(pickleable)
        with open(save_name, "wb") as f:
            pickle.dump(savable, f)

    def load_spillfile(self, save_name):
        with open(save_name, "rb") as f:
            self.spilled = pickle.load(f)



