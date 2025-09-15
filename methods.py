from init import MyList  

numbers = MyList()

print("Original list:", numbers.lst)


new_numbers = numbers.my_append(5)
print("After adding 5:", new_numbers)


shorter_list = numbers.my_pop()
print("After removing last item:", shorter_list)


final_list = numbers.my_delete(1)
print("After deleting item at index 1:", final_list)

print("Final state of list inside object:", numbers.lst)
