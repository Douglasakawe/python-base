#!/usr/bin/env python3
import os 
import sys

# LBYL - Look Before You Leap
# EAFP - Easy to Ask Forgiveness than permission
# (É mais fácil perdir perdão do que permissão)

# try:
#     raise RuntimeError("Ocorreu um erro")
# except Exception as e:
#     print(str(e))


try:
	names = open("names.txt").readlines()
except FileNotFoundError as e:
	print(f"{str(e)}.")
	sys.exit(1)
	# TODO: Usar retry
else:
    print("Archive is opened")
finally:
    print("Executing this evertime")

try:
	print(names[2])
except:
	print("[Error] Missing name in the list")
	sys.exit(1)

