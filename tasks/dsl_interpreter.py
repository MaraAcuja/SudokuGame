# Use this interpreter, by typing 'python dsl_interpreter.py airport.dsl' into the console.
# If you want to use some other .dsl file, just change the path :)

import sys

# my functions:
# (could be outsourced in its own module)

functions = {'arrive': lambda a, b: a + b,
             'leave': lambda a, b: a - b,
             'land': lambda a, b: a + b,
             'depart': lambda a, b: a - b}

variables = {}

# check if exactly two files are given (dsl_interpreter.py and airport.dsl)
if len(sys.argv) != 2:
    sys.exit(1)

# open .dsl and go through each line
with open(sys.argv[1]) as file:
    # initialization for actual parking situation
    parking = {"cars": 0,
               "planes": 0,
               "busses": 0,
               "taxis": 0,
               "helicopters": 0
               }

    for line in file:
        line = line.strip()

        # check if the line is a comment
        if not line or line[0] == '~':
            continue
        parts = line.split()
        #print("parts: " + parts[0])

        # check the instructions for each line and execute them
        if parts[0] == 'How':
            print("There are " + str(parking[parts[2]]) + " " + parts[2] + " at the airport.")

        else:
            a = parking[parts[1]]
            b = int(parts[0])

            parking[parts[1]] = functions[parts[2]](a, b)
