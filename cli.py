'''
info-bot CLI
- displays the menu and returns the user's choice...

menu display:
1 - x
2 - y
...
0 - back (if it's the main menu, then "back" -> "exit")
'''

'''
VARS
'''

#dictionary for main menu
main_dict = {
"1":"Start new session",
"2":"Load previous session",
"0":"exit"
};

'''
FUNCTIONS
'''

def error(msg):
	print("ERROR :: "+msg);

def main_menu():
	print("Info-Bot :: Main-Menu");
	for key in main_dict.keys():
		print(str(key)+" - "+main_dict[key]);
	choice = input("-> ");
	if choice not in main_dict.keys():
		print("Invalid choice...");
		return(None);
	else:
		return(choice);

'''
MAIN
'''
if __name__ == "__main__":
	main_menu();
