import csv
import random

from old_users_dataset import users


def arred(number):
    int_value = int(number)

    if int_value == number:
        return number

    difference = round(number - int_value, 1)

    if difference >= 0.8:
        return int_value + 1
    elif difference >= 0.3:
        return int_value + 0.5
    else:
        return int_value


subjects = set()
user_names = list()

csv_list = [["nome"]]

for user in users:
    user_names.append(user)

    for subject in list(users[user].keys()):
        subjects.add(subject)

csv_list[0].extend(list(subjects))

for name in user_names:
    current_user = [name]
    chosen_subjects = random.sample(list(subjects), random.randint(3, len(subjects)))
    for subject in subjects:
        if subject in chosen_subjects:
            current_user.append(arred(random.uniform(0, 5)))
        else:
            current_user.append("-")
    csv_list.append(current_user)

file = open("users.csv", "w")
writer = csv.writer(file, "excel")

for row in csv_list:
    writer.writerow(row)
    print(row)
