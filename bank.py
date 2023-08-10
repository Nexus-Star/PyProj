import json
import os

def main():
    print("Hello And Welcome To RealMasterChief's Bank, The Best In The World Of Online Banking.")
    while True:
        answer=input("Do you have an account already? [Y/N]: ")
        answer=answer.upper()
        if answer not in ["N","Y"]:
            print("Input not recognized. Please try again.")
            continue
        elif answer=="N":
            account_name, account_balance=create_account()
        elif answer=="Y" and not os.path.exists('account.json'):
            print("You do not have an existing account.")
            print("Do you want to create an account, press ['C'].")
            print("Do you want to log out, press ['L'].")
            while True:
                choice=input("Choice: ")
                choice=choice.upper()
                if choice not in ["Q","C"]:
                    print("Input not recognized. Please try again.")
                    continue
                if choice=="Q":
                    
                    break
                elif choice=="C":
                    account_name,account_balance=create_account()
                    break
        elif answer=="Y":
            account_name,account_balance = login_user()  
        logged_in = True   
        while logged_in:
            choice=interact_with_user()
            choice = choice.upper()
            if choice == "L":
                logged_in = False
            elif choice == "U":
                print(f"Username is: {account_name}")
                back_to_main_menu()


def back_to_main_menu():
    while True:
        back=input("To go back to Main Menu, press ['B']: ")
        back=back.upper()
        if back!="B":
            print("Input not recognized. Please try again.")
            continue
        break
    return back

def create_account():
    account_list=[]
    while True:
        print("It's time to create an account!")
        account_name=input("Please Enter an account name: ")
        account_balance=0
    
        if os.path.exists('account.json'):
            with open('account.json','r') as p:
                account_list=json.load(p)
        with open('account.json','w') as p:
            account_list.append([account_name,account_balance])
            json.dump(account_list,p)
        print("Account was created successfully.")
        break
    return account_name,account_balance
  
def login_user():
    with open("account.json", "r") as f:
        account_list = json.load(f)
    account_found = False
    while not account_found:
        account_name = input("Please enter an account name: ")
        for i in account_list:
            if i[0] == account_name:
                account_found = True
                
                account_balance = i[1]
        if not account_found:
            print("Account does not exist. Please try again.")
            continue
    return account_name, account_balance


def interact_with_user():
    print("Do you want to...")
    print("1.Show username, press [U].")
    print("2.Logout, press [L].")
    while True:
        choice=input("Choice: ")
        choice = choice.upper()
        if choice not in ["L","U"]:
            print("Input not recognized. Please try again.")
            continue
        break
    return choice
main()
