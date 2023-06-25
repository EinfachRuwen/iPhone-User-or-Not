import json
import sys


def find_users_by_name(users, name):
    matching_users = []
    for user in users:
        if user["name"] == name:
            matching_users.append(user)
    return matching_users


def print_message(message):
    print("\033[1m" + message + "\033[0m")


while True:
    json_file = input("Gib den Dateinamen der JSON-Datei ein: ")

    try:
        with open(json_file, encoding='utf-8') as file:
            data = json.load(file)
        break
    except FileNotFoundError:
        print()
        print_message("Eine Datei mit dem Namen '{}' existiert nicht. Bitte versuche es erneut.".format(json_file))
        print()


max_id = max(data, key=lambda x: x["id"])["id"] if data else 0

while True:
    name = input("Name: ")

    matching_users = find_users_by_name(data, name)

    if len(matching_users) > 1:
        print()
        print_message("Es gibt mehrere Benutzer mit dem Namen '{}'.".format(name))
        print("Folgende Benutzer wurden gefunden:")

        for user in matching_users:
            print("ID: {}".format(user["id"]))
            print("Bild-URL: {}".format(user["picture"]))
            print("Ist iPhone-Benutzer: {}".format(user["isiPhoneUser"]))
            print()

        proceed = input("Möchtest du trotzdem fortfahren? (y/n): ").lower()
        if proceed != "y":
            continue

    elif len(matching_users) == 1:
        existing_user = matching_users[0]
        print()
        print_message("Ein Benutzer mit dem Namen '{}' existiert bereits:".format(name))
        print("ID: {}".format(existing_user["id"]))
        print("Bild-URL: {}".format(existing_user["picture"]))
        print("Ist iPhone-Benutzer: {}".format(existing_user["isiPhoneUser"]))

        proceed = input("Möchtest du trotzdem fortfahren? (y/n): ").lower()
        if proceed != "y":
            continue

    picture = input("Bild-URL: ")
    picture = picture.replace("https://ruwen.is-from.space/", "https://ruwen.is-from.space/r/")

    is_iphone_user_input = input("Ist iPhone-Benutzer? (y/n): ").lower()

    is_iphone_user = is_iphone_user_input in ["y", "yes"]

    max_id += 1

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
    print()
    print(f"Es sind {num_users} Benutzer in der Liste.")
    print("-" * 50)  # Zeichnet eine Linie

    # Neustart des Skripts
    max_id = max(data, key=lambda x: x["id"])["id"]