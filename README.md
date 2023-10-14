# Smpkg, Duel Platform Package Manager
![Image was supposed to be here](https://github.com/manav-harsana/smpkg/blob/main/config/images/banner.png?raw=true)

# Future of this project (2023/10/14)
This Project will move to a new repository under a new name very soon! I have been working behind the doors and am making some massive changes by the time I release the next version the script will be much more advanced and better with multiple features, but this will take longer than the initially planned "weekly" releases. Next release is supposed to be big and possibly the first official 1.0 release.
Some Features Confirmed to be added are:
- Auto Fetch Updates for script
- Option to enable/disable FOSS/Non-FOSS Repositories
- Smaller commands
- Custom scripts for each app (This means that now even more different kinds of packages can be published)
- A New name!
- A New logo!
- Better Optimised codebase
- Many Many more apps/packages in the repositories
- Android Support
- And more!

## What Is Smpkg?
smpkg is a script entirely written in python which provides a GNU/Linux Package manager like functionality to Android and Windows. Current builds are in very early stages and only support Windows packages.

## Why Smpkg?
Smpkg directly fetches downloads for the desired app present in the repository eliminating searching for apps on the web.

## Installation
The package is portable but a few dependencies are required:
- python 3.10+
- pip
- shutil
- requests
- subprocess
- termcolor
- tqdm

In Terminal Run:
```
pip install shutil requests tqdm termcolor
git clone https://github.com/manav-harsana/smpkg.git
# or download zip file manually
cd smpkg
python .\smpkg.py
```

## To-do (WIP)

| Features | Progress|
|-------------|------------|
|Automatically fetch repository and smpkg update and notify user |  ×××××××××10 |
|Android Support | ×××××××××10 |
|Separate FOSS and "Non-Free" repositories | ××××××××10 |
|Handle updates for all apps in repository| ××××××7••• |
|GitHub.io Webpage|×××××6••••|

## Latest Build Status
|Smpkg Version| 0.3.1 |
|-------------------|-----|
|Package Branch|Stable|
|Repository Version|0.4|
|Support|Windows currently (Android not added yet)|
|Requirements| Python 3/3+|
|Python Dependencies| requests, shutil, os, sys, termcolor, subprocess|

## Screenshots (v0.3 beta)
![Image was supposed to be here](https://github.com/manav-harsana/smpkg/blob/main/config/images/icon.png?raw=true)
![Image was supposed to be here](https://github.com/manav-harsana/smpkg/blob/main/config/images/screenshot1.png?raw=true)
![Image was supposed to be here](https://github.com/manav-harsana/smpkg/blob/main/config/images/screenshot2.png?raw=true)
![Image was supposed to be here](https://github.com/manav-harsana/smpkg/blob/main/config/images/screenshot3.png?raw=true)
![Image was supposed to be here](https://github.com/manav-harsana/smpkg/blob/main/config/images/screenshot4.png?raw=true)
![Image was supposed to be here](https://github.com/manav-harsana/smpkg/blob/main/config/images/screenshot5.png?raw=true)

### Further Details
- License: GNU GPL 3.0+
- Category: Free and Open Source Software
