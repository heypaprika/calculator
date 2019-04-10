class mode_controller:
    def __init__(self, modenum):
        # 뷰쪽 클래스 view
        self.modenum = modenum

    @property
    def mode(self):
        return self.modenum

    @mode.setter
    def mode(self, value):
        self.modenum = value

    def updateview(self):
        # self.modenum에 따라 view 보이기.