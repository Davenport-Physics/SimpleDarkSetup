#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  SimpleDarkSetup.py
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
	from InitialSetup import InitialSetupBlock
	from Common import *
except ImportError:
	sys.path.insert(0, "DarkSectorCodeData.zip")
	from InitialSetup import InitialSetupBlock
	from Common import *
	
WorkingDirectoryString = "DarkSectorCode"

def main(args):
	
	global WorkingDirectory
	
	if len(args) > 1:
		HandleArguments(args)
	
	GetCurrentLocalDirectory()
	InitialSetupBlock(WorkingDirectoryString)
	
	return 0

"""

	HandleArguments
	
	Recieves a list of string arguments. It parses the commands and
	alters any data specified by the commands. This function is usually
	called first.
	
	Returns nothing

"""	
def HandleArguments(args):
	
	global WorkingDirectory
	
	return

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
