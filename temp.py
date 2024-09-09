import text_utils

# Open the file in read mode
with open('sample.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

# Count the total number of words in the file
total_words = text_utils.count_words(''.join(lines))

# Calculate the average number of words per line
average_words_per_line = total_words // len(lines)

# Print the result
print(f"Average words per line: {average_words_per_line}")
