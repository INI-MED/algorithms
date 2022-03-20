import random


class ArrayGeneration:
    def __init__(self, array_size: int):
        self.array_size = array_size
        self.random_array = []

    def random_array_gen(self) -> list:
        for item in range(self.array_size):
            self.random_array.append(random.randint(1, 100))
        return self.random_array


class Array:

    def __init__(self):
        self.array = ArrayGeneration(100).random_array_gen()

    def resize(self):
        new_array = []
        if not self.is_empty():
            new_array = self.array.copy()
        self.array = new_array

    def get(self, index: int) -> int:
        return self.array[index]

    def put(self, item: int):
        self.resize()
        self.array[self.size() - 1] = item

    def put_on_ind(self, item: int, index: int):
        return self.array.insert(index, item)

    def size(self) -> int:
        return len(self.array)

    def is_empty(self):
        return self.size() == 0


class VectorArray:

    def __init__(self):
        self.array = ArrayGeneration(100).random_array_gen()
        self.arr_size = 0
        # self.vector = vector

    def put(self, item: int):
        if self.size() == len(self.array):
            self.resize()
        self.array[self.size()] = item
        self.arr_size += 1
        print(self.arr_size)

    def size(self) -> int:
        return self.arr_size

    def resize(self):
        new_array = []
        if not self.is_empty():
            new_array = self.array.copy()
        self.array = new_array

    def get(self, index: int) -> int:
        return self.array[index]

    def put_on_ind(self, item: int, index: int):
        return self.array.insert(index, item)

    def is_empty(self):
        return self.size() == 0


class MatrixArray:

    def __init__(self):
        self.array = ArrayGeneration(100).random_array_gen()
        self.arr_size = 0 
        self.vector = 100

    def size(self) -> int: 
        return self.arr_size 

    def is_empty(self) -> bool: 
        return self.size() == 0

    def get(self, index: int) -> int:
        return self.array.get(self.arr_size / self.vector)[self.size % self.vector]

    def resize(self): 
        pass 

    def put(self, item: int): 
        if self.size() == len(self.array) * self.vector:
            self.array.put(Object[self.vector])
        self.array.get(self.arr_size / self.vector)[self.size % self.vector] = item
        self.arr_size += 1





