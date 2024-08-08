
""" with open("score.txt") as file:
    contents = file.read()
    print(contents)
    file.close() """ 

with open("new_score.txt", mode="a") as file:
    file.write("\n New text.")
