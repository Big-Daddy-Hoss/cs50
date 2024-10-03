import argparse

parser = argparse.ArgumentParser(description="Go Meow")
parser.add_argument("-n", default=1, help ="Number of times to meow")
args = parser.parse_args()

for i in range(int(args.n)):
    print("meow")