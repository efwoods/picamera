import picamera
import time
import json
import subprocess
import pygame
from wave import *
import pyaudio
import RPi.GPIO as GPIO
from time import sleep

def send_to_shell(command):
	p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()
	print(output.strip())

def take_a_picture(camera, name_of_picture):
	save_as = name_of_picture + '.jpg'
	camera.start_preview()
	time.sleep(2)
	camera.capture(save_as)
	camera.stop_preview()

def record_a_video(camera, name_of_video):
	save_as = name_of_video + '.h264'
	camera.start_preview()
	camera.start_recording(save_as)
	time.sleep(5)
	camera.stop_recording()
	camera.stop_preview()

def detect_faces(name_of_picture, shell_script):
	open_image = name_of_picture + '.jpg'
	curl_command = '\"curl -X POST -u \"apikey:EyXqAzJDlot3MJWc7nLSYHUqANe9jppChT9X8l8QyWNj\" -F \"images_file=@' + open_image +'\" \"https://gateway.watsonplatform.net/visual-recognition/api/v3/detect_faces?version=2018-03-19\"\"'
	print(curl_command)
	command = "/bin/sh /home/pi/picamera/" + shell_script + ' '  + curl_command
	p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()
	print(output.strip())

def play_sound():
	pygame.mixer.init()
	pygame.mixer.music.load("hello_world.wav")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
def speak(shell_script, text):
#	text = ''

	command = "/bin/sh /home/pi/picamera/" + 'voice.sh'

	print(command)
	send_to_shell(command)
##	play_sound()
	audio_filename = '/home/pi/picamera/hello_world.wav'
	play_sound_omxplayer(shell_script, audio_filename)

def test_sound():
	chunk = 1024
	f = wave.open(r"/usr/share/sounds/alsa/Rear_Center.wav","rb")
	
	p = pyaudio.PyAudio()

	stream = p.open(format = p.get_format_from_width(f.getsampwidth()),
		channels = f.getnchannels(),
		rate = f.getframerate(),
		output = True)

	data = f.readframes(chunk)

	while data:
		stream.write(data)
		data = f.readframes(chunk)

	stream.stop_stream()
	stream.close()

	p.terminate()

def play_sound_omxplayer(shell_script, audio_filename):	
	subcommand = '\"omxplayer' + ' ' + audio_filename + '\"'
	# /usr/share/sounds/alsa/Rear_Center.wav\"'
	command = "/bin/sh /home/pi/picamera/" + shell_script + ' '  + subcommand
	send_to_shell(command)



def test_arm():
	pin = 12
	wave_arm(pin)

def test_eye():
	shell_script = 'test.sh'
#	camera = picamera.PiCamera()
#	take_a_picture(camera, 'example')
##	record_a_video(camera, 'examplevid')
#	detect_faces('example', shell_script)

def test_expression():
	LEDpin = 33
	blink(LEDpin)

def test_ear():

def test_voice():
##	play_sound()
#	text = 'Friend'
#	speak(shell_script, text)
##	test_sound()
#	audio_filename = '/home/pi/picamera/hello_world.wav'
#	play_sound_omxplayer(shell_script, audio_filename)

def blink(pin):
	wave(pin)

def main():

if __name__=='__main__':
	main()
