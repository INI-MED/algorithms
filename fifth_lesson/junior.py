import time
from single import Array, VectorArray


class ArrayInterface:

    def __init__(self):
        self.single_array = Array()
        self.vector_array = VectorArray()

    def get(self, index: int):
        return self.single_array.get(index)

    def put(self, item: int):
        self.vector_array.put(item)

    def put_on_ind(self, item: int, index: int):
        self.single_array.put_on_ind(item, index)

    def size(self):
        return self.single_array.size()

    def is_empty(self) -> bool:
        return self.size() == 0


class TestClass:
    def __init__(self, total: int):
        self.total = total
        self.data = ArrayInterface()

    def test_put(self):
        start = time.time()
        for item in range(self.total):
            self.data.put(item)
        return f"{self.total}: {time.time() - start}"


t = TestClass(10).test_put()
t1 = TestClass(100).test_put()
t2 = TestClass(1000).test_put()
t3 = TestClass(10000).test_put()
t4 = TestClass(100000).test_put()
t5 = TestClass(1000000).test_put()

print(t + "\n" + t1 + "\n" + t2 + "\n" + t3 + "\n" + t4 + "\n" + t5)

