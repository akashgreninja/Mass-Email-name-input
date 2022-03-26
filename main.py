Variable="[name]"

with open("./Input/Names/invited_names.txt") as names:
     names_1=names.readlines()
     # print(names_1)

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_1=letter.read()
    for name in names_1:
        stripped_name=name.strip()
        new_name=letter_1.replace(Variable,stripped_name)
        print(new_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt",mode="w")as new:
            new.write(new_name)





