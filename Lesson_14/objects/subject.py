from utils import *

class Subject:
    def __init__(self, sub_id='', sub_name='') -> None:
        self.sub_id = sub_id
        self.sub_name = sub_name

    def display_menu(self):
        while True:
            print('---------------------------------')
            print('Chon 1 trong cac chuc nang ben duoi:')
            print('1. Them moi mon hoc')
            print('2. Cap nhap thong tin mon hoc')
            print('3. Xoa thong tin mon hoc')
            print('4. Tim kiem thong tin mon hoc')
            print('5. Quay lai menu truoc do')
            user_input = input('Chon chuc nang: ')
            if user_input == '1':
                self.add_subject()
            elif user_input == '2':
                self.update_subject()
            elif user_input == '3':
                self.delete_subject()
            elif user_input == '4':
                self.search_subject()
            elif user_input == '5':
                print('BYE BYE')
                # time.sleep(1)
                return
            else:
                print('Vui long nhap dung ma so chuc nang quy dinh')

    def input_subject_info(self):
        self.sub_name = input('Ten Mon hoc: ')

    def add_subject(self):
        # input information from keyboard
        print('*********** Nhap thong tin mon hoc ***********')
        self.sub_id = input('Ma Mon hoc: ')
        self.input_subject_info()

        # format data. 
        # For example: 
        # PY000005|Nguyễn Phương Thảo|08/09/1995|0|Hà Nội|0964330956|nguyenthao.npt98@gmail.com
        sub_infor_str = '|'.join([self.sub_id, self.sub_name, '\n'])
        add_sub_status = write_txt_file('data/monhoc.txt', [sub_infor_str], 'a+')
        if add_sub_status:
            print('Them moi mon hoc thanh cong')
        else:
            print('Them moi mon hoc khong thanh cong')

    def update_subject(self):
        while True:
            print('************ Nhap vao Ma mon hoc can cap nhat thong tin *************')
            sub_Id_input = input('Ma Mon hoc: ')
            sub_infors = read_txt_file('data/monhoc.txt')
            print(f'sub_infors: {sub_infors}')
            # get list of ma sv
            for idx, sub in enumerate(sub_infors):   
                sub_Id = sub.split('|')[0]
                print(f'sub_Id: {sub_Id}')
                if sub_Id_input == sub_Id:
                    print('Nhap ten moi cua mon hoc')
                    self.input_subject_info()
                    # format data. 
                    # For example: 
                    # PY000005|Nguyễn Phương Thảo|08/09/1995|0|Hà Nội|0964330956|nguyenthao.npt98@gmail.com
                    sub_infor_str = '|'.join([sub_Id_input, self.sub_name, '\n'])
                    sub_infors[idx] = sub_infor_str
                    print(f'sub_infors: {sub_infors}')
                    update_sub_status = write_txt_file('data/monhoc.txt', sub_infors, 'w+')
                    if update_sub_status:
                        print('Cap nhat thong tin mon hoc thanh cong')
                        return True
                    else:
                        print('Cap nhat thong tin mon hoc khong thanh cong. Vui long thu lai sau')
                        return False
                    
            print('Mon hoc khong ton tai trong danh sach. Vui long nhap ma sv khac')



    def delete_subject(self):
        while True:
            print('************ Nhap vao Ma Mon hoc *************')
            sub_Id_input = input('Ma Mon hoc: ')
            sub_infors = read_txt_file('data/monhoc.txt')
            # get list of ma sv
            for idx, sub in enumerate(sub_infors):   
                sub_Id = sub.split('|')[0]
                print(f'sub_Id: {sub_Id}')
                if sub_Id_input == sub_Id:
                    sub_infors.pop(idx)
                    del_sub_status = write_txt_file('data/monhoc.txt', sub_infors, 'w+')
                    if del_sub_status:
                        print('Xoa thong tin mon hoc thanh cong')
                        return True
                    else:
                        print('Xoa thong tin mon hoc khong thanh cong. Vui long thu lai sau')
                        return False
            print('Mon hoc khong ton tai trong danh sach. Vui long nhap ma mon hoc khac')

    def search_subject(self):
        print('************ Nhap vao Ma Mon hoc *************')
        sub_Id_input = input('Ma Mon hoc: ')
        sub_infors = read_txt_file('data/monhoc.txt')
        # get list of ma sv
        for sub in sub_infors:   
            sub_Id = sub.split('|')[0]
            if sub_Id_input == sub_Id:
                print('*********** Thong tin mon hoc tim thay nhu sau: ************ ')
                print(f'Ma Mon hoc: {sub_Id}')
                print(f'Ten Mon hoc: {sub.split("|")[1]}')
                return
        print(f'Khong ton tai mon hoc voi ma mon hoc {sub_Id_input}')