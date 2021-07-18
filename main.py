
import database as db
from user_module import User

class AuthSystem(User):
    
    def __init__(self, user):
        self.logged_in_user = user
        self.greeting(self.logged_in_user)
        
    def login(self):
        user_list = list(db.data.keys())
        for i in range(len(user_list)):
            print("press ", i+1, " for ", user_list[i])
        user_selection_inp = int(input())
        self.logged_in_user = user_list[user_selection_inp-1]
        self.greeting(user=self.logged_in_user)

    def view_roles(self):
        roles = db.data[self.logged_in_user]['role']
        print("You have below roles:")
        for role in roles:
            print(role)
        self.greeting(user=self.logged_in_user)

    def access_resource(self):
        print('Enter resource you want access:')
        res = str(input())
        print('Enter ACTION TYPE you want to perform')
        action_type = str(input())
        user_roles = db.data[self.logged_in_user]['role']
        for role in user_roles:
            if action_type in db.roles[role]['ACTION_TYPE'] and res in db.roles[role]['RESOURCE'] :
                print('You have access!!!')
                self.greeting(self.logged_in_user)
        print("Sorry, you don't have access :(")
        self.greeting(self.logged_in_user)


    def greeting(self, user='admin'):
        self.logged_in_user = user
        print("Hi ", self.logged_in_user, "!")
        if self.logged_in_user == 'admin':
            print("press 1 for login as another user")
            print("press 2 for create user")
            print("press 3 for edit role")
            inp = int(input())
            if inp == 1:
                self.login()
            elif inp == 2:
                self.create_user()
            elif inp == 3:
                self.edit_role()
    
        else:
            print("press 1 for login as another user")
            print("press 2 for view roles")
            print("press 3 for access resource")
            inp = int(input())
            if inp == 1:
                self.login()
            elif inp == 2:
                self.view_roles()
            elif inp == 3:
                self.access_resource()



if __name__ == '__main__':

    AuthSystem('admin')
