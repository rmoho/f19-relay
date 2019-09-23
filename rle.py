#!/usr/bin/env python3

import sys

def main(args):



	#dude im so sorry i dont really understand this challenge, but i did stuff for 'operating modes' section 

    if argv[1] == "c":		#compress file at argv[2]

    	with open (argv[2], "r") as f:		

    		for line in f:					#prints each line of file
				memory = ""					#Set a variable to remember letters
				counter = 0					#Set a variable to count how many letters
    			for letter in line:			#For each character in the line
					if memory == "":		#If memory variable is empty, 
						memory = letter		#Store that letter
					elif letter == memory:	#If the letter matches the one stored in memory...
						counter += 1		#Increase counter
					elif letter != memory:	#When a different letter is encountered...
						print(f"{counter}{memory}") 	#Print out the # of times the previous letter was counted and what letter it was
						memory = letter					#Set memory equal to the new letter
					elif letter == " "					#If letter is a space
						print(" ")						#Print a space


    if argv[1] == "x": 		#decompress file at argv[2]

    	with open (argv[2], "r") as f:		

    		for line in f:		#prints each line of file
    			for letter in f:					#The following block is in pseudo-code
					if letter == number:			#If the character encountered is a number
						print(that number X letters)		#Print the following character (which should be a letter) 'number' of times


    return 0

if __name__ == "__main__":
    main(sys.argv)



