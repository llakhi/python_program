# split a string and display separately

filename = input("Type file name")
print ("Filename : ",filename)

print ("Split the file name and show ")
data = filename.split('.')

print("file name - " ,data[0])
print("file name - " ,data[1])

 
# Write a program and display all the duplicates of list

alist = [10,20,30,10,40,50]
print (list(set(alist)))


aname = "python is general purpose interpreted cross platform programming lang"
print (aname)

print("Diplay in upper case:-",(aname.upper()))

print("Display count of p in string:- ",aname.count("p"))

print ("Replace with Ruby :- ",(aname.replace("python","ruby")))

print ("Count no of words and display :- ",aname.count(""))



# IF statement

       
a = 10
b=12

if a < b :
    print (" A is smaller ")
else:
        print("B is greater")


print(list(range(1,10))) # range only works with list or tuple

print(list(range(1,10,2)))  #display even numbers

print (list(range(10,0,-1))) # display in reverse order

# FOR LOOP

alist = [10,20,30,40,50]
for val in alist:
    print(val)

# with range

for val in range (1,5):
    print (val)

#display all the keys

    adict = {"chap1":10,"chap2":20,"chap3": 30 }
    for item in adict.keys():
        print("key :",item)
        print ("value :",adict[item])

# forloop with string

name = "pythono programming"
for char in name :
    print(char)

aset = {10,10,10}
for val in aset:
    print(val)
 
