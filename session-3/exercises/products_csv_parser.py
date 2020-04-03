# Kaizend 3: Python for Scripting - Exercises
#
# Requirements: 
    # Name the exercise file products_csv_parser.py
    # Use argparse for passing the filename of the CSV input file
    # Remove all products that don’t have categories
    # Output a new CSV file that contains all products that have categories
    # Prompt the user to specify the filename of the CSV output file
    # Fix flake8 errors (if you don’t know how to do this yet, refer to How to Use Flake8 Guide)


import argparse
import csv
import os
import requests
import sys

def remove_products_without_category(reader):
    """
        Remove all products that don’t have categories
    """
    return [row for row in reader if row['Categories']]


def main(output_file):
    with f:
        reader = csv.DictReader(f)
        cleaned_products = remove_products_without_category(reader)
        
        if output_file:
            with open(output_file, 'w', newline='') as out:
                writer = csv.DictWriter(out, fieldnames=reader.fieldnames)
                writer.writeheader()
                writer.writerows(cleaned_products)
                    
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='Product CSV Parser', 
        epilog='This is just an extra description'
    )

    parser.add_argument('-f','--filename', metavar='', help='File to parse.')
    parser.add_argument('-o','--output', metavar='', help='File output.')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')

    args = parser.parse_args()

    try:
        f = open(args.filename)
    except FileNotFoundError as err:
        print(f"Error: {err}")
        sys.exit(2)
    except TypeError as err:
        print(f'Error: No file supplied \n {err}')
        print('Please supply file to be parsed using -f flag. or : ')
        sys.exit(1)
        

main(args.output)