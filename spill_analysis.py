import pickle
import spiller

SPILLFILE = "/tmp/trace_spill.pickle"

def func_file(item):
    return item["file_name"], item["function_name"]
def line_id(item):
    return func_file(item), item["line"]
readme = spiller.Spiller(include_code=False)
readme.load_spillfile(SPILLFILE)

prev_capture = next(readme.analysis_items())
prev_function = func_file(prev_capture)
prev_line = line_id(prev_capture)
prev_start_time = prev_capture["time"]

line_runtimes = []

for capture in readme.analysis_items():
    this_line = line_id(capture)
    if this_line != prev_line:
        new_start_time = capture["time"]
        # print(f"delta {prev_start_time=}, {new_start_time=}, is {new_start_time-prev_start_time}:  {prev_line}")
        print(f"finished {prev_line}; {new_start_time-prev_start_time}")

        prev_line = this_line
    else:
        print(f"again in line{capture}")
    prev_capture = capture






