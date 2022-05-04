import tkinter as tk
import requests
from tkinter import ttk
import bs4
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import json
import datetime


def get_covid_data():
    url = "https://www.worldometers.info/coronavirus/#countries"
    html_data = requests.get(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
    all_data = {}

    for block in info_div:
        text = block.find("h1", class_=None).get_text()

        count = block.find("span", class_=None).get_text()

        all_data[text] = count

    return all_data


def AStateData():
    ws = tk.Tk()
    ws.title('State Data')
    ws.geometry('550x250')
    ws['bg'] = '#AC99F2'

    game_frame = tk.Frame(ws)
    game_frame.pack()

    my_game = ttk.Treeview(game_frame)

    my_game['columns'] = ('player_id', 'player_name', 'player_Rank')

    my_game.column("#0", width=0, stretch=tk.NO)
    my_game.column("player_id", anchor=tk.CENTER, width=130)
    my_game.column("player_name", anchor=tk.CENTER, width=130)
    my_game.column("player_Rank", anchor=tk.CENTER, width=130)
    #my_game.column("player_states", anchor=tk.CENTER, width=80)
    #my_game.column("player_city", anchor=tk.CENTER, width=80)

    my_game.heading("#0", text="", anchor=tk.CENTER)
    my_game.heading("player_id", text="S.no", anchor=tk.CENTER)
    my_game.heading("player_name", text="State", anchor=tk.CENTER)
    my_game.heading("player_Rank", text="Active Case", anchor=tk.CENTER)

    url = "https://covid-india-cases.herokuapp.com/activetimeline/"
    res = requests.get(url)
    a = json.loads(res.text)

    for i in range(len(a)):
        # l2 = tk.Label(my_window,  text=f'{a[i]["State UT"]} - {a[i][str(datetime.date.today())]}')  #
        # l2.grid(row=i,column= 3,sticky='ew')

        my_game.insert(parent='', index='end', iid=i, text='',
                       values=(f'{i}', f'{a[i]["State UT"]}', f'{a[i]["2022-04-05"]}'))


    my_game.pack()

    ws.mainloop()

def RStateData():
    ws = tk.Tk()
    ws.title('State Data')
    ws.geometry('550x250')
    ws['bg'] = '#7DF9FF'

    game_frame = tk.Frame(ws)
    game_frame.pack()

    my_game = ttk.Treeview(game_frame)

    my_game['columns'] = ('player_id', 'player_name', 'player_Rank')

    my_game.column("#0", width=0, stretch=tk.NO)
    my_game.column("player_id", anchor=tk.CENTER, width=130)
    my_game.column("player_name", anchor=tk.CENTER, width=130)
    my_game.column("player_Rank", anchor=tk.CENTER, width=130)

    my_game.heading("#0", text="", anchor=tk.CENTER)
    my_game.heading("player_id", text="S.no", anchor=tk.CENTER)
    my_game.heading("player_name", text="State", anchor=tk.CENTER)
    my_game.heading("player_Rank", text="Recoverd Case", anchor=tk.CENTER)

    url = "https://covid-india-cases.herokuapp.com/curedtimeline/"
    res = requests.get(url)
    a = json.loads(res.text)

    for i in range(len(a)):
        # l2 = tk.Label(my_window,  text=f'{a[i]["State UT"]} - {a[i][str(datetime.date.today())]}')  #
        # l2.grid(row=i,column= 3,sticky='ew')

        my_game.insert(parent='', index='end', iid=i, text='',
                       values=(f'{i}', f'{a[i]["State UT"]}', f'{a[i]["2022-04-05"]}'))


    my_game.pack()

    ws.mainloop()

def DStateData():
    ws = tk.Tk()
    ws.title('State Data')
    ws.geometry('550x250')
    ws['bg'] = '#D2042D'

    game_frame = tk.Frame(ws)
    game_frame.pack()

    my_game = ttk.Treeview(game_frame)

    my_game['columns'] = ('player_id', 'player_name', 'player_Rank')

    my_game.column("#0", width=0, stretch=tk.NO)
    my_game.column("player_id", anchor=tk.CENTER, width=130)
    my_game.column("player_name", anchor=tk.CENTER, width=130)
    my_game.column("player_Rank", anchor=tk.CENTER, width=130)

    my_game.heading("#0", text="", anchor=tk.CENTER)
    my_game.heading("player_id", text="S.no", anchor=tk.CENTER)
    my_game.heading("player_name", text="State", anchor=tk.CENTER)
    my_game.heading("player_Rank", text="Death Case", anchor=tk.CENTER)

    url = "https://covid-india-cases.herokuapp.com/deathtimeline/"
    res = requests.get(url)
    a = json.loads(res.text)

    for i in range(len(a)):
        # l2 = tk.Label(my_window,  text=f'{a[i]["State UT"]} - {a[i][str(datetime.date.today())]}')  #
        # l2.grid(row=i,column= 3,sticky='ew')

        my_game.insert(parent='', index='end', iid=i, text='',
                       values=(f'{i}', f'{a[i]["State UT"]}', f'{a[i]["2022-04-05"]}'))


    my_game.pack()

    ws.mainloop()

def StateData():
    root = tk.Tk()
    root.geometry("500x300")
    root.title("Covid-19 Traker ")
    g = ("Andalus", 20, "bold")
    f = ("poppins", 15, "bold")
    root.config(bg="#FFFDD0")

    mainlabel = tk.Label(root, text="\nState Wise Data of  India\n", font=g, bg="#FFFDD0")
    mainlabel.pack()

    gbtn = tk.Button(root, text="Active Cases", font=f, relief='solid', command=AStateData)
    gbtn.pack()

    rbtn = tk.Button(root, text="Recovered Cases", font=f, relief='solid', command=RStateData)
    rbtn.pack()

    bbtn = tk.Button(root, text="Death Cases", font=f, relief='solid', command=DStateData)
    bbtn.pack()

    root.mainloop()


# Graphical Data which needs to be displayed
def GraphicalActiveData():
    mng = plt.get_current_fig_manager()
    #mng.full_screen_toggle()
    url = "https://covid-india-cases.herokuapp.com/activetimeline/"
    res = requests.get(url)
    a = json.loads(res.text)
    people = ()
    Quantity = []
    for i in range(len(a)):
        people = people + (a[i]["State UT"],)
        Quantity.append(a[i]['2022-04-06'])
    print(people)

    plt.barh(people, Quantity, color='#0000CD', edgecolor='#1E90FF')
    plt.title('Active Cases')
    plt.ylabel('States')
    plt.xlabel('Active Cases')
    plt.show()


def GraphicalRecoveredData():
    mng = plt.get_current_fig_manager()
    #mng.full_screen_toggle()
    url = "https://covid-india-cases.herokuapp.com/curedtimeline/"
    res = requests.get(url)
    a = json.loads(res.text)
    people = ()
    Quantity = []
    for i in range(len(a)):
        people = people + (a[i]["State UT"],)
        Quantity.append(a[i]['2022-04-06'])
    print(people)

    plt.barh(people, Quantity, color='#00FF7F', edgecolor='#006400')
    plt.title('Recovered Cases')
    plt.ylabel('States')
    plt.xlabel('Recovered Cases')
    plt.show()


def GraphicalDeathData():
    mng = plt.get_current_fig_manager()
    # mng.full_screen_toggle()
    url = "https://covid-india-cases.herokuapp.com/deathtimeline/"
    res = requests.get(url)
    a = json.loads(res.text)
    people = ()
    Quantity = []
    for i in range(len(a)):
        people = people + (a[i]["State UT"],)
        Quantity.append(a[i]['2022-04-06'])
    print(people)

    plt.barh(people, Quantity, color='red', edgecolor='#8B0000')
    plt.title('Death Cases')
    plt.ylabel('States')
    plt.xlabel('Death Cases')
    plt.show()


# Graphical Data which needs to be displayed
def GraphicalData():
    root = tk.Tk()
    root.geometry("500x300")
    root.title("Covid-19 Traker ")
    g = ("Andalus", 20, "bold")
    f = ("poppins", 15, "bold")
    root.config(bg="#dde8ff")


    mainlabel = tk.Label(root, text="\nGraphical Data\n", font=g, bg="#dde8ff")
    mainlabel.pack()

    gbtn = tk.Button(root, text="Active Cases", font=f, relief='solid', command=GraphicalActiveData)
    gbtn.pack()

    rbtn = tk.Button(root, text="Recovered Cases", font=f, relief='solid', command=GraphicalRecoveredData)
    rbtn.pack()

    bbtn = tk.Button(root, text="Death Cases", font=f, relief='solid', command=GraphicalDeathData)
    bbtn.pack()

    root.mainloop()

def HelpLine():
    #root = tk.Tk()
    #lbl = tk.Label(root, text=r"http://www.twitter.com/MoHFW_INDIA", fg="blue", cursor="hand2")
    #lbl.pack()
    #lbl.bind("<Button-1>", callback)
    #root.mainloop()
    my_window = tk.Tk()
    my_window.geometry("300x300")
    my_window.title("    HelpLine")

    l1 = tk.Label(my_window, text='HelpLine Number', font=("Arial", 25, "bold"))  # added one Label
    l1.grid(row=0, column=3, sticky='ew', ipady=20)


    l4 = tk.Label(my_window, text=f'8291722764')  #
    l4.grid(row=5, column=3, sticky='ew')

    l3 = tk.Label(my_window, text=r"http://www.twitter.com/MoHFW_INDIA", fg="blue", cursor="hand2")  #
    l3.grid(row=6, column=3, sticky='ew')

    my_window.mainloop()


if __name__ == "__main__":
    my_window = tk.Tk()
    my_window.geometry("650x350")
    my_window.title("Covid19 Tracker")  # Adding a title

    bg = tk.PhotoImage(file="download.png")
    label1 = tk.Label(my_window, image=bg)
    label1.place(x=0, y=0)

    l1 = tk.Label(my_window, text='Covid 19 Tracker', font=("Arial", 25, "bold"))  # added one Label
    l1.grid(row=0, column=2, sticky='ew', ipady=20)

    a = get_covid_data()
    keys = a.keys()
    b = []
    for i in keys:
        b.append(i)

    l2 = tk.Label(my_window, text=f'{b[0]} : {a[b[0]]}')  #
    l2.grid(row=5, column=3, sticky='ew')

    tk.Button(text="State Data", command=StateData,
              bg="green",
              activeforeground="Orange",
              activebackground="blue",
              font="Andalus",
              highlightcolor="purple",
              justify="right",
              relief="groove"
              ).grid(row=5, column=1, sticky='ew')
    tk.Button(text="Graphical Data", command=GraphicalData, bg="green",
              activeforeground="Orange",
              activebackground="blue",
              font="Andalus",
              highlightcolor="purple",
              justify="right",
              relief="groove").grid(row=6, column=1, sticky='ew')
    tk.Button(text="HelpLine", command=HelpLine, bg="green",
              activeforeground="Orange",
              activebackground="blue",
              font="Andalus",
              highlightcolor="purple",
              justify="right",
              relief="groove").grid(row=7, column=1, sticky='ew')

    l3 = tk.Label(my_window, text=f'{b[1]} : {a[b[1]]}')  #
    l3.grid(row=6, column=3, sticky='ew')

    l4 = tk.Label(my_window, text=f'{b[2]} : {a[b[2]]}')  #
    l4.grid(row=7, column=3, sticky='ew')

    my_window.mainloop()
