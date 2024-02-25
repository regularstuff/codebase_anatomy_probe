from timeit import timeit
from pprint import pprint




# t1 = timeit("tri1(300)", setup="from triangles import tri1", number=3)
# t2 = timeit("tri2(300)", setup="from triangles import tri2", number=3)
# t3 = timeit("tri3(300)", setup="from triangles import tri3", number=3)
# t4 = timeit("tri4(300)", setup="from triangles import tri4", number=3)
# print(t1, t2, t3, t4)


SPILLFILE = "/tmp/spill1.pickle"
from spiller import Spiller
s = Spiller(include_code=False)
from triangles import tri1

s.start_spill()
for i in range(2):
    tri1(0)
s.stop_spill()
s.save_spillfile(SPILLFILE)

from spill_analysis import SpillAnalyser

a1 = SpillAnalyser(spillfile=SPILLFILE)

pprint(a1.line_timings())


