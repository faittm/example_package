from dataclasses import dataclass
import cv1_ref
import argparse

@dataclass
class ProgArguments():
    file: str
    year: int


def parse_args() -> ProgArguments:
    parser = argparse.ArgumentParser(
        prog='Example Package',
        description='Package description... can be loaded from README.md')

    parser.add_argument('--file', nargs="+", help='where are we looking', type=str)
    parser.add_argument('--year', nargs="?", help='which year are we looking at', type=int)

    args = parser.parse_args()
    
    if not args.file and not args.year:
        parser.print_help()
        exit(1)

    return ProgArguments(**vars(args))


def main():
    args = parse_args()
    if args.file is not None and args.year is not None:
        ppl = cv1_ref.load_data_file(args.file,args.year)
        print(cv1_ref.count_average_salary(ppl))