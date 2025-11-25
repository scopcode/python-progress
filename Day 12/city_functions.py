def formatted_city_country(city, country, population = ""):
    if population:
        city_country_population = city + ", " + country + ", " + population
        return city_country_population.title()
    else:
        city_country = city + ", " + country
        return city_country.title() 