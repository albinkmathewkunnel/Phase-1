def count_up_to(max_num):
    count = 1
    while count <= max_num:
        yield count  # Pauses execution and returns the current number
        count += 1   # Resumes here on the next call

# Calling the function returns a generator object, it doesn't run the code yet
counter = count_up_to(3)

# You extract values manually using next() or automatically with a loop
print(next(counter))  # Output: 1
print(next(counter))  # Output: 2
print(next(counter))  # Output: 3
# print(next(counter)) # Raises StopIteration because the function finished
