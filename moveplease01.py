#!/usr/bin/python3
import shutil
import os

def main():
    
    os.chdir('/home/student/mycode/')

    shutil.move('raynor.obj', 'ceph_storage/')

    #prompting user for new file name
    xname = input('What is the new name for kerrigan.obj? ')

    #renaming file name
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
