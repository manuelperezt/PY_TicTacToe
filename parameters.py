import tkinter.font as tkFont

rows = 3
columns = 3
number_pieces = 3


class ButtonParam:
    bd = 0.5
    relief = 'sunken'
    bg = 'white'
    font = ('Helvetica', 100)


class ContainerParam:
    height = 200
    width = 200
    highlight = 'black'


class Player:
    fg = {'X': 'blue',
          'O': 'red'}


class FrmMessageParam:
    height = 300


class WindowsParam:
    title = "Tic-Tac-Toe"
