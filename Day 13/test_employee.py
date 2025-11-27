import unittest
from employee import Employee

class TestEmployee (unittest.TestCase):

    def setUp(self):
        self.first_name = "Alex"
        self.last_name = "Russel"
        self.annual_salary = 100000
        self.salary_raise = 10000
    
    def test_default_salary_raise(self):
        self.employee_alex = Employee(self.first_name,self.last_name,self.annual_salary)
        self.employee_alex.give_raise()
        self.assertEqual("Alex", self.employee_alex.first_name)
        self.assertEqual("Russel", self.employee_alex.last_name)
        self.assertEqual(105000, self.employee_alex.annual_salary)

    def test_custom_salary_raise(self):
        self.employee_alex = Employee(self.first_name,self.last_name,self.annual_salary)
        self.employee_alex.give_raise(10000)
        self.assertEqual("Alex", self.employee_alex.first_name)
        self.assertEqual("Russel", self.employee_alex.last_name)
        self.assertEqual(110000, self.employee_alex.annual_salary)
                
unittest.main()
    
