numbers = [1, 2, 3, 4, 5, 6]

def is_even(num):
    return num % 2 == 0

result = filter(is_even, numbers)

print(list(result))