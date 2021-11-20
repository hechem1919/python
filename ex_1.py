myfile_read = open('myfile.txt','r')
#myfile_write = open('myfile.txt','w')
#myfile_append = open('myfile.txt','a')
#myfile_write_or_create = open('myfile.txt','w+')
rows = myfile_read.readlines()
print(rows)
myfile_read.close()

with open("myfile.txt", "r") as fp:
    content = fp.read()
    print(content)
myfile_read.close()