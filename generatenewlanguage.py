import random

alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
assignment = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
dummy = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
output = {}
stringtesting = []
randomnumberlist = []
random.shuffle(alphabets)
for i in range(0,len(dummy)):
    assignmentnumber = i
    alphabetsnumber = i
    output[assignment[assignmentnumber]] = alphabets[alphabetsnumber]

assignment.clear()
alphabets.clear()

f = open("code.txt", 'w')
f.write(str(output))
f.close()