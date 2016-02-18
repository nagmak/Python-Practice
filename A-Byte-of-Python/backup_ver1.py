import os
import time

#Files & Directories to be backed up are specified in list
source = ['/Users/nagma/Documents/CSProgramming/CSPython/Learning']

#Backup stored in a main backup directory
target_dir = '/Users/nagma/Documents/CSProgramming/CSPython/Learning/Backup'

#Backed up in a zip file
#Name of zip archive is the current date and time
target = target_dir + os.sep + \
		time.strftime('%Y%m%d%H%M%S') + '.zip'

#Create target directory if not present
if not os.path.exists(target_dir):
	os.mkdir(target_dir)

#Use zip command to put files in a zip archive
# -r includes all subdirectories & files as well
zip_command = "zip -r {0} {1}".format(target, ' '.join(source))


#Run backup
print("Zip command is:")
print(zip_command)
print("Running:")

if os.system(zip_command) == 0:
	print('Successful backup to', target)
else:
	print('Backup FAILED')
