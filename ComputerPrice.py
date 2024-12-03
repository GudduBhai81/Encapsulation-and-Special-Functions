class Computer:
    def __init__(self):
        self.__minprice = 90000
    def sell(self):
        print("Selling Price = {}".format(self.__minprice))
    def setMaxPrice(self, price):
        self.__minprice = price
c = Computer ()
c.sell()

c.__minprice= 100000
c.sell()

c.setMaxPrice (100000)
c.sell()