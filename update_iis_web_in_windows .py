import os
import glob
import shutil
import sys
import getopt
import logging
import subprocess




def copy_ext_files(source_dir, dest_dir, ext):
    if not os.path.exists(source_dir):
        logging.error("Source folder %s not exist" % source_dir)
        sys.exit(1)
    if not os.path.exists(dest_dir):
        logging.info("Target folder %s not exist. now created" % dest_dir)
        os.makedirs(dest_dir)
    os.chdir(source_dir)
    for file in glob.glob(ext):
        try:
            shutil.copy2(os.path.join(source_dir, file), dest_dir)
        except IOError as e:
            print "Copy Problem : %s" % e
            sys.exit(1)

			
			
source_dir = 'c:\\git\\source'	
target_dir = 'C:\\inetpub\\wwwroot'
ext_list = ['*.html','*.htm']

#Update Files
for ext in ext_list:
   print ext
   copy_ext_files(source_dir, target_dir, ext)


#Restrat IIS
command_stop = "net stop w3svc"
command_start = "net start w3svc"
proc = subprocess.call(command_stop)
proc = subprocess.call(command_start)


 