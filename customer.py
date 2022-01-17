class Customer:#enter new parameter
    def __init__(self, id, custPin= 1234 , custBalance = 10000):
        self.id = id
        self.pin = custPin
        self.balance = custBalance

    def checkId(self): #each method return the value of itself
        return self.id
    def checkPin(self):
        return self.pin
    def checkBalance(self):
        return self.balance
    def changePins(self, newPin):
        self.pin = newPin
    def changeBalance(self, newBalance):
        self.balance += newBalance #adding balance

    def withdrawBalance(self, nominal): #new function for debit
        self.balance -= nominal
    def depositBalance(self, nominal): #new function for saving
        self.balance += nominal
