import os
path =r'C:\Users\lihai\Desktop\归档'
index = 0
for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file))==True:
        if file.find('.jpeg')>0:
            newname = "c"+ str(index) +'.jpeg'
            os.rename(os.path.join(path,file),os.path.join(path,newname))
            index += 1
            print( file,'ok')