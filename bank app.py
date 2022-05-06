
def operation():
            op = int(input("enter the operation no. :-1. viewbalance 2. deposit 3. withdraw 4. transfer "))




class user():
    def __init__(self,first,last,gender,age):
        self.first = first.strip().title
        self.last = last.strip().title
        self.gender = gender
        self.email = first+"."+last+"@"+"itvedant.com"
        self.age = age
    
class bank(user):
    def __init__(self,first,last,gender,age):
        super().__init__(first,last,gender,age)
        self.__balance = 0

    def viewbalance(self):
        if op == "1":
            print(f" current balance : {self.__balance}")

    def deposite(self,amt):
        self.__balance = self.__balance + amt

    def withdraw(self,amt):
        if(amt>100 and amt<self.__balance):
            self.__balance = self.__balance - amt
            print(f"current balance is {self.__balance}")
        else:
            print("insufficient balance")

    def transfer(self,user,amt):
        if (self.__balance>=amt and amt>0):
            self.__balance = self.__balance - amt
            user.__balance = user.__balance + amt
            

        
if(__name__ == "__main__"):
    user1 = bank("rohit","yadav","male",19)
    user2 = bank("raj","pal","male",10)

'''def operation():
    op = int(input("enter the operation no. :-1. viewbalance 2. deposit 3. withdraw 4. transfer "))
    if op ==1:
        a = input("enter you id: ")
        if a==user1:
            print({self.__balance})
        elif a==user2:
            print({self.__balance})
'''
