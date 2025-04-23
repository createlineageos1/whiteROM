ascii = r"""
           _     _ _       _____   ____  __  __ 
          | |   (_) |     |  __ \ / __ \|  \/  |
 __      _| |__  _| |_ ___| |__) | |  | | \  / |
 \ \ /\ / / '_ \| | __/ _ \  _  /| |  | | |\/| |
  \ V  V /| | | | | ||  __/ | \ \| |__| | |  | |
   \_/\_/ |_| |_|_|\__\___|_|  \_\\____/|_|  |_|
                                                
                          whiteROM 1.0 by @createlineageos1                      
"""

print(ascii)

print("Booting up...")
from kernel import Kernel
import time
from commands import CommandProcessor
from conf import Configuration
import os
print("Booted up")


system_commands = [
    'cp.cmd',
    'cp.bored',
    'cp.showfetch',
    'cp.systurnoff',
    'cp.ota',
    'cp.usrdata',
    'cp.hme',
    'cp.trigger_panic'
]

kernel = Kernel()


while True:
    cp = CommandProcessor()
    user_input = input(f"usr@whiterom:{os.curdir}/$>> ").split(" ")
    entered_command = user_input[0]
    args = user_input[1:]
    
    command_found = False
    
    for command_str in system_commands:
        command_name = command_str.split('.')[-1]
        if command_name == entered_command:
            try:
                command_func = eval(command_str)
                command_func(*args)
                command_found = True
                break
            except Exception as e:
                print(f"Error while executing the command '{entered_command}': {e}")
                break
    if not command_found:
        print(f"Command '{entered_command}' not found.")
