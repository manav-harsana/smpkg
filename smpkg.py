# smpkg Is a multiplatform (currently only for windows)
#package manager script which aims to add
# the GNU/Linux package manager like functionality to other OS's
# This package is licensed Under the GNU General Public License 3.0+ (GNU GPL 3.0+)

## Import Required dependencies
import os, sys, shutil, requests, subprocess
from termcolor import colored, cprint
from urllib.request import urlretrieve
from subprocess import Popen, PIPE

## Define StartUp Text
strtinfo=colored("\033[1msmpkg early development \nVersion: 0.1 development \nType help to get started\033", 'green')
print(strtinfo)

## Manage tmp folder
try: ## Create tmp folder
    os.mkdir("tmp")
except OSError as error: ##Skip if tmp already exists
    print(colored("\033[1mWARNING:\033", 'yellow', attrs=['blink']), "The 'tmp' directory already exists from previous sessions\n it probably has old data consider properly exiting the \n session later using 'exit' command.")

## Comandline Setup
while strtinfo==strtinfo: ##Simple workaround to create a never ending loop
    cmd=input(colored("\033[1m> \033", 'green')) ## Entry marker
    if cmd=="exit": ## Define 'exit' command
        cnfrmext=input("Are you sure you want to exit? the tmp folder will be cleared [Yes/No]") ## confirm exit
        if cnfrmext=='Yes' or cnfrmext=='yes' or cnfrmext=='y' or cnfrmext=='Y': ## is yes?
            shutil.rmtree('tmp') ## remove tmp folder and files
            break ## break the loop
        elif cnfrmext=='': ## is no?
            print("Not exiting...") ## tell user 'not exiting'
            continue ## continue loop
    if cmd=="help": ## Define 'help' command
        print("Version: 0.1 dev \nYour Platform: Windows\nRepository Version: 0.1 dev \nPackages: 1") ## print help output
    if cmd=="smpkg -i librewolf": ## Demo for getting package
        cnfrminstl=input("Do you want to install Librewolf? [Yes/No]")
        if cnfrminstl=='Yes' or cnfrminstl=='yes' or cnfrminstl=='y' or cnfrminstl=='Y': ## is yes?
            print("Downloading librewolf version: 117.0.1-1") ## to confirm download is running
            url="https://gitlab.com/api/v4/projects/44042130/packages/generic/librewolf/117.0.1-1/librewolf-117.0.1-1-windows-x86_64-setup.exe" ## download url
            query_parameters={"downloadformat":"csv"} ## to define download format
            response = requests.get(url, params=query_parameters, stream=True) ## start download, stream=True (that means the file will be written to storage and not to RAM first)
            with open("tmp/librewolf-117.0.1-1.exe", mode="wb") as file: ## define stored file name and conditions
                for chunk in response.iter_content(chunk_size=10 * 1024): ## Write the file for every 10kb downloaded
                    file.write(chunk) ## write that chunk
            print("Download Complete running installer..") ## Confirm Download is completed!
            os.system("tmp/librewolf-117.0.1-1.exe")
        elif cnfrminstl=='No' or cnfrminstl=='no' or cnfrminstl=='N' or cnfrminstl=='n':
            print("Installation Aborted by user")
