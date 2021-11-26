import sys 
# append parent directory to path to enable import from parent directory
sys.path.append('..')

import unittest
from utils import User, Building, AdminWindow

class TestUser(unittest.TestCase):
    def test_get_name(self):
        name = "John"
        user = User(name)
        self.assertEqual(user.get_name(), name)

    def test_get_id(self):
        name = "John"
        user = User(name)
        self.assertIsNotNone(user.get_id())

class TestBuilding(unittest.TestCase):
    def test_get_name(self):
        name = "B1"
        user = Building(name)
        self.assertEqual(user.get_name(), name)

    def test_get_id(self):
        name = "B1"
        user = Building(name)
        self.assertIsNotNone(user.get_id())

class TestAW(unittest.TestCase):
    def setUp(self):
        self.building_names = ["MGH", "BLD"]
        self.usernames = ["bill", "jane"]
        self.building_list = [Building(self.building_names[i]) for i in range(2)]
        self.user_list = [User(self.usernames[i]) for i in range(2)]

        self.admin_window = AdminWindow(self.user_list, self.building_list)
        self.admin_window.grant_access_to_user(self.user_list[0].get_id(), self.building_list[0].get_id())

    def test_grant_access_to_user(self):
        self.admin_window.grant_access_to_user(self.user_list[0].get_id(), self.building_list[1].get_id())
        access = self.admin_window.is_user_authorized_to_enter(self.user_list[0].get_id(), self.building_list[1].get_id())
        self.assertEqual(access, True)

    def test_remove_access_for_user(self):
        self.admin_window.remove_access_for_user(self.user_list[0].get_id(), self.building_list[1].get_id())
        access = self.admin_window.is_user_authorized_to_enter(self.user_list[0].get_id(), self.building_list[1].get_id())
        self.assertEqual(access, False)

    def test_lock_unlock_building(self):
        self.admin_window.lock_building(self.building_list[0].get_id())
        access = self.admin_window.is_user_authorized_to_enter(self.user_list[0].get_id(), self.building_list[0].get_id())
        with self.subTest('check if locked'):
            self.assertEqual(access, False)

        self.admin_window.unlock_building(self.building_list[0].get_id())
        access = self.admin_window.is_user_authorized_to_enter(self.user_list[0].get_id(), self.building_list[0].get_id())
        with self.subTest('check if unlocked'):
            self.assertEqual(access, True)
