from timeit import timeit
from pprint import pprint




t1 = timeit("tri1(300)", setup="from triangles import tri1", number=300)
t2 = timeit("tri2(300)", setup="from triangles import tri2", number=300)
t3 = timeit("tri3(300)", setup="from triangles import tri3", number=300)
t4 = timeit("tri4(300)", setup="from triangles import tri4", number=300)
print(t1, t2, t3, t4)


SPILLFILE = "/tmp/spill1.pickle"
from spiller import Spiller
from spill_analysis import SpillAnalyser
from triangles import tri1, tri2, tri3, tri4

def time_trace(func):
    s = Spiller(include_code=False)
    s.start_spill()
    for i in range(8):
        func(10)
    s.stop_spill()
    s.save_spillfile(SPILLFILE)
    a = SpillAnalyser(spillfile=SPILLFILE)
    return(a.line_timings()[1])

trace1 = time_trace(tri1)
trace2 = time_trace(tri2)
trace3 = time_trace(tri3)
trace4 = time_trace(tri4)


print(f"tri1: tri2 -> timeit: {t1 / t2} trace: {trace1 / trace2}")
print(f"tri1: tri3 -> timeit: {t1 / t3} trace: {trace1 / trace3}")
print(f"tri1: tri4 -> timeit: {t1 / t4} trace: {trace1 / trace4}")



# s = Spiller(include_code=False)
# s.start_spill()
# tri4(3)
# s.stop_spill()
# s.save_spillfile(SPILLFILE)
# a = SpillAnalyser(SPILLFILE)
# print(a.line_timings())
# pprint(s.report())

