from utils import Building, User, AdminWindow

building_names = ["MGH", "BLD"]
usernames = ["bill", "jane"]
building_list = [Building(building_names[i]) for i in range(2)]
user_list = [User(usernames[i]) for i in range(2)]

admin_window = AdminWindow(user_list, building_list)

def get_input(message = "Enter an input", valid_inputs=[], invalid_input_message="Enter a valid input"):
    input_string = input(f"{message}: {valid_inputs}")
    while input_string not in valid_inputs:
        input_string = input(f"{invalid_input_message}: {valid_inputs}")
    return input_string

def run_app():
    input_action = ""
    while input_action != "exit":
        input_action = input("What action do you want to take? \n1 to grant access \n2 to revoke access \
            \n3 to enter a building \n4 to lock a building \n5 to unlock a building: ")
        if input_action == "1":
            user_input = get_input(message = "What user do you want to grant access for?", \
                valid_inputs = usernames, invalid_input_message = "enter a valid name")

            building_input = get_input(message = "What building do you want to grant access for?", \
                valid_inputs = building_names, invalid_input_message = "enter a valid building")

            user = user_list[0] if user_input == "bill" else user_list[1]
            building = building_list[0] if building_input == "MGH" else building_list[1]

            admin_window.grant_access_to_user(user.get_id(), building.get_id())
            print(f"User {user_input} granted access to building {building_input}")
        elif input_action == "2":
            user_input = get_input(message = "What user do you want to remove access from?", \
                valid_inputs = usernames, invalid_input_message = "enter a valid name")

            building_input = get_input(message = "What building do you want to remove access from?", \
                valid_inputs = building_names, invalid_input_message = "enter a valid building")

            user = user_list[0] if user_input == "bill" else user_list[1]
            building = building_list[0] if building_input == "MGH" else building_list[1]

            admin_window.remove_access_for_user(user.get_id(), building.get_id())
            print(f"User {user_input} removed from accessing building {building_input}")
        elif input_action == "3":
            user_input = get_input(message = "What user do you want to check access for?", \
                valid_inputs = usernames, invalid_input_message = "enter a valid name")        

            building_input = get_input(message = "What building do you want to check access from?", \
                valid_inputs = building_names, invalid_input_message = "enter a valid building")  

            user = user_list[0] if user_input == "bill" else user_list[1]
            building = building_list[0] if building_input == "MGH" else building_list[1]           

            if admin_window.is_user_authorized_to_enter(user.get_id(), building.get_id()):
                print(f"User: {user.get_name()} is allowed in {building.get_name()}")
            else:
                print(f"User: {user.get_name()} is not allowed in {building.get_name()}")
        elif input_action == "4":
            building_input = get_input(message = "What building do you want to lock?", \
                valid_inputs = building_names, invalid_input_message = "enter a valid building")  

            building = building_list[0] if building_input == "MGH" else building_list[1]   

            admin_window.lock_building(building.get_id())
            print(f"Building: {building.get_name()} is now locked")
        elif input_action == "5":
            building_input = get_input(message = "What building do you want to unlock?", \
                valid_inputs = building_names, invalid_input_message = "enter a valid building")  

            building = building_list[0] if building_input == "MGH" else building_list[1]   

            admin_window.unlock_building(building.get_id())
            print(f"Building: {building.get_name()} is now unlocked")
        elif input_action == "exit":
            print("Exited admin window")
        else:
            print("Enter a valid choice")


def setup():
    admin_window.grant_access_to_user(user_list[0].get_id(), building_list[0].get_id())
    admin_window.grant_access_to_user(user_list[0].get_id(), building_list[1].get_id())       

if __name__ == "__main__":
    setup()
    run_app()