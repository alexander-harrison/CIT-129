#opening file and assigning it to a variable
f = open("icon_files/icon_data.txt").readlines()

#making list for file to go into
iconList=[]

#stripping the quotes( ' ' ) from the strings within list
for i in f:
    iconList.append(i.strip())

#switching strings to integers within the list
iconList = [int(i) for i in iconList] 

#turning the 0's and 1's into true and false, making a new list
bool_list = [bool(i) for i in iconList]

#printing list to make sure it worked(this is temporary, only for testing purposes)
print(bool_list)

#for loop to assign a string value to false and true then printing it
for i in bool_list:
    if i == False:
        print("#")
    else:
        print("@")
