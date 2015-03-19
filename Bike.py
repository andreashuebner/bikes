class Bike():
    ''' Constructor function to create an instance of a bike class
    
    Args:
        model: The model of the bike {string}.
        weight: The weight of the bike in kg {int}.
        cost: The cost to procude the bike in usd {int}.
        
        Should either weight or cost be a float, 
        it will be cast silently to int
        
    Raises:
        RuntimeError in case one of arguments is missing
        or weight or cost cannot be cast to int
    '''
    
    def __init__(self,model,weight,cost):
        if model == None or weight == None or cost == None:
            raise TypeError ("Bike construct requires model, weight and cost as parameters")
        try:
            self._model = model
            self._weight = weight
            self._cost = cost
            #to check whether weight and cost are numbers
            self._weight = int(self._weight)
            self._cost = int(self._cost)
        except:
            raise TypeError("Parameters weight and cost need to be numbers")
            
    def get_weight(self):
        return self._weight
        
    def get_cost(self):
        return self._cost
    
    def get_model(self):
        return self._model
        