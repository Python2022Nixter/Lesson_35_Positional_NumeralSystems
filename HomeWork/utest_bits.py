
import array
import unittest
from unittest import TestCase

def num_to_UP1(num, n):
    return num * 2**n

def num_to_UP2(num, n):
    return num << n

class Checker(TestCase):
    
    NUMBERS = 1000000
    UPS_TO = 10
    ARRAY = [i for i in range(NUMBERS)]
    ARRAY2 = []
    
    
    # def test_one(self):
    #     for i in self.ARRAY:
    #         self.ARRAY2.append(num_to_UP1(i, UPS_TO))
    #     self.assertEqual(num_to_UP1((self.ARRAY[self.NUMBERS - 1]), 1), self.ARRAY2[self.NUMBERS - 1])
    #     pass
    
    # def test_two(self):
    #     for i in self.ARRAY:
    #         self.ARRAY2.append(num_to_UP2(i, UPS_TO))
    #     self.assertEqual(num_to_UP2((self.ARRAY[self.NUMBERS - 1]), 1), self.ARRAY2[self.NUMBERS - 1])
    #     pass
    
    # def test_three(self):
    #     for i in self.ARRAY:
    #         num_to_UP1(i, self.UPS_TO)
    #     self.assertEqual(num_to_UP1((self.ARRAY[self.NUMBERS - 1]), self.UPS_TO), num_to_UP2((self.ARRAY[self.NUMBERS - 1]), self.UPS_TO))
    #     pass
    
    def test_four(self):
        for i in self.ARRAY:
            num_to_UP2(i, self.UPS_TO)
        self.assertEqual(num_to_UP1((self.ARRAY[self.NUMBERS - 1]), self.UPS_TO), num_to_UP2((self.ARRAY[self.NUMBERS - 1]), self.UPS_TO))
        pass
    
    
unittest.main()