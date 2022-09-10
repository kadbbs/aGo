

class GoBoard:
    def __int__(self,width,height):
        self.width=width
        self.height=height





class StoneString:
    def __int__(self,player,stones,liberties):
        self.becolgings=player
        self.stones=set(stones)
        self.liberties=set(liberties)

    @classmethod
    def merge(cls,str1,str2):
        assert str1.becolgings==str2.becolgiings
        allstones=str1.stones|str2.stones

