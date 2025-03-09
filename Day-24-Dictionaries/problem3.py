countries = ["India", "France", "Japan", "Canada"]
capitals = ["New Delhi", "Paris", "Tokyo", "Ottawa"]

countries_capitals = dict(zip(countries,capitals))

country_name = input("Enter a country name:")


if country_name in  countries_capitals:
    print(f"The capital of {country_name} is {countries_capitals[country_name]} ")
else:
    print(f"sorry country is not in the list")






