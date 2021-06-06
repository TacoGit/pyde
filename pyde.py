from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
from tkinter.font import Font
import subprocess
import time
import os

compiler = Tk()
compiler.title('pyde')
compiler.geometry("800x379")
file_path = ''


def set_file_path(path):
    global file_path
    file_path = path


def open_file():
    path = askopenfilename(filetypes=[('Python', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python', '*.py'), ('All files', '*.*')])
    else:
        path = file_path
    with open(path + ".py", 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


def run():
    code_output.delete('1.0', END)
    code = editor.get('1.0', END)
    if "input" in code:
        input_notallowed = Toplevel()
        text = Label(input_notallowed, text= '  pyde (tkinter) does not allow input!  ')
        text.pack()
        return

    with open('./autosaveCompiled' , 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path('./autosaveCompiled')

    time.sleep(0.05)
    command = f'python ./autosaveCompiled'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)
    os.remove("./autosaveCompiled")


menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

compiler.config(menu=menu_bar)

font = Font(family='Nunito',
              size=12,
              underline=0,
              overstrike=0)

editor = Text(height=10, font=font)
editor.pack()

button1 = Button(compiler, text="Run code", command=run)
button1.place(x=55, y=250)

button2 = Button(compiler, text="Save as", command=save_as)
button2.place(x=60, y=283)

button3 = Button(compiler, text="Exit", command=exit)
button3.place(x=67, y=316)

code_output = Text(height=10)
code_output.pack()
code_output.place(x=175, y=226)


compiler.mainloop()