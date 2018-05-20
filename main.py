from music21 import converter, instrument, note, chord, stream, interval, meter, key, roman
import tkinter as tk
from tkinter import Canvas, Radiobutton, Grid, Frame

#Initalizing the first image
s = stream.Score(id='mainScore')
p0 = stream.Part(id='part0')
m01 = stream.Measure(number=1)
chord = roman.RomanNumeral('I','C')
chord.quarterLength = 4
m01.append(chord)
p0.append([m01])
s.insert(0, p0)
chordimg = s.write(fmt='musicxml.png')

def get_chord():
    roman_name = num1Entry.get()
    chord2 = roman.RomanNumeral(str(roman_name),'C')
    chord2.quarterLength = 4
    s[0][0][0] = chord2
    
    chordimg = s.write(fmt='musicxml.png')
    return chordimg
    
def updata_image():
    chordimg = get_chord()
    photo = tk.PhotoImage(file=chordimg)
    canvas.photo = photo
    canvas.itemconfig(image_box,image=photo)
    
root =tkinter.Tk()
root.title('Chord Calculator')

Image_Frame = Frame(root)
Image_Frame.pack(side=tk.TOP)
Button_Frame = Frame(root)
Button_Frame.pack(side=tk.BOTTOM)

Octave_frame = Frame(Button_Frame)
Octave_frame.pack(side=tk.LEFT)

Chord_frame = Frame(Button_Frame)
Chord_frame.pack(side=tk.RIGHT)

canvas = Canvas(Image_Frame,width=300, height=100, bg='white')
canvas.grid(column=0,row=0)
photo = tk.PhotoImage(file=chordimg,master=root)
image_box = canvas.create_image(0,0,image=photo,anchor=tk.NW)

#input1
num1Entry = tkinter.Entry(Chord_frame)
num1Entry.grid(column=1,row=0)

#button
computeButton = tkinter.Button(Chord_frame,text='Clickme',command=updata_image)
computeButton.grid(column=2,row=0)


#button for octave
v = 0
option1 = Radiobutton(Octave_frame, text="Treble", variable=v, value=0)
option1.grid(column=0,row=0)

option2 = Radiobutton(Octave_frame, text="Bass", variable=v, value=1)
option2.grid(column=0,row=1)

root.mainloop()
