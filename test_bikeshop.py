import unittest

from Bikeshop import BikeShop
from Bike import Bike
from Customer import Customer

class TestBikeBikeShop(unittest.TestCase):
    def test_create_bike_shop(self):
        bikeShop = BikeShop("Andreas Bikeshop",10)
        self.assertIsInstance(bikeShop,BikeShop,"Should be able to create instance of BikeShop")
        
        with self.assertRaises(TypeError,msg = "Trying to create instance of BikeShop without name raises TypeError"):
            bikeShop = BikeShop()
            
        with self.assertRaises(TypeError,msg = "Trying to create instance of BikeShop without non number as margin parameter\
        raisesTypeError"):
            bikeShop = BikeShop("Andreas","Peter")
            
    def test_add_bikes_to_bikeshop(self):
        bikeShop = BikeShop("Andreas Bikeshop",20)
        bike1 = Bike("Slow bike",30,500)
        bike2 = Bike("Medium bike",40,600)
        bike3 = Bike("Fast bike",50,700)
        customer1 = Customer("Andreas")
        
        with self.assertRaises(TypeError,msg = "Try to calling add bike method with non bike object should raise Error"):
            bikeShop.add_bike(customer1)
            
        bikeShop.add_bike(bike1)
        bikeShop.add_bike(bike2)
        bikeShop.add_bike(bike3)
        self.assertItemsEqual([bike1,bike2,bike3],bikeShop.return_bikes(),msg="After adding bike1, bike2 and bike3,\
        all three bikes should be owned by the bikeshop I added them to")
        
    def test_return_bikes_below_price(self):
        shop1 = BikeShop("Andreas Bikeshop",10) #shop with margin of 10%
        bike1 = Bike("Cheap bike",30,100) #this will cost 110
        bike2 = Bike("Expensive bike",40,500) #this will cost 550
        bike3 = Bike("Medium expensive bike",40,300) #this will cost 330
        bike4 = Bike("Another cheap bike",45,200) #this will cost 220
        shop1.add_bike(bike1)
        shop1.add_bike(bike2)
        shop1.add_bike(bike3)
        shop1.add_bike(bike4)
        
        with self.assertRaises(TypeError,msg = "Trying to call function return_bikes_for_budget with non number\
        for budget raises TypeError"):
            shop1.return_bikes_for_budget("Andreas")
        self.assertItemsEqual([bike1,bike3,bike4],shop1.return_bikes_for_budget(330),msg="After adding 4 bikes and asking\
        for all bikes up to 330 USD, all bikes costing up to 330 usd after adding margin are return")
        
        
        
        