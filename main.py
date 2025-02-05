import argparse
import create_tables
import sys


def print_tables(tables: dict):
    for table_name in tables:
        print(f"\n{table_name}")
        for row in tables[table_name]:
            print(f"{row} | {'   '.join(tables[table_name][row])} |")


def main(arguments):
    parser = argparse.ArgumentParser()

    parser.add_argument("filename", help="the .json file with the encoded table", type=str)
    parser.add_argument("flipflop", help="flip-flop type (from: D, T, RS, JK)", type=str)
    parser.add_argument("-p", "--print", help="prints the tables in the terminal", action="store_true")
    parser.add_argument("-s", "--save", help="doesn't do anything yet", type=str)
    args = parser.parse_args()

    tables = create_tables.create_tables(args.filename, args.flipflop)

    if args.print:
        print_tables(tables)


if __name__ == "__main__":
    main(sys.argv)