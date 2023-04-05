import os


class Directory:
    def __init__(self, name, path, is_home = False):
        self.path = path
        self.is_home = is_home
        self.dir_name = name
        self.prev_dir = None
        self.sub_dirs = []

    def set_sub_dirs(self):
        dir_names = os.listdir(self.path)
        for name in dir_names:
            path = self.path + name
            dir = Directory(name, path)
            dir.prev_dir = self
            self.sub_dirs.append(dir)

    def get_dir(self, dir_name):
        for dir in self.sub_dirs:
            if dir.dir_name == dir_name:
                return dir
        return None