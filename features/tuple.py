from collections import namedtuple

class Tuple(namedtuple('Tuple',[('x'), ('y'), ('z'), ('w')])):

    def isPoint(self) -> bool:
        return self.w == 1.0


    def isVector(self) -> bool:
        return self.w == 0.0
