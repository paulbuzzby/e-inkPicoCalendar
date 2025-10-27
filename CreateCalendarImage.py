from datetime import datetime
from datetime import timedelta 
import json
import logging
import sys

from ImageCreator import *
from iCalendarHelper import *

        
logging.basicConfig(filename="logfile.log", format='%(asctime)s %(levelname)s - %(message)s', filemode='a')
logger = logging.getLogger('eInkCalendar')
logger.addHandler(logging.StreamHandler(sys.stdout))  # print logger to stdout
logger.setLevel(logging.INFO)

configFile = open('config.json')
config = json.load(configFile)

logger.info("JSON config loaded {}".format(config))

icsLocation = config["icsURL"]
dayToCapture = config["dayToCapture"]

#dayToCapture
now = datetime.now()
now8 = now + timedelta(days=dayToCapture)
start_date = (now.year, now.month, now.day)
end_date =   (now8.year, now8.month, now8.day)


calendarFile = GetCalendarFile(logger, icsLocation)
calEvents = ExtractCalendarEvents(calendarFile, start_date, end_date)
eventsImage = BuildEvents(calEvents)

#eventsImage.show()
eventsImage.save('calendar_test.png')
im = eventsImage.convert("L")
im = im.transpose(Image.ROTATE_90)
# 1-bit, no dithering for clean pixels
mono = im.convert("1", dither=Image.NONE)

# E-ink drivers often want inverted polarity

mono = ImageOps.invert(mono.convert("L")).convert("1", dither=Image.NONE)

# File for the Pico (PBM P4). Windows Photos won’t open it. That’s fine.
mono.save("calendar_test.pbm")
print("Done")