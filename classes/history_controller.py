# 이전 history 보려면 cur_idx를 이용해서 가장 최근꺼부터 하나씩 이전꺼로 이동


class history_controller:
    def __init__(self):
        self.reset_history()

    # 현재 저장된 history 수
    def __len__(self):
        return len(self._history_list)

    # history_list 를 string으로 반환, e.g. '['3*4+16=28', '15/3=5', '25//2=12']'
    def __str__(self):
        return str(self._history_list)

    # 새로운 history를 history_list에 저장
    # input 형태 : string , e.g. history = '3*4+16=28'
    def save_history(self, history):
        self._history_list.append(history)

    # index 받아서 해당 history 삭제
    def del_history(self, idx):
        self._history_list.pop(idx)
        # 예외처리
        if idx >= 0:
            self.cur_idx = idx-len(self._history_list) if idx != len(self._history_list) else -1
        else:
            self.cur_idx = idx + 1 if idx != -1 else -1

    # history_list 초기화
    def reset_history(self):
        self._history_list = []
        self.cur_idx = -1

    # 현재 보고있는 history의 결과값 가져오기
    def get_result_value(self):
        result_value = self._history_list[self.cur_idx].split('=')[-1]
        return result_value

    # index 받아서 해당 history 리턴
    # index 안넣어줄 경우 가장 최근에 저장된 history 리턴
    def show_history(self, idx=-1):
        if len(self._history_list) == 0:
            return ''
        return self._history_list[idx]

    def move_prev_history(self):
        if abs(self.cur_idx) < len(self._history_list):
            self.cur_idx -= 1
        return self.show_history(self.cur_idx)

    def move_next_history(self):
        if self.cur_idx < -1:
            self.cur_idx += 1
        return self.show_history(self.cur_idx)








''' 작동 확인용 '''
def print_Current_History_Status(x):
    print('-'*70)
    print('현재 저장된 hisory 목록 :', x)
    print('현재 저장된 hisory 개수 :', len(x))
    print('현재 cur_idx가 가리키는 history :', 'index:', x.cur_idx, ', history:', x.show_history(x.cur_idx))
    print('-'*70)

if __name__=='__main__':
    H = history_controller()
    H.save_history('3*4+16=28');    print_Current_History_Status(H)
    H.save_history('15/3=5');       print_Current_History_Status(H)
    H.save_history('25//2=12');     print_Current_History_Status(H)
    H.save_history('1+1=2');        print_Current_History_Status(H)
    H.save_history('2+3=5');        print_Current_History_Status(H)
    H.save_history('8-2=6');        print_Current_History_Status(H)

    H.move_prev_history();          print_Current_History_Status(H)
    H.move_prev_history();          print_Current_History_Status(H)

    H.del_history(H.cur_idx);       print_Current_History_Status(H)
    H.del_history(2);               print_Current_History_Status(H)
    H.del_history(H.cur_idx);       print_Current_History_Status(H)
    H.del_history(H.cur_idx);       print_Current_History_Status(H)

    print(H.get_result_value())

    print()
