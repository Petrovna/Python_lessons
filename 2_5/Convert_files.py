import os.path
import subprocess

source = 'Source'
result = 'Result'
files = os.listdir(source)
for file in files:
   src = os.path.join(source, file)
   rslt = os.path.join(result, '200_'+file)
   subprocess.run(['convert' , src, '-resize', '200', rslt])

