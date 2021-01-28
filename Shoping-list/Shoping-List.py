##Shoping a List 
import os
#new open to apps
def welcome():
    print_Welcome = 'Welcome to apps' 
    print(print_Welcome.center(80))
welcome()
#help of apps
def help():
    
    print('''-->Hi Iam one robat the apps<--
                **my name is 'Atom'**
            to apps you have a one List and more.
            you can a Enter 'shwo' to show your List,
            sure!, you can Enter 'count' to number a items your List
            for clearing a display enter clear
            and you can Enter 'exit' to exit a apps
                 **a nice your times**
''')
help()    
#the List of a empty 
Shoping_List = []

#shoping function
def Shoping():
    while True:
        new = input('--> ')
        Shoping_List.append(new)
        if new == 'exit':
            break
        elif new == "help":
            help()
            Shoping
        elif new == "clear":
            os.system("clear")
        elif new == 'show':
            Shoping_List.pop()
            for item in Shoping_List:
                print(f"[+]- {item}")
        elif new == 'count':
            Shoping_List.pop()
            print('it is number of your list ---->',len(Shoping_List))   
Shoping()
