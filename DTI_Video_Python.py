import serial
import vlc
import time


media_player=vlc.MediaPlayer() 
movie1 = vlc.Media("Bike_Riding.mp4") #play cycling video
media_player.set_media(movie1)

ser=serial.Serial("COM5", timeout=1) #set up connection between arduino and python

while True:
    command = ser.read() #read data from arduino
    if command:
        # flush serial for unprocessed data
        ser.flushInput()
        print("new command:", command)
        decode=command.decode("utf-8") #convert data in arduino from bytes to integer
        print("decoded value: ",decode)
##        print("decoded command: ", decode)
        if str(decode) == '1': #if user is cycling (1) play the video
            print("Playing movie")
            media_player.play() #play the video
            time.sleep(0.5) #delay 0.5sec
        elif str(decode)=='0': #if user is not cycling (0) pause the video
            print("pause")
            media_player.set_pause(3) #pause for 3 sec
            time.sleep(0.5) #delay 0.5sec

            

