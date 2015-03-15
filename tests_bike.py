import unittest
from Bikeshop import BikeShop
from Bike import Bike


class TestBike(unittest.TestCase):
    def test_create_bike(self):
        ''' Im am able to create a new instance of Bike and set and get attributes'''
        bike = Bike('Slow',30,550)
        self.assertIsInstance(bike,Bike,msg="bike is instance of Bike")
        with self.assertRaises(TypeError,msg="Trying to create instance of Bike without parameters should raise error"):
            bike = Bike()
        with self.assertRaises(TypeError,msg="Trying to create instance of Bike with non number for weight should raise error"):
            bike = Bike("Andreas","Peter",50)
        with self.assertRaises(TypeError,msg="Trying to create instance of Bike with non number for cost should raise error"):
            bike = Bike("Andreas",50,"Peter")
            
    def test_receive_bike_parameters(self):
        ''' After creating an instance of bike, I should be able to get the correct attributes with getter functions '''
        
        bike = Bike('Slow bike',40,800)
        self.assertEquals(bike.get_weight(),40)
        self.assertEquals(bike.get_cost(),800)
        
    
        
class TestBikeShop(unittest.TestCase):
    def test_create_bikeshop(self):
        ''' I am able to create a new instance of BikeShop class '''
        bikeShop = BikeShop()
        self.assertIsInstance(bikeShop,BikeShop,msg="bikeShop is instance of BikeShop")
        
 
        
