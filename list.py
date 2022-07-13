import os
from os import listdir
from os.path import isfile, join

import numpy
import pandas


arr = [2,4,5,7,9]
arr_2d = [[1,2],[3,4]]
 
#print("The Array is: ", arr) #printing the array
#print("The 2D-Array is: ", arr_2d) #printing the 2D-Array


mypath = r"/mnt/efs/fs1/data/YTBB/custom3/yt_bb_detection_validation/0"

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

#files = os.listdir('.')
#print(onlyfiles)


z = []

#numpy.array(z, dtype=object)

for i in onlyfiles:
    # Replacing "," , converting to lower and then splitting
    z.append(i.replace("_"," ").replace("."," ").lower().split())



#print(z)


index = [i[0] for i in z] #first element of every list in yourlist
not_index_list = [i[1:] for i in z]
pandas = pandas.DataFrame(not_index_list, index = index)
pandas.to_csv("mylist2.csv")

#df = pandas.DataFrame(files)

#df.to_csv('monnom.csv')

#numpy.savetxt('tktmonamie5.csv', z, delimiter=';', fmt="%s")
#numpy.savetxt('nanvkd.csv', arr_2d, delimiter=',')



