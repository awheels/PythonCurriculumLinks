#Madlib Program
import os, re

print("Madlib Program")

# Will display a list of all txt files in the assets folder
for each in os.listdir("assets/"):
    if each.endswith('txt'):
        print(each)
selection = input("What file is the Madlib that you would like to use? ")

while selection not in os.listdir("assets/"):
    selection = input("Could not find a match for that Madlib. Please try again.")


#opening file and setting variables
with open("assets/"+selection,"r",encoding = "utf-8") as my_file:
    word_types = ["{adj}","{noun}", "{plural_noun}", "{animal}", "{place}", "{plural_food}", "{funny_noise}", "{person_you_know}"]
    user_inputs = []
    user_inputs_index = []
    my_read_file = my_file.read()
    # adding space in front of various punctuation so the special word types are not missed
    my_read_file = re.sub('([.,!?])', r' \1 ', my_read_file)
    my_read_file = re.sub('\s{2,}', ' ', my_read_file)
    new_read_file = my_read_file.split()
    x = 0
    for item in new_read_file:
            if item in word_types and user_inputs_index == []:
                user_inputs.append(item)
                user_inputs_index.append(new_read_file.index(item))
            else:
                if item in word_types:
                    user_inputs.append(item)
                    user_inputs_index.append(new_read_file.index(item,(int(user_inputs_index[-1])+1)))
    for each in user_inputs:
        user_inputs[x] = input("Please Enter a(n) " + each + ": ")
        x += 1
    z = 0
    for word in user_inputs:
        y = int(user_inputs_index[z])
        new_read_file[y] = word
        z += 1
    print (" ".join(new_read_file))

my_file.close()
