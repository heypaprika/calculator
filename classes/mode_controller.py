class mode_controller:
    # rectangle 클래스 객체가 들어와서 해당 rectangle(frame)에 view해 줄 것.
    def __init__(self, rectangle, modenum):
        self.modenum = modenum
        # self.view = rectangle(modenum)
        self.rectangle = rectangle

    @property
    def mode(self):
        return self.modenum

    @mode.setter
    def mode(self, value):
        self.modenum = value

    def updateview(self):
        # self.modenum에 따라 view 보이기.
        self.rectangle.view(modenum) # 이건 별로 같은데,,, 그럼 어떤 방식???
