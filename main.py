from numpy import asarray
from tkinter import *
from analasis import *


board = asarray(
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


cp = ["#b1e4b9", "#70a2a3"]
ac = ["#bfe3c4", "#7aa3a3"]


class Game:
    can: Canvas

    def __init__(self):
        self.root = Tk()
        self.draw_ui()
        self.load_icon()

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
                )
        self.root.geometry("512x512")
    
    def load_icon(self):
        try:
            photo = PhotoImage(file = '/usr/share/pixmaps/checkers.png')
            self.root.wm_iconphoto(False, photo)
        except:
            print("Unable To Load Icon...")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    Game().run()
