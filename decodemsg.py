import ast
f = open('code.txt','r')
language = f.readline()
language = ast.literal_eval(language)
encrytedmsg = str(input("Write your msg which u want to decode here: "))
encrytedmsg = encrytedmsg.lower()
outputmsg = ""
for i in encrytedmsg:
    if language.__contains__(i):
        key_list = list(language.keys())
        val_list = list(language.values())

        position = val_list.index(i)

        outputmsg = outputmsg + key_list[position]
    else:
        outputmsg = outputmsg + i

outputmsg = outputmsg.capitalize()
print("Here is your decoded msg: "+outputmsg)
