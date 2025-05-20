import os
import argparse
import pandas as pd

# imports, csv loader, gpt

# import input files
# What do input files look like?
# Hierarchy of classification, input of 50 line dataframe from GOD DATA

def load_input_files():
    with open("CommodityHierarchy.csv") as my_file:
        hierarchy_df = pd.read_csv(my_file)
    return hierarchy_df

#Choose a gpt to compare:

# load config, api token

# SCORING:
# Exact Match: 2 pts
# Unknown 1 ptpy
# Any Category Match: .5 per


# load results
# CSV OUTPUT:
# INPUT DATA, GOD RESULT, GPT 1, SCORE, GPT 2 SCORE, TOTAL SCORE
def build_report(args):
    print(args)
    df = load_input_files()
    import ipdb; ipdb.set_trace()

def main():
    print("hello")
    parser  = argparse.ArgumentParser(description="GPT api calling tool")
    sub_parsers = parser.add_subparsers()

    p = sub_parsers.add_parser('vendor', help='vendor')
    p.add_argument('gpt', help='gpt name')
    p.add_argument("num_rows", help='Number of rows')
    p.set_defaults(handler=build_report)


    # run appropriate handler
    args = parser.parse_args()
    if hasattr(args, 'handler'):
        args.handler(args)
    else:
        parser.print_help()


if __name__=="__main__":
    main()