import turtle
import pandas as pd

from mahasiswa_gerry import Mahasiswa

class Pena:
    def __init__(self, mahasiswa, color):
        self.mahasiswa = Mahasiswa(*mahasiswa)
        self.t = turtle.Turtle()
        self.t.shape("classic")
        self.t.color(color)
        self.t.speed(7)
    
    def gambar_segitiga(self, ukuran):
        self.t.penup()
        self.t.forward(-400)
        self.t.pendown()
        self.t.begin_fill()
        for _ in range(3):
            self.t.forward(ukuran)
            self.t.left(120)
        self.t.end_fill()

df = pd.read_excel("data_mi23.xlsx", "Table 1")
data = df.values.tolist()

mahasiswa_mi = []
for mahasiswa in data:
    color = "red"
    if mahasiswa[1] == "2023A":
        color = "purple"
    if mahasiswa[1] == "2023B":
        color = "blue"
    if mahasiswa[1] == "2023C":
        color = "green"
    if mahasiswa[1] == "2023D":
        color = "orange"
    if mahasiswa[1] == "2023E":
        color = "gold"
    if mahasiswa[1] == "2023F":
        color = "red"
    mahasiswa_mi.append(Pena(mahasiswa, color))

screen = turtle.Screen()
screen.bgcolor("white")

for i, pena in enumerate(mahasiswa_mi):
    pena.gambar_segitiga(50)
    if i < len(mahasiswa_mi) - 1:
        mahasiswa_mi[i+1].t.penup()
        mahasiswa_mi[i+1].t.goto(75*(i+1), 0)
        mahasiswa_mi[i+1].t.pendown()

screen.exitonclick()