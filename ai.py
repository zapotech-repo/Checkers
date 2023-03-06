from analasis import *
from bidict import bidict


queue = []
boards = bidict()
info = {}
id_counter = 0
_init = False

def init(bd):
    global _init
    if _init:
        raise RuntimeError("Cannot Re-Init")
    _init = True
    queue.append(bd)

