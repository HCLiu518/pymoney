#!/opt/anaconda3/bin/python
from pyrecord import Records
from pycategory import Categories
from tkinter import *
from tkinter import messagebox

"""
initiate & open file
"""
categories = Categories()
root = Tk()
try:
    with open('records.txt') as fh:
        contents = fh.readlines()

        ### check if the file has content
        if not contents:
            raise OSError

        records = Records(contents)
        start_record = NORMAL
        set_money = DISABLED
except OSError:
    records = Records()
    start_record = DISABLED
    set_money = NORMAL

"""
function
"""

def set_initial_money():
    try:
        money = initial_money_str.get()
        records.money = money
        current_money_str.set(f'Now you have {records.money } dollars.')
    except ValueError as err:
        messagebox.showwarning("Error message",str(err))
    else:
        initial_money_btn['state'] = DISABLED
        initial_money_entry['state'] = DISABLED
        find_category_btn['state'] = NORMAL
        res_category_btn['state'] = NORMAL
        add_record_btn['state'] = NORMAL
        delete_record_btn['state'] = NORMAL
        find_category_entry['state'] = NORMAL
        record_date_entry['state'] = NORMAL
        record_category_entry['state'] = NORMAL
        record_description_entry['state'] = NORMAL
        record_amount_entry['state'] = NORMAL

def add_record():
    date = record_date_str.get()
    category = record_category_str.get()
    description = record_description_str.get()
    amount = record_amount_str.get()
    try:
        records.add([date,category,description,amount],categories)
    except ValueError as err:
        messagebox.showwarning("Error message",str(err))
    else:
        current_money_str.set(f'Now you have {records.money} dollars.')
        record_date_str.set("")
        record_category_str.set("")
        record_description_str.set("")
        record_amount_str.set("")
        view_records()

def view_records():
    records_list = records.view()
    result_box.delete(0,END)
    find_category_str.set("")
    for i, record in enumerate(records_list):
        result_box.insert(i, record)

def save_records():
    records.save()

def delete_record():
    selected_record = result_box.get(ACTIVE)
    print(selected_record)

"""
layout
"""
f = Frame(root, borderwidth=5)
f.grid(row=0, column=0)

find_category_label = Label(f, text='Find category:')
find_category_label.grid(row=0,column=0,columnspan=2)

find_category_str = StringVar()
find_category_entry = Entry(f, textvariable=find_category_str, state=start_record)
find_category_entry.grid(row=0, column=2, columnspan=3)

find_category_btn = Button(f, text='Find', state=start_record, command=lambda: print('Hi'))
find_category_btn.grid(row=0, column=5,sticky="W")

res_category_btn = Button(f, text='Reset', state=start_record, command=view_records)
res_category_btn.grid(row=0, column=6,sticky="W")

result_box_label = Label(f, text=f'{"Date": <10s} {"Category": <15s} {"Description": <15s} Amount', font = ('Courier',12))
result_box_label.grid(row=1, column=0, columnspan=7, sticky='W')

result_box = Listbox(f, width=52, height=15, font = ('Courier',12))
result_box.grid(row=2, column=0, columnspan=7, rowspan=8)

initial_money_label = Label(f, text='Initial money:')
initial_money_label.grid(row=2,column=8,columnspan=2,sticky='E')

initial_money_str = StringVar()
initial_money_entry = Entry(f, textvariable=initial_money_str, state = set_money)
initial_money_entry.grid(row=2,column=10,columnspan=2)

initial_money_btn = Button(f, text='Set', state=set_money, command=set_initial_money)
initial_money_btn.grid(row=3, column=11, sticky="E")

blank_lable = Label(f)
blank_lable.grid(row=4, column=8)

record_date_label = Label(f, text='Date:')
record_date_label.grid(row=5,column=8,columnspan=2,sticky='E')

record_date_str = StringVar()
record_date_entry = Entry(f, textvariable=record_date_str, state=start_record)
record_date_entry.grid(row=5,column=10,columnspan=2)

record_category_label = Label(f, text='Category:')
record_category_label.grid(row=6,column=8,columnspan=2,sticky='E')

record_category_str = StringVar()
record_category_entry = Entry(f, textvariable=record_category_str, state=start_record)
record_category_entry.grid(row=6,column=10,columnspan=2)

record_description_label = Label(f, text='Description:')
record_description_label.grid(row=7,column=8,columnspan=2,sticky='E')

record_description_str = StringVar()
record_description_entry = Entry(f, textvariable=record_description_str, state=start_record)
record_description_entry.grid(row=7,column=10,columnspan=2)

record_amount_label = Label(f, text='Amount:')
record_amount_label.grid(row=8,column=8,columnspan=2,sticky='E')

record_amount_str = StringVar()
record_amount_entry = Entry(f, textvariable=record_amount_str, state=start_record)
record_amount_entry.grid(row=8,column=10,columnspan=2)

add_record_btn = Button(f, text='Add a record', state=start_record, command=add_record)
add_record_btn.grid(row=9, column=11, sticky="E")

current_money_str = StringVar()
current_money_str.set(f'Now you have {records.money } dollars.')
current_money_label = Label(f, textvariable=current_money_str)
current_money_label.grid(row=10,column=0,columnspan=5,sticky='W')

delete_record_btn = Button(f, text='Delete', state=start_record, command=delete_record)
delete_record_btn.grid(row=10, column=6, sticky="E")

"""
main
"""
view_records()
mainloop()
save_records()




"""
while True:
    
    operate_command = input("\nWhat do you want to do (add / view / delete / view categories / find / exit)? ")

    if operate_command == "add":

        record = input("Add an expense or income record with description and amount:\n")
        records.add(record, categories)
    
    elif operate_command == "view":

        records.view()
    
    elif operate_command == "delete":

        delete_record = input("Which record do you want to delete? ")
        records.delete(delete_record)

    elif operate_command == "view categories":

        categories.view()

    elif operate_command == "find":
        category = input('Which category do you want to find? ')
        target_categories = categories.find_subcategories(category)
        records.find(category, target_categories)

    elif operate_command == "exit":

        if records.save():
            break

    else:
        ### Wrong command
        print("Invalid command. Try again.")

"""