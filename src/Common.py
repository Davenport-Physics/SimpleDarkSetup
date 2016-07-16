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
import urllib.request

"""

	MakeDirectory
	
	Receives a string variable which ought to be the name of a directory.
	If the length of the Directory is zero, i.e it doesn't have any usable
	data, then an error would have occurred and no directory would be made.
	
	On the otherhand, if len(directory) > 0, it will attempt to make a
	directory. If a directory cannot be made, it probably already exists.
	
	Returns nothing

"""
def MakeDirectory(Directory = ""):
	
	#Stat if directory exists. May not be necessary?
	
	#May want to return error code?
	if len(Directory) == 0:
		print("Error: MakeDirectory called with no directory name")
		return
	
	try:
		os.mkdir(Directory)
	except OSError:
		print("Directory %s already exists." % (Directory))
	
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

	https://docs.python.org/3/library/urllib.html

"""
	
def DownloadFileFromUrl(DownloadObj, Directory):
	
	print("DownloadFileFromUrl STUB")
	
"""

	https://docs.python.org/3.5/library/tarfile.html

"""
	
def ExtractTarBall(TarBallFile, Directory):
	
	ReducedTarBallFile = TarBallFile.replace("tar.gz", "")
	MakeSubprocessCall("tar -xvzf " + TarBallFile + " " ReducedTarBallFile)
	

class DownloableFiles(object):
	
	def __init__(self, ProgramName = "", Link = "", File = ""):
		
		self.ProgramName = ProgramName
		self.Link = Link
		self.File = File
		
	def PrintObjContents(self):
		
		print("ProgramName = %s" % (self.ProgramName))
		print("Link = %s" % (self.Link))
		print("File = %s\n" % (self.File))
		
	def GetProgramName(self):
		
		return self.ProgramName
		
	def GetFileLink(self):
		
		return self.Link
		
	def GetFile(self):
		
		return self.File
		
