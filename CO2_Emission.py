from tkinter import *

screen = Tk()
screen.geometry("400x300")
screen.title("Przelicznik emisji CO2")
heading = Label(text="Wpływ człowieka na emisje gazów cieplarnianych", bg="grey", fg="black", width="900", height="3")
heading.pack()

waga_text = Label(text = "Podaj wagę")
wzrost_text = Label(text = "Podaj wzrost")
wiek_text = Label(text = "Podaj wiek")

waga_text.place(x=15, y=70)
wzrost_text.place(x=15, y=100)
wiek_text.place(x=15, y=130)

waga = IntVar()
wzrost = IntVar()
wiek = IntVar()

waga_entry = Entry(textvariable=waga)
wzrost_entry = Entry(textvariable=wzrost)
wiek_entry = Entry(textvariable=wiek)

waga_entry.place(x=250, y=70)
wzrost_entry.place(x=250, y=100)
wiek_entry.place(x=250, y=130)

#Wybór płci

plec_text = Label(text = "Wybierz płeć")
plec_text.place(x=15, y=160)

options = StringVar()
dropdown = OptionMenu(screen, options, "Mężczyzna", "Kobieta").place(x=250, y=160)

if dropdown == "Mężczyzna":
    dropdown = float(-161)
else:
    dropdown = float(5)

#Wybieranie aktywności danego człowieka

activity_text = Label(text = "Wybierz poziom aktywności fizycznej")
activity_text.place(x=15, y=190)

options1 = IntVar()
dropdown1 = OptionMenu(screen, options1, "Mała aktywność fizyczna", "Umiarkowana aktywność fizyczna", "Osoba aktywna fizycznie", "Bardzo duża aktywność fizyczna", "Esktremalna aktywność fizyczna").place(x=250, y=190)

if dropdown1 == "Mała aktywność fizyczna":
    dropdown1 = float(1.2)
if dropdown1 == "Umiarkowana aktywność fizyczna":
    dropdown1 = float(1.375)
if dropdown1 == "Osoba aktywna fizycznie":
    dropdown1 = float(1.55)
if dropdown1 == "Bardzo duża aktywność fizyczna":
    dropdown1 = float(1.725)
if dropdown1 == "Esktremalna aktywność fizyczna":
    dropdown1 = float(1.9)


#Wyliczanie emisji dwutlenku węglą przez danego człowieka

def run():
    emisja = float(((waga*10)+(wzrost*6.25)-(wiek*5)+dropdown)*dropdown1)
    print(emisja)

oblicz = Button(text = "Oblicz emisję", command=run)
oblicz.place(x=87.5, y=240)

'''''
emisja = float(((waga*10)+(wzrost*6.25)-(wiek*5)+plec)*activity)
print(emisja)
'''''
screen.mainloop()