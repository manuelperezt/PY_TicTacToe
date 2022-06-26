import tkinter as tk
from parameters import *
from functools import partial


class Board:
    def __init__(self, rows: int = 3, columns: int = 3):
        self.controller = None
        self.window = tk.Tk()
        self.window.title(WindowsParam.title)
        self.rows = rows
        self.columns = columns

        self.board_frm = tk.Frame(master=self.window)
        self.message_frm = tk.Frame(master=self.window, height=FrmMessageParam.height)
        self.buttons = {}
        for r in range(self.rows):
            for c in range(self.columns):
                container_frm = tk.Frame(master=self.board_frm,
                                         height=ContainerParam.height,
                                         width=ContainerParam.width,
                                         highlightbackground=ContainerParam.highlight)
                container_frm.grid_propagate(False)
                container_frm.pack_propagate(False)
                button_btn = tk.Button(container_frm,
                                       # height=buttonParam.height,
                                       # width=buttonParam.width,
                                       font=ButtonParam.font,
                                       bd=ButtonParam.bd,
                                       relief=ButtonParam.relief,
                                       bg=ButtonParam.bg,
                                       command=partial(self.button_click, r, c),
                                       anchor=tk.CENTER)

                container_frm.grid(row=r, column=c)

                self.buttons[(r, c)] = [container_frm, button_btn]

        self.message_lbl = tk.Label(master=self.message_frm, text=f"Welcome. Player X plays")
        self.arrange()
        self.window.resizable(False, False)

    def clear(self):
        for button in self.buttons:
            self.buttons[button][1].config(text="")

    def set_controller(self, controller):
        self.controller = controller

    def button_click(self, row: int, col: int):
        self.controller.button_click(row, col)

    def set_message(self, text: str):
        self.message_lbl.configure(text=text)

    def arrange(self):
        self.board_frm.pack(fill=tk.BOTH, expand=True, side=tk.TOP)
        self.message_lbl.pack(fill=tk.Y, expand=True)
        self.message_frm.pack(fill=tk.BOTH, expand=True, side=tk.BOTTOM)
        for b in self.buttons:
            self.buttons[b][1].pack(fill=tk.BOTH, expand=True)

    def set_button_status(self, player: str, row, col) -> None:
        self.buttons[(row, col)][1].config(text=player, fg=Player.fg[player])
