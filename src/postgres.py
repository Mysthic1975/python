import psycopg2
from src.city_dictionary import CityDictionary


class DatabaseModel:
    def __init__(self, host="localhost", port="5433", dbname="postgres", user="postgres", password="admin"):
        self.connection = psycopg2.connect(
            host=host, port=port, dbname=dbname, user=user, password=password
        )
        self.create_table_if_not_exists()  # Tabelle direkt nach Verbindung erstellen

    def create_table_if_not_exists(self):
        with self.connection.cursor() as cursor:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS cities (
                    id SERIAL PRIMARY KEY,
                    name TEXT UNIQUE NOT NULL
                )
            ''')
        self.connection.commit()

    def get_data(self):
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM cities")
            return cursor.fetchall()

    def insert_data(self, city_id, city_name):  # Changed parameter name
        with self.connection.cursor() as cursor:
            cursor.execute("INSERT INTO cities (id, name) VALUES (%s, %s)", (city_id, city_name,))
            self.connection.commit()

    def update_city(self, city_id, new_city_name):
        with self.connection.cursor() as cursor:
            cursor.execute("UPDATE cities SET name = %s WHERE id = %s", (new_city_name, city_id,))
            self.connection.commit()

    def delete_city(self, city_id):  # Changed parameter name
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM cities WHERE id = %s", (city_id,))
            self.connection.commit()

    def delete_all_data(self):
        with self.connection.cursor() as cursor:
            cursor.execute("DELETE FROM cities")
        self.connection.commit()


class DataView:
    @staticmethod  # Mark the method as static
    def display_data(data):
        if not data:
            print("Die Liste ist leer.")
        else:
            for city_id, city_name in data.items():
                print(f"{city_id}: {city_name}")


class DataController:
    def __init__(self):
        self.model = DatabaseModel()
        self.view = DataView()
        self.city_dict = CityDictionary()  # Create an instance of CityDictionary
        self.load_data_from_db()  # Load data from database into dictionary

    def load_data_from_db(self):
        data = self.model.get_data()  # Get data from database
        for row in data:
            self.city_dict.add_city(row[0], row[1])  # Add each city to the dictionary

    def get_and_display_data(self):
        self.view.display_data(self.city_dict.get_cities())  # Display data from dictionary

    def add_city(self, city_id, city_name):  # Add the city_id and city_name parameters
        if city_id not in self.city_dict.get_cities():
            self.city_dict.add_city(city_id, city_name)  # Add city to dictionary
        else:
            print(f"Die Stadt-ID {city_id} ist bereits in Verwendung. Bitte wählen Sie eine andere ID.")

    def delete_city(self, city_id):  # Changed parameter name
        self.city_dict.delete_city(city_id)  # Delete city from dictionary

    def update_city(self, city_id, new_city_name):
        self.city_dict.update_city(city_id, new_city_name)  # Update city in dictionary

    def save_data_to_db(self):
        self.model.delete_all_data()  # Delete all data from database
        cities = self.city_dict.get_cities()  # Get data from dictionary
        for city_id, city_name in cities.items():
            if city_id in self.model.get_data():
                self.model.update_city(city_id, city_name)  # Update city in the database
            else:
                self.model.insert_data(city_id, city_name)  # Insert each city into the database
