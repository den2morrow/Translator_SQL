from msilib.schema import ComboBox
from stat import FILE_ATTRIBUTE_NORMAL
from tkinter import *
from tkinter import font
from tkinter import messagebox
from tkinter.ttk import Combobox
from Translator_SQL import *
def button_press():
    a = entry1.get()
    b = entry2.get()
    c = entry3.get()

    result = requests_sql(a,b,c)
    entry4.delete(0, END)
    entry4.insert(0, result)
def cb1foo():
    global label6,label7,entry6,entry5
    if cb1Enabled.get() != 0:
        label6['state']=ACTIVE
        label7['state']=ACTIVE
        entry6['state']=NORMAL
        entry5['state']=NORMAL
    else:
        label6['state']=DISABLED
        label7['state']=DISABLED
        entry6['state']=DISABLED
        entry5['state']=DISABLED
def cb2foo():
    global label8,label9,entry7,combx1
    if cb2Enabled.get() != 0:
        label9['state']=ACTIVE
        label8['state']=ACTIVE
        entry7['state']=NORMAL
        combx1['state']=NORMAL
    else:
        label9['state']=DISABLED
        label8['state']=DISABLED
        entry7['state']=DISABLED
        combx1['state']=DISABLED
def cb3foo():
    global label10,entry8
    if cb3Enabled.get() != 0:
        label10['state']=ACTIVE
        entry8['state']=NORMAL
    else:
        label10['state']=DISABLED
        entry8['state']=DISABLED
SIZET = 14





window = Tk()
window.title("")
window.resizable(width=False, height=False)
window.geometry("970x440")
window.iconbitmap()
label1 = Label(
    text="Переводчик с естественного языка на SQL",
    fg="white",
    bg="black", 
    width=90, 
    height=2,
    font=('Courier New',14))
label1.pack()

label2 = Label(text="Введите название таблицы:",font=('Courier New',SIZET))
label2.place(x=20, y=50)
entry1 = Entry(width=25,font=('Courier New',SIZET))
entry1.place(x=20, y=80)

label3 = Label(text="Введите агрегаторную функцию:",font=('Courier New',SIZET))
label3.place(x=330,y=50)
entry2 = Entry(width=25,font=('Courier New',SIZET))
entry2.place(x=330,y=80)

label4 = Label(text="Введите имя столбца:",font=('Courier New',SIZET))
label4.place(x=670,y=50)
entry3 = Entry(width=25,font=('Courier New',SIZET))
entry3.place(x=670,y=80)


cb1Enabled = IntVar()
cb1 = Checkbutton(text="Есть ли условие?", font=('Courier New',SIZET), variable=cb1Enabled, command=cb1foo)
cb1.place(x=20,y=150)
label6 = Label(text="Введите имя столбца:",font=('Courier New',SIZET),state=DISABLED)
label6.place(x=330,y=120)
entry5 = Entry(width=25,font=('Courier New',SIZET),state=DISABLED)
entry5.place(x=330,y=150)
label7 = Label(text="Введите условие:",font=('Courier New',SIZET),state=DISABLED)
label7.place(x=670,y=120)
entry6 = Entry(width=25,font=('Courier New',SIZET),state=DISABLED)
entry6.place(x=670,y=150)

cb2Enabled = IntVar()
cb2 = Checkbutton(text="Есть ли сортировка?", font=('Courier New',SIZET), variable=cb2Enabled, command=cb2foo)
cb2.place(x=20,y=220)
label8 = Label(text="Введите имя столбца:",font=('Courier New',SIZET), state=DISABLED)
label8.place(x=330,y=190)
entry7 = Entry(width=25,font=('Courier New',SIZET), state=DISABLED)
entry7.place(x=330,y=220)
label9 = Label(text="Убывание/Возрастание:",font=('Courier New',SIZET), state=DISABLED)
label9.place(x=670,y=190)
combox1Values = ["Убывание", "Возрастание"]
combx1 = Combobox(values = combox1Values, state=DISABLED) #combobox.get()
combx1.place(x=670,y=220)

cb3Enabled = IntVar()
cb3 = Checkbutton(text="Есть ли лимит вывода?", font=('Courier New',SIZET), variable=cb3Enabled, command=cb3foo)
cb3.place(x=20,y=290)
label10 = Label(text="Введите лимит:",font=('Courier New',SIZET), state=DISABLED)
label10.place(x=330,y=260)
entry8 = Entry(width=25,font=('Courier New',SIZET), state=DISABLED)
entry8.place(x=330,y=290)




button1 = Button(
    text="Получить результат",
    bg="black",
    fg="white",
    command=button_press,
    font=('Courier New',SIZET))
button1.place(x=20,y=360)

label5 = Label(text="Результат:",font=('Courier New',SIZET))
label5.place(x=330,y=340)
entry4 = Entry(width=55,font=('Courier New',SIZET))
entry4.place(x=330,y=370)

window.mainloop()
