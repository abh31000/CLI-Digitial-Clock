from datetime import datetime
from typing import List
from termcolor import cprint
import itertools, numpy, os, time, sys, shutil

#Code's messy and needs lots of refactoring and clean-up lol

#Style 1
colon = ["      ", "  ██  ", "      ", "  ██  ", "      "]
zero = ["██████", "██  ██", "██  ██", "██  ██","██████"]
one = ["  ██", "  ██", "  ██", "  ██", "  ██"]
two = ["██████", "    ██", "  ██  ","██    ", "██████"]
three = ["██████", "    ██", "  ██  ", "    ██", "██████"]
four = ["██  ██", "██  ██", "██████", "    ██","    ██"]
five = ["██████", "██    ", "██████", "    ██", "██████"]
six = ["██████", "██    ", "██████", "██  ██", "██████"]
seven = ["██████", "    ██", "    ██", "    ██", "    ██"]
eight = ["██████", "██  ██", "██████", "██  ██", "██████"]
nine = ["██████", "██  ██", "██████", "    ██", "██████"]
#style_1 = [zero, one, two, three, four, five, six, seven, eight, nine]


def clean_screen():
	os.system('clear')

def get_time_digits(time:str)->List[str]:
	#Gets all characters in 'Current time' strings
	t_digits = [str(d) for d in time]	
	return t_digits

def get_ascii(digits:List[str])->List[List]:
	t_ascii = []
	for d in digits:
		if(d == "0"):
			t_ascii.append(zero)
		elif(d == "1"):
			t_ascii.append(one)
		elif(d == "2"):
			t_ascii.append(two)
		elif(d == "3"):
			t_ascii.append(three)
		elif(d == "4"):
			t_ascii.append(four)
		elif(d == "5"):
			t_ascii.append(five)
		elif(d == "6"):
			t_ascii.append(six)
		elif(d == "7"):
			t_ascii.append(seven)
		elif(d == "8"):
			t_ascii.append(eight)
		elif(d == "9"):
			t_ascii.append(nine)
		elif(d == ":"):
			t_ascii.append(colon)
	
	return t_ascii

def get_current_time():
	now = datetime.now()
	current_time = now.strftime("%H:%M")
	return current_time

def print_time(digits):
	
	print("\033[?25l",end="\r") #Hide cursor

	#Get middle of the screen
	columns = shutil.get_terminal_size().columns
	lines = shutil.get_terminal_size().lines
	
	# To center the clock
	x_padding = int(columns/2)-24
	y_padding = int(lines/2)-4

	print("\n"*y_padding)

	for i in range(len(digits)):
		for j in range(5):
			if(j == 0):
				print(" "*x_padding, end='\t')
				cprint(digits[i][j], 'green', end='\t')
			elif(j == 2):
				cprint(digits[i][j], 'green', attrs=['blink'], end='\t') #Make only the colon blink
			else:
				cprint(digits[i][j],'green', end='\t')
			
		print("")

def main():
	while True:
		time.sleep(0.1)
		clean_screen()
		ds = get_time_digits(get_current_time())
		acs = get_ascii(ds)
		acs_mat = numpy.array(acs)
		acs_transpose = numpy.transpose(acs_mat)
		print_time(acs_transpose)
		print("")


if __name__ == '__main__':
	try:
		main()
	
	except KeyboardInterrupt:
		print("\033[?25h") #Show cursor again
		sys.exit()

sys.exit()


#Maybe will add multiple styles and fonts for this Digital clock
"""Style 2
zero2 = ["    ▒▒████████▒▒","  ██████░░▒▒████", "  ████▓▓    ██████", "██████        ██████ ", "██████        ██████ ", "██████        ██████ ", "██████        ██████ ", "██████        ██████ ", "██████        ██████ ", "██████        ██████ ","██████        ██████ ", "██████        ██████ ", "▒▒████▒▒      ██████", " ██████▒▒  ██████ ", "  ░░  ████████", "      ░░ "]
one2 = ["        ████", "      ██████ ","████████████","████████████","░░░░░░██████","      ██████","      ██████","      ██████","      ██████","      ██████","      ██████","      ██████","      ██████","      ██████"]
two2 = []

style_2 = [zero2, one2, two2]"""