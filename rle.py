#!/usr/bin/env python3

import sys

def main(args):



	#dude im so sorry i dont really understand this challenge, but i did stuff for 'operating modes' section 




    if argv[1] == "c":		#compress file at argv[2]

    	with open (argv[2], "r") as f:		

    		for line in f:		#prints each line of file
    			print (line)


    if argv[1] == "x": 		#decompress file at argv[2]

    	with open (argv[2], "r") as f:		

    		for line in f:		#prints each line of file
    			print (line)

    return 0

if __name__ == "__main__":
    main(sys.argv)



