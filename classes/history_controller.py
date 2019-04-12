# mode에 따라 다른 history 가져야 하나..?
# 이전 history 보려면 cur_idx를 이용해서 가장 최근꺼부터 하나씩 이전꺼로 이동

class history_controller:
    def __init__(self):
        self._history_list = []
        self._cur_idx = -1

    # 현재 저장된 history 수
    def __len__(self):
        return len(self._history_list)

    # 새로운 history를 history_list에 저장
    # '=' 입력시 저장
    # e.g. history = '3*4+16=28'
    def save_history(self, history):
        self._history_list.append(history)

    # 현재 보고있는 history 삭제
    def del_history(self):
        self._history_list.pop(self._cur_idx)

    # history_list 초기화
    def reset_history(self):
        self._history_list = []

    # 현재 보고있는 history의 결과값 가져오기
    def get_history(self):
        result_value = self._history_list[self._cur_idx].split('=')[-1]
        return result_value

    # 특정 history의 값 리턴
    def show_history(self,i):
        if len(self._history_list) == 0:
            return ''
        return self._history_list[i]

    def move_prev_history(self):
        if abs(self._cur_idx) < len(self._history_list):
            self._cur_idx -= 1
        self.show_history(self._cur_idx)

    def move_next_history(self):
        if self._cur_idx < -1:
            self._cur_idx += 1
        self.show_history(self._cur_idx)

