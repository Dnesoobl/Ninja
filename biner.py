
import os
from pyfiglet import figlet_format
os.system("clear")
####
a = figlet_format("Binary")
print ("\033[31;1m",a,"""\033[37;0m
Author: Ahmad
team  : None
""")
####
a = int(input(">> " ))
print ("")
print (f"binary dari {a} : ",f"\033[32;1m{a:04b}\033[37;0m")
print ("")
