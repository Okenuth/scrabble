import PySimpleGUI as sg
from boton import Boton
class Tablero1():
  def __init__(self):
    self.matriz=[[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0],
                 [0,0,2,0,0,0,1,0,1,0,0,0,2,0,0],
                 [0,2,0,0,0,1,0,0,0,1,0,0,0,2,0],
                 [0,0,0,0,1,0,0,1,0,0,1,0,0,0,0],
                 [0,0,0,1,0,0,2,0,2,0,0,1,0,0,0],
                 [0,0,1,0,0,1,0,0,0,1,0,0,1,0,0],
                 [0,1,0,0,2,0,0,2,0,0,2,0,0,1,0],
                 [1,0,0,1,0,0,2,0,2,0,0,1,0,0,1],
                 [0,1,0,0,2,0,0,2,0,0,2,0,0,1,0],
                 [0,0,1,0,0,1,0,0,0,1,0,0,1,0,0],
                 [0,0,0,1,0,0,2,0,2,0,0,1,0,0,0],
                 [0,0,0,0,1,0,0,1,0,0,1,0,0,0,0],
                 [0,2,0,0,0,1,0,0,0,1,0,0,0,2,0],
                 [0,0,2,0,0,0,1,0,1,0,0,0,2,0,0],
                 [0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]
    ]
  def crearTablero(self):
    layout = []
    for i in self.matriz:
      row = []
      for j in i:
        button = Boton(j).get_boton()
        row.append(button)
      layout.append(row)

    window = sg.Window('Tablero', layout)

    while True:
      casillero = window.Read()
      print(casillero)

    window.close()