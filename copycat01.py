#!/usr/bin/env python3


# The following line will create the directory if it does not exist already

#import aditional code to complete our task
import shutil
import os

def main():
    os.chdir("/home/student/mycode/")
    shutil.copy("5g_research/sdn_network.txt" , "5g_research/sdn_network.txt.copy")
    shutil.copytree("5g_research/" , "5g_research_backup/")

if __name__ == "__main__":
    main()






