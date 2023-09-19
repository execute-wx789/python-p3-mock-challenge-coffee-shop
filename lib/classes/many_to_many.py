class Coffee:
    all = []
    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)
        
    def orders(self):
        return [order for order in Order.all if order.coffee is self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        listHold = self.orders()
        return (sum([sumHold.price for sumHold in listHold]))/len(listHold)
    
    def __setattr__(cls,name,value):
        if hasattr(cls,"name"):
            pass
        else:
            super().__setattr__(name,value)


class Customer:
    all = []
    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if isinstance(name,str) and 1 <= len(name) <= 15:
            self._name = name
        
    def orders(self):
        return [order for order in Order.all if order.customer is self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        new_order = Order(self,coffee,price)
        return new_order


    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    def __setattr__(cls,name,value):
        if hasattr(cls,"price"):
            pass
        else:
            super().__setattr__(name,value)

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self,customer):
        if isinstance (customer,Customer):
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self,coffee):
        if isinstance (coffee,Coffee):
            self._coffee = coffee