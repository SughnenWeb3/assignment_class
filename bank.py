import random

class Bank:

	total_banks = []

	def __init__(self, bank_name:str, bank_type:str, bank_branch:str):
		self.bank_name = bank_name
		self.bank_type = bank_type
		self.branches: list[str] = [bank_branch]
		self.all_accounts: list[str] = []
		self.total_customers: int = 0
		self.all_transactions: list[str] = []

firstbank = Bank("First Bank", "Commercial", "Lagos")
opay = Bank("OPAY", "MFB", "Jos")
palmpay = Bank("palmpay", "MFB", "Mkd")

class Account(Bank):
	def __init__(self, bank_name:str, bank_type:str, acc_name:str, acc_type:str, amount:float, bank_branch:str = "Abuja", email:bool = False, sms:bool = False, isadmin:bool = False, isfrozen:bool = False):
		Bank.__init__(self, bank_name, bank_type, bank_branch)
		self.acc_name = acc_name
		self.acc_type = acc_type
		self.balance = amount
		self.acc_number = random.randint(1000000000, 9999999999)
		self.txn_count = 0
		self.txns = []
		self.email = email
		self.sms = sms
		self.isadmin = isadmin
		self.isfrozen = isfrozen
		

	
	def add_user(self, acc_name)-> str:
		self.all_accounts.append({"name": acc_name, "acc_number": self.acc_number, "balance": self.balance})
		#print(self.all_accounts)
		return f"Account Name: {self.acc_name}, Account Balance: {self.balance}, Account Number: {self.acc_number}" 

	def deposit(self, amount:float)-> str:
		if self.isfrozen:
			print(f"This account: {self.acc_number} is frozen and cannot perform transactions at this time!")
			return 
		elif amount > 0:
			self.balance += amount
			self.txn_count += 1
			self.txns.append({"type": "deposit", "amount": amount})
			if self.sms == True:
				self.sms_credit_alert(amount)
				return
			if self.email == True:
				self.email_credit_alert(amount)
				return
			else:
				return "SUCCESS"
		else:
			return "Invalid amount!"

	def withdraw(self, amount)-> str:
		if self.isfrozen:
			print(f"This account: {self.acc_number} is frozen and cannot perform transactions at this time!")
			return
		elif amount <= 0:
			return "Invalid amount!"
		elif amount > self.balance:
			return "Insufficient balance!"
		else:
			self.balance -= amount
			self.txn_count += 1
			self.txns.append({"type": "withdrawal", "amount": amount})
			if self.sms == True:
				self.sms_debit_alert(amount)
				return
			if self.email == True:
				self.email_debit_alert(amount)
				return
			else:
				return "SUCCESS"


	def transfer(self, receiver, amount)-> str:
		if self.isfrozen:
			print(f"This account: {self.acc_number} is frozen and cannot perform transactions at this time!")
			return
		else:
			self.withdraw(amount)
			if self.sms == True:
				self.sms_debit_alert(amount)
			if self.email == True:
				self.email_debit_alert(amount)
			else:
				return "Transfer Successful"
			receiver.deposit(amount)
			if self.sms == True:
				self.sms_credit_alert(amount)
			if self.email == True:
				self.email_credit_alert(amount)
			else:
				return "Transfer Successful"

			
	def freeze(self):
		if self.isadmin == True:
			self.isfrozen = True
		else:
			self.isfrozen = False
			return "Only Admins can modify an Account!"

	def unfreeze(self):
		if self.isadmin == True:
			self.isfrozen = False
		else:
			self.isfrozen = True
			return "Only admins can modify an Account!"

	def sms_credit_alert(self, amount):
		print(f"""
		SMS ALERT!
		Acct: {self.acc_number}
		Amount: ${amount} CR
		Desc: Incoming Deposit from {self.acc_name}
		Available Bal: {self.balance}
		Date:
		""")

	def sms_debit_alert(self, amount):
		print(f"""
		SMS ALERT!
		Acct: {self.acc_number}
		Amount: ${amount} DB
		Desc: Outgoing Withdrawal from {self.acc_name}
		Available Bal: {self.balance}
		Date:
		""")

	def email_credit_alert(self, amount):
		print(f"""
		EMAIL ALERT!
		Dear {self.acc_name},
		We wish to Inform you that a Credit transaction occurred on your account with us.
		The details of this transaction are shown below:
		Acct: {self.acc_number}
		Amount: ${amount}
		Desc: VIA 101CT000006075-DATA
		Value Date:
		Remarks: 
		Time of Transaction:
		Document number: 6075459008
		Available Balance: $ {self.balance}
		""")

	def email_debit_alert(self, amount):
		print(f"""
		EMAIL ALERT!
		Dear {self.acc_name},
		We wish to Inform you that a Debit transaction occurred on your account with us.
		The details of this transaction are shown below:
		Acct: {self.acc_number}
		Amount: ${amount}
		Desc: VIA 101CT000006075-DATA
		Value Date:
		Remarks: 
		Time of Transaction:
		Document number: 6075459008
		Available Balance: $ {self.balance}
		""")




mp = Account(firstbank.bank_name, firstbank.bank_type, "MP", "Savings", 1000)
tosin = Account("OPAY", "MFB", "Tosin", "Savings", 2000, "Jos", True, True)


print(tosin.add_user("Tosin"))
print()
print(tosin.deposit(1000))
print()
print(tosin.withdraw(500))
print()
print(tosin.transfer(mp, 200))


print(mp.__dict__)
print()
print(tosin.__dict__)
print()
print(opay.__dict__)