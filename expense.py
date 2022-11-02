from PyInquirer import prompt
import csv

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"input",
        "name":"spender",
        "message":"New Expense - Spender: ",
    },
]



def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    users = []
    with open('users.csv','r') as file:
        users = file.readlines()
        if infos.get('spender') not in [user.rstrip() for user in users]:
            print("Spender should be chosen among existing users !")
            return
    for user in users:
        user.rstrip()
    with open('expense_report.csv', 'a') as f:
        writer = csv.writer(f)
        if len(users) == 1:
            writer.writerow([infos.get('amount'), infos.get('label'), infos.get('spender')])
        else:
            for user in users:
                if (user.rstrip() == infos.get('spender')):
                    writer.writerow([infos.get('amount'), infos.get('label'), infos.get('spender')])
                else:
                    writer.writerow([int(infos.get('amount'))//((len(users)-1 )* -1), infos.get('label'), user.rstrip()])
    print("Expense Added !")
    return True


