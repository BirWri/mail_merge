#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# Open the starting letter file
starting_file = open("./Input/Letters/starting_letter.txt")
print(starting_file.readlines())

# Open and iterate through the list of invited names list

with open("./Input/Names/invited_names.txt", "r") as file:
    for line in file:
        print(line)



