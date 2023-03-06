from analasis import *


queue = []
_init = False

def init(bd):
    global _init
    if _init:
        raise RuntimeError("Cannot Re-Init")
    _init = True
    queue.append(bd)

