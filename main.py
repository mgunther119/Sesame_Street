import os
import argparse
import pandas as pd

# imports, csv loader, gpt

# import input files
# What do input files look like?
# Hierarchy of classification, input of 50 line dataframe from GOD DATA

#Choose a gpt to compare:

# load config, api token

# SCORING:
# Exact Match: 2 pts
# Unknown 1 pt
# Any Category Match: .5 per


# load results
# CSV OUTPUT:
# INPUT DATA, GOD RESULT, GPT 1, SCORE, GPT 2 SCORE, TOTAL SCORE


def main():
    parser  = argparse.ArgumentParser(description="GPT api calling tool")
    sub_parsers = parser.add_subparsers()
    
