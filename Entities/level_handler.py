class Level:
    """
    Klasa odpowiedzialna za przechowywanie informacji na temat level'a.
    """
    # Konstruktor
    def __init__(self, level=1):
        self.level = level
        self.experience = 0