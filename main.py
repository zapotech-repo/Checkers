from numpy import asarray, ndarray
from tkinter import *
from analasis import *


cp = ["#b1e4b9", "#70a2a3"]
ac = ["#bfe3c4", "#83a3a3"]


class Game:
    can: Canvas
    pids: dict[tuple[int, int], int]
    board: ndarray[int]

    def __init__(self):
        self.root = Tk()
        self.pids = {}
        self.turn = 0
        self.draw_ui()
        self.load_icon()
        self.reset()

    def reset(self):
        self.board = asarray(
            [
                [0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 1, 0, 1, 0],
                [0, 1, 0, 1, 0, 1, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [-1, 0, -1, 0, -1, 0, -1, 0],
                [0, -1, 0, -1, 0, -1, 0, -1],
                [-1, 0, -1, 0, -1, 0, -1, 0],
            ]
        )
        self.draw_pieces()

    def draw_ui(self):
        self.root.title("Checkers")
        self.can = Canvas(self.root, highlightthickness=0)
        self.can.place(x=0, y=0, width=512, height=512)
        for x in range(8):
            for y in range(8):
                self.can.create_rectangle(
                    64 * x,
                    64 * y,
                    64 * x + 64,
                    64 * y + 64,
                    fill=cp[(x + y) % 2],
                    activefill=ac[(x + y) % 2],
                    outline="black",
                    activeoutline="green",
                    activewidth=2
                )
        self.root.geometry("512x512")

    def draw_pieces(self):
        for i in self.pids.values():
            self.can.delete(i)
        self.pids = {}
        for x in range(8):
            for y in range(8):
                if self.board[x, y]:
                    self.pids[(x, y)] = self.can.create_oval(
                        *self.xy2sc(x+1/16,y+1/16), *self.xy2sc(x+15/16,y+15/16), fill = "red" if self.board[x, y]<0 else "black", outline = "yellow" if abs(self.board[x, y])==2 else "black", width=5
                    )
    def xy2sc(self,x,y):
        if self.turn:
            x=8-x
            y=8-y
        return 64 * y,64 * x
    def load_icon(self):
        try:
            photo = PhotoImage(file="/usr/share/pixmaps/checkers.png")
            self.root.wm_iconphoto(False, photo)
        except:
            print("Unable To Load Icon...")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    Game().run()
