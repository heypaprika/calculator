# 이전 history 보려면 cur_idx 를 이용해서 가장 최근꺼부터 하나씩 이전꺼로 이동
# __history_list 의 첫번째 index : 가장 최근에 저장된 history

class HISTORY:
    def __init__(self, h):
        if type(h) != str: h = str(h)
        self.h = h

    def __len__(self):
        return len(self.h)

    def get_history_str(self):
        return str(self.h)

    def get_ans_str(self):
        return self.h.split('=')[-1].strip()

    def get_ans_float(self):
        return float(self.h.split('=')[-1])


class history_controller:
    def __init__(self):
        self.reset_history()

    # 현재 저장된 history 수
    def __len__(self):
        return len(self.__history_list)

    def __getitem__(self, idx):
        return self.__history_list[idx]

    # 새로운 history를 HISTORY class 객체로 history_list 의 첫번째 자리에 저장
    # input 형태 : string , e.g. history = '3*4+16=28'
    def save_history(self, history):
        self.__history_list.insert(0, HISTORY(history))

    # index 받아서 유효한 index 면 해당 history 삭제 & cur_idx 업데이트
    def del_history(self, idx):
        if 0 < idx <= len(self.__history_list):
            del self.__history_list[idx]
            if idx <= self.cur_idx:
                self.cur_idx -= 1
        else:
            print('IndexError')

    # history_list 초기화
    def reset_history(self):
        self.__history_list = []
        self.cur_idx = 0

    def reset_cur_idx(self):
        self.cur_idx = 0

    # 현재 저장된 모든 history 들을 리스트로 리턴
    def get_all_histories(self):
        return [h.get_history_str() for h in self.__history_list]

    # index 받아서 유효한 index 면 해당 history 리턴
    # index 안넣어줄 경우 가장 최근에 저장된 history 리턴
    def get_history(self, idx=0):
        if len(self.__history_list) == 0:
            return ''
        elif idx >= len(self.__history_list):
            print('IndexError')
            return ''
        return self.__history_list[idx].get_history_str()

    def move_prev_history(self):
        if self.cur_idx < len(self.__history_list) - 1:
            self.cur_idx += 1
        return self.get_history(self.cur_idx)

    def move_next_history(self):
        if self.cur_idx > 0:
            self.cur_idx -= 1
        return self.get_history(self.cur_idx)



""" 작동 확인용 """
def print_Current_History_Status(x):
    print('-'*70)
    print('현재 저장된 hisory 목록 :', x.get_all_histories())
    print('현재 저장된 hisory 개수 :', len(x))
    print('현재 cur_idx가 가리키는 history :', 'index:', x.cur_idx, ', history:', x.get_history(x.cur_idx))
    print('-'*70)

if __name__=='__main__':
    ex_l = ['3*4+16=28', '15/3=5', '25//2=12', '1+1=2', '2+3=5', '8-2=6']
    # history_controller 객체 선언.
    calc_History = history_controller()
    print('\n* history 저장 작동 확인')
    for ex in ex_l:
        calc_History.save_history(ex)
        print_Current_History_Status(calc_History)
    print('\n* history move_prev_history & move_next_history 함수 작동 확인')
    for _ in range(3):
        calc_History.move_prev_history()
        print_Current_History_Status(calc_History)
    calc_History.move_next_history()
    print_Current_History_Status(calc_History)
    print('\n* history 삭제 작동 확인')
    calc_History.del_history(1)
    print_Current_History_Status(calc_History)
    calc_History.del_history(3)
    print_Current_History_Status(calc_History)
    calc_History.del_history(calc_History.cur_idx)
    print_Current_History_Status(calc_History)
    print('\n* history 결과값만 가져오기 (cur_idx에 해당하는 history)')
    print(calc_History[calc_History.cur_idx].get_ans_str())

    print()






""" 구버전 
class history_controller:
    def __init__(self):
        self.reset_history()

    # 현재 저장된 history 수
    def __len__(self):
        return len(self.__history_list)

    # history_list 를 string 으로 반환, e.g. '['3*4+16=28', '15/3=5', '25//2=12']'
    def __str__(self):
        return str(self.__history_list)

    # 새로운 history를 history_list 의 첫번째 자리에 저장
    # input 형태 : string , e.g. history = '3*4+16=28'
    def save_history(self, history):
        self.__history_list.insert(0, history)

    # index 받아서 유효한 index 면 해당 history 삭제 & cur_idx 업데이트
    def del_history(self, idx):
        if idx <= len(self.__history_list):
            self.__history_list.pop(idx)
            if idx <= self.cur_idx:  
                self. cur_idx -= 1

    # history_list 초기화
    def reset_history(self):
        self.__history_list = []
        self.cur_idx = 0

    def reset_cur_idx(self):
        self.cur_idx = 0

    # 현재 저장된 모든 history 들을 리스트로 리턴
    def get_all_histories(self):
        return self.__history_list

    # index 받아서 유효한 index 면 해당 history 리턴
    # index 안넣어줄 경우 가장 최근에 저장된 history 리턴
    def get_history(self, idx=0):
        if (len(self.__history_list) == 0) or (idx >= len(self.__history_list)):
            return ''
        return self.__history_list[idx]

    def move_prev_history(self):
        if self.cur_idx < len(self.__history_list)-1:
            self.cur_idx += 1
        return self.get_history(self.cur_idx)

    def move_next_history(self):
        if self.cur_idx > 0:
            self.cur_idx -= 1
        return self.get_history(self.cur_idx)

    # 현재 보고있는 history 의 결과값 가져오기
    # def get_result_value(self):
    #     result_value = self.__history_list[self.cur_idx].split('=')[-1]
    #     return result_value






''' 작동 확인용 '''
def print_Current_History_Status(x):
    print('-'*70)
    print('현재 저장된 hisory 목록 :', x)
    print('현재 저장된 hisory 개수 :', len(x))
    print('현재 cur_idx가 가리키는 history :', 'index:', x.cur_idx, ', history:', x.get_history(x.cur_idx))
    print('-'*70)

if __name__=='__main__':
    calc_History = history_controller();       print_Current_History_Status(calc_History)
    calc_History.save_history('3*4+16=28');    print_Current_History_Status(calc_History)
    calc_History.save_history('15/3=5');       print_Current_History_Status(calc_History)
    calc_History.save_history('25//2=12');     print_Current_History_Status(calc_History)
    calc_History.save_history('1+1=2');        print_Current_History_Status(calc_History)
    calc_History.save_history('2+3=5');        print_Current_History_Status(calc_History)
    calc_History.save_history('8-2=6');        print_Current_History_Status(calc_History)

    calc_History.move_prev_history();          print_Current_History_Status(calc_History)
    calc_History.move_prev_history();          print_Current_History_Status(calc_History)
    calc_History.move_prev_history();          print_Current_History_Status(calc_History)
    calc_History.move_next_history();          print_Current_History_Status(calc_History)


    calc_History.del_history(1);               print_Current_History_Status(calc_History)
    calc_History.del_history(3);               print_Current_History_Status(calc_History)
    calc_History.del_history(calc_History.cur_idx);       print_Current_History_Status(calc_History)

    print(calc_History.get_all_histories())

    print()

"""