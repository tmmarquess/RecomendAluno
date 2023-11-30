import csv

file = open("users.csv")

csv_list = csv.DictReader(file, restkey="nome")

users = dict()
subjects = list(csv_list.fieldnames)
subjects.remove("nome")

for user in csv_list:
    users[user["nome"]] = {
        key: float(value)
        for key, value in user.items()
        if (key != "nome" and value != "-")
    }
