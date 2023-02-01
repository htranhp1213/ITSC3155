def get_combined_dict(dict1, dict2):
    dict3 = {}
    for key in dict1:
        if key in dict2:
           n = int(dict1.get(key) + dict2.get(key)) #add value of the same key in both dict
           dict3[key] = n
           #dict3.add(key, n)
    return dict3
        

my_dict_1 = {'a': 5, 'b': 12, 'c': 3, 'd': 9}
my_dict_2 = {'b': 4, 'c': 9, 'd': 10, 'e': 16}
combined_dict = get_combined_dict(my_dict_1, my_dict_2)
print(combined_dict)
    
