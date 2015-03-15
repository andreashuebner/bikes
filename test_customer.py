import unittest

from Customer import Customer

class TestCustomer(unittest.TestCase):
    def test_create_customer(self):
        ''' Im able to create a customer with the required parameters '''
        bikeCustomer = Customer('Andreas')
        self.assertIsInstance(bikeCustomer,Customer,msg="I should be able to create an instance of Customer")
        
        with self.assertRaises(TypeError,msg="Should throw error when name parameter is missing"):
            bikeCustomer = Customer()
            
        with self.assertRaises(TypeError,msg="Should throw error when money parameter not a number"):
            bikeCustomer = Customer("Andreas","Peter")
            
    def test_add_substract_fund(self):
        bikeCustomer = Customer('Andreas')
        self.assertEquals(0,bikeCustomer.get_fund(),msg="Initial fund should be 0")
        
        bikeCustomer = Customer('Andreas',500)
        self.assertEquals(500,bikeCustomer.get_fund(),msg="When creating instance with\
        initial fund of 500, then getter function should return 500")
        
        bikeCustomer = Customer('Andreas',500)
        bikeCustomer.add_fund(200)
        self.assertEquals(700,bikeCustomer.get_fund(),msg="Add 200 to 500 fund should return 700 fund")
        
        