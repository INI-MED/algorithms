

class DynamicArray:

    def __init__(self, capacity: int = 0):
        self.index = 0
        self.capacity = capacity
        self.arr = [None for _ in range(self.capacity)]
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def __getitem__(self, item):
        if not -self.size <= item < self.size:
            raise IndexError
        return self.arr[item]

    def __setitem__(self, key, value):
        self.arr[key] = value

    def is_empty(self) -> bool:
        return self.size == 0

    def clear(self) -> None:
        for i in range(self.size):
            self.arr[i] = None

    def add(self, elem) -> None:
        if self.size + 1 >= self.capacity:
            if self.capacity == 0:
                self.capacity = 1
            else:
                self.capacity *= 2
            new_arr = DynamicArray(self.capacity)
            for i in range(self.size):
                new_arr[i] = self.arr[i]
            self.arr = new_arr
        self.arr[self.size] = elem
        self.size += 1

    def remove_at(self, rm_index: int):
        if rm_index >= self.size or rm_index < 0:
            raise IndexError
        data = self.arr[rm_index]
        new_arr = DynamicArray(self.size - 1)
        i, j = 0, 0
        while i < self.size:
            if i == rm_index:
                j -= 1
            else:
                new_arr[j] = self.arr[i]
            i += 1
            j += 1
        self.arr = new_arr
        self.size -= 1
        return data

    def index_of(self, elem) -> int:
        for i in range(self.size):
            if elem == self.arr[i]:
                return i
        return -1

    def remove(self, elem) -> bool:
        index = self.index_of(elem)
        if index == -1:
            return False
        self.remove_at(index)
        return True

    def __contains__(self, item) -> bool:
        return self.index_of(item) != -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index > self.size:
            raise StopIteration
        else:
            data = self.arr[self.index]
            self.index += 1
            return data


if __name__ == "__main__":
    print(DynamicArray())
