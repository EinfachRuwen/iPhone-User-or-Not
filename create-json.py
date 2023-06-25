import json
import sys
import difflib


def find_users_by_name(users, name):
    matching_users = []
    for user in users:
        if user["name"].lower() == name.lower():
            matching_users.append(user)
    return matching_users


def print_message(message, is_bold=False):
    if is_bold:
        print("\033[1m" + message + "\033[0m")
    else:
        print(message)


while True:
    json_file = input("Gib den Dateinamen der JSON-Datei ein: ")

    try:
        with open(json_file, encoding='utf-8') as file:
            data = json.load(file)
        break
    except FileNotFoundError:
        print()
        print_message("Eine Datei mit dem Namen '{}' existiert nicht. Bitte versuche es erneut.".format(json_file), True)
        print()


max_id = max(data, key=lambda x: x["id"])["id"] if data else 0

while True:
    name = input("Name: ")

    matching_users = find_users_by_name(data, name)

    if len(matching_users) > 1:
        print()
        print_message("Es gibt mehrere Benutzer mit dem Namen '{}'.".format(name), True)
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
        print_message("Ein Benutzer mit dem Namen '{}' existiert bereits:".format(name), True)
        print("ID: {}".format(existing_user["id"]))
        print("Bild-URL: {}".format(existing_user["picture"]))
        print("Ist iPhone-Benutzer: {}".format(existing_user["isiPhoneUser"]))

        proceed = input("Möchtest du trotzdem fortfahren? (y/n): ").lower()
        if proceed != "y":
            continue

    similar_names = difflib.get_close_matches(name, [user["name"] for user in data], n=1, cutoff=0.8)
    if similar_names:
        similar_user = next((user for user in data if user["name"].lower() == similar_names[0].lower()), None)
        if similar_user:
            print()
            print_message("Ein ÄHNLICHER Benutzer mit dem Namen '{}' existiert bereits:".format(similar_user["name"]), True)
            print("ID: {}".format(similar_user["id"]))
            print("Bild-URL: {}".format(similar_user["picture"]))
            print("Ist iPhone-Benutzer: {}".format(similar_user["isiPhoneUser"]))
            print()
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
    print("Es sind {} Benutzer in der Liste.".format(num_users))
    print("-" * 30)
    print()
