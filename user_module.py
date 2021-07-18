import database as db

class User():

    def __init__(self):
        pass

    def create_user(self):
        print("enter user's name")
        name = str(input())
        print("enter user's role(for multiple roles give comma seperated roles).")
        role = str(input()).upper().split(',')
        db.data[name] = {'role': role}
        print(name, " created succesfully!")
        self.greeting(user='admin')

    def edit_role(self):
        user_list = list(db.data.keys())
        for i in range(len(user_list)):
            print("press ", i + 1, " to change ", user_list[i], "'s role")
        user_selection_inp = int(input())
        print(user_list[user_selection_inp - 1], ' current roles:', db.data[user_list[user_selection_inp - 1]]['role'])
        print('enter new roles')
        role = str(input()).lower().split(',')
        db.data[user_list[user_selection_inp - 1]] = {'role': role}
        print(user_list[user_selection_inp - 1], " roles changed succesfully!")
        self.greeting(user='admin')
