import os

from directory import Directory

DIRECTORY_NOT_FOUND = "Error: Directory not found"

class BetancurShell:
    def __init__(self, home_dir_name = "C:/", name = "OS"):
        self.home_dir = Directory(name, home_dir_name, is_home=True)
        self.working_dir = self.home_dir
        self.working_dir.set_sub_dirs()
        self.is_Admin = False

    def change_working_dir(self, dir_name):
        new_dir = self.working_dir.get_dir(dir_name)
        if new_dir is not None:
            self.working_dir = new_dir
            self.working_dir.set_sub_dirs()
        else:
            print(DIRECTORY_NOT_FOUND + ", '" + dir_name + "' does not exist")

    def change_prev_dir(self):
        if self.working_dir.is_home is False:
            self.working_dir = self.working_dir.prev_dir
            self.working_dir.set_sub_dirs()
        else:
            print("Currently at home directory")

    def change_home_dir(self):
        self.working_dir = self.home_dir

    def make_dir(self, path, dir_name):
        os.mkdir(path + "/" + dir_name)

    def create_file(self, path, file_name, permission):
        pass

    def print_working_dir(self):
        print(self.working_dir.path)

    def list_directories_demo(self):
        print(self.working_dir.dir_name)
        for dir in self.working_dir.sub_dirs:
            print("- ",dir.dir_name)

