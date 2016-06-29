"""Rien a dire."""
import sys

class Myclasse:
    """blabla."""
    def __init__(self):
        """coucuoc ca va."""
        pass

    def mytoto(self):
        """ Pareil rien."""
        return "fonction f"

class MyChild(Myclasse):
    """Toto rien a explicaquer en details RAS."""
    def __init__(self):
        """Focntion init de base."""
        super().__init__(self)
        x = input('Donnez un nombre ?')
        self.x = x

    def meth1(self, a, b, c):
        """Methode de nouvelle generation ultra hightech haha."""
        print(a, b, c)

my_constante = MyChild()
sys.exit(1)
