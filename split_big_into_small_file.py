'''This is used to split a big file into many small file'''
import sys,os

kilobytes = 1024
megabytes = kilobytes*1000
chunksize = int(200*megabytes)#default chunksize

def split(fromfile,todir,chunksize=chunksize):
    if not os.path.exists(todir):#check whether todir exists or not
        os.mkdir(todir)
    else:
        # remove all files in the path
        for fname in os.listdir(todir):
            os.remove(os.path.join(todir,fname))
    partnum = 0
    inputfile = open(fromfile,'r',encoding='UTF-8')#open the fromfile
    while True:
        chunk = inputfile.read(chunksize)
        if not chunk:             #check the chunk is empty
            break
        partnum += 1
        filename = os.path.join(todir,('part%04d'%partnum))
        fileobj = open(filename,'w',encoding='UTF-8')#make partfile
        fileobj.write(chunk)         #write data into partfile
        fileobj.close()
    return partnum
if __name__=='__main__':
        fromfile  = r'D:\rm\data_raw\c_export_all.csv' #The file that you need to be splited
        todir     = r'D:\rm\1013\data' #The path where to store those splited small files
        chunksize = int(100000000) #max size of a small file, 100000000 is around 100M 
        absfrom,absto = map(os.path.abspath,[fromfile,todir])
        print('Splitting',absfrom,'to',absto,'by',chunksize)
        try:
            parts = split(fromfile,todir,chunksize)
        except:
            print('Error during split:')
            print(sys.exc_info()[0],sys.exc_info()[1])
        else:
            print('split finished:',parts,'parts are in',absto)
