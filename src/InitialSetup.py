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
	
"""

LocalDirectory is a Directories object. It stores the directory the program
is currently being ran from.

UserDirectory is a Directories object. It stores the user's home directory.
i.e /home/eld

WorkingDirectory is a Directories object. It stores the directory that
will contain all of the software.

"""
LocalDirectory = None
UserDirectory = None
WorkingDirectory = None
	
	
"""

	InitialSetupBlock

"""
def InitialSetupBlock(WorkingDirectoryString):
	
	global WorkingDirectory
	global UserDirectory
	
	WorkingDirectory = Directories(WorkingDirectoryString)
	LocalDirectory = Directories(GetCurrentLocalDirectory())
	UserDirectory = Directories(GetUserHomeDirectoryString(
		LocalDirectory.GetDirectory()))
	DownloadObjList = ReadLinksFile_And_GetFileObjectsList()
	
	ReadCacheFile()
	WorkingDirectory.MakeDirectory()
	DownloadNecessaryFiles(DownloadObjList)
	ExtractNecessaryFiles(DownloadObjList)
	
	if CheckIfBashrcHasTagsAlready() is False:
		AddExportToBashrc()
	
	
"""

	DownloadNecessaryFiles

"""
	
def DownloadNecessaryFiles(DownloadObjList):
	
	global WorkingDirectory
	
	for obj in DownloadObjList:
		if CheckIfFileAlreadyDownloaded(obj, WorkingDirectory.GetDirectory()) is False:
			print("")
			DownloadFileFromUrl(obj, WorkingDirectory.GetDirectory())
		

"""

	ExtractNecessaryFiles

"""
def ExtractNecessaryFiles(DownloadObjList):
	
	global WorkingDirectory
	
	for i in DownloadObjList:
		if ".tar.gz" in i.GetFile():
			ExtractTarBall(i, WorkingDirectory.GetDirectory())
		elif ".zip" in i.GetFile():
			ExtractZip(i, WorkingDirectory.GetDirectory())
		else:
			print("Unknown archive extension")
	
"""

	ReadCacheFile
	
	TODO
	
	Implement file structure to read steps currently taken with 
	SimpleDarkSetup

"""

def ReadCacheFile():
	
	global WorkingDirectory
	fp = None
	
	print("ReadCacheFile STUB")
	
	DarkSectorCacheString = WorkingDirectory.GetDirectory() + "/.darksectorcache"
	
	try:
		fp = open(DarkSectorCacheString, "r")
		#...
		fp.close()
	except FileNotFoundError:
		pass
		#fp = open(DarkSectorCacheString, "w")
		#...
		#fp.close()

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
	
	return MakeArchiveFileObjectList(StringList)

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
		if counter != 0 and counter % 3 == 0:
			
			try:
				
				obj = DownloableFiles(ProgramName=temp[0], Url=temp[1], File=temp[2])
				DownloableFilesObjectList.append(obj)
				
			except TypeError:
				
				print(temp)
				print("TypeError Exception: InitialSetup.py" % (len(temp)))
				
			temp = []
			counter = 0
			
		else:
			
			StringList[i] = StringList[i].replace("\n", "")
			temp.append(StringList[i])
			counter += 1
		
	return DownloableFilesObjectList
	
def MakeArchiveFileObjectList(StringList):
	
	DownloableFilesObjectList = []
	
	ProgramName = ""
	Url = ""
	File = ""
	Hash = ""
	ArchiveDirecctory = ""
	RenameFile = False
	
	StartBraceFound = False
	for line in StringList:
		if "{" in line:
			if StartBraceFound is True:
				print("Error. Found too many start braces in Links file.")
				sys.exit(0)
			else:
				StartBraceFound = True
		if "Program" in line:
			ProgramName = SplitLineAndGetIndexI(line, 1)
		elif "URL" in line:
			Url = SplitLineAndGetIndexI(line, 1)
		elif "DownloadFile" in line:
			File = SplitLineAndGetIndexI(line, 1)
		elif "SHA256HASH" in line:
			Hash = SplitLineAndGetIndexI(line, 1)
		elif "ReplaceExtractedArchive" in line:
			RenameFile = ConvertStrToBool(SplitLineAndGetIndexI(line, 1))
		elif "ExtractedArchive" in line:
			ArchiveDirectory = SplitLineAndGetIndexI(line, 1)
		elif "}" in line:
			DownloableFilesObjectList.append(ArchivedFiles(
				ProgramName=ProgramName,Url=Url, File=File,
				Hash=Hash, ArchiveDirectory=ArchiveDirectory,
				RenameFile=RenameFile))
			
			ProgramName = ""
			Url = ""
			File = ""
			Hash = ""
			ArchiveDirectory = ""
			RenameFile = False
			StartBraceFound = False
			
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
	
	print("CheckIfBashrcHasTagsAlready STUB")
	
	try:
		fp = open(UserDirectory.GetDirectory() + "/.bashrc", "r")
		#...
		fp.close()
	except FileNotFoundError:
		print(".bashrc does not seem to exist")
	
	return True

"""

	AddExportToBashrc
	
	*Should be called after files have been downloaded and extracted
	
	Returns nothing

"""
def AddExportToBashrc():
	
	global UserDirectory
	
	if CheckIfBashrcHasTagsAlready() is True:
		return
		
	fp = open(UserDirectory.GetDirectory() + "/.bashrc", "a")
	print("AddExportToBashrc STUB")
	fp.close()
