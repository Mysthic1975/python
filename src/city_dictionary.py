# city_dictionary.py

class CityDictionary:
    def __init__(self):
        self.cities = {}

    def add_city(self, city_id, city_name):
        if city_id not in self.cities:
            self.cities[city_id] = city_name
            print(f"Die Stadt '{city_name}' wurde hinzugefügt.")
        else:
            print(f"Die Stadt-ID {city_id} ist bereits in Verwendung.")

    def delete_city(self, city_id):
        if city_id in self.cities:
            del self.cities[city_id]
            print(f"Die Stadt mit ID {city_id} wurde gelöscht.")
        else:
            print(f"Ungültige Stadt-ID: {city_id}")

    def get_cities(self):
        return self.cities
