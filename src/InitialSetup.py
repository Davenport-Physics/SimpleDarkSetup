#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  InitialSetup.py
#  
#  Copyright 2016 Emma Davenport <Davenport.physics@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#

import sys

try:
	from Common import *
except ImportError:
	sys.path.insert(0, "DarkSectorCodeData.zip")
	from Common import *
	
UserDirectory = None
WorkingDirectory = None
	
def InitialSetupBlock(WorkingDirectoryString):
	
	global WorkingDirectory
	global UserDirectory
	
	WorkingDirectory = Directories(WorkingDirectoryString)
	UserDirectory = Directories(GetUserHomeDirectoryString(GetCurrentLocalDirectory()))
	
	WorkingDirectory.MakeDirectory()
	
	DownloadObjList = ReadLinksFile_And_GetFileObjectsList()
	
	for i in DownloadObjList:
		DownloadFileFromUrl(i, WorkingDirectory.GetDirectory())
	
	
	if CheckIfBashrcHasTagsAlready() == False:
		AddExportToBashrc()
	

"""

	ReadLinksFile_And_GetFileObjectsList
	
	Opens a file called Links and stores the contents in a list declared
	as StringList, line by line. It then proceeds to call the function
	MakeDownloadableFileObjectList.
	
	Returns a list of DownloadableFiles objects

"""	
def ReadLinksFile_And_GetFileObjectsList():
	
	fp = open("Links", "r")
	StringList = []
	for line in fp:
		StringList.append(line)
		
	fp.close()
	
	return MakeDownloadableFileObjectList(StringList)

"""

	MakeDownloadableFileObjectList
	
	When given an appropriate list of strings, i.e a list of strings
	related to non-local files (Files that need to be downloaded), this
	code will attempt to group strings of three.
	
	It assumes that the StringList file is not out of order, which
	relies on the user writing data in the appriopriate manner in the
	Links file. The following is the appropriate manner a Links file
	ought to be structured
	
	<Program name>
	<URL to download program>
	<Name of the downloaded file verbatim>
	
	<Program name>
	...
	
	Returns a list of DownloadableFiles objects

"""
	
def MakeDownloadableFileObjectList(StringList):
	
	x = len(StringList)
	
	DownloableFilesObjectList = []
	temp = []
	counter = 0
	for i in range(0, x):
		if counter != 0 and counter%3 == 0:
			
			try:
				
				obj = DownloableFiles(ProgramName=temp[0], Url=temp[1], File=temp[2])
				DownloableFilesObjectList.append(obj)
				
			except TypeError:
				
				print(temp)
				print("TypeError Exception: InitialSetup.py" % (len(temp)))
				
			temp = []
			counter = 0
			
		else:
			
			StringList[i] = StringList[i].replace("\n","")
			temp.append(StringList[i])
			counter += 1
		
	return DownloableFilesObjectList
	

"""

	CheckContentsOfDownloadObjList
	
	When given a list filled with DownloadFiles objects,
	it will iterate through the list calling the method
	PrintObjContents
	
	Returns no value

"""
def CheckContentsOfDownloadObjList(DownloadObjList):
	
	for i in range(len(DownloadObjList)):
		DownloadObjList[i].PrintObjContents()


"""

	CheckIfBashrcHasTagsAlready
	
	Determines whether the .bashrc file in the home directory of the user
	has already been altered to have the appropriate export variables
	
	returns a boolean

"""

def CheckIfBashrcHasTagsAlready():
	
	fp = open( UserDirectory.GetDirectory() + "/.bashrc", "r" )
	
	print("CheckIfBashrcHasTagsAlready STUB")
	
	fp.close()
	
	return True

"""

	AddExportToBashrc
	
	*Should be called after files have been downloaded and extracted
	
	Returns nothing

"""
def AddExportToBashrc():
	
	global UserDirectory
	
	if CheckIfBashrcHasTagsAlready() == True:
		return
		
	fp = open( UserDirectory.GetDirectory() + "/.bashrc", "a")
	
	print("AddExportToBashrc STUB")
	
	fp.close()
	
