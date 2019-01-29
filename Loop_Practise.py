# capture string and display as

astring= input(" Type string name ")
print ("String Name :",astring)

print ("Display as per length")

if len(astring)<5 :
    print ("String is too short")
elif len(astring) > 30 :
    print ("String is too long")
else :
    print ("String is good")


# exercise 2


astring= input(" Type string name ")
print ("String Name :",astring)

print (" Check string case and reverse the case ")

if astring.islower() :
    print(astring.upper())
else :
    print(astring.lower())


# exercise 3 - display all unique elements of group and length of the list 

alist = ["google.com","unix.com","facebook.com","inked.in", "google.com"]

uniquelist = set(alist)
mylist= []
for val in uniquelist :
    mylist.append(len(val))
print(mylist)

for val in uniquelist :
   print(len(val))


#exercise 4 : write a programs to cpature input as below adn convert it to list
   #enter any string : unix, java, oracle , hadoop

   # output - [ 'unix', 'java', 'oracle' , 'hadoop']

string = "unix, java, oracle , hadoop"
mylist= string.split(",")
print(mylist)



for val in range(1,11):
    mystr = str(val)+".py"
    print(mystr)


for val in range (1,101):
    mystr= "192.168.0."+str(val)
    print(mystr)
    
   
