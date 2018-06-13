import glob

print('test')

for filename in glob.iglob('/home/tito/**/*.pdf', recursive=True):
    print(filename)



