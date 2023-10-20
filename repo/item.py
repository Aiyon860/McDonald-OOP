import csv

class Item:
    pay_rate = 1.0
    all = []
    def __init__(self, name: str, price: float, quantity = 0, isTakeaway = False):
        # Run validations to the received arguments
        assert type(name) == str
        assert type(price) == float
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert type(quantity) == int
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero!"
        assert type(isTakeaway) == bool
        assert isTakeaway == True or isTakeaway == False, f"Error: {isTakeaway}; No options other than 'True or False' !"

        # Assign to self object
        self.__name = name
        self.__price = price
        self.__quantity = quantity
        self.__isTakeaway = isTakeaway

        # Actions to execute ()
        Item.all.append(self)

        ### Getter and Setter 
        @property
        def name(self):
            return self.__name
        
        @name.setter
        def name(self, value):
            if value == '':
                raise Exception("Cannot fill the name with null value!")
            elif value == ' ':
                raise Exception("Cannot fill the name with blank value!")
            elif len(value) > 10:
                raise Exception("The name is too long!")
            else:
                self.__name = value
                print(f"Setting a value: '{self.__name}'")

        @property
        def price(self):
            return self.__price
        
        @price.setter
        def price(self, value):
            if value < 0:
                raise Exception("The price cannot under 0 !")
            else: 
                self.__price = value
                print("Getting a value: '{self.__price}'")

        @property
        def quantity(self):
            return self.__quantity
        
        @quantity.setter
        def quantity(self, value):
            if value < 0:
                raise Exception("The quantity cannot under 0 !")
            else:
                self.__quantity = value
                print("Getting a value: '{self.__quantity}'")

    """ def __receipt(self):

    def get_receipt(self):
        return __receipt() """

    