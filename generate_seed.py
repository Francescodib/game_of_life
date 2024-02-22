import random

# Define the number of lines and characters per line
num_lines = 500
chars_per_line = 500

# Characters to choose from
chars = ['*', '_']

# Open a file to write
with open('seed.txt', 'w') as file:
    # Generate and write each line
    for _ in range(num_lines):
        line = ''.join(random.choice(chars) for _ in range(chars_per_line))
        file.write(line + '\n')

print('File "seed.txt" has been created with random "*" and "_" values.')