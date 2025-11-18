class Car():

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 0 

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back odometer!")
    
    def increment_odometer(self,miles):
        self.odometer_reading += miles
    
    def fill_gas_tank(self,litres):
        self.gas_tank += litres
        print("This car has now " + str(self.gas_tank) + " litres of gas.")

class Battery():
    def __init__(self, battery_size = 70):
        self.battery_size = battery_size    
        
    def update_battery_size(self,newsize):
        oldsize = self.battery_size
        self.battery_size = newsize
        print("The battery has been updated to  " + str(self.battery_size) + " from " + 
              str(oldsize) )
        if self.battery_size <= 70:
            print("The range will be now 100 km")
        elif self.battery_size <= 140:
            print("The range will be now 200 km")
        elif self.battery_size <= 280:
            print("The range will be now 400 km")
        elif self.battery_size > 280:
            print("Infinity!")


    def get_range(self):
        if self.battery_size <= 70:
            print("The range will be 100 km")
        elif self.battery_size <= 140:
            print("The range will be 200 km")
        elif self.battery_size <= 280:
            print("The range will be 400 km")
        elif self.battery_size > 280:
            print("Infinity!")

    def describe_battery(self):
        print("This car has " + str(self.battery_size) + " kwh battery")

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()
    
    def fill_gas_tank(self):
        print("Are you out of you mind, this is an electric.")
    


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.update_battery_size(250)
my_tesla.battery.get_range()
my_tesla.fill_gas_tank()


my_elantra = Car("Hyundai", "Elantra", 2025)
print(my_elantra.get_descriptive_name())
my_elantra.fill_gas_tank(23)
