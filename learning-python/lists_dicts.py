dataSet = [0,1,2,3,4,5,6]
mixedSet = [1,"TWO",3,"four",5,"6"]
bestDict = {"name":"caleb", "age": 25,  "key": "VALUE",}

dataSet.append(7);
mixedSet.insert(0,"zer0")
listLength = len(dataSet)
dataSet.sort(reverse=True) #SEE 'True' is capitalize
dataSet.pop(4) #removes from the array (position 4 in this case)

giantList = dataSet + mixedSet
print giantList

print 6 in giantList

a = range(0,40,3) #makes a list from 0 to 40 in steps of 3
b = range (100, 40, -5)

#.join
# print " & ".join(giantList) # .join for strings only in this case

print bestDict["name"],"is STUPID"
#NOTICE TH COMMA CAUSES A SPACE - you can also use:
print bestDict["name"]+"is stuuupid"
print bestDict.keys()
