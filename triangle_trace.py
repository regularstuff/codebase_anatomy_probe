""" Tracing exercise
Four approaches to calculating triangle numbers
"""
from pprint import pprint
import spiller
import triangles

SPILLFILE = "/tmp/trace_spill.pickle"

mytrace = spiller.Spiller(include_code=False)
mytrace.start_spill()
result2 = triangles.tri2(3)
if result2 > 0:
    result1 = triangles.tri1(3)
if "result1" not in locals():
    pprint("wow")
    exit(1)
if result1 > result2:
    result3 = triangles.tri3(3)
else:
    result4 = triangles.tri4(3)
if "result3" in locals():
    result4 = triangles.tri4(3)
else:
    result3 = triangles.tri3(3)
prev = 0
for x in 4, 5, 6:
    count = triangles.tri1(x)
    if x <= prev:
        print("Wow again")
        exit(1)
    prev = x


mytrace.stop_spill()
mytrace.save_spillfile(SPILLFILE)


del mytrace

a_spill = spiller.Spiller()
a_spill.load_spillfile(SPILLFILE)
pprint(a_spill.report())
