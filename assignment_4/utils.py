import uuid
from random import random
import math

def generate_random_string(num_char = 15):
    # generates a random character string of length num_char
    return ''.join([chr(x) for x in [math.floor(random()*26) + 97 for i in range(num_char)]])

class Building:
    def __init__(self, name=None):
        self.id = uuid.uuid4()
        self.name = name if name else generate_random_string(num_char=15)

    def __str__(self):
        return self.get_name()

    def get_id(self):
        return self.id    

    def get_name(self):
        return self.name

class User:
    def __init__(self, name=None):
        self.id = uuid.uuid4()
        self.name = name if name else generate_random_string(num_char=15)

    def __str__(self):
        return self.get_name()

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

class AdminWindow:
    def __init__(self, user_list, building_list):
        self.access_dict = {}
        self.building_locked_dict = {building.get_id(): False for building in building_list}
        self.building_list = building_list
        self.user_list = user_list

    def grant_access_to_user(self, user_id, building_id):
        if not self._is_user_input_valid(user_id):
            print("Invalid user ID")

        if not self._is_building_input_valid(building_id):
            print("invalid building id")

        if building_id in self.access_dict:
            if user_id not in self.access_dict[building_id]:
                self.access_dict[building_id].append(user_id)
        else:
            self.access_dict[building_id] = [user_id]

    def remove_access_for_user(self, user_id, building_id):
        if building_id in self.access_dict:
            if user_id in self.access_dict[building_id]:
                self.access_dict[building_id].remove(user_id)

    def is_user_authorized_to_enter(self, user_id, building_id):
        if building_id in self.building_locked_dict:
            if self.building_locked_dict[building_id]: return False
        if building_id in self.access_dict:
            return user_id in self.access_dict[building_id]
        return False

    def lock_building(self, building_id):
        if building_id in self.building_locked_dict:
            self.building_locked_dict[building_id] = True

    def unlock_building(self, building_id):
        if building_id in self.building_locked_dict:
            self.building_locked_dict[building_id] = False

    def _is_user_input_valid(self, user_id):
        for user in self.user_list:
            if user.get_id() == user_id:
                return True
        return False

    def _is_building_input_valid(self, building_id):
        for building in self.building_list:
            if building.get_id() == building_id:
                return True
        return False