# Smpkg, Duel Platform Package Manager
![Image was supposed to be here](https://github.com/manav-harsana/smpkg/blob/main/config/images/banner.png?raw=true)

## What Is Smpkg?
smpkg is a script entirely written in python which provides a GNU/Linux Package manager like functionality to Android and Windows. Current builds are in very early stages and only support Windows packages with no repository yet.

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

## Todo (WIP)

| Features | Progress|
|-------------|------------|
|Automatically fetch repository and smpkg update and notify user |  ××××××××8•• nearly there|
|Handle updates for all apps in repository| 0%•••••••••• not started yet|
|Android Support | ×2•••••••• just started|
| Separate FOSS and "Non-Free" repositories | ××××5••••• midway|
|Logo |×××××××××10 complete|

## Build Status
|Smpkg Version| 0.3|
|-------------------|-----|
|Package Branch|Beta|
|Repository Version|0.3|
|Support|Windows currently (Android not added yet)|
|Requirements| Python 3/3+|
|Python Dependencies| requests, shutil, os, sys, termcolor, subprocess|

## Screenshots
![Image was supposed to be here](https://github.com/manav-harsana/smpkg/blob/main/config/images/icon.png?raw=true)
![Image was supposed to be here](https://github.com/manav-harsana/smpkg/blob/main/config/images/screenshot1.png?raw=true)
![Image was supposed to be here](https://github.com/manav-harsana/smpkg/blob/main/config/images/screenshot2.png?raw=true)
![Image was supposed to be here](https://github.com/manav-harsana/smpkg/blob/main/config/images/screenshot3.png?raw=true)
![Image was supposed to be here](https://github.com/manav-harsana/smpkg/blob/main/config/images/screenshot4.png?raw=true)
![Image was supposed to be here](https://github.com/manav-harsana/smpkg/blob/main/config/images/screenshot5.png?raw=true)

### Further Details
- License: GNU GPL 3.0+
- Category: Free and Open Source Software
