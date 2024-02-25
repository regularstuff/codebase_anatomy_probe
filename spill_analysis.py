import pickle
import spiller
from collections import namedtuple
import statistics




class SpillAnalyser:

    def func_file(self, item):
        return item["file_name"], item["function_name"]

    def line_id(self, item):
        return self.func_file(item), item["line"]

    def __init__(self, spillfile):
        self.spillfile = spillfile
        self.spiller = None

    def line_timings(self):
        timed_line = namedtuple("LineTiming",
                                field_names="line_no, event, time, func, file",
                                )
        self._load_spillfile()
        timings = []
        for log in self.spiller.analysis_items():
            timings.append(timed_line(file=log["file_name"],
                                      line_no=["line"],
                                      event=log["event"],
                                      time=log["time"],
                                      func=log["function_name"]))

        prev = timed_line(line_no=0, event=None, time=None, func=None, file=None)
        cumulative = 0
        list_of_cumulative = []

        state = ''
        for cur in timings:
            if cur.event == "call":
                state = 'Accumulating'
            if prev.event == "line" and cur.event in ["line", "return"] and state=='Accumulating':
                cumulative += cur.time - prev.time
            if cur.event == "return":
                state='Returning'
                list_of_cumulative.append(cumulative)
                cumulative = 0
            prev = cur
        return list_of_cumulative, statistics.mean(list_of_cumulative)





    def _load_spillfile(self):
        self.spiller = spiller.Spiller(include_code=False)
        self.spiller.load_spillfile(self.spillfile)


    def dump(self):
        self._load_spillfile()
        traces = self.spiller.analysis_items()
        prev_capture = next(traces)
        prev_function = self.func_file(prev_capture)
        prev_line = self.line_id(prev_capture)
        prev_start_time = prev_capture["time"]

        line_runtimes = []

        for capture in traces:
            this_line = self.line_id(capture)
            if this_line != prev_line:
                new_start_time = capture["time"]
                # print(f"delta {prev_start_time=}, {new_start_time=}, is {new_start_time-prev_start_time}:  {prev_line}")
                print(f"finished {prev_line}; {new_start_time - prev_start_time}")

                prev_line = this_line
            else:
                print(f"again in line{capture}")
            prev_capture = capture

        return 1


