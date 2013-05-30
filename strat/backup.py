#!/usr/bin/python
import os


src="./"
dest="~/Dropbox/fantacy/pt/"
cmd = "rsync -aP" + ' '+ src +' ' + dest

print "this will excute "
print "\"", cmd, "\""
choice=raw_input("Are you sure? y/n\n")
if choice=='y':
    print cmd
    os.system(cmd)
else:
    print "abord"

