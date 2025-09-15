def my_append(lst, item):
    
    new_list = lst + [item]
    return new_list

def my_pop(lst):
    
    if len(lst) == 0:
        return "List is empty!"
    return lst[:-1]

def my_delete(lst, index):
    
    if index >= len(lst):
        return "Index too big!"
    new_list = lst[:index] + lst[index+1:]
    return new_list