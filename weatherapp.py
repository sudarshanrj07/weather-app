import tkinter as tk
import requests

HEIGHT=400
WIDTH=500

def test_function(entry):
	print("its done",entry)

def get_weather(city):
	weather_key = '4f9624d4e0731dc796665626044ddf69'
	url = 'http://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'celsius'}
	response = requests.get(url, params=params)
	weather =response.json()

	label['text']=format_response(weather)


def format_response(weather):
	try:	
			name = weather['name']
			desc = weather['weather'][0]['description']
			country = weather['sys']['country']


			final_str = 'city: %s\ncondition: %s\ncountry: %s'%(name, desc, country)
	except:
		final_str ='may be the u have entered the wrong details '

	return final_str

root =tk.Tk()

canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_lable = tk.Label(root, image=background_image)
background_lable.place(relwidth=1 , relheight=1)

frame = tk.Frame(root, bg='#9999ff' , bd=5 )
frame.place(relx=0.5,rely=0.1, relwidth=0.75, relheight=0.08 , anchor='n')

entry=tk.Entry(frame , font=('courier',14))
entry.place(relwidth= 0.65 , relheight=1)

button=tk.Button(frame, text="get weather" , font=40 , command=lambda: get_weather(entry.get()) )
button.place(relx=0.7 , relwidth=0.3, relheight =1)

lower_frame = tk.Frame(root, bg = '#9999ff', bd =10)
lower_frame.place(relx=0.5 , rely = 0.25, relwidth =0.75, relheight =0.65, anchor='n')

label=tk.Label(lower_frame,font=('courier',18))
label.place( relwidth=1 , relheight =1)

root.mainloop()
