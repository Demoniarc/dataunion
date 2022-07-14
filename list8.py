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
    i=i[::-1]
    i=i.replace("_"," ", 7)
    i=i.lstrip("txt.")
    i=i[::-1]
    i=z.append(i.split())


x = numpy.array(z)
x = numpy.delete(x, [0,1,2,3], axis=1)
x = x.astype(int)





g = (x[:,1] - x[:,0]).reshape(numpy.ma.size(x, axis=0),1)

d = numpy.append(x,g,1)

#print(z)
#print(x)

#print(d)

#print(g)

#reshape(numpy.ma.size(x, axis=0),numpy.ma.size(x, axis=1)+1)

index = [i[0] for i in d] #first element of every list in yourlist
not_index_list = [i[1:] for i in d]
pandas = pandas.DataFrame(not_index_list, index = index)
pandas.to_csv("4.csv")




#df = pandas.DataFrame(files)

#df.to_csv('monnom.csv')

#numpy.savetxt('tktmonamie5.csv', z, delimiter=';', fmt="%s")
#numpy.savetxt('nanvkd.csv', arr_2d, delimiter=',')



