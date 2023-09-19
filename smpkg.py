# smpkg Is a multiplatform (currently only for windows)
#package manager script which aims to add
# the GNU/Linux package manager like functionality to other OS's
# This package is licensed Under the GNU General Public License 3.0+ (GNU GPL 3.0+)

## Import Required dependencies
import os, sys, shutil, requests, subprocess, urllib.request
from termcolor import colored, cprint
from urllib.request import urlretrieve
from subprocess import Popen, PIPE
from tqdm import tqdm
pkg_repo= open("repository\main.smrepo").read().splitlines()
## Define StartUp Text
strtinfo=colored("\033[1msmpkg early beta \nVersion: 0.2 beta \nType help to get started\033", 'green')
print(strtinfo)

## Manage tmp folder
try: ## Create tmp folder
    os.mkdir("tmp")
except OSError as error: ##Skip if tmp already exists
    print(colored("\033[1mWARNING:\033", 'yellow', attrs=['blink']), "The 'tmp' directory already exists from previous sessions\n it probably has old data consider properly exiting the \n session later using 'exit' command.")

## Updates (Still in progress!)
#print("Checking for updates...")
#currentVersion = "0.2"
#currentRelease = "2"
#
#datafile = requests.get('', stream=True)
#localfile='tmp\smpkg-updates.txt'
#with open(localfile, 'wb')as file:
#    file.write(datafile.content)
#updaterfile=open('tmp\smpkg-updates.txt', 'r')
#latestVersion=updaterfile.readline(2)
#latestrelease=updaterfile.readline(3)
#latestBranch=updaterfile.readline(4)
#if currentRelease==latestrelease:
#    print('Smpkg is on latest release 0.2 beta')
#else:
#    print('A new release', latestVersion, latestBranch, 'is available, run "smpkg -u" to update to the latest release.')
#    print(latestVersion, latestBranch, latestrelease)

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
        print("Version: 0.2 beta \nYour Platform: Windows\nRepository Version: 0.2 \nPackages: 2 \nCommands: \nsmpkg -l: lists all packages \nsmpkg -f: finds packages with entered characters \nsmpkg -i: downloads and installs packages \nsmpkg -u: check for updates and install if available") ## print help output
    if cmd=="smpkg -f":
        pkg=input("Find a package: ")
        with open(r'repository\main.smrepo', 'r') as fp:
            print("Listing packages with",pkg,":")
            for l_no, line in enumerate(fp):
                # search string
                if pkg in line:
                    print(line, end="")
                    # don't look for next lines
    if cmd=='smpkg -i':
        pkg=input("Enter package name to install: ")
        if pkg in pkg_repo:
            cnfrminstl=input("Do you want to proceed to download and install? [Yes/No] ")
            if cnfrminstl=='Yes' or cnfrminstl=='yes' or cnfrminstl=='y' or cnfrminstl=='Y': ## is yes?
                print("Obtaining info...")
                with open(r'repository\main.smrepo', 'r') as fp:
                    for l_no, line in enumerate(fp):
                        if pkg in line:
                            pkg_id=str(l_no)
                with open(r'repository\main.smurl', 'r') as fp:
                    for l_no, line in enumerate(fp):
                        if pkg_id in str(l_no):
                            pkg_url=line.replace('\n', '')
                with open(r'repository\main.sminfo', 'r') as fp:
                    for l_no, line in enumerate(fp):
                        if pkg_id in str(l_no):
                            pkg_info=line.replace('\n', '')
                print("Downloading", pkg_info)
                os.chdir("tmp")
                response = requests.get(pkg_url, stream=True) ## start download, stream=True (that means the file will be written to storage and not to RAM first)
                total_size_in_bytes= int(response.headers.get('content-length', 0))
                block_size=1024
                progress_bar=tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True)
                with open(pkg_info, mode="wb") as file:
                     for data in response.iter_content(block_size):
                         progress_bar.update(len(data))
                         file.write(data) ## write that chunk
                progress_bar.close()
                print("Download Complete..")
                print("Executing Installer..")
                os.system(pkg_info)
                print("Installer Executed..")
                os.chdir("..")
            elif cnfrminstl=='No' or cnfrminstl=='no' or cnfrminstl=='N' or cnfrminstl=='n':
                print("Installation Aborted by user")
        else:
            print("Package not in repository")
    if cmd=='smpkg -l':
        print("Listing all packages in repository: ")
        print(pkg_repo)
