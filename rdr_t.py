import all_drives
import os
from os import path
import shutil

drives = all_drives.get_drives()
# fname = os.path.basename(os.path.dirname(__file__))

def pathR(pathSet):
	if pathSet == '':
		pathSet = "C:/Users/trisa/Desktop/py-proj";
	else: 
		pathSet = pathSet

	result_generator = os.walk(pathSet)
	files_result = [x for x in result_generator]
	full_paths = []
	for folder, dir_list, file_list in files_result:
	     
	    # add in any recursively found sub-folders
	    full_paths.extend([os.path.join(folder, sub) for sub in dir_list])
	     
	    # add in any recursively found non-folder files
	    full_paths.extend([os.path.join(folder, file) for file in file_list])

	return full_paths

def cr_file(toFile, toPath):
	dirPath = pathR(toPath)
	file = open(toFile+".txt", "w") 
	for allf in dirPath:
		file.write(allf + '\n')
	file.close()	
	os.system('cls')

def exist_file(toFile, toPath):
	if not path.exists(toFile+'.txt'):
		cr_file(toFile, toPath)
	else :
		os.unlink(toFile+'.txt')
		cr_file(toFile, toPath)

def make_store(drive_letter):
	dData = 'dData_'+drive_letter
	if 'dData' in os.getcwd():
		os.chdir('../')
	if not path.exists(dData): #and not dData in os.getcwd():
		print('creating folder')
		os.mkdir(dData)
		os.chdir('./'+dData)
		print('current path: ' + os.getcwd())
	else: 
		# destroy existing directories and files and recreate
		shutil.rmtree(dData)
		os.mkdir(dData)
		print('changing directory')
		os.chdir('./'+dData)
		print('current path: ' + os.getcwd())     

def parentDir(drive):
	# create storage folder
	dr_listfolders = os.listdir(drive)
	for folder in dr_listfolders:
		# check if txt is already created, pass the folder name 
		toTrackPath = drive+folder
		exist_file(folder, toTrackPath)

def doAllDrives():
	# parentDir('C:/','C')
	for dr in drives:
		setDrive = dr+':/'
		make_store(dr)
		parentDir(setDrive)

doAllDrives()