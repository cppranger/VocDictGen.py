from randomnames import *
from tkinter import *
import random
import functools
import countries
import states


def task(number):
    number = str(number)[::-1]
    result = ''
    for i, num in enumerate(number):
        if i % 3 == 0:
            result += '.'
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
    rnd = random.randint(0, 3)
    if rnd == 0:
        return randName()
    elif rnd == 1:
        return randNumber()
    elif rnd == 2:
        return randTel()
    else:
        return randPlace()


def fileWriter(dictations=30, strs=30):
    for i in range(0, dictations):
        file = open("c:/lists/list[{}].txt".format(i + 1), "w")
        print('File #{} successfully created!'.format(i + 1))
        for y in range(0, strs):
            file.write(randRand() + '\n')


def clicked():
    fileWriter()
    # if not dictat.get() or not lenlist.get() or dictat.get().isdigit() or not lenlist.get().isdigit():
        # messagebox.showerror('Неверный тип!', 'Введите целое число')
    # else:
        # fileWriter(int(dictat.get()), int(lenlist.get()))


window = Tk()
window.title("Vocabulary Dictation Generator")
window.geometry('300x300')

lbl = Label(window, text="This small app generates vocabulary dictations!")
lbl.place(x=20, y=100)
btn = Button(window, text="Generate!", command=clicked)
btn.place(x=200, y=240)

# dictat_lbl = Label(window, text="Quantity of files: ")
# dictat = Entry(window, width=10)
# lenlist_lbl = Label(window, text="Quantity of list entries: ")
# lenlist = Entry(window, width=10)
# dictat.place(x=150, y=150)
# dictat_lbl.place(x=20, y=150)
# lenlist.place(x=150, y=180)
# lenlist_lbl.place(x=20, y=180)
window.mainloop()