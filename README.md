
# e-inkPicoCalendar

This repo contains the code needed create the image of my upcoming calendar that is then separately sent to an e-ink display via. 

This project started life as [e-inkCalendar](https://github.com/paulbuzzby/e-inkCalendar) which used a pi zero with a battery pack.

The problem I had is that the battery would drain quite fast (within a week). 
This is an attempt to get much better battery life by using a picoW to change the e-ink display and I will offload the calendar image generation to my NAS server.

This repo is the python code needed to create the image. the image is then hosted on a very simple python http server which is accessable locally.
In the future i would like to offload this to something simple in Azure but as I have a linux box 24/7 at home this was just as easy.


![On the Fridge](Images/onfridge.JPEG)

![Front Display](Images/frontview.JPEG)

![Back Display](Images/backview.JPEG)




## How It Works




Features of the calendar: 
- Displays Day and date then lists start time and duration of events
- The calendar always starts from today and fills with as many events that will fit.
- Timestamp of when the last update occured printed on the bottom left of screen

## Bugs / improvement idea's

- Not sure how the system handles events spanning multiple days
- Currently only works against outlook.com calendars

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
    "shutdownOnUpdate":true,
    "imagename":"display/calendar"
}
```

## Python commands used for testing

```bash
python -m http.server 9000 --directory /home/paul/e-inkPicoCalendar/display
```
This will launch a web server to host the files that the pico can then download

## CRONTab updates

edit CRONTAB via 

```
crontab -e
```

I had issues getting everything to run correctly and had to make sure the crontab stuff was done under my uses and to NOT use sudo

Then add these lines so that the server to server the calendar image is loaded when the server reboots
```
@reboot sleep 30; python -m http.server 9000 --directory /home/paul/e-inkPicoCalendar/display &
*/10 * * * * cd /home/paul/e-inkPicoCalendar && python CreateCalendarImage.py >> myscript.log 2>&1
```
Change your directory locations as needed
