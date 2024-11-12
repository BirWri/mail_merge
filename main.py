PLACEHOLDER = "[name]"

# Open and iterate through the list of invited names list and make it into a list
names = []
with open("./Input/Names/invited_names.txt", "r") as file:
    for line in file:
        names.append(line)
print(names)

# Open the letter template
with open("./Input/Letters/starting_letter.txt") as letter_file:
    full_letter = letter_file.read()

    # Replace in the names
    for name in names:
        stripped_name = name.strip()
        new_letter = full_letter.replace(PLACEHOLDER, stripped_name)
        # Write a new letter as a separate file
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt","w") as completed_letter:
            completed_letter.write(new_letter)


# Write a new letter as a separate file



