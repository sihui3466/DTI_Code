import serial
import vlc
import time


media_player=vlc.MediaPlayer()
movie1 = vlc.Media("Bike_Riding.mp4")
media_player.set_media(movie1)

ser=serial.Serial("COM5", timeout=1)

while True:
    command = ser.read()
    if command:
        # flush serial for unprocessed data
        ser.flushInput()
        print("new command:", command)
        decode=command.decode("utf-8")
        print("decoded value: ",decode)
##        print("decoded command: ", decode)
        if str(decode) == '1':
            print("Playing movie")
            media_player.play()
            time.sleep(0.5)
        elif str(decode)=='0':
            print("pause")
            media_player.set_pause(3)
            time.sleep(0.5)

            

