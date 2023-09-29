# Smpkg, Duel Platform Package Manager
![Image was supposed to be here](https://github.com/manav-harsana/smpkg/blob/main/config/images/banner.png?raw=true)

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
|Automatically fetch repository and smpkg update and notify user |  ××××××7••• |
|Android Support | ×××××6•••• |
|Separate FOSS and "Non-Free" repositories | ××××5••••• |
|Handle updates for all apps in repository| ××3••••••• |
|GitHub.io Webpage|×2••••••••|

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
