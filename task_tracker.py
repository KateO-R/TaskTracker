import tkinter as tk


def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

def mark_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task = task_listbox.get(selected_task)
        task_listbox2.insert(tk.END, task)
        task_listbox.delete(selected_task)



root = tk.Tk()
root.title("My tasks")
root.configure(background="DarkSlateGray1")

text1 = tk.Label(root, text="Enter the task:", bg="DeepSkyBlue3")
text1.grid(row=0, column=0, columnspan=3)

task_entry = tk.Entry(root, width=60, bg="DarkTurquoise", fg="ForestGreen")
task_entry.grid(row=1, column=0, columnspan=3, pady=15, padx=10, ipady=15)

add_task_button = tk.Button(root, text="Add task", bg="BlueViolet", command=add_task)
add_task_button.grid(row=2, column=1, columnspan=3, pady=10)

delete_button = tk.Button(root, text="Delete task", bg="brown3", command=delete_task)
delete_button.grid(row=3, column=1, columnspan=3, pady=10)

mark_button = tk.Button(root, text="Mark as done", command=mark_task)
mark_button.grid(row=4, column=1, columnspan=3, pady=10)

text2 = tk.Label(root, text="Tasks to Do:", bg="DeepSkyBlue3")
text2.grid(row=5, column=1, pady=20)

task_listbox = tk.Listbox(root, height=20, width=50, bg="DeepSkyBlue1")
task_listbox.grid(row=6, column=1, columnspan=1)

text3 = tk.Label(root, text="Already done:", bg="medium sea green")
text3.grid(row=5, column=2)

task_listbox2 = tk.Listbox(root, height=20, width=50, bg="light green")
task_listbox2.grid(row=6,column=2)

root.mainloop()
