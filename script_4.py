sum = 0
for i in range (5):
    
    while True: # repeat the try and except block until input is int
        
        try:
            print('Enter int #',(i+1), ': ', end = '')
            myInt = input() # accept input, whatever kinds
            if (int(myInt)): # cast input into int, if true, conditional block execute
                int(myInt)
            break
        except ValueError:
            print('Invalid input. Please enter an int')
            
    sum += int(myInt)
print ('Your sum is', sum)
        