import os.path
import subprocess
from multiprocessing.dummy import Pool as ThreadPool

source = 'Source'
result = 'Result'
files = os.listdir(source)
for file in files:
   src = os.path.join(source, file)
   rslt = os.path.join(result, '200_'+file)
   subprocess.run(['convert' , src, '-resize', '200', rslt])

