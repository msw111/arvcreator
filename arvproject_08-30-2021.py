
import os
import random

from shutil import copyfile
from shutil import move

def copyf(s1,d1):
    copyfile(s1,d1)

#build directory variables
activitypath = "e:\\arvtargets\\Activity"
activitywaterpath = "e:\\arvtargets\\ActivityWater"
alltargetspath = "e:\\arvtargets\\ALLTARGETS"
animalspath = "e:\\arvtargets\\Animals"
animalswaterpath = "e:\\arvtargets\\AnimalsWater"
machinespath = "e:\\arvtargets\\Machines"
machineswaterpath = "e:\\arvtargets\\MachinesWater"
naturepath = "e:\\arvtargets\\Nature"
naturewaterpath = "e:\\arvtargets\\NatureWater"
objectspath = "e:\\arvtargets\\Objects"
structurespath = "e:\\arvtargets\\Structures"
structureswaterpath = "e:\\arvtargets\\StructuresWater"
structuresoldpath = "e:\\arvtargets\\StructuresOld"
vegetationpath = "e:\\arvtargets\\Vegetation"

pairs = "e:\\ARV\\test2021-08-30"

#build pathectory objects

# fetch 2 files at random from the directories(pass object directory list 1 & 2 / directory variables 1 & 2)
def fetch(xxpath,yypath):
    
    activitylist = os.listdir(activitypath)
    activitywaterlist = os.listdir(activitywaterpath)
    animalslist = os.listdir(animalspath)
    animalswaterlist = os.listdir(animalswaterpath)
    alltargetslist = os.listdir(alltargetspath)
    structureslist = os.listdir(structurespath)
    structureswaterlist = os.listdir(structureswaterpath)
    structuresoldlist = os.listdir(structuresoldpath)
    machineslist = os.listdir(machinespath)
    machineswaterlist = os.listdir(machineswaterpath)
    naturelist = os.listdir(naturepath)
    naturewaterlist = os.listdir(naturewaterpath)
    objectslist = os.listdir(objectspath)
    vegetationlist = os.listdir(vegetationpath)

    if xxpath == 'activity':
        path1=activitypath
        list1=activitylist
    elif xxpath == 'activitywater': 
        path1=activitywaterpath
        list1=activitywaterlist
    elif xxpath == 'animals': 
        path1=animalspath
        list1=animalslist  
    elif xxpath == 'animalswater': 
        path1=animalswaterpath
        list1=animalswaterlist 
    elif xxpath == 'alltargets': 
        path1=alltargetspath
        list1=alltargetslist 
    elif xxpath == 'structures': 
        path1=structurespath
        list1=structureslist 
    elif xxpath == 'structureswater': 
        path1=structureswaterpath
        list1=structureswaterlist 
    elif xxpath == 'structuresold': 
        path1=structuresoldpath
        list1=structuresoldlist
    elif xxpath == 'machines': 
        path1=machinespath
        list1=machineslist
    elif xxpath == 'machineswater': 
        path1=machineswaterpath
        list1=machineswaterlist
    elif xxpath == 'nature': 
        path1=naturepath
        list1=naturelist
    elif xxpath == 'naturewater': 
        path1=naturewaterpath
        list1=naturewaterlist
    elif xxpath == 'objects': 
        path1=objectspath
        list1=objectslist
    elif xxpath == 'vegetation': 
        path1=vegetationpath
        list1=vegetationlist
    else:
        print("Wrong xxpath variable")
        
    if yypath == 'activity':
        path2=activitypath
        list2=activitylist
    elif yypath == 'activitywater': 
        path2=activitywaterpath
        list2=activitywaterlist
    elif yypath == 'animals': 
        path2=animalspath
        list2=animalslist  
    elif yypath == 'animalswater': 
        path2=animalswaterpath
        list2=animalswaterlist 
    elif yypath == 'alltargets': 
        path2=alltargetspath
        list2=alltargetslist 
    elif yypath == 'structures': 
        path2=structurespath
        list2=structureslist 
    elif yypath == 'structureswater': 
        path2=structureswaterpath
        list2=structureswaterlist 
    elif yypath == 'structuresold': 
        path2=structuresoldpath
        list2=structuresoldlist
    elif yypath == 'machines': 
        path2=machinespath
        list2=machineslist
    elif yypath == 'machineswater': 
        path2=machineswaterpath
        list2=machineswaterlist
    elif yypath == 'nature': 
        path2=naturepath
        list2=naturelist
    elif yypath == 'naturewater': 
        path2=naturewaterpath
        list2=naturewaterlist
    elif yypath == 'objects': 
        path2=objectspath
        list2=objectslist
    elif yypath == 'vegetation': 
        path2=vegetationpath
        list2=vegetationlist
    else:
        print("Wrong yypath variable")

     
    index1=(random.randint(0,len(list1)-1))
    index2=(random.randint(0,len(list2)-1))
    src1=path1+'\\'+list1[index1]
    src2=path2+'\\'+list2[index2]
    writeoutput(src1,src2)
    
    

# write output paris (pass source files 1 and 2)
def writeoutput(src1,src2):
    rand1=(random.randint(1000,9999))
    rand2=(random.randint(1000,9999))
    rand3=(random.randint(1000,9999))
    if rand3 > 5000:
        dest1 = pairs+'\\'+str(rand1)+"-"+str(rand2)+"-x.jpg"
        dest2 = pairs+'\\'+str(rand1)+"-"+str(rand2)+"-y.jpg"
    else:
        dest2 = pairs+'\\'+str(rand1)+"-"+str(rand2)+"-x.jpg"
        dest1 = pairs+'\\'+str(rand1)+"-"+str(rand2)+"-y.jpg"
    copyf(src1,dest1)
    copyf(src2,dest2)
    storage1 = src1.replace('arvtargets','arvtargetsused')
    storage2 = src2.replace('arvtargets','arvtargetsused')
    
    move(src1,storage1)
    move(src2,storage2)

##############################################################################################
count = 0
while (count < 5):
    
    
    xxpath='activity'
    yypath='structures'
    fetch(xxpath,yypath)
    
    xxpath='activity'
    yypath='structureswater'
    fetch(xxpath,yypath)
    
    xxpath='activity'
    yypath='structuresold'
    fetch(xxpath,yypath)
    
    xxpath='activity'
    yypath='nature'
    fetch(xxpath,yypath)
    
    xxpath='activity'
    yypath='naturewater'
    fetch(xxpath,yypath)
    
    xxpath='activity'
    yypath='objects'
    fetch(xxpath,yypath)
    
    xxpath='activity'
    yypath='vegetation'
    fetch(xxpath,yypath)

    xxpath='activitywater'
    yypath='structures'
    fetch(xxpath,yypath)

    xxpath='activitywater'
    yypath='structuresold'
    fetch(xxpath,yypath)
    
    xxpath='activitywater'
    yypath='nature'
    fetch(xxpath,yypath)
    
    xxpath='activitywater'
    yypath='objects'
    fetch(xxpath,yypath)
    
    xxpath='activitywater'
    yypath='vegetation'
    fetch(xxpath,yypath)
    
    xxpath='animals'
    yypath='structures'
    fetch(xxpath,yypath)
    
    xxpath='animals'
    yypath='structureswater'
    fetch(xxpath,yypath)
    
    xxpath='animalswater'
    yypath='machines'
    fetch(xxpath,yypath)
    
    xxpath='animalswater'
    yypath='structures'
    fetch(xxpath,yypath)
    
    xxpath='animals'
    yypath='machineswater'
    fetch(xxpath,yypath)
    
    xxpath='animals'
    yypath='nature'
    fetch(xxpath,yypath)
    
    xxpath='animals'
    yypath='naturewater'
    fetch(xxpath,yypath)
    
    xxpath='animals'
    yypath='objects'
    fetch(xxpath,yypath)
    
    xxpath='animals'
    yypath='vegetation'
    fetch(xxpath,yypath)

    xxpath='structures'
    yypath='nature'
    fetch(xxpath,yypath)
    
    xxpath='structures'
    yypath='naturewater'
    fetch(xxpath,yypath)
    
    xxpath='structures'
    yypath='vegetation'
    fetch(xxpath,yypath)
    
    xxpath='structureswater'
    yypath='nature'
    fetch(xxpath,yypath)

    xxpath='structureswater'
    yypath='vegetation'
    fetch(xxpath,yypath)
    
    xxpath='machines'
    yypath='nature'
    fetch(xxpath,yypath)
    
    xxpath='machines'
    yypath='nature'
    fetch(xxpath,yypath)
    
    xxpath='machines'
    yypath='vegetation'
    fetch(xxpath,yypath)
    
    xxpath='machineswater'
    yypath='nature'
    fetch(xxpath,yypath)
    
    xxpath='machineswater'
    yypath='vegetation'
    fetch(xxpath,yypath)
    
    xxpath='objects'
    yypath='vegetation'
    fetch(xxpath,yypath)
    
    xxpath='alltargets'
    yypath='alltargets'
    fetch(xxpath,yypath)
    
    xxpath='alltargets'
    yypath='alltargets'
    fetch(xxpath,yypath)
    
    
    count +=1

print("DONE !!!!!!!!!!!!!!!!!!!!")


    

    
    
    
    
