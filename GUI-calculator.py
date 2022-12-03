#GUI-calculator.py
#คำนวณปริมาณน้ำหอม จากปริมาณเทียน

from tkinter import *
from tkinter import ttk, messagebox

GUI = Tk()
GUI.title('Candle calcultor')
GUI.geometry('500x700')

bg = PhotoImage(file='candle.png')

BG = Label(GUI, image=bg)
BG.pack()

L = Label(GUI,text='ปริมาณเทียน(กรัม)',font=(None,20))
L.pack()

v_quantity = StringVar() #ตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI, textvariable=v_quantity, font=(None,20))
E1.pack() #เอาสิ่งที่เราได้แปะที่ GUI

def Cal():
    try:
        quan = float(v_quantity.get())
        calc = quan * 0.12
        messagebox.showinfo('All fragrance weight','ปริมาณน้ำหอมที่ต้องใส่ {} ml'.format(calc))
        v_quantity.set('1')
    except:
        messagebox.showwarning('กรอกผิด','กรุณากรอกเฉพาะตัวเลขเท่านั้น')
        v_quantity.set('1')

B = ttk.Button(GUI, text='Calaulate', command=Cal)
B.pack(ipadx=30, ipady=20, pady=20)

GUI.mainloop() #เพื่อให้โปรแกรมรันตลอดเวลา