from tkinter import *
from Translator_SQL import *
def button_press():
    a = entry1.get()
    b = entry2.get()
    c = entry3.get()

    result = requests_sql(a,b,c)
    entry4.delete(0, END)
    entry4.insert(0, result)




window = Tk()

window.title("")
window.resizable(width=False, height=False)
window.iconbitmap()
label1 = Label(
    text="Переводчик с естественного языка на SQL",
    fg="white",
    bg="black",
    width=50,
    height=2,
    font=50)
label1.pack()

label2 = Label(text="Введите название таблицы:")
label2.pack()
entry1 = Entry(width=50)
entry1.pack()

label3 = Label(text="Введите агрегаторную функцию:")
label3.pack()
entry2 = Entry(width=50)
entry2.pack()
label4 = Label(text="Введите название столбца:")
label4.pack()
entry3 = Entry(width=50)
entry3.pack()

button = Button(
    text="Получить результат",
    bg="black",
    fg="white",
    command=button_press)
button.pack()

label5 = Label(text="Результат:")
label5.pack()
entry4 = Entry(width=50)
entry4.pack()

window.mainloop()