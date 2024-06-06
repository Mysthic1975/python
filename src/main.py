from src.postgres import DataController

if __name__ == "__main__":
    controller = DataController()
    while True:
        print("\nWähle eine Aktion:")
        print("1: Städte anzeigen")
        print("2: Stadt hinzufügen")
        print("3: Stadt löschen")
        print("4: Stadt aktualisieren")
        print("5: Beenden")

        choice = input("Deine Wahl: ")

        if choice == "1":
            controller.get_and_display_data()
        elif choice == "2":
            city_id = int(input("Stadt-ID: "))  # Ask the user for the city ID
            new_city_name = input("Stadtname: ")
            controller.add_city(city_id, new_city_name)
        elif choice == "3":
            try:
                city_id_to_delete = int(input("Stadt-ID: "))
                controller.delete_city(city_id_to_delete)
            except ValueError:
                print("Ungültige Eingabe. Bitte gib eine Zahl ein.")
        elif choice == "4":
            try:
                city_id_to_update = int(input("Stadt-ID: "))
                new_city_name = input("Neuer Stadtname: ")
                controller.update_city(city_id_to_update, new_city_name)
            except ValueError:
                print("Ungültige Eingabe. Bitte gib eine Zahl ein.")
        elif choice == "5":
            controller.save_data_to_db()  # Save data to database before exiting
            break
        else:
            print("Ungültige Wahl.")
