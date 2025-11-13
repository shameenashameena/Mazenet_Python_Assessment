# Exercise 2: List Manipulation

def get_even_numbers(numbers):
    even_nums = []
    for num in numbers:
        if num % 2 == 0:
            even_nums.append(num)
    return sorted(even_nums, reverse=True)


nums = [10, 3, 8, 5, 12, 7, 4]
result = get_even_numbers(nums)
print(result)
