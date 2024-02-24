import pickle
import spiller

SPILLFILE = "/tmp/trace_spill.pickle"

def func_file(item):
    return item["file_name"], item["function_name"]
def line_id(item):
    return func_file(item), item["line"]
readme = spiller.Spiller()
readme.load_spillfile(SPILLFILE)

prev = next(readme.analysis_items())
prev_function = func_file(prev)
prev_line = line_id(prev)
line_start_time = prev["time"]

for x in readme.analysis_items():
    this_line = line_id(x)
    if this_line != prev_line:
        print(f"calculate time for previous line {prev_line}")
        print(f"moving on to {this_line}")
    else:
        print(x)
    prev_line = this_line
    prev = x






