from shell import BetancurShell
from ShellCommands.commands import command

NORM_USER = "User@BetancurShell:~ "

ADMIN_USER = "User@BetancurShell:$~ "

def init_shell():
    shell = BetancurShell()

    end = False

    while end is False:
        if shell.is_Admin:
            command_line = input(ADMIN_USER)
        else:
            command_line = input(NORM_USER)
        command(shell, command_line)
