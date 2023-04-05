import ctypes
import os.path
import sys


def cd(shell, dir_name):
    if dir_name == "..":
        shell.change_prev_dir()
    elif dir_name == "-":
        shell.change_home_dir()
    else:
        shell.change_working_dir(dir_name)


def ls(shell):
    shell.list_directories_demo()


def pwd(shell):
    shell.print_working_dir()


def mkdir(shell, value):
    data = value.split()
    '''if data[0] == "this":
        shell.make_dir(shell.working_dir.path, data[1])
        shell.working_dir.set_sub_dirs()
        return'''

    if real_mapping(data[0], location_mappings):
        shell.make_dir(location_mappings[data[0]](shell), data[1])
        shell.working_dir.set_sub_dirs()

    elif real_dir(data[0]):
        shell.make_dir(data[0], data[1])

    else:
        print("Error: invalid directory")


def request(shell, value):
    list = value.split()

    if real_mapping(list[0], request_mappings) is False:
        print("Error: invalid request")
        return

    if len(list) == 1:
        return request_mappings[value](shell)
    request_mappings[value](shell, extract_input(value))


def this(shell):
    return shell.working_dir.path


def admin(shell):
    if shell.is_Admin is False:
        shell.is_Admin = True
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        print("permission granted")
    else:
        print("permission already established")


def cmd(shell, value):
    data = value.split()

    extraction = extract_input(value)

    if real_mapping(data[0], cmd_mapping) is False:
        print("Error: mapping not found")
        return
    cmd_mapping[data](shell, extraction)


def param():
    pass


def all_cmd():
    pass


command_mappings = {
    'cd': cd,
    'ls': ls,
    'pwd': pwd,
    'mkdir': mkdir,
    'request': request,
}

request_mappings = {
    'admin': admin,
    'cmd': cmd
}

cmd_mapping = {
    "param", param
}

param_mapping = {
    "-all", all_cmd()
}

location_mappings = {
    'this': this,
}

file_permissions_mappings = {

}


def command(shell, user_input):
    # command_input = command_mappings[user_input]
    if user_input == "":
        return
    list = user_input.split()

    extraction = extract_input(user_input)

    if real_command(list[0]) is False:
        print("Error: invalid command")
        return

    if len(list) == 1:
        command_mappings[user_input](shell)
    else:
        command_mappings[list[0]](shell, extraction)

    # list[0](shell, list[1])


def real_mapping(input, mapping):
    for cmd in mapping:
        if cmd == input:
            return True
    return False


def real_command(command_input):
    for command in command_mappings:
        if command == command_input:
            return True
    return False


def real_dir(dir_input):
    return os.path.isdir(dir_input)


def extract_input(input):
    list = input.split()
    extraction = []
    for i in range(len(list)):
        if i == 0:
            pass
        else:
            extraction.append(list[i])

    return " ".join(extraction)