from utils import *

class Student:
    def __init__(self, st_ID='', st_name='', st_dob='', st_sex='', st_address='', st_mobile='', st_email='') -> None:
        self.st_ID = st_ID
        self.st_name = st_name
        self.st_dob = st_dob
        self.st_sex = st_sex
        self.st_address = st_address
        self.st_mobile = st_mobile
        self.st_email = st_email
        
    def display_menu(self):
        while True:
            print('---------------------------------')
            print('Chon 1 trong cac chuc nang ben duoi:')
            print('1. Them moi sinh vien')
            print('2. Cap nhap thong tin sinh vien')
            print('3. Xoa thong tin sinh vien')
            print('4. Tim kiem thong tin sinh vien')
            print('5. Quay lai menu truoc do')
            user_input = input('Chon chuc nang: ')
            if user_input == '1':
                self.add_student()
            elif user_input == '2':
                self.update_student()
            elif user_input == '3':
                self.delete_student()
            elif user_input == '4':
                self.search_student()
            elif user_input == '5':
                print('BYE BYE')
                # time.sleep(1)
                return
            else:
                print('Vui long nhap dung ma so chuc nang quy dinh')

    def input_st_info(self):
        self.st_name = input('Ten SV: ')
        self.st_dob = input('Ngay sinh: ')
        self.st_sex = input('Gioi tinh: ')
        self.st_address = input('Dia chi: ')
        self.st_mobile = input('So dien thoai: ')
        self.st_email = input('Email: ')

    def add_student(self):
        # input information from keyboard
        print('*********** Nhap thong tin sinh vien ***********')
        self.st_ID = input('Ma SV: ')
        self.input_st_info()

        # format data. 
        # For example: 
        # PY000005|Nguyễn Phương Thảo|08/09/1995|0|Hà Nội|0964330956|nguyenthao.npt98@gmail.com
        st_infor_str = '|'.join([self.st_ID, self.st_name, self.st_dob, self.st_sex, self.st_address, self.st_mobile, self.st_email, '\n'])
        add_st_status = write_txt_file('data/hocvien.txt', [st_infor_str], 'a+')
        if add_st_status:
            print('Them moi sinh vien thanh cong')
        else:
            print('Them moi sinh vien khong thanh cong')

    def update_student(self):
        print('************ Nhap vao Ma SV can cap nhat thong tin *************')
        while True:
            st_Id_input = input('Ma SV: ')
            st_infors = read_txt_file('data/hocvien.txt')
            # get list of ma sv
            for idx, st in enumerate(st_infors):   
                st_Id = st.split('|')[0]
                if st_Id_input == st_Id:
                    print('Nhap thong tin moi cua sinh vien')
                    self.input_st_info()
                    # format data. 
                    # For example: 
                    # PY000005|Nguyễn Phương Thảo|08/09/1995|0|Hà Nội|0964330956|nguyenthao.npt98@gmail.com
                    st_infor_str = '|'.join([st_Id_input, self.st_name, self.st_dob, self.st_sex, self.st_address, self.st_mobile, self.st_email, '\n'])
                    st_infors[idx] = st_infor_str
                    add_st_status = write_txt_file('data/hocvien.txt', st_infors, 'w+')
                    if add_st_status:
                        print('Cap nhat thong tin sinh vien thanh cong')
                        return True
                    else:
                        print('Cap nhat thong tin sinh vien khong thanh cong. Vui long thu lai sau')
                        return False
                    
            print('Sinh vien khong khong ton tai trong danh sach. Vui long nhap ma sv khac')



    def delete_student(self):
        while True:
            print('************ Nhap vao Ma SV *************')
            st_Id_input = input('Ma SV: ')
            st_infors = read_txt_file('data/hocvien.txt')
            # get list of ma sv
            for idx, st in enumerate(st_infors):   
                st_Id = st.split('|')[0]
                if st_Id_input == st_Id:
                    st_infors.pop(idx)
                    add_st_status = write_txt_file('data/hocvien.txt', st_infors, 'w+')
                    if add_st_status:
                        print('Xoa thong tin sinh vien thanh cong')
                        return True
                    else:
                        print('Xoa thong tin sinh vien khong thanh cong. Vui long thu lai sau')
                        return False
            print('Sinh vien khong ton tai trong danh sach. Vui long nhap ma sv khac')

    def search_student(self):
        print('************ Nhap vao Ma SV *************')
        st_Id_input = input('Ma SV: ')
        print(f'st_Id_input: {st_Id_input}')
        st_infors = read_txt_file('data/hocvien.txt')
        print(f'st_infors: {st_infors}')
        # get list of ma sv
        for idx, st in enumerate(st_infors):   
            st_Id = st.split('|')[0]
            print(f'st_Id: {st_Id}')
            if st_Id_input == st_Id:
                print('*********** Thong tin sinh vien tim thay nhu sau: ************ ')
                print(f'Ma SV: {st_Id_input}')
                print(f'Ho ten: {st.split("|")[1]}')
                print(f'Ngay sinh: {st.split("|")[2]}')
                print(f'Gioi tinh: {st.split("|")[2]}')
                print(f'Dia chi: {st.split("|")[3]}')
                print(f'So dien thoai: {st.split("|")[4]}')
                print(f'Email: {st.split("|")[5]}')
                return
        print(f'Khong ton tai sinh vien voi ma sv {st_Id_input}')