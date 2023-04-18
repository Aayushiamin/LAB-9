import dataclasses
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox 
from utils import bind_close, get_tk_attr, get_dir, get_detail
import requests
from tkinter import messagebox

window=tk.Tk()

#window.geometry("600*600")

bind_close(window)
window.title("Pokemon Information")

def get_pokemon_info():
    pokemon_name = pok_inputuser.get()
    URL = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"

    data = requests.get(URL)
    if data.status_code == 404:
        messagebox.showerror("Error", f"Unable to fetch Information for {pokemon_name} from the pokeAPI.")

    return

data = dataclasses.json()
stats_data = data['stats']

print("length",len(data['stats']))
print(data['name'])


input_frame = tk.Frame(window)
input_frame.grid(row=0,column=0,padx=50,pady=20)

# input_frame.place(relx=0.5,rely=0.1,anchor="center")
pok_lable = tk.Label(input_frame,text="Pokemon Name:")
pok_lable.grid(row=0)

# pok_lable.pack()
pok_inputuser = tk.Entry(input_frame,textvariable="")

print(pok_inputuser.get())

# print(get_tk_attr(pok_inputuser))
# print(get_dir(pok_inputuser))
pok_inputuser.grid(row=0,column=1)

pok_btn = tk.Button(input_frame,text="Get Info",command=get_pokemon_info)
pok_btn.grid(row=0,column=2)

# pok_inputuser.pack()

main_frame = tk.Frame(window)
main_frame.grid(row=1,column=0)

info_frame = tk.LabelFrame(main_frame,text="Info")

info_frame.grid_columnconfigure(0,weight=1)
info_frame.grid(row=0,column=0, padx=0, pady=50, sticky='we')

heigh_label = tk.Label(info_frame,text="Height:")
heigh_label.grid(row=0,column=0,padx=10, pady=10)

heigh_val = tk.Label(info_frame,text="")
heigh_val.grid(row=0,column=1,padx=10, pady=10)

weight_label = tk.Label(info_frame,text="Weight:")
weight_label.grid(row=1,column=0,padx=10, pady=10)

weight_val = tk.Label(info_frame,text="")
weight_val.grid(row=1,column=1,padx=10, pady=10)

type_label = tk.Label(info_frame,text="Type:")
type_label.grid(row=2,column=0,padx=10, pady=10)

type_val = tk.Label(info_frame,text="")
type_val.grid(row=2,column=1,padx=10, pady=10)

# info_frame.pack()

heigh_val.config(text=f"{data['height']} dm")
weight_val.config(text=f"{data['weight']} hg")
type_val.congig(text =", ".join([t['type']['name'].title() for t in data['types']]))


# print("stats_datastats_data",stats_data)

stats_frame = tk.LabelFrame(main_frame,text="Stats")
info_frame.grid_columnconfigure(1,weight=1)
stats_frame.grid(row=0,column=1, padx=10, pady=50,sticky='we')

hp_label = tk.Label(stats_frame, text="HP:")
hp_label.grid(row=0, column=0)

hp_bar = ttk.Progressbar(stats_frame, orient="horizontal", length=100, mode="determinate")
hp_bar.grid(row=0, column=1, padx=10, pady=10)

attack_label = tk.Label(stats_frame, text="Attack:")
attack_label.grid(row=1, column=0)

attack_bar = ttk.Progressbar(stats_frame, orient="horizontal", length=100, mode="determinate")
attack_bar.grid(row=1, column=1, padx=10, pady=10)

defense_label = tk.Label(stats_frame, text="Defense:")
defense_label.grid(row=2, column=0)

defense_bar = ttk.Progressbar(stats_frame, orient="horizontal", length=100, mode="determinate")
defense_bar.grid(row=2, column=1, padx=10, pady=10)

special_attack_label = tk.Label(stats_frame,text="Special Attack:")
special_attack_label.grid(row=3,column=0)

special_attack_bar = ttk.Progressbar(stats_frame,orient="horizontal",length=100,value=0,mode="determinate")
special_attack_bar.grid(row=3,column=1,padx=10, pady=10)


speed_label = tk.Label(stats_frame,text="Speed:")
speed_label.grid(row=4,column=0)

speed_bar = ttk.Progressbar(stats_frame,orient="horizontal",length=100,value=0,mode="determinate")
speed_bar.grid(row=4,column=1,padx=10, pady=10)


special_defense_label = tk.Label(stats_frame,text="Special Defense:")
special_defense_label.grid(row=5,column=0)

special_defense_bar = ttk.Progressbar(stats_frame,orient="horizontal",length=100,value=0,mode="determinate")
special_defense_bar.grid(row=5,column=1,padx=10, pady=10)


stats_data = data ['stats']
for stat in stats_data:

    if stat['stat']['name'] == 'hp':
        hp_bar.config(value=stat['base_stat'])

    elif stat['stat']['name'] == 'attack':
        attack_bar.config(value=stat['base_stat'])

    elif stat['stat']['name'] == 'defense':
        defense_bar.config(value=stat['base_stat'])

    elif stat['stat']['name'] == 'special-attack':
        special_attack_bar.config(value=stat['base_stat'])

    elif stat['stat']['name'] == 'special-defense':
        special_defense_bar.config(value=stat['base_stat'])
        
    elif stat['stat']['name'] == 'speed':
        speed_bar.config(value=stat['base_stat'])


window.mainloop()

