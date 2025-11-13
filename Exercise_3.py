# Excercise 3: Tuple and Set Operations

def sorted_elements(strings_list):
    # Step 1: Convert list to tuple
    strings_tuple = tuple(strings_list)

    # Step 2: Convert tuple to set to remove duplicates
    unique_set = set(strings_tuple)

    # Step 3: Convert set to sorted list
    sorted_list = sorted(list(unique_set))

    return sorted_list


data = ["apple", "banana", "apple", "cherry", "banana", "date"]
result = sorted_elements(data)
print(result)

