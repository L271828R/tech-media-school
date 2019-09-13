class Currency:
    def __init__(self, pair, rate):
        self.name = "{}/{}".format(pair[0], pair[1])
        self.inverse_name = "{}/{}".format(pair[1], pair[0])
        self.nom = pair[0]
        self.den = pair[1]
        if rate is not None:
            self.xrate = float(rate)
        else:
            self.xrate = None
        
        if rate is not None:
            self.inverse_xrate = 1/float(rate)
        else:
            self.inverse_xrate = None

    def __mul__(self, obj):
        if obj.nom == self.den and self.xrate is not None and obj.xrate is not None:
            return Currency((self.nom, obj.den), self.xrate * obj.xrate)
        elif obj.den == self.nom and self.xrate is not None and obj.xrate is not None:
            return Currency((self.den, obj.nom), self.xrate * obj.xrate)
        else:
            return None

    def __rmul__(self, obj):
        return self.__mul__(obj)
