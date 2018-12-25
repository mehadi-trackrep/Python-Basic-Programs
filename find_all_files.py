from os import listdir
from os.path import isfile, join
all_dirs = ['./Matplotlib', './Numpy', './Pandas'] #, './']

for mypath in all_dirs:
    print('Files in ', mypath, ' directory:\n')
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    # print ('The files are:\n', [file.replace(".ipynb","") for file in onlyfiles])
    print ('The files are:\n', [file.replace(".ipynb","") for file in onlyfiles])
    print ('\n')
