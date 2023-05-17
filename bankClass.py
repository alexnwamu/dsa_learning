class bank:
    def __init__(self,accNO,name,balance):
        self.account = accNO
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f'You have successfully deposited {amount} your new balance is {self.balance}')
        return



class saving(bank):
    def __init__(self, accNO, name, balance):
        super().__init__(accNO, name, balance)
        self.interest = 5
    def checkinterest(self):
        print('Your interest is',self.interest)
        return
    
alex = saving(200,'james',20000)

alex.checkinterest()
