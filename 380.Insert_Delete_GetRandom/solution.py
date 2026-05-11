import random

class RandomizedSet:

    def __init__(self):
        self.values = []
        self.index_map = {}

    def insert(self, val: int) -> bool:
        if val in self.index_map:
            return False

        self.index_map[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.index_map:
            return False

        index = self.index_map[val]
        last_value = self.values[-1]

        self.values[index] = last_value
        self.index_map[last_value] = index

        self.values.pop()
        del self.index_map[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# We cannot remove directly from the middle of a list
# because it would shift elements left -> O(n)

# Trick:
# 1. Take the last element in the list
# 2. Move it into the spot of the element we want to remove
# 3. Update its index in the hashmap
# 4. Pop the last element from the list -> O(1)

# Example:
# values = [10, 20, 30, 40]
# remove 20 at index 1

# Move last element (40) into index 1:
# values = [10, 40, 30, 40]

# Pop the duplicate last element:
# values = [10, 40, 30]

# Update hashmap:
# 40 is now at index 1