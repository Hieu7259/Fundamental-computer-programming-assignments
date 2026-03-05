import random
randompoints = int(input("Enter the number of random points to generate: "))
inside_circle = 0
for _ in range(randompoints):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
        inside_circle += 1
pi_estimate = 4 * inside_circle / randompoints
print(f"The estimated value of pi is: {pi_estimate}")