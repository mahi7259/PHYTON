a = open("/content/anjan2.txt",'r')
content=a.read()
print(content)

a = open("/content/anjan2.txt",'w')
content=a.write("thank you")
print(content)

a = open("/content/anjan2.txt",'a')
content=a.write("thank you")
print(content)

a = open("/content/anjan2.txt",'rb')
content=a.read()
print(content)

a = open("/content/anjan2.txt",'wb')
content=a.write(b"text here")
print(content)

a = open("/content/anjan2.txt",'ab')
content=a.write(b"text here")
print(content)
