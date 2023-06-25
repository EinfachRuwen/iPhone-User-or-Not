import json

json_file = input("Geben Sie den Dateinamen der JSON-Datei ein: ")

with open(json_file, encoding='utf-8') as file:
    data = json.load(file)

max_id = max(data, key=lambda x: x["id"])["id"] if data else 0

while True:
    name = input("Name: ")
    picture = input("Bild-URL: ")
    is_iphone_user_input = input("Ist iPhone-Benutzer? (y/n): ").lower()

    is_iphone_user = is_iphone_user_input in ["y", "yes"]

    max_id += 1

    # Aktualisieren der Bild-URL mit /r/ am Anfang
    picture = "https://ruwen.is-from.space/r/" + picture.split("/")[-1]

    new_data = {
        "id": max_id,
        "name": name,
        "picture": picture,
        "isiPhoneUser": is_iphone_user
    }

    data.append(new_data)

    with open(json_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    num_users = len(data)
    print(f"Es sind {num_users} Benutzer in der Liste.")
