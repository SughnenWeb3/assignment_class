class Bank:
    #minimum_variable = 20 this is the best practice
    total_banks = []
    def __init__(self, name, type, branch):
        self.name = name
        self.type = type
        self.branch = branch
        self.isAdmin = False
        self.freezed = False
        self.min_bal = 20 #always use best practice instead of this

        Bank.total_banks +=1

    def freeze(self, account, freeze = True):
        account.freeze = freeze
        print(f"Sorry!, your {account.name}, your account number: [{account.number}] is frozen")
opay = Bank("Opay", "MFB", "Jos")
FB = Bank("First bank", "Commercial","Makurdi")

print(opay.__dict__)
print(FB.__dict__)
        