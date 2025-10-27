
# e-inkPicoCalendar

This repo contains the code needed to drive a 7.5" e-ink display and act as a calendar. 

This project started life as [e-inkCalendar](https://github.com/paulbuzzby/e-inkCalendar) which used a pi zero with a battery pack.

The problem I had is that the battery would drain quite fast (within a week). 
This is an attempt to get much better battery life by using a picoW to change the e-ink display and I will offload the calendar image generation to my NAS server.


![On the Fridge](Images/onfridge.JPEG)

![Front Display](Images/frontview.JPEG)

![Back Display](Images/backview.JPEG)



## Hardware Required

- [Waveshare 800×480 7.5inch E-Ink display HAT for Raspberry Pi](https://www.waveshare.com/7.5inch-e-paper-hat.htm) - Be careful as there is a version that also does red. While you will be able to make it work the driver code would need changing. Make sure you just buy the black and white display


- [Magnets 20 x 10 x 2mm](https://www.amazon.co.uk/gp/product/B07VMMK12N) - Glued into the 3D printed case

- [25cm Micro USB USB 2.0 Male Connector to Micro USB 2.0 Female Extension Cable Pitch 17.5mm With screws Panel Mount Hole](https://www.aliexpress.com/item/1005002626850501.html) - Used to make charging easier.

- 6x M3x8 hex bolts to hold the 3D printed case together

- 3D printer - to print the case


## How It Works




Features of the calendar: 
- Battery life needs more testing but should last a couple of weeks. The Rpi zero 2 may be more power hungry than the Rpi zero. Retriving the calendar information takes the most amount of time. Maybe this can be optimised. I also have to force a wait command in the CronJob to make sure the system connects to the wifi
- Displays Day and date then lists start time and duration of events
- The calendar always starts from today and fills with as many events that will fit.
- Battery level is displayed in top right corner
- Timestamp of when the last update occured printed on the bottom left of screen

## Bugs / improvement idea's

- Not sure how the system handles events spanning multiple days
- Currently only works against outlook.com calendars
- Would like to add a button to force a refresh

## Share your outlook Calendar

1. Login to [Outlook](www.outlook.com)
2. Top right corner press the Cog (settings)
3. Select the "View all outlook settings" link
* Select Calendar and then Shared calendars
* Under "Publish a calendar" select your calendar and "Can view all details" option
* click the "Publish" link
![Calendar](Images/ShareCalendar1.png)

* You will then see an ICS link be generated
![Calendar](Images/ShareCalendar2.png)

**Make a note of the ICS link. You will need it later**




## Config file
Should look like

```json
{
    "icsURL": "",    
    "dayToCapture": 8,
    "shutdownOnUpdate":true
}
```

## Python commands needed

```bash
python -m http.server 9000 --directory /home/paul/e-inkPicoCalendar/display
```
This will launch a web server to host the files that the pico can then download

## CRONTab updates

edit CRONTAB via 

```
sudo crontab -e
```

Then add this line so that the server to server the calendar image is loaded when the server reboots
```
@reboot sleep 30; sudo python -m http.server 9000 --directory /home/paul/e-inkPicoCalendar/display &
```



@reboot sleep 30; cd /home/pi/e-inkCalendar && sudo python3 main.py &