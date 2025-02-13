import queue
import serial
import struct
import tkinter as tk
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from matplotlib.figure import Figure
from collections import deque
from threading import Thread

DATA_SIZE = 8

# def test1(ser: serial.Serial):
#     line = ser.readline()
#     try:
#         decoded = line.decode().strip()
#         num = int(decoded)
#         print("Получена число:", num, "Её квадрат:", num ** 2)
#     except:
#         print("Получены байты:", line)
#
# def test2(ser: serial.Serial):
#     data = ser.read(DATA_SIZE)
#     print("Получены байты:", data)
#     num, num2, num3 = struct.unpack("ifi", data)
#     print(num, num2, num3)
#
#
# with serial.Serial(PORT, BAUDRATE) as ser:
#     print("Порт открыт")
#     while True:
#         # test1(ser)
#         test2(ser)


def lerp(a, b, t):
    return a + (b - a) * t

def alerp(a, b, v):
    return (v - a) / (b - a)


def map_num(value: int, min_i: int, max_i: int, min_o: float, max_o: float) -> float:
    ratio = alerp(min_i, max_i, value)
    return lerp(min_o, max_o, ratio)


class SerialPlotter:
    def __init__(self, root, container, maxlen: int, port: str, baudrate: int):
        self.root = root
        self.container = container

        self.data1 = deque(maxlen=maxlen)
        self.data2 = deque(maxlen=maxlen)
        self.queue = queue.Queue()

        self.running = True
        # self.iter = 0

        self.ser = serial.Serial(port, baudrate)
        self.thread = Thread(target=self.listen_serial)
        self.thread.start()

        self.setup_gui()
        self.update_plot()

    def setup_gui(self):
        frmGraphEKG = tk.Frame(self.container, pady=10, padx=10, relief=tk.RAISED, borderwidth=1)
        frmGraphEKG.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        fig1 = Figure(figsize=(2, 2))
        self.ax1 = fig1.add_subplot(111)
        self.line1, = self.ax1.plot([], [])

        self.ax1.set_ylim(-2, 2)

        self.canvas1 = FigureCanvasTkAgg(fig1, master=frmGraphEKG)
        self.canvas1.get_tk_widget().pack(fill=tk.BOTH, expand=1)

        frmGraphEMG = tk.Frame(self.container, pady=10, padx=10, relief=tk.RAISED, borderwidth=1)
        frmGraphEMG.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        fig2 = Figure(figsize=(2, 2))
        self.ax2 = fig2.add_subplot(111)
        self.line2, = self.ax2.plot([], [])

        self.ax2.set_ylim(-2, 2)

        self.canvas2 = FigureCanvasTkAgg(fig2, master=frmGraphEMG)
        self.canvas2.get_tk_widget().pack(fill=tk.BOTH, expand=1)

    def listen_serial(self):
        while self.running:
            data = self.ser.read(DATA_SIZE)
            arr = struct.unpack("ii", data)

            self.queue.put(arr)


    def update_plot(self):
        try:
            while True:
                num1, num2 = self.queue.get_nowait()
                self.data1.append(map_num(num1, 0, 1024, -1.0, 1.0))
                # self.data2.append(map_num(num1, 0, 1024, -1.0, -1.0)) # Инвертированный первый пин
                self.data2.append(map_num(num2, 0, 1024, -1.0, 1.0))
                # self.iter += 1
        except queue.Empty:
            ...

        # self.line1.set_data(range(self.iter+1-len(self.data1), self.iter+1), self.data1)
        self.line1.set_data(range(1, len(self.data1)+1), self.data1)
        self.ax1.relim()
        self.ax1.autoscale_view(scaley=False)
        self.canvas1.draw()

        # self.line2.set_data(range(self.iter+1-len(self.data2), self.iter+1), self.data2)
        self.line2.set_data(range(1, len(self.data2)+1), self.data2)
        self.ax2.relim()
        self.ax2.autoscale_view(scaley=False)
        self.canvas2.draw()

        self.root.after(100, self.update_plot)

    def on_close(self):
        self.running = False
        self.thread.join()
        self.ser.close()
        self.root.destroy()

