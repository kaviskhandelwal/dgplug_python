#!/usr/bin/env python
""" duplicate_image.py is a python program to search duplicate images in a given directory """

import os , sys
import hashlib					
from PIL import Image
import types					""" Package check NoneType EXIF information """
file_list = []					

def MD5(location, file):                        """ Function to get MD5 code of Image file having no EXIF information """
	os.chdir(location)
        with open(file, "r") as picture:
                fileContents = picture.read()
                md5 = hashlib.md5()
                md5.update(fileContents)
                hash = md5.hexdigest()
                return hash

def exif(location, file):			""" Function to get EXIF information of Imagefile """
        res = {}
	os.chdir(location)
        res = Image.open(file)._getexif()
        if isinstance( Image.open(file)._getexif(), types.NoneType):

                return MD5(location, file)
        else :  return res

def search(path):				""" Function to get a list of all 'jpg' and 'jpeg' image file """
       
        filelist = []

        for r,d,f in os.walk(path):
                for files in f:
                        if (files.endswith(".jpg") or files.endwith(".JPG")) :
                                os.path.join(r,files)
                                file = [r, files]
				filelist.append(file)
	return filelist
	
	

def check_for_duplicate():				""" Function to check the duplicate images in a directory """

        global file_list

        for n in file_list:
             
		info = exif(n[0], n[1])
                for x in file_list:

			info2 = exif(x[0], x[1])
                        if(info == info2):
				if ((n[1] == x[1] and n[0] != x[0]) or (n[1] != x[1])):
                               		print "%s path -> %s  is duplicate of %s path -> %s " %(n[1],n[0], x[1],x[0])                            


if __name__=='__main__':
        file_list = search(sys.argv[1])			""" List of all 'jpg' and ' jpeg' images """
	check_for_duplicate()				 

