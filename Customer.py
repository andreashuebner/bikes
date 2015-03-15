class Customer():
    ''' Class that represent a customer with a name, an amount of money and an instance of Bike as own bike '''
    def __init__(self,name,money=0):
        ''' Constructor function for customer
        
        Args:
            name: Name of customer {string}
            money: Optional start money for customer {number}
            
        Raises:
            Type error when name parameter not provided
            or parameter money not a number
            
       ''' 
        if name == None:
            raise TypeError("Required first parameter name")
        self._name = name
        self._money = money
        try:
            self._money = int(self._money)
        except:
            raise TypeError("Second parameter for money needs to be a number")
            
    def get_fund(self):
        ''' Returns available fund of customer
        
        Returns:
            Available fund in USD {int}
            
        '''
        
        return int(self._money)
    
    def add_fund(self,moneyToAdd):
        ''' Add money to customer's fund
        
        Args:
            moneyToAdd: Money to add {int}
            
        Raises:
            TypeError in case parameter moneyToAdd not provided
            or cannot be casted to int
        '''
        
        if moneyToAdd == None:
            raise TypeError("Requires one number as parameter")
        try:
            self._money = self._money + int(moneyToAdd)
        except:
            raise TypeError("Money to be added needs to be a number")
            
        