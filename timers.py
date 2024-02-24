from timeit import timeit




t1 = timeit("tri1(300)", setup="from triangles import tri1", number=300)
t2 = timeit("tri2(300)", setup="from triangles import tri2", number=300)
t3 = timeit("tri3(300)", setup="from triangles import tri3", number=300)
t4 = timeit("tri4(300)", setup="from triangles import tri4", number=300)
print(t1, t2, t3, t4)

import spiller
spill1 = spiller.Spiller(include_code=False)
from triangles import tri1, tri2, tri3, tri4
spill1.start()
for i in range(5):
    tri1(5)
spill1.stop()
spill1.save_spillfile("/tmp/spill1.pickle")


