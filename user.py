from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New User - Name: ",
    },
]

def add_user(*args):
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('users.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([infos.get('name')])
    print("User Added !")
    return True