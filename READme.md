# Assignment 2: Networking using Connected Devices
## Overview
The objective of the project is to create a working project using networking/IoT devices. The devices are to have some physical aspect which includes sensors/devices(SesneHats).

Watch demonstration on YouTube - https://youtu.be/PJPEZuKRuoo?feature=shared.

## Project Description
Before going into detail about the project, a brief background on the idea behind it. We are currently in winter, across the country there will be heating systems on to esnure houses keep warm. Businesses also will have these systems running throughout the day. One thing in common with both a local business and someone living in a family home is the majority of them will have some type of plant situated somewhere in their building.

It is here my project comes in. It will be a device focused process, that ensures that indoor plants are getting enough water to stay healthly. A Raspberry Pi device with sensors will detect the temperature of the room. It will also detect the humidity of the room using sensors. Using the python language and Visual Studio Code a threshold for temperature and humidity will be setup.

Within Visual Studio Code the threshold for temperature set at equal to or over 30 degrees Celecius of Raspberry Pi. For humidity the threshold will be less than or equal to 40 percent. Another threshold of between 30 degrees and 40 percent will be set as a "must take action now" high bar. The sensehat LED's will be set to different colours depending on the current enviroment. 

The purpose of the LED's will be to display a message to the user on the Raspberry Pi once it it switched on, indicating the current condition of the room and what action to take. The LED's will be white for the high bar(between 30 and 40), red for temperature(over 30), blue for humidity(below 40) and green if the room is in perfect condition. If viewed on a computer temperature and humidity will be contintinually posted into the terminal in JSON format. Once the program is run it will continue in this loop, with the terminal messages explaining what is occuring throughout the process.

Once a trigger for a threhold has been set off for any one of the conditions, the user will get a notification on their Blynk app on their phone. This will be a Blynk event and be lablled as to whihc threshold was met. Also on Blynk the user will receive an email for each individiaul threshold(temperature, humidity, high bar).

## Set up and run project
#### Needed for Project
* Visual Studio Code
* Blynk
* Raspberry Pi
* SenseHat

#### Copy Github project Url
* Click on code
* Copy HTTPS

#### Open account on Blynk
* Follow https://blynk.cloud/dashboard/login
* Sign up with your email account

#### Blynk
* Click on "Developer zone"
* Click on New template
* Add your device and setup

#### Visual Studio Code
* Open terminal, type: ssh <configured pi name> | Enter password | Now in ssh mode
* Open terminal, type: python <filename.py> to run python code

#### Project Dependencies:
* VS Code, python extension version: 22.1.3
* Wifi

## Links
#### Links to my project
1. https://github.com/Jake-Nagle123/IoT-devices.git
2. https://blynk.cloud/dashboard/login
3. https://youtu.be/PJPEZuKRuoo?feature=shared
