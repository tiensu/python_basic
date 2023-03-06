from utils import *

class Score:
    def __init__(self, st_Id='', sub_Id='', prog_score='', end_score='', final_score='') -> None:
        self.st_Id = st_Id
        self.sub_Id = sub_Id
        self.prog_score = prog_score
        self.end_score = end_score
        self.final_score = final_score

    def display_menu(self):
        while True:
            print('---------------------------------')
            print('Chon 1 trong cac chuc nang ben duoi:')
            print('1. Them moi diem thi')
            print('2. Cap nhap thong tin diem thi')
            print('3. Xoa thong tin diem thi')
            print('4. Tim kiem thong tin diem thi')
            print('5. Thong ke diem thi')
            print('6. Quay lai menu truoc do')
            user_input = input('Chon chuc nang: ')
            if user_input == '1':
                self.add_score()
            elif user_input == '2':
                self.update_score()
            elif user_input == '3':
                self.delete_score()
            elif user_input == '4':
                self.search_score()
            elif user_input == '5':
                self.statistic_score()
            elif user_input == '6':
                print('BYE BYE')
                # time.sleep(1)
                return
            else:
                print('Vui long nhap dung ma so chuc nang quy dinh')

    def cal_final_score(self):
        self.final_score = (int(self.prog_score) + int(self.end_score)*2)/3

    def input_score_info(self):
        # self.st_Id = input('Ten Sinh vien: ')
        # self.sub_Id = input('Ten Mon hoc: ')
        self.prog_score = input('Diem qua trinh: ')
        self.end_score = input('Diem ket thuc: ')

    def add_score(self):
        # input information from keyboard
        print('*********** Nhap thong tin diem thi ***********')
        self.st_Id = input('Ma Hoc vien: ')
        self.sub_Id = input('Ma Mon hoc: ')
        self.input_score_info()
        self.cal_final_score()

        # format data. 
        # For example: 
        # PY000005|Nguyễn Phương Thảo|08/09/1995|0|Hà Nội|0964330956|nguyenthao.npt98@gmail.com
        score_infor_str = '|'.join([self.st_Id, self.sub_Id, self.prog_score, self.end_score, str(self.final_score), '\n'])
        add_score_status = write_txt_file('data/diemthi.txt', [score_infor_str], 'a+')
        if add_score_status:
            print('Them moi diem thi thanh cong')
        else:
            print('Them moi diem thi khong thanh cong')

    def update_score(self):
        while True:
            print('************ Nhap vao Ma mon hoc va Ma hoc vien de cap nhat thong tin diem thi *************')
            sub_Id_input = input('Ma Mon hoc: ')
            st_Id_input = input('Ma Hoc vien: ')
            score_infors = read_txt_file('data/diemthi.txt')
            # print(f'sub_infors: {sub_infors}')
            # get list of ma sv
            for idx, sco in enumerate(score_infors): 
                st_Id = sco.split('|')[0]  
                sub_Id = sco.split('|')[1]
                # print(f'sub_Id: {sub_Id}')
                if sub_Id_input == sub_Id and st_Id_input == st_Id:
                    # print('Nhap diem qua trinh va diem ket thu:')
                    self.input_score_info()
                    self.cal_final_score()
                    # format data. 
                    # For example: 
                    # PY000005|Nguyễn Phương Thảo|08/09/1995|0|Hà Nội|0964330956|nguyenthao.npt98@gmail.com
                    score_infor_str = '|'.join([st_Id, sub_Id_input, self.prog_score, self.end_score, str(self.final_score), '\n'])
                    # print(f'score_infor_str: {score_infor_str}')
                    score_infors[idx] = score_infor_str
                    # print(f'sub_infors: {sub_infors}')
                    update_score_status = write_txt_file('data/diemthi.txt', score_infors, 'w+')
                    if update_score_status:
                        print('Cap nhat thong tin diem thi thanh cong')
                        return True
                    else:
                        print('Cap nhat thong tin diem thi khong thanh cong. Vui long thu lai sau')
                        return False
                    
            print('Diem thi khong ton tai trong danh sach. Vui long chon diem thi khac de cap nhat')


    def delete_score(self):
        while True:
            print('************ Nhap vao Ma Hoc vien va Ma Mon hoc *************')
            sub_Id_input = input('Ma Mon hoc: ')
            st_Id_input = input('Ma Hoc vien: ')

            score_infors = read_txt_file('data/diemthi.txt')
            # get list of ma sv
            for idx, sco in enumerate(score_infors):   
                st_Id = sco.split('|')[0]  
                sub_Id = sco.split('|')[1]
                # print(f'sub_Id: {sub_Id}')
                if sub_Id_input == sub_Id and st_Id_input == st_Id:
                    score_infors.pop(idx)
                    del_score_status = write_txt_file('data/diemthi.txt', score_infors, 'w+')
                    if del_score_status:
                        print('Xoa thong tin diem thi thanh cong')
                        return True
                    else:
                        print('Xoa thong tin diem thi khong thanh cong. Vui long thu lai sau')
                        return False
            print('Diem thi khong ton tai trong danh sach. Vui long nhap thong tin khac')

    def search_score(self):
        print('************ Nhap vao Ma Hoc vien va Ma Mon hoc *************')
        sub_Id_input = input('Ma Mon hoc: ')
        st_Id_input = input('Ma Hoc vien: ')

        score_infors = read_txt_file('data/diemthi.txt')
        # get list of ma sv
        for sco in score_infors:   
            st_Id = sco.split('|')[0]  
            sub_Id = sco.split('|')[1]

            if sub_Id_input == sub_Id and st_Id_input == st_Id:
                print('*********** Thong tin diem thi tim thay nhu sau: ************ ')
                print(f'Ma Hoc vien: {st_Id}')
                print(f'Ma Mon hoc: {sub_Id}')
                print(f'Diem qua trinh: {sco.split("|")[2]}')
                print(f'Diem tong ket: {sco.split("|")[3]}')
                return
        print(f'Khong ton tai diem thi voi ma hoc vien {st_Id} va ma mon hoc {sub_Id_input}')

    def statistic_score(self):
        score_a, score_b, score_c, score_d = [], [], [], []
        score_infors = read_txt_file('data/diemthi.txt')
        for sco in score_infors:
            fi_score = float(sco.split('|')[4])
            if fi_score >= 90 and fi_score <= 100:
                score_a.append(fi_score)
            elif fi_score >= 70 and fi_score < 90:
                score_b.append(fi_score)
            elif fi_score >= 50 and fi_score < 70:
                score_c.append(fi_score)
            else:
                score_d.append(fi_score)
        
        score_a_str = "Number of score A: " + str(len(score_a))
        score_b_str = "Number of score B: " + str(len(score_b))
        score_c_str = "Number of score C: " + str(len(score_c))
        score_d_str = "Number of score D: " + str(len(score_d))
        score_statistic = ('\n').join([score_a_str, score_b_str, score_c_str, score_d_str])
        if write_txt_file('data/score_statistic.txt', score_statistic, 'w+'):
            print('Write statistic score into txt file sucessfully')
        else:
            print('Write statistic score into txt file not sucessfully')