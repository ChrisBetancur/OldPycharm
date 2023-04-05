import os.path

#path = os.path.realpath("C:/Users")
#print(os.listdir(path))
# os.startfile(path)
'''from shell import BetancurShell

shell = BetancurShell("C:/Users", "Users")
# shell.change_working_dir("chris")
# shell.change_working_dir("Blog")
shell.change_prev_dir()
print(shell.working_dir.dir_name)'''
#shell.list_directories_demo()

# print(shell.working_dir.prev_dir.dir_name)

from engine import init_shell

init_shell()


'''f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()'''

