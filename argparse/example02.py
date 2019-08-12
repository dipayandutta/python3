import argparse

parser = argparse.ArgumentParser()
parser.add_argument('command',nargs='?',default='hello')
args = parser.parse_args()

if args.command == 'Hello':
    print ("You Made It!")
else:
    print("You Didnot Make It!")
