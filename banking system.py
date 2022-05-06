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
    while(True):
        print("1 . Create account")
        print("2 . view balance")
        print("3. Deposite money")
        print("4. Withdraw money")
        print("5. transfer money")

        c=input()
        if c not in ["1","2","3","4","5"]:
            continue
        else:
            c = int(c)

        if c ==1:
            c1 = input("enter your first name: ")
            c2 = input("enter your last name : ")
            c3 = input("enter your gender : ")
            c4 = input("enter your age : ")
            user(c1,c2,c3,c4)
            print("account created sucessfully")
            print(self.first,self.last,self.gender,self.age,self.email)























        

    
