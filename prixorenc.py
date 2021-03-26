import os
import sys
import time


__Author__ = "AnonPrixor"
__Version__ = "1.0"
__CreatedD__ = "March 27, 2021"
__CreatedT__ = "6:25 AM (PHT)"

def backmenu():
	back = input("\033[1;97mDo you want to go back to menu [Y/N]: ")
	if (back == "Y") or (back == "y"):
		menu()
	if (back == "N") or (back == "n"):
		print("ThankYou for using my tool.")
		time.sleep(2)
		os.system("clear")
		sys.exit()

def logo():
	print("""\033[1;31m
    ____       _                 ______          
   / __ \_____(_)  ______  _____/ ____/___  _____
  / /_/ / ___/ / |/_/ __ \/ ___/ __/ / __ \/ ___/
 / ____/ /  / />  </ /_/ / /  / /___/ / / / /__  
/_/   /_/  /_/_/|_|\____/_/  /_____/_/ /_/\___/

  " ENCRYPT YOUR PYTHON | MORE UPDATE COMING "
	""")
	print("""
Version: 1.0
	""")

def menu():
	logo()
	print("""
1. Encrypt
2. Tool Info
	""")
	choice = input("Please Choose [1/2]: ")
	if (choice == "1"):
		print("Example: /sdcard/file.py")
		enc = input("File: ")
		os.system("python -m py_compile " +enc)
		print("Your file saved in > __pycache__")
	if (choice == "2"):
		print("""
Author : AnonPrixor
Version: 1.0
" Aim and Chase your Dreams, Don't Anyone Stop you chasing your dreams!"
Created Date : March 27, 2021
Created Time : 6:25 AM (PHT)
		""")
		

menu()