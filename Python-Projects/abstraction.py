from abc import ABC, abstractmethod

class car(ABC):
	def paySlip(self,amount):
		pass

class DebitCardPayment(car):
	def payment(self, amount):
		print('Your purchase amount of {} exceeded your 100$ limit '.format(amount))

obj = DebitCardPayment()
obj.paySlip("101$")
obj.payment("101$")