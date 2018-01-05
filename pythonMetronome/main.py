import tkinter, threading, time, winsound
from tkinter import messagebox

def play_beat():
    winsound.PlaySound('metro1.wav', winsound.SND_ASYNC)
    return

def beat_loop():
    while True:
        global state
        global bpm
        while(state):
            freq = 60/bpm
            sound_thread = threading.Thread(target = play_beat)
            sound_thread.start()
            time.sleep(freq)
                
def toggle_metro():
    global state
    global bpm
    global canvas
    if(not state):
        try:
            change_bpm()
            bpm
        except NameError:
            messagebox.showerror(title = 'Error', message = 'BPM not specified')
            return
    state = not state
    if (state):
        canvas.config(state = 'normal')
    else:
        canvas.config(state = 'disabled')
    return

def change_bpm():
    global bpm
    try:
        bpm = int(bpm_field.get())
    except ValueError:
        pass
    return
    
global state
state = False
global bpm

beat_thread = threading.Thread(target = beat_loop)
beat_thread.start()

top = tkinter.Tk()
top.title('Metronome')
toggle_b = tkinter.Button(top, text = 'on/off', command = lambda: toggle_metro())
toggle_b.grid(row = 0, column = 2, padx = 10, pady = 10)

global canvas
canvas = tkinter.Canvas(top, width = 50, height = 50)
canvas.grid(row = 0, column = 3, padx = 10, pady = 10)
circle = canvas.create_oval(10, 22, 20, 32, fill = 'green', disabledfill = 'red', outline = '')
canvas.config(state = 'disabled')

bpm_label = tkinter.Label(top, text = 'BPM: ')
bpm_label.grid(row = 0, column = 0, padx = 10, pady = 10)
bpm_field = tkinter.Entry(top, width = 4)
bpm_field.grid(row = 0, column = 1, padx = 10, pady = 10)

top.mainloop()
