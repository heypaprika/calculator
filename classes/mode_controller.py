class mode_controller:
    # rectangle 클래스 객체가 들어와서 해당 rectangle(frame)에 view해 줄 것.
    # tkinter에서는 각각 요소들을 row, col로 배치시키던데,, main, mode_controller 각각을 어디까지 해야하는지 고민,,
    def __init__(self, frame, modenum):
        self.modenum = modenum

        # 뷰를 바꿀 프레임
        self.frame = frame

    @property
    def mode(self):
        return self.modenum

    @mode.setter
    def mode(self, value):
        self.modenum = value

    def updateview(self):
        # 해당하는 frame에 배치된 위젯 list만 가지고 와서
        # 적절하게 frame을 보여주기
        pass
