from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Project_Code import pardazesh

window = tk.Tk()
window.title("Manu Microprogram Simulator")

frame1 = Frame(window, bg="#362FD9", padx=10, pady=10)
frame1.pack(fill="both", expand=True)
frame2 = Frame(window, bg="#362FD9", padx=10, pady=10)
frame2.pack(fill="both", expand=True)
frame1_1 = LabelFrame(frame1, text="Assembly Code", bg="#362FD9", padx=20)
frame1_1.pack(fill="both", expand=True, side=LEFT)
frame1_2 = LabelFrame(frame1, text="MicroProgram",
                      bg="#362FD9", padx=20)  # 2.272FF
frame1_2.pack(fill="both", expand=True, side=LEFT)
frame1_3 = Frame(frame1, bg="#362FD9", padx=20)
frame1_3.pack(fill="both", expand=True, side=LEFT)
frame1_3_1 = LabelFrame(
    frame1_3, text="MicroProgram Memory", bg="#362FD9")
frame1_3_1.pack(fill="both", expand=True, side=TOP)
frame1_3_2 = LabelFrame(frame1_3, text="Main Memory",
                        bg="#362FD9")
frame1_3_2.pack(fill="both", expand=True, side=BOTTOM)
text_mcrprgrm = Text(frame1_2, width=45, height=5,
                     fg="white", bg="#1B2430", insertbackground='white')
text_mcrprgrm.pack(fill="both", expand=True)
text_assembly = Text(frame1_1, width=35, fg="white",
                     bg="#1B2430", insertbackground='white')
text_assembly.pack(fill="both", expand=True)


framebtn = Frame(frame2, pady=40, padx=150, bg="#1B2430")
framebtn.pack(fill="both", expand=True, side=LEFT)

framerg = Frame(frame2, pady=40, padx=150, bg="#1B2430")  # 0c73f9
framerg.pack(fill="both", expand=True, side=RIGHT)

AClbl = Label(framerg, text="AC", bg="#1B2430", fg="#85CDFD")
AClbl.grid(row=0, column=0)
acEntry = Entry(framerg, bg="#1B2430", fg="white")
acEntry.grid(row=0, column=1)

PClbl = Label(framerg, text="PC", bg="#1B2430", fg="#85CDFD")
PClbl.grid(row=1, column=0)
pcEntry = Entry(framerg, bg="#1B2430", fg="white")
pcEntry.grid(row=1, column=1)

DRlbl = Label(framerg, text="DR", bg="#1B2430", fg="#85CDFD")
DRlbl.grid(row=2, column=0)
drEntry = Entry(framerg, bg="#1B2430", fg="white")
drEntry.grid(row=2, column=1)

ARlbl = Label(framerg, text="AR", bg="#1B2430", fg="#85CDFD")
ARlbl.grid(row=3, column=0)
arEntry = Entry(framerg, bg="#1B2430", fg="white")
arEntry.grid(row=3, column=1)

CARlbl = Label(framerg, text="CAR", bg="#1B2430", fg="#85CDFD")
CARlbl.grid(row=4, column=0)
carEntry = Entry(framerg, bg="#1B2430", fg="white")
carEntry.grid(row=4, column=1)

SBRlbl = Label(framerg, text="SBR", bg="#1B2430", fg="#85CDFD")
SBRlbl.grid(row=5, column=0)
sbrEntry = Entry(framerg, bg="#1B2430", fg="white")
sbrEntry.grid(row=5, column=1)

Slbl = Label(framerg, text="S", bg="#1B2430", fg="#85CDFD")
Slbl.grid(row=6, column=0)
sEntry = Entry(framerg, bg="#1B2430", fg="white")
sEntry.grid(row=6, column=1)

mcprgrmlbl = Label(framerg, text="MICROPROGRAM", bg="#1B2430", fg="#85CDFD")
mcprgrmlbl.grid(row=1, column=5)
mcprgrmEntry = Entry(framerg, width=50, bg="#1B2430", fg="white")
mcprgrmEntry.grid(row=1, column=6)

obj = pardazesh()

style = ttk.Style(frame1_3)
style.theme_use("clam")  # set theam to clam
style.configure("Treeview", background="#1B2430",
                fieldbackground="#1B2430", foreground="white")
style.configure('Treeview.Heading', background="PowderBlue")
table1 = ttk.Treeview(frame1_3_1, columns=(
    'addrs', 'lbl', 'inst', 'content'), show='headings')
table1.heading('addrs', text="Address")
table1.column('addrs',  anchor=CENTER, stretch=NO, width=170)
table1.heading('lbl', text="Label")
table1.column('lbl',  anchor=CENTER, stretch=NO, width=170)
table1.heading('inst', text="Instruction")
table1.column('inst',  anchor=CENTER, stretch=NO, width=170)
table1.heading('content', text="Content")
table1.column('content',  anchor=CENTER, stretch=NO, width=170)
table1.grid(row=0, column=0, sticky='nsew')

table1.tag_configure('oddrow', background="#7975E6")
table1.tag_configure('evenrow', background="#0630AD")

# add a scrollbar
scrollbar1 = ttk.Scrollbar(
    frame1_3_1, orient=tk.VERTICAL, command=table1.yview)
table1.configure(yscroll=scrollbar1.set)
scrollbar1.grid(row=0, column=1, sticky='ns')

table2 = ttk.Treeview(frame1_3_2, columns=(
    'addrs', 'lbl', 'inst', 'content'), show='headings')
table2.heading('addrs', text="Address")
table2.column('addrs',  anchor=CENTER, stretch=NO, width=170)
table2.heading('lbl', text="Label")
table2.column('lbl',  anchor=CENTER, stretch=NO, width=170)
table2.heading('inst', text="Instruction")
table2.column('inst',  anchor=CENTER, stretch=NO, width=170)
table2.heading('content', text="Content")
table2.column('content',  anchor=CENTER, stretch=NO, width=170)
table2.grid(row=0, column=0, sticky='nsew')

table2.tag_configure('oddrow', background="#7975E6")
table2.tag_configure('evenrow', background="#0630AD")
table2.tag_configure('stprow', background="#DB005B")

# add a scrollbar
scrollbar2 = ttk.Scrollbar(
    frame1_3_2, orient=tk.VERTICAL, command=table2.yview)
table2.configure(yscroll=scrollbar2.set)
scrollbar2.grid(row=0, column=1, sticky='ns')


def Entry_Changes(input, res):
    input.delete(0, END)
    input.insert(0, res)


def update():
    Entry_Changes(acEntry, obj.AC)
    Entry_Changes(pcEntry, obj.PC)
    Entry_Changes(drEntry, obj.DR)
    Entry_Changes(arEntry, obj.AR)
    Entry_Changes(carEntry, obj.CAR)
    Entry_Changes(sbrEntry, obj.SBR)
    Entry_Changes(sEntry, obj.S)
    Entry_Changes(mcprgrmEntry, obj.program_instruction[obj.CAR])
    # Clear the treeview list items
    for item in table1.get_children():
        table1.delete(item)
    for i in range(2047, -1, -1):
        addrs = i
        data = (addrs, obj.memory_lable[addrs],
                obj.memory_instruction[addrs], obj.memory_value[addrs])
        if i % 2 == 0:
            table1.insert(parent='', index=0, values=data, tags=('evenrow'))
        else:
            table1.insert(parent='', index=0, values=data, tags=('oddrow'))
    # Clear the treeview list items
    for item in table2.get_children():
        table2.delete(item)
    for i in range(127, -1, -1):
        addrs = i
        data = (addrs, obj.program_lable[addrs],
                obj.program_instruction[addrs], obj.program_value[addrs])
        if i == obj.CAR:
            if (obj.CAR == 30):
                pass
            else:
                table2.insert(parent='', index=0,
                              values=data, tags=('stprow'))

        elif i % 2 == 0:
            table2.insert(parent='', index=0, values=data, tags=('evenrow'))
        else:
            table2.insert(parent='', index=0, values=data, tags=('oddrow'))


def compile():
    str = text_mcrprgrm.get('1.0', 'end')
    if (str == "\n"):
        flag1 = 0
    else:
        flag1 = obj.assembler_program(str)
    str = text_assembly.get('1.0', 'end')
    if (str == "\n"):
        flag2 = 0
    else:
        flag2 = obj.assembler_asembly(str)
    if (flag1 and flag2):
        obj.upload_code()
        obj.flagupload = 1
        messagebox.showinfo("info", "Compilation was successful")
        update()
    else:
        obj.flagupload = 0
        messagebox.showerror("ERROR", "Compilation wasn't successful")
        messagebox.showwarning(
            "WARNING", "Don't put a space between commands f1, f2 and f3")


def reset():
    if (obj.flagupload):
        obj.upload_code()
        messagebox.showinfo("info", "The Computer was Reset")
        update()
    else:
        messagebox.showerror("ERROR", "No Compile")


def stprun():
    if (obj.flagupload):
        obj.step_run()
        update()


def run():
    if (obj.flagupload):
        obj.run()
        update()


btn_cmp = Button(framebtn, text="ASSEMBLE", command=compile,
                 height=2, width=15, bg="#85CDFD", relief="raised", overrelief="flat")
btn_cmp.grid(row=0, column=0, sticky='e', padx=10, pady=5)

btn_rst = Button(framebtn, text="RESET", command=reset,
                 height=2, width=15, bg="#85CDFD", relief="raised", overrelief="flat")
btn_rst.grid(row=1, column=0, sticky='e', padx=10, pady=5)

btn_run = Button(framebtn, text="RUN", command=run,
                 height=2, width=15, bg="#85CDFD", relief="raised", overrelief="flat")
btn_run.grid(row=0, column=1, sticky='w', pady=5)

btn_stp = Button(framebtn, text="STEP", command=stprun,
                 height=2, width=15, bg="#85CDFD", relief="raised", overrelief="flat")
btn_stp.grid(row=1, column=1, sticky="w", pady=5)


menubar = Menu(window)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=filemenu)
window.config(menu=menubar)
filemenu.add_command(label="exit", command=window.quit)

window.geometry("800x750")
window.mainloop()
