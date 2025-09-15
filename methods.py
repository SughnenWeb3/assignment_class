import init


numbers = [2,3,3,{}, "we"]
print("Original list:", numbers)

new_numbers = init.my_append(numbers, 5)
print("After adding 5:", new_numbers)


shorter_list = init.my_pop(new_numbers)
print("After removing last item:", shorter_list)

final_list = init.my_delete(shorter_list, 1)
print("After deleting item at index 1:", final_list)

print("Original list is still:", numbers)