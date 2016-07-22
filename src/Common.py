#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Common.py
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

import subprocess as sp
import os
import os.path
import urllib
import tarfile
import hashlib
	
"""

	MakeSubprocessCall
	
	Receives a string variable and calls it command. Using the command
	variable it will attempt to interact with a shell, in a somewhat
	dangerous manner, and run the command specified by the variable
	command.
	
	Using Python facilities is preferable to using bash/shell commands
	
	Returns a string

"""
def MakeSubprocessCall(command):
	
	return str(sp.check_output(command, shell = True))
	
	
"""

	TODO

	https://docs.python.org/3/library/urllib.html
	

"""
	
def DownloadFileFromUrl(DownloadObj, Directory):
	
	SubProcessCommand = "wget -O " + Directory + "/" + DownloadObj.GetFile()
	SubProcessCommand += " " + DownloadObj.GetUrl()
	
	MakeSubprocessCall(SubProcessCommand)
	
	
"""

	CheckIfFileAlreadyDownloaded
	
	TODO
	
	Finish Comments

"""
def CheckIfFileAlreadyDownloaded(DownloadObj, Directory):
	
	if CheckIfFileExists(DownloadObj.GetFile(), Directory) == False:
		return False
	
	"""
	
		If not provided a Hash, the file should be redownloaded. This
		is the case for zip files downloaded from github, whose hash
		may change constantly.
	
	"""
	if len(DownloadObj.GetHash()) == 0:
		return False

	LocalFileHash = GetLocalHash(DownloadObj, Directory)		
	return CheckSHA256Hash(LocalFileHash, DownloadObj.GetHash())
	
	
def CheckIfFileExists(File, Directory):
	
	TempFile = Directory + "/" + File
	
	return os.path.exists(TempFile)
	
def CheckSHA256Hash(CurrentHash, RealHash):
	
	print("CheckSHA256Hash STUB")
	
	if CurrentHash == RealHash:
		return True
	
	return False

"""

	GetLocalHash
	
	TODO

"""	

def GetLocalHash(DownloadObj, Directory):
	
	print("GetLocalHash STUB")
	
	Hash = hashlib.sha256()
	
	try:
		fp = open(Directory + "/" + DownloadObj.GetFile())
		for chunk in iter( lambda: fp.read(4096), b"" ):
			Hash.update(chunk)
		fp.close()
	except FileNotFoundError:
		print("GetLocalHash FileNotFoundError")
		return ""
		
		
	return Hash.hexdigest()
	

"""
	
	TODO

	https://docs.python.org/3.5/library/tarfile.html

"""
	
def ExtractTarBall(TarBallFile, Directory):
	
	print("Extracting " + TarBallFile)
	
	tar = tarfile.open(Directory + "/" + TarBallFile, "r:gz")
	tar.extractall(Directory)
	tar.close()
	
	print("Done extracting " + TarBallFile)
	

"""

	TODO
	
	Implement using Python Libs
	
	https://docs.python.org/2/library/zipfile.html

"""	

def ExtractZip(ZipFile, Directory):
	
	print("Extracting " + ZipFile)
	MakeSubprocessCall("unzip " + Directory + "/" + ZipFile + " -d " + Directory)
	print("Done extracting " + ZipFile)

	
"""

	GetCurrentLocalDirectory

"""
def GetCurrentLocalDirectory():
	
	return MakeSubprocessCall("pwd")
	
	
def GetUserHomeDirectoryString(string):
	
	if len(string) == 0:
		return
		
	tempstring = None
	
	if string[0] == 'b':
		string = string[1:-1]
	
	tempstring = string.replace("\n","")
	tempstring = tempstring.replace("'", "")
		
	DelimitedList = tempstring.split("/")
	return "/" + DelimitedList[1] + "/" + DelimitedList[2]
	

class DownloableFiles(object):
	
	def __init__(self, ProgramName = "", Url = "", File = "", Hash = "", RenameFile = False):
		
		self.ProgramName = ProgramName
		self.Url = Url
		self.File = File
		self.Hash = Hash
		self.RenameFile = RenameFile
		
	def PrintObjContents(self):
		
		print("ProgramName = %s" % (self.ProgramName))
		print("Url = %s" % (self.Url))
		print("File = %s\n" % (self.File))
		
	def GetProgramName(self):
		
		return self.ProgramName
		
	def GetUrl(self):
		
		return self.Url
		
	def GetFile(self):
		
		return self.File
		
	def GetHash(self):
		
		return self.Hash
		
	def GetRenameFileBool(self):
		
		return self.RenameFile
		
		
class ArchivedFiles(DownloableFiles):
	
	def __init__(self, ProgramName = "", Url = "", File = "", Hash = "", ArchiveDirectory = "", RenameFile = False):
		
		self.ProgramName = ProgramName
		self.Url  = Url
		self.File = File
		self.Hash = Hash
		self.RenameFile = RenameFile
		self.ArchiveDirectory = ArchiveDirectory
		
	def GetArchiveDirectory(self):
		
		return self.ArchiveDirectory
		
		
class Directories(object):
	
	def __init__(self, Directory = ""):
		
		self.Directory = Directory
		
		
	"""

	MakeDirectory
	
	Receives a string variable which ought to be the name of a directory.
	If the length of the Directory is zero, i.e it doesn't have any usable
	data, then an error would have occurred and no directory would be made.
	
	On the otherhand, if len(directory) > 0, it will attempt to make a
	directory. If a directory cannot be made, it probably already exists.
	
	Returns nothing

	"""

	def MakeDirectory(self):
		
		if len(self.Directory) == 0:
			print("Error: MakeDirectory called with no directory name")
			return
		try:
			os.mkdir(self.Directory)
		except OSError:
			print("Directory %s already exists." % (self.Directory))
		
	def GetDirectory(self):
		
		return self.Directory
		
