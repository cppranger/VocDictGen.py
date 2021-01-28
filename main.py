from randomnames import *
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import filedialog
import datetime
import random
import functools
import os
import countries
import states
import month


def task(number):
    number = str(number)[::-1]
    result = ''
    for i, num in enumerate(number):
        if i % 3 == 0:
            result += ','
        result += num
    result = result[::-1][:-1]
    return result


def randName():
    # print('randName: ', end='')
    rnd = random.randint(0, 3)
    if rnd == 0:
        return Full()
    elif rnd == 1:
        return 'Mr.' + Last()
    elif rnd == 2:
        return 'Mrs.' + Last()
    else:
        return 'Ms.' + Last()


def randTel():
    # print('randTel: ', end='')
    rnd = random.randint(0, 3)
    a = functools.partial(random.randint, 0, 9)
    if rnd == 0:
        gen = "+7-{}{}{}-{}{}{}-{}{}{}{}".format(a(), a(), a(), a(), a(), a(), a(), a(), a(), a())
    elif rnd == 1:
        gen = "{}{}{}-{}{}{}-{}{}{}".format(a(), a(), a(), a(), a(), a(), a(), a(), a())
    elif rnd == 2:
        gen = "{}{}-{}{}-{}{}".format(a(), a(), a(), a(), a(), a())
    else:
        gen = "8(8332) {}{}-{}{}-{}{}".format(a(), a(), a(), a(), a(), a())
    return gen


def randNumber():
    # print('randNumber: ', end='')
    rnd = random.randint(0, 9)
    gen = random.randint(11, 3999999)
    randn = str(task(gen))
    if rnd == 0:
        return str(randn) + ' millimeters'
    elif rnd == 1:
        return str(randn) + ' centimeters'
    elif rnd == 2:
        return str(randn) + ' meters'
    elif rnd == 3:
        return str(randn) + ' kilometers'
    elif rnd == 4:
        return str(randn) + ' feet'
    elif rnd == 5:
        return str(randn) + ' grams'
    elif rnd == 6:
        return str(randn) + ' rubles'
    elif rnd == 7:
        return str(randn) + ' dollars'
    else:
        return str(randn) + ' kilograms'


def randPlace():
    # print('randPlace: ', end='')
    rnd = random.randint(0, 1)
    if rnd == 0:
        return countries.countries[(random.randint(0, len(countries.countries)-1))]
    else:
        return states.states[(random.randint(0, len(states.states)-1))]


def randRand():
    rnd = random.randint(0, 4)
    if rnd == 0:
        return randName()
    elif rnd == 1:
        return randNumber()
    elif rnd == 2:
        return randTel()
    elif rnd == 3:
        return randDate()
    else:
        return randPlace()


def randDate():
    rnd_month = random.randint(1, 12)
    rnd_data = random.randint(1, month.numbs[rnd_month])
    rnd_year = random.randint(1000, 3000)
    return str(rnd_data) + ' ' + str(month.months[rnd_month]) + ' ' + str(rnd_year)


def fileWriter(dictations=30, strs=30):
    bar['value'] = 0
    now = datetime.datetime.now()
    for i in range(0, dictations):
        now_time = str(now.year) + '-' + str(now.month) + '-' + str(now.day) + '-' + str(now.hour) + '-' + str(now.minute) + '-' + str(now.second) + '-#' + str(i+1)
        filename = folder_path.get() + '/list[{}].txt'.format(now_time)
        file = open(filename, "w", encoding='utf-8')
        txt.insert(END, 'File #{} successfully created!\n'.format(i + 1))
        for y in range(0, strs):
            file.write(randRand() + '\n')
            bar['value'] += 100 // (dictations * strs)
    txt.insert(END, 'Successfully generated {} lists!\n'.format(dictations))
    os.startfile(folder_path.get())


def clicked():

    if not dictat.get() or not lenlist.get() or not dictat.get().isdecimal() or not lenlist.get().isdecimal():
        messagebox.showerror('Неверный тип!', 'Введите целое число')
    else:
        fileWriter(int(dictat.get()), int(lenlist.get()))


def textClear():
    txt.delete('1.0', END)


def fileDir():
    global folder_path
    filename = filedialog.askdirectory()
    folder_path.set(filename)


def settings():
    settingsWindow = Toplevel(window)
    global folder_path
    lblPath = Label(settingsWindow, text="Choose directory: ")
    lblPath.place(x=10, y=10)
    txtPath = Text(settingsWindow, width=15, height=1)
    txtPath.place(x=10, y=30)
    txtPath.insert(END, folder_path.get())
    btnPath = Button(settingsWindow, text="Open", command=fileDir)
    btnPath.place(x=140, y=30)


window = Tk()
window.title("VocDictGen v0.5b")
window.geometry('300x350')
window.resizable(width=False, height=False)

lbl = Label(window, text="This small app generates vocabulary dictations!")
lbl.place(x=20, y=10)
btn = Button(window, text="Generate!", command=clicked)
btn.place(x=220, y=255)
txt = Text(window, width=33, height=10)
scroll = Scrollbar(command=txt.yview)
scroll.pack(side=LEFT, fill=Y)
txt.config(yscrollcommand=scroll.set)
txt.place(x=15, y=40)
logo = Label(window, text="github: @cppranger")
logo.place(x=105, y=330)

bar = Progressbar(window, length=200)
bar.place(x=50, y=300)

dictat_lbl = Label(window, text="Quantity of files: ")
dictat = Entry(window, width=21)
dictat.insert(END, '5')
lenlist_lbl = Label(window, text="Quantity of list entries: ")
lenlist = Entry(window, width=21)
lenlist.insert(END, '5')
dictat.place(x=150, y=210)
dictat_lbl.place(x=20, y=210)
lenlist.place(x=150, y=230)
lenlist_lbl.place(x=20, y=230)

menu = Menu(window)
new_item = Menu(menu)
new_item.add_command(label='Настройки', command=settings)
new_item.add_command(label='Очистить ввод', command=textClear)
menu.add_cascade(label="Файл", menu=new_item)
window.config(menu=menu)

folder_path = StringVar()
folder_path.set('c:/lists')

window.mainloop()
