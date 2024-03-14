def remove_duplicates(sorted_array):
    if not sorted_array:
        return []

    
    unique_elements = [sorted_array[0]]

    
    for num in sorted_array[1:]:
    
        if num != unique_elements[-1]:
            unique_elements.append(num)

    return unique_elements


input_array = [15, 14, 25, 14, 32, 14, 31]
result_array = remove_duplicates(sorted(input_array))


print("Original Array:", input_array)
print("Array without duplicates:", result_array)
