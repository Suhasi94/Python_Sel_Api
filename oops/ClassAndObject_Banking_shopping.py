# OOPS 2 and 3
# class and object
#----------------------- BANKING CLASS ------------------------#

class BankAccount:
    # shared by all the customers or instance of BankAccount class
    interest_rate = 0.04   #class variable
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        self.transactions = []
        self.transactions.append(f"***** Initial deopsit : {balance} *****")

    def deposit(self, amount):
        self.balance = self.balance + amount
        self.transactions.append(f"amount deposited : {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise Exception("Insufficient Funds")
        self.balance = self.balance - amount
        self.transactions.append(f"amount withdrawn : {amount}")

    def statement(self):
        for item in self.transactions:
            print(item)
        print(f"****** total balance {self.balance} *****")

    def transfer_funds(self, to_account, amount):
        if amount > self.balance:
            raise Exception("Insufficient funds!!")
        to_account.deposit(amount)
        self.balance -= amount

    def roi(self):
        interest_amount = self.balance * BankAccount.interest_rate
        self.balance = self.balance + interest_amount
        

c1 = BankAccount("steve", 1000)
c2 = BankAccount("marry", 3000)
c3 = BankAccount("job", 2000)
c4 = BankAccount("jon")


#---------------------------------------------------------------------------------------
#------------------------------------- Shopping cart ----------------------------------#
class ShoppingCart:
    # class variable
    prices = {"iPhone": 800, "iMac": 2500, "iWatch": 3000, "iPad": 3500}
    products = {"iPhone": 5, "iMac": 3, "iWatch": 2, "iPad": 4}
    
    def __init__(self):
        self.cart = []

    def add_item(self, name, quantity):
        if name not in Shoppingcart.products:
            raise Exception("Product not available")
        elif quantity > shoppingcart.products[name]:
            raise Exception("Product out of stock")
        else:
            self.cart.append({"name": name, "quantity": quantity, "price": ShoppingCart.prices[name]})
            ShoppingCart.products[name] -= quantity

    def remove_item(self, name):
        for item in self.cart:
            if name == item['name']:
                if item['quantity'] > 1:
                    item['quantity'] = item['quantity'] - 1
                else:
                    self.cart.remove(item)

    def total_cost(self):
        total = 0.00
        for item in self.cart:
            total += item['quantity'] * item['price']
        return total
    
c1 = ShoppingCart()
c2 = ShoppingCart()
