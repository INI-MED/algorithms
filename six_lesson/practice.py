import random


class SortClass:

	def __init__(self, arr: list): 
		self.arr = arr

	def swap(self, a: int, b: int): 
		x = self.arr[a]
		self.arr[a] = self.arr[b]
		self.arr[b] = x

	def sort(self): 
		for item in range(len(self.arr)//2 - 1):
			self.move_max_to_root(item, len(self.arr))
		for item in range(len(self.arr) - 1): 
			self.swap(0, item)
			self.move_max_to_root(0, item)
		return self.arr

	def move_to_max_root(self, root: int, size: int): 
		for item in range(root+1): 
			if self.arr[root] < self.arr[item]: 
				self.swap(root, item)

	def move_max_to_root(self, root: int, size: int): 
		l = 2 * root + 1
		r = 2 * root + 2
		x = root
		if l < size and self.arr[l] > self.arr[x]: 
			x = l
		if r < size and self.arr[r] > self.arr[x]: 
			x = r 
		if x == root: 
			return
		self.swap(x, root)
		self.move_to_max_root(x, size)


def insertion() -> list:
	arr = [random.randint(0, 10) for _ in range(10)]
	sort = SortClass(arr)
	return sort.sort()


f = insertion()
print(f)





