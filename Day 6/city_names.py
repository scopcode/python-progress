def city_country(city,country):
    message  = ('"' + city.title() + ', ' + country.title() + '"')
    return message

sentence = city_country("delhi","india")
print(sentence)
sentence = city_country("moscow","russia")
print(sentence)
sentence = city_country("miami","america")
print(sentence)
