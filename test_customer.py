import unittest

from Customer import Customer
from Bike import Bike

class TestCustomer(unittest.TestCase):
    def test_create_customer(self):
        ''' Im able to create a customer with the required parameters '''
        bikeCustomer = Customer("Andreas")
        self.assertIsInstance(bikeCustomer,Customer,msg="I should be able to create an instance of Customer")
        
        with self.assertRaises(TypeError,msg="Should throw error when name parameter is missing"):
            bikeCustomer = Customer()
            
        with self.assertRaises(TypeError,msg="Should throw error when money parameter not a number"):
            bikeCustomer = Customer("Andreas","Peter")
            
    def test_add_substract_fund(self):
        bikeCustomer = Customer("Andreas")
        self.assertEquals(0,bikeCustomer.get_fund(),msg="Initial fund should be 0")
        
        bikeCustomer = Customer("Andreas",500)
        self.assertEquals(500,bikeCustomer.get_fund(),msg="When creating instance with\
        initial fund of 500, then getter function should return 500")
        
        bikeCustomer = Customer("Andreas",500)
        bikeCustomer.add_fund(200)
        self.assertEquals(700,bikeCustomer.get_fund(),msg="Add 200 to 500 fund should return 700 fund")
        
        with self.assertRaises(TypeError,msg="Trying to add fund without parameter should raise TypeError"):
            bikeCustomer.add_fund()
            
        with self.assertRaises(TypeError,msg="Trying to add fund with non number parameter should raise TypeError"):
            bikeCustomer.add_fund("Andreas")
            
    def test_customer_buys_bike(self):
        bikeCustomer = Customer("Andreas")
        bikeCustomer.add_fund(800)
        bike = Bike("Medium bike",30,500) #for our tests the parameters are irrelevant
        
        with self.assertRaises(TypeError,msg="Trying to buy a bike requires number as price parameter"):
            bikeCustomer.buy_bike()
            
        with self.assertRaises(TypeError,msg="Try to buy a bike with non number parameter raises error"):
            bikeCustomer.buy_bike("Andreas")
        
        bikeCustomer = Customer("Andreas")
        bikeCustomer.add_fund(800)
        self.assertEquals(bikeCustomer.buy_bike(700,bike),True,msg="With funds of 800, buying a bike for 700 USD is possible")
        self.assertEquals(bikeCustomer.get_fund(),100,msg="After buying for 700 USD with funds of 800,\
        remaining fund should be 100")
        
        bikeCustomer = Customer("Andreas")
        bikeCustomer.add_fund(600)
        self.assertEquals(bikeCustomer.buy_bike(700,bike),False,msg="With funds of 600, not possible to buy bike for 700 USD")
        self.assertEquals(bikeCustomer.get_fund(),600,msg="With founds of 600 and not possible a bike,\
        the fund should remain unchanged with 600 USD")
        
        bikeCustomer = Customer("Andreas")
        bikeCustomer.add_fund(800)
        bikeCustomer.buy_bike(700)
        
        
        
        
       
        
        
        
        
        
        