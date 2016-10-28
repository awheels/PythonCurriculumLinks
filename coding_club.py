student_interests = ['Basketball', 'Drawing', 'Coding', 'Smiling', 'Petting Cute Dogs']

for item in student_interests:
    if item == "Coding":
        print("Glad to hear that coding is an interest of yours. You should sign up for the Computing Contest. It'll be great fun!")
        exit()

student_response = input("I see that you didn't list coding as an interests. Do you want to start learning a little more about it? (y/n)")
if student_response == "y":
    print("Well that is great news! You should sign up for the Computing Contest. It'll be great fun!")
else:
    print("Ok, no problem. Keep enjoying", student_interests[-1], "and", student_interests[-2], ".")
