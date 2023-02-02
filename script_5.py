class BankAccount():
    #name = input('Enter your name: ')
    #balance = 0.0
    def __init__(self, name, balance = 0.0):
        self.name = name #self.name ~ this.name = name//parameters in java
        self.balance = balance

    def get_balance(self):
        str = '{} has a balance of {}'.format(self.name, self.balance)
        return str
         #hardcode name and balance since they can be changed due to users
         #{}:1 for name, {}:2 for balance
    def deposit(self, amount):
                    
        self.balance += amount
        print('After deposit:',self.get_balance())
    
    def withdraw(self, amount):

        if amount<=self.balance: # if the amount requested to withdraw is within acc balance
            self.balance -= amount
            print('After withdrawal:',self.get_balance())

        else:
            print('You will reach your limited balance and get overwithdraw fees')
            print('After withdrawal,',self.get_balance())
# creating an object of BankAccount
s = BankAccount('Tran', 100.0)
  
# Calling functions with that class object
print(s.get_balance())
s.deposit(150.0)
s.withdraw(80.0)

