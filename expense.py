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
    with open('users.csv') as file:
        if infos.get('spender') not in [line.rstrip() for line in file]:
            print("Spender should be chosen among existing users !")
            return
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('expense_report.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([infos.get('amount'), infos.get('label'), infos.get('spender')])
    print("Expense Added !")
    return True


