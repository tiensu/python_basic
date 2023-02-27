'''
Bài 1:
1. Tạo class Vehicle:
- Có 2 thuộc tính là max_speed và name. Hai thuộc tính này được gán giá trị khởi tạo lúc khai báo đối tượng của class
- Hai phương thức:
+ phương thức get_veh(): Hiển thị thông tin về các thuộc tính của đối tượng của class
+ phương thức set_veh(): Gán giá trị mới cho các thuộc tính của đối tượng
+ phương thức check_speed(): Kiểm tra tốc độ của đối tượng theo các dải giá trị: 0 -30: 
Slow, 30-70: Normal, > 70: Fast. In ra thông báo tương ứng

2. Tạo hai đối tượng của class.
3. Hiển thị thông tin của các đối tượng vừa tạo
4. Cập nhật thông tin mới cho một trong 2 đối tượng. Kiểm tra lại hành động cập nhật bằng cách hiển thi thông tin mới.
5. Hiển thị thông tin về dải tốc độ của 2 đối tượng.
6. Biến tất cả các thuộc tính và phương thức của class (trừ phương thức get_veh() và set_veh()) thành private rồi thực hiện lại
các yêu cầu từ số 3 đến số 5. Xem kết quả và giải thích.

Bài 2:
1. Tạo một class Math_Operation:
- Có 2 thuộc tính private là value_1, và value_2. Hai thuộc tính này được gán giá trị khởi tạo lúc đầu.
- Có các phương thức private sau:
+ Phương thức 1: Kiểm tra kiểu dữ liệu của 2 thuộc tính bên trên.
+ Phương thức 2: Tính tổng 2 thuộc tính nếu có thể. Nếu không thể thì in ra thông báo lỗi
+ Phương thức 3: Nếu 2 thuộc tính có kiểu list (cùng số phần tử) thì tạo ra một list thứ 3 bằng cách cộng các phần tử tương ứng của 2 list ban đầu.
+ Phương thức 4: Nếu 2 thuộc tính có kiểu string (cùng số lượng ký tự) thì tạo ra một string thứ 3 bằng cách xen kẽ từng ký tự của 2 list ban đầu.
- Có các phương thức public sau:
+ Phương thức 5: Gán giá trị mới cho 2 thuộc tính bằng các giá trị nhập từ bàn phím.
+ Phương thưc 6: Hiển thị tổng của 2 thuộc tính.
+ Phương thức 7: Hiển thị list thứ 3 trong trường hợp 2 thuộc tính có kiểu list
+ Phương thức 8: Hiển thị string thứ 3 trong trường hợp 2 thuộc tính có kiểu string

2. Viết hàm main() bên ngoài class để thực hiện các yêu cầu sau:
- Tạo một đối tượng của class Math_Operation:
- Hiển thị tổng của 2 thuộc tính của đối tượng vừa tạo.
- Gán giá trị mới cho 2 thuộc tính của đối tượng là 2 list có cùng số lượng phần tử. Sau đó hiển thị list thứ 3.
- Gán giá trị mới cho 2 thuộc tính của đối tượng là 2 string có cùng số lượng ký tự. Sau đó hiển thị string thứ 3.

'''