print ("Hello")

print ("Unix")


name = "python programming"
print(name)


aname = 'unix programming'
print(aname)

print("I Love",aname)


bname = """java programming """
print (bname)

alist =[10,20,30]
print("Elements are :",alist)
print("First element:",alist[0])
print("Second element:",alist[1])
print("Thirs element:",alist[2])

alist[0]= 1000
print("After Modifying :",alist)

blist = ["unix","oracle","perl"]
print("Elements are :",blist)


clist = [10,30,"python","a","z",40]
print("Elements are :",clist)

atup = (10,20,30,40,50,60)
print (atup)


btup = ("unix","oracle","pearl")
print (btup)

ctup = (10,30,"python","a","z",40)
print (ctup)

#dic = { key :value , key :value} -- This is single line comment
''' this
is multi line
comment
'''

adict = {"chapter1":10,"chapter2":20,"chapter3":30,"chapter1":800}
print (adict)

print("1st CHapter ",adict["chapter1"])

print(adict["chapter2"])

name = " I love python programming"
print(name)
print(name.capitalize())
print(name.upper())


print(name.count("python"))
print(name.split(" "))

#remove space at both ends
name = "  python  "
print (name.strip())

#remove space at both left end
name = "  python  "
print (name.lstrip())


# replace python with perl
name = "I Love python programming "
newstring = (name.replace("python","ruby"))

print (name)
print(newstring)
