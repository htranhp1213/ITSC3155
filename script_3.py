def char_count(str):
    dict = {} # declare dictionary without size and initialiation
    for i in str:   # loop through the string
        key = dict.keys()
        if i in key:
            dict[i] += 1 # move to next element in key when it's already exist
        else:
            dict[i] =1
    return dict
str = input("Enter a string: ")
print(str)
print(char_count(str))
