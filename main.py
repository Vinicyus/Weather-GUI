import tkinter as tk
from tkinter import font
import requests
from PIL import Image, ImageTk

HEIGHT = 500
WIDTH = 600

def format_response(json, module):
	if module == 1:
		try:
			city = json['city']['name']
			desc = json['list'][0]['weather'][0]['main']#['description']
			temp = json['list'][0]['main']['temp']
			final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (city, desc, temp)
		except:
			final_str = 'Sorry, there was an error.'
		return final_str
	elif module == 2:
		try:
			desc = json['list'][8]['weather'][0]['main']
			temp = json['list'][8]['main']['temp']
			final_str = '     24Hrs\n\n     %s \n    %s°C' % (desc, temp)
		except:
			final_str = 'Sorry, there was an error.'
		return final_str
	elif module == 3:
		try:
			desc = json['list'][16]['weather'][0]['main']
			temp = json['list'][16]['main']['temp']
			final_str = '     48Hrs\n\n     %s \n    %s°C' % (desc, temp)
		except:
			final_str = 'Sorry, there was an error.'
		return final_str
	elif module == 4:
		try:
			desc = json['list'][24]['weather'][0]['main']
			temp = json['list'][24]['main']['temp']
			final_str = '     72Hrs\n\n     %s \n    %s°C' % (desc, temp)
		except:
			final_str = 'Sorry, there was an error.'
		return final_str

def get_weather(city):
	key = '0ec8938f3a93af120547a046ee099595'
	url = 'https://api.openweathermap.org/data/2.5/forecast'
	params = {'APPID': key, 'q': city, 'units': 'Metric'}
	response = requests.get(url, params=params)
	json = response.json()

	#current weather
	label['text'] = format_response(json, 1)
	icon_name = json['list'][0]['weather'][0]['icon']
	open_image(icon_name, 1)

	#24hrs
	forecast_label_24['text'] = format_response(json, 2)
	forecast_icon_24 = json['list'][8]['weather'][0]['icon']
	open_image(forecast_icon_24, 2)

	#24hrs
	forecast_label_48['text'] = format_response(json, 3)
	forecast_icon_48 = json['list'][16]['weather'][0]['icon']
	open_image(forecast_icon_48, 3)

	#24hrs
	forecast_label_72['text'] = format_response(json, 4)
	forecast_icon_72 = json['list'][24]['weather'][0]['icon']
	open_image(forecast_icon_72, 4)

def open_image(icon, module):
	if module == 1:
		size = int(lower_frame.winfo_height()*0.8)
		img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
		weather_icon.delete("all")
		weather_icon.create_image(0,0, anchor='nw', image=img)
		weather_icon.image = img
	elif module == 2:
		size = int(forecast_frame.winfo_height()*0.25)
		img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
		forecast_icon_24.delete("all")
		forecast_icon_24.create_image(0,0, anchor='nw', image=img)
		forecast_icon_24.image = img
	elif module == 3:
		size = int(forecast_frame.winfo_height()*0.25)
		img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
		forecast_icon_48.delete("all")
		forecast_icon_48.create_image(0,0, anchor='nw', image=img)
		forecast_icon_48.image = img
	elif module == 4:
		size = int(forecast_frame.winfo_height()*0.25)
		img = ImageTk.PhotoImage(Image.open('./img/'+icon+'.png').resize((size, size)))
		forecast_icon_72.delete("all")
		forecast_icon_72.create_image(0,0, anchor='nw', image=img)
		forecast_icon_72.image = img


root = tk.Tk()
root.title("Weather App")
root.iconbitmap('sun_icon.ico')

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#42c2f4', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier', 12), textvariable="entryText")
entry.insert(0, "São Paulo")
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Get Weather", font=('Courier', 12), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(root, bg='#42c2f4', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.2, anchor='n')

label = tk.Label(lower_frame, bg='white', font=('Courier', 14), anchor='nw', justify='left', bd=5)
label.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(label, bg='white', bd=0, highlightthickness=0)
weather_icon.place(relx=0.75, rely=0, relwidth=0.25, relheight=0.9)


#forecast
forecast_frame = tk.Frame(root, bg='#42c2f4', bd=10)
forecast_frame.place(relx=0.5, rely=0.48, relwidth=0.75, relheight=0.4, anchor='n')

#24hrs forecast
forecast_label_24 = tk.Label(forecast_frame, bg='white', font=('Courier', 10), anchor='nw', justify='left', bd=5)
forecast_label_24.place(relwidth=0.3, relheight=1)

forecast_icon_24 = tk.Canvas(forecast_label_24, bg='white', bd=0, highlightthickness=0)
forecast_icon_24.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.9)

#48hrs forecast
forecast_label_48 = tk.Label(forecast_frame, bg='white', font=('Courier', 10), anchor='nw', justify='left', bd=5)
forecast_label_48.place(relx=0.35, relwidth=0.3, relheight=1)

forecast_icon_48 = tk.Canvas(forecast_label_48, bg='white', bd=0, highlightthickness=0)
forecast_icon_48.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.9)

#72hrs forecast
forecast_label_72 = tk.Label(forecast_frame, bg='white', font=('Courier', 10), anchor='nw', justify='left', bd=5)
forecast_label_72.place(relx=0.7, relwidth=0.3, relheight=1)

forecast_icon_72 = tk.Canvas(forecast_label_72, bg='white', bd=0, highlightthickness=0)
forecast_icon_72.place(relx=0.3, rely=0.4, relwidth=0.4, relheight=0.9)


root.mainloop()