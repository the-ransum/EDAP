import requests
import tkinter as tk
from tkinter import messagebox
import webbrowser

from app_tray import tray
from autopilot import resource_path, RELEASE

def update():
	releases_url = 'https://api.github.com/repos/the-ransum/EDAP/releases'
	response = requests.get(releases_url)
	# Raise an exception if the API call fails.
	response.raise_for_status()
	data = response.json()
	
	try:
		latest_release = data[0]['tag_name']
	except Exception as e:
		print(e)
		
	if latest_release and latest_release != RELEASE:
		message = 'A newer version of EDAP is available\nWould you like to go to the download page?'
		root = tk.Tk()
		root.withdraw()
		root.tk.call('wm', 'iconphoto', 
		             root._w, 
		             tk.PhotoImage(file=resource_path('assets/logo.png')))
		
		go_to_update = messagebox.askyesno("EDAP - Update", message)
		
		if go_to_update:
			webbrowser.open_new(data[0]['html_url'])
			return True
		
	return False

if __name__ == '__main__':
	if not update():
		tray()
