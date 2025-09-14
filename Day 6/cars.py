def car_details(manufacturer, model, **car_info) :
    car = {}
    car["Manufacture"] = manufacturer.title()
    car["Car Model"] = model.title()
    for key,value in car_info.items():
        car[key.title()] = value.title()
    return car

car_1 = car_details("suzuki", "wagon r", type = "sedan", price = "economy")
car_2 = car_details("subaru", "outback", color = "blue", tow_package = "True")
print(car_1)
print(car_2)
    