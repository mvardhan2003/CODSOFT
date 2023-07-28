import tkinter as tk
from tkinter import messagebox

# Function to add a new task to the list
def add_task():
    task_name = entry_task.get()
    if task_name.strip() != "":
        listbox_tasks.insert(tk.END, task_name)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task name.")

# Function to mark a task as completed
def mark_completed():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.itemconfig(index, {'fg': 'gray'})
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed.")

# Function to remove a task from the list
def remove_task():
    try:
        index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create widgets
frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, width=50, height=10, bg="lightyellow")
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=50)
entry_task.pack(pady=10)

button_add_task = tk.Button(root, text="Add Task", command=add_task)
button_add_task.pack(side=tk.LEFT, padx=10)

button_mark_completed = tk.Button(root, text="Mark Completed", command=mark_completed)
button_mark_completed.pack(side=tk.LEFT, padx=10)

button_remove_task = tk.Button(root, text="Remove Task", command=remove_task)
button_remove_task.pack(side=tk.LEFT, padx=10)

root.mainloop()
