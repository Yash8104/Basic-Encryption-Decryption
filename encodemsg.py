import ast
f = open('code.txt','r')
language = f.readline()
language = ast.literal_eval(language)
f.close()
msg = str(input("Write your msg which u want to encode here: "))
msg = msg.lower()
outputmsg = ""
for i in msg:
    if language.__contains__(i):
        outputmsg = outputmsg + language.get(i)
    else:
        outputmsg = outputmsg + i

outputmsg = outputmsg.capitalize()
print("Here is your encoded msg : " + outputmsg)
