import random

class RandomNumberGenerator:
    def __init__(self):
        self.numbers = [-1, 0, 1, 2, 3]
        self.probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]

    def nextNum(self):
        # Use random.choices to select a number with the specified probabilities
        return random.choices(self.numbers, self.probabilities)[0]

# Test the method
rng = RandomNumberGenerator()
results = {num: 0 for num in rng.numbers}
for _ in range(1000):
    num = rng.nextNum()
    results[num] += 1

print(results)
