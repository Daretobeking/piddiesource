#!/usr/bin/env python3

import random
# dice roller
import argparse
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument('--dice', dest='sides', type=int, help='How many sides?')
args = parser.parse_args()
sides = args.sides

print(f"output: {sides}")
