import argparse

parser = argparse.ArgumentParser()
parser.add_argument("hello")

args = parser.parse_args()

if args.hello == 'dipayan':
    print("Hello World!")

else:
    print("Hello World")
