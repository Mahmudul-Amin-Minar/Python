'''This Code will separate your media files those have .mp4, .mkv, .avi extension and size above 1GB.
   It will search all your drives if there are any files that match with the description, then it will create a folder named Large files
   on that drive and move all your large files
   
   Thank you...
   
   This is totally a fun project.
   '''
   

import os
import shutil
import string

letters = string.ascii_uppercase
drives = ''


for i in letters:
	if (os.path.exists(i+':\\')):
		drives += i

number = len(drives)-1

try:
	
	while(number>=0):
		print('\nCurrently Scanning '+drives[number])
		
		flag = 1
		
		for folder,subfolders,files in os.walk(drives[number]+':\\'):
				
			for file in files:
				if(os.path.getsize(folder+'\\'+file)>1073741824 and file.endswith(('mp4','mkv','avi'))):
					if(flag==1 and (os.path.exists(drives[number]+':\\Large Files'))==False):
						flag=0
						os.makedirs(drives[number]+':\\Large Files')
						
					if(os.path.exists(drives[number]+':\\Large Files\\'+file)==False):
						shutil.move(folder+'\\'+file,drives[number]+':\\Large Files')
					else:
						pass
					
					print('|'.center(20))
			
		number-=1
	
except(UnicodeEncodeError,PermissionError):
	pass
	
print('\n\n\nThanks For using this software'.center(20))
print('\nNow open your computer Drives and you will Find a folder named Large files, open that folder and you will find all your Media files that is larger than 1 GB.....')
print('ENJOY'.center(40))
