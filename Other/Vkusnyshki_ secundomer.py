import tkinter as tk
# главное меню виджет верхнего уровня Tk, который представляет в основном основную ветку приложения
root = tkinter.Tk()
root.configure(background='yellow')
root.geometry('600x800')

# создать виджет метки
label = tkinter.Label(root, text='hello')
label.pack(pady=10)
# кнопка
def button_action():
    print('Кнопочка :)')

button = tkinter.Button(root, text="нажми на меня", foreground='green', command=button_action)
button.pack(pady=10)
# проверка кнопки
def check_button_action():
    print(check_button_var.get())
    # состояния кнопок по умолчанию - 0 и 1
    if check_button_var.get() == 1:
        root.configure(background='white')
    else:
        root.configure(background='black')

check_button_var = tkinter.IntVar()
check_button = tkinter.Checkbutton(root, text='on/off', variable=check_button_var,
                                   command=check_button_action)
check_button.pack(pady=10)
# вход
entry_frame = tk.Frame(root, borderwidth=5, relief=tkinter.SUNKEN)
entry_frame.pack()

text_box = tkinter.Entry(entry_frame)
text_box.pack()

# функция активация кнопки
def get_entry_text():
    print(text_box.get())
    label.configure(text=text_box.get())
button = tkinter.Button(entry_frame, text="get entry", command=get_entry_text)
button.pack(pady=10)
# прокрутка
slider_frame = tkinter.Frame(root, borderwidth=5, relief=tkinter.SUNKEN)
slider_frame.pack(pady=10)


# упаковать виджет в родительский виджет
label.pack()
# вызвать главный цикл Tk, держит окно открытым
root.mainloop()


'''def calculate_total_bill(value):
    print(value)
    if bill_amount_entry.get() !='':
        tip_percent = float(value)
        bill = float(bill_amount_entry.get())
        tip_amount = tip_percent * bill
        text = f'{bill + tip_amount}'
        bill_with_tip.configure(text=text)

        slider = tkinter.Scale(slider_frame, from_0.00,)'''