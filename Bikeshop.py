from Bike import Bike

class BikeShop():
    ''' Class that represents a bike shop '''
    
    
    def __init__(self,name,margin=20):
        ''' Constructor function for BikeShope
        
        Args:
            name: Name of bike shop {string}
            [margin]: Margin to apply to cost of bike in perc (so 10 = 10%). Defaults to 20%. If a float is given as parameter, will be cast to int 
            
        '''
        self._name = name
        try:
            self._margin = int(margin)
        except:
            raise TypeError("Parameter margin needs to be an integer")
        self._listBikes=[] #list of bikes
        
    def add_bike(self,bike):
        ''' Function to add a bike
        
        Args:
            bike: Bike object to add {instance of bike}
            
        Raises:
            TypeError if bike is not an instance of Bike
            
       '''
        
        if not isinstance(bike,Bike):
            raise TypeError("You can only add a bike to the bike shop")
         
        #calculate price
        
        self._listBikes.append(bike)
    def return_bikes_for_budget(self,budget):
        '''Return all bikes in list that can be purchased with certain budget
        
        Args:
            budget: The budget to check (will be rounded to int) {int}
        Returns:
            All bikes in list that can be purchases with this budget
            
        Raises:
            TypeError if budget not a number
            
        '''
        
        try:
            budget = int(budget)
        except:
            raise TypeError("Available budget needs to be number")
            
        listAffordableBikes = []
        for bike in self._listBikes:
            price = int(bike.get_cost() * (1 + (self._margin/100)))
            if price <= budget:
                listAffordableBikes.append(bike)
                
        return listAffordableBikes
    def return_bikes(self):
        ''' Returns all bikes owned by bike shop 
        
        Returns:
            List with all bikes owned [<Bike>]
        '''
        
        return self._listBikes
        