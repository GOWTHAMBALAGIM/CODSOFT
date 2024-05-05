from tkinter import *
import tkinter.messagebox


def entertask():
    input_text = ""

    def add():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            listbox_task.insert(END, input_text)
            root1.destroy()

    root1 = Tk()
    root1.title("Add task")
    entry_task = Text(root1, width=40, height=4)
    entry_task.pack()
    button_temp = Button(root1, text="Add task", command=add)
    button_temp.pack()
    root1.mainloop()


def updatetask():
    input_text = ""
    if listbox_task.curselection() == ():
        tkinter.messagebox.showwarning(title="Warning!", message="Please select the task")
        return
    else:
        input_text = listbox_task.get(listbox_task.curselection()[0])

    def update():
        global input_text
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            selected = listbox_task.curselection()
            listbox_task.delete(selected[0])
            listbox_task.insert(selected[0], input_text)
            root1.destroy()

    root1 = Tk()
    root1.title("Update task")
    entry_task = Text(root1, width=40, height=4)
    entry_task.insert(tkinter.END, input_text)
    entry_task.pack()
    button_temp = Button(root1, text="Update task", command=update)
    button_temp.pack()
    root1.mainloop()


def deletetask():
    if listbox_task.curselection() == ():
        tkinter.messagebox.showwarning(title="Warning!", message="Please select the task")
        return
    else:
        selected = listbox_task.curselection()
        listbox_task.delete(selected[0])


def markcompleted():
    if listbox_task.curselection() == ():
        tkinter.messagebox.showwarning(title="Warning!", message="Please select the task")
        return
    else:
        marked = listbox_task.curselection()
        temp = marked[0]
        temp_marked = listbox_task.get(marked)
        temp_marked = temp_marked + " ✔"
        listbox_task.delete(temp)
        listbox_task.insert(temp, temp_marked)


window = Tk()
window.title("To-Do List")

frame_task = Frame(window)
frame_task.pack()

listbox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="Helvetica")
listbox_task.pack(side=tkinter.LEFT)

scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

entry_button = Button(window, text="Add task", width=50, command=entertask)
entry_button.pack(pady=3)

update_button = Button(window, text="Update Task ", width=50, command=updatetask)
update_button.pack(pady=3)

delete_button = Button(window, text="Delete selected task", width=50, command=deletetask)
delete_button.pack(pady=3)

mark_button = Button(window, text="Mark as completed ", width=50, command=markcompleted)
mark_button.pack(pady=3)

window.mainloop()