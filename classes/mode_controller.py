class Mode:
    def isVisible(self, bool):
        return bool

class rectangle(Mode):
    def __init__(self, width=1, height=1):
        self.width = width
        self.height = height


class mode_controller(rectangle):
    def __init__(self, prev_rectangle, after_rectangle):
        self.prev = prev_rectangle
        self.after = after_rectangle
        self.updateview()

    def updateview(self):
        a = self.prev.isVisible(True)
        b = self.after.isVisible(False)
        return a, b

if __name__ == '__main__':
    a_rect = rectangle(50,50)
    # a_rect 를 button, textinputs 로 꾸미기.
    #
    #
    #
    b_rect = rectangle(60,60)
    # b_rect 를 button, textinputs 로 꾸미기.
    #
    #
    #
    mode_controller(a_rect, b_rect)