class ATMcard:
    def __init__(self, defaultPin, defaultBalance):  #argument
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance

    def checkPin(self):
        return self.defaultPin #each method need to return itself
    def checkBalance(self):
        return self.defaultBalance