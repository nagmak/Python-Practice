import os
import time

source = ['/Users/nagma/Documents/CSProgramming/CSPython/Learning']

#Backup stored in a main backup directory
target_dir = '/Users/nagma/Documents/CSProgramming/CSPython/Learning/Backup'

#Create target directory if not present
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

today = target_dir + os.sep + time.strftime('%Y%m%d')

#Current time is the name of the zip archive
now = time.strftime('%H%M%S')

#Name of the zip file
target = today + os.sep + now + '.zip'

#Create subdirectory if it doesnt exist
if not os.path.exists(today):
	os.mkdir(today)
	print('Successfully created directory', today)

#Use zip command to put files in a zip archive
zip_command = "zip -r {0} {1}".format(target, ' '.join(source))

#Run backup
print("Zip command is:")
print(zip_command)
print("Running:")
if os.system(zip_command) == 0:
	print('Successful backup to', target)
else:
	print('Backup FAILED')