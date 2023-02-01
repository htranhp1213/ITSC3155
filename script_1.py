def get_unique_list(list):
    v2 = [] # new list to store unique element
    for i in list:
       if i not in v2:
        v2.append(i)
    
    return v2

my_list = [1, 2, 3, 2, 1, 4]
unique_list = get_unique_list(my_list)
print(unique_list)
