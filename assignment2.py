import BlynkLib
from time import sleep
import time
from sense_hat import SenseHat

# Define Colours
RED = (255, 0, 0) # RGB for Red
GREEN = (0, 255, 0) # RGB for Green
BLUE = (0, 0, 255) # RGB for Blue
WHITE = (255, 255, 255) # RGB for White

# Initialise SenseHat
sense = SenseHat()
sense.clear(GREEN) # #Start with Colour Green

# Blynk Cloud Setup

# Blynk authentication token
BLYNK_AUTH ='T-n3xXL5ApMWdsJcftpDWnGhanIkBkXT'

# Intialise the Blynk instance
blynk = BlynkLib.Blynk(BLYNK_AUTH)


def get_environmental_data(deviceID):

	# Retrieve temperature and humidity data from SenseHat
	temp = sense.get_temperature()
	humidity = sense.get_humidity()

	# Create a dictionary
	data = {
	     "deviceID": deviceID,
	     "temp": round(temp, 2),
	     "humidity": round(humidity, 2)
	}

	return data

deviceID = "20109020" # Device ID number

# Register handler for virtual pin v2 write event
@blynk.on("V2")
def handle_v2_write(value):
    print("Switch triggered!") # 1 When switched on / 0 when switched Off
    button_value = value[0]
    print(f'Current button value: {button_value}')
    if button_value=="1":
        sense.clear(0, 255, 0) # Colour changes to green once Online (RGB colours)
    else:
        sense.clear()

# Testing of temperature and Humidity, Starting Blynk
if __name__ == "__main__":
    print("Starting script...")
    print("Blynk application also started. Listening for events...")
    try:             # Get latest data
        while True:
            blynk.run() # Process Blynk events
            sleep(1) # Add a short delay to avoid CPU usuage

            data = get_environmental_data(deviceID)    
            temp = data["temp"]
            humidity = data["humidity"]

            # Print data - Printed in JSON format
            print(data) 

            # Display messages / conditions for Rasberry Pi
            if temp >= 30 and humidity <= 40:                 # Comination of temp(>=30) and humidity(<=36)
                print("Displaying Hot and Dry room message") # message for terminal
                sense.show_message("NEED WATER ASAP..!", text_colour=WHITE)
                blynk.log_event("heatwave_event")       # generate an event on Blynk every time Threshold is met
                print("Temp event logged")              # Message to Terminal confirming event created
                sleep(0.1)                              # Delay to prevent high CPU usage
            elif  temp >= 30:                           # Temp less than or equal to 30
                print("Displaying Hot room message")    # message for terminal
                sense.show_message("HOT! WATER SOON!", text_colour=RED)
                blynk.log_event("temp_event")              # generate an event on Blynk every time Threshold is met
                print("Temp event logged")                 # Message to Terminal confirming event created
                sleep(0.1)                                 # Delay to prevent high CPU usage
            elif humidity <= 40:                        # Humidity less than or equal to 40 
                print("Displaying Dry room message")    # message for terminal
                sense.show_message("DRY! WATER SOON!", text_colour=BLUE)
                blynk.log_event("humidity_event")           # generate an event on Blynk every time Threshold is met
                print("Humidity event logged")              # Message to Terminal confirming event created
                sleep(0.1)                              # Delay to prevent high CPU usage
            else:
                print("Displaying everything fine message") # message for terminal
                sense.show_message("ALL CLEAR!", text_colour=GREEN)
            
            blynk.run() # Process Blynk events
            blynk.virtual_write(0, sense.temperature)
            blynk.virtual_write(1, sense.humidity)

            time.sleep(1) # 1 second delay to prevent high CPU usage
    except KeyboardInterrupt:
            print("Application stopped.")
            sense.clear()  # Clear the colour from the SenseHat