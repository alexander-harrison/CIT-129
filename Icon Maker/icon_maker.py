f = open("icon_files/icon_data.txt").readlines()

iconList=[]
for i in f:
    iconList.append(i.strip())
    
iconList = [int(i) for i in iconList] 

bool_list = [bool(i) for i in iconList]

print(bool_list)

for i in bool_list:
    if i == False:
        print("#")
    else:
        print("@")
