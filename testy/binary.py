
fname='binarki.txt'

def fileOpen(fname):
    with open(fname) as f:
        content = f.readlines()
        content=[x.strip() for x in content]
    # you may also want to remove whitespace characters like `\n` at the end of each line
    return content


content=fileOpen(fname)
content=[int(x) for x in content]
print(content)

print('\n')
listaBin=[]
for i in content:
    listaBin.append(bin(i)[2:].zfill(16)+'B')

for i in listaBin:print(i)





