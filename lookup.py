"""
A CLI tool for lookup up airport codes
"""
# use sys to read command line arguments
# use bios to read the file containing airport codes as JSON
import sys
import bios

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        airport_codes = bios.read('./airport_codes.json')
        exit_code = 0

        for i in sys.argv[1:]:
            try:
                print(f'{i} => {airport_codes[i]}')
            except KeyError:
                print(f'{i} => ERROR: No data exists for {i}.')
                exit_code += 1

        sys.exit(exit_code)

    else:
        print('Please enter an airport code to lookup.')
        sys.exit(1)
