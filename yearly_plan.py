import json
import os
from rich import print 

DATA_FILE = "clients.json"

clients=[]
def main():
    global clients
    clients=load_data()
    while True :
        show_menu()
        choice=int(input("Choice: "))

        if choice ==1:
            register()
        elif choice==2:
            day_off()
        elif choice== 3:
            show_status()
        elif choice ==4:
            print("Thanks for using our System!")
            break
        else:
                print("[red]Invalid choice![/red]")


def show_menu():
     print("""
    [blue]
    =====================
     ANUAL LEAVE SYSTEM
    =====================

    1.Register
    2.Take a day off
    3.Status
    4.Exit
    [/blue]

    """)


def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []

def save_data():
    with open(DATA_FILE, "w") as file:
        json.dump(clients, file, indent=4)


def register():
    name=input("Name: ")
    try:
        day=int(input("Days granted: "))
    except ValueError:
        print("Invalid input, make sure to only put numbers ")
    pid=f"P{len(clients)+1:03}"

    client={
        "Name":name,
        "Days":day,
        "Pid":pid
       }
    clients.append(client)
    save_data()

    print("[green]Client registered successfully![/green]")
    print(f"Passenger ID: {pid}")

def day_off():
    search=input("Enter a Name or an Id: ")q2
    day_out=int(input("Enter how may day you want to go off: "))
    for client in clients:
        if (search==client["Name"] or search==client["Pid"]):
            print("[green]Client found successfuly[/green]")
            client["Days"]=int(client["Days"])-day_out
            print(client)
            return
        print("[red]User not found![/red]")

def show_status():
    search=input("Enter a Name or an Id: ")
    for client in clients:
        if (search==client["Name"] or search==client["Pid"]):
            print("[green]Client found successfuly[/green]")
            print(client)
            return
        print("[red]User not found![/red]")


if __name__=="__main__":
    main()
