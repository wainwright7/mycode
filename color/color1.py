#!/usr/bin/env python3
"""Alta3 Research || Author RZFeeser@alta3.com
Learning how to use functions"""

import crayons


def main():
    """run time code. Always indent under function"""

    print(f"{crayons.red('red')} white {crayons.blue('blue')}")  # f-string (newest version of str templating)

    # print 'yellow string' in yellow
    print(crayons.yellow('yellow string', bold=True))

    # print 'magenta string' in magenta
    print(crayons.magenta('I passed Net+', bold=True))

    # print 'white string' in white
    print(crayons.white('white string', bold=True))

    print(f"{crayons.green('Python')} {crayons.blue('is Awsome')}")

# this condition is only true if our script is run directly
# it is NOT true if our code is imported into another script
if __name__ == "__main__":
    main()

