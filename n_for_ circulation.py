import numpy as np
import copy


n=2

array=np.ones(n).tolist()
array_out=[]
array_out.append(copy.copy(array))

def xunhuan(j=0,r=6):

    if j==n:
        return array
    while array[j]<=r:
        xunhuan(j+1)
        array[j]=array[j]+1
        if j+1<n:
            array[j+1]=1
        #print array
        array_out.append(copy.copy(array))

xunhuan()

final=[]
for i in range(np.shape(array_out)[0]):
    count = 0
    for j in range(np.shape(array_out)[1]):
        if array_out[i][j]<7:
            count=count+1
        if count==np.shape(array_out)[1]:
            final.append(array_out[i])
