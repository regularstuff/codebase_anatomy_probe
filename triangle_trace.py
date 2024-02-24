""" Tracing exercise
Four approaches to calculating triangle numbers
"""
from pprint import pprint
import spiller
import triangles

tri2spill = spiller.Spiller()
tri2spill.start()
triangles.tri2(500)
tri2spill.stop()
tri2spill.save_spillfile("/tmp/tri2_spill.pickle")

del tri2spill

a_spill = spiller.Spiller()
a_spill.load_spillfile("/tmp/tri2_spill.pickle")
pprint(a_spill.report())
