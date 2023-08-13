from student import Student
from data import students

def menu():
  print('-'*15, 'Chương Trình Quản Lý Học Sinh', '-'*15, end='\n')
  print('| ', '1. Hiển thị danh sách học sinh', ' '*26, end='|\n')
  print('| ', '2. Thêm một học sinh vào danh sách', ' '*22, end='|\n')
  print('| ', '3. Cập nhật một sinh viên trong danh sách', ' '*15, end='|\n')
  print('| ', '4. Xoá một sinh viên trong danh sách', ' '*20, end='|\n')
  print('| ', '5. Hiển thị danh sách học sinh theo DTB', ' '*17, end='|\n')
  print('| ', '6. Hiển thị danh sách học sinh theo Hành Kiểm', ' '*11, end='|\n')
  print('| ', '7. Hiển thị danh sách học sinh theo Danh Hiệu', ' '*11, end='|\n')
  print('| ', '8. Thoát chương trình', ' '*35, end='|\n')
  print('-'*61, end='\n')

def run() :
  back = 0
  while (True):
    if (back != 8 and back != 0):
      print("Nhập sai chức năng. Vui lòng nhập lại.")
    elif (back == 8):
      print("\nKết thúc chương trình.")
      return
    elif (back == 0): 
      menu()
      func = int(input("\nChọn chức năng bạn muốn thực hiện: "))
      print("\n")
      match func:
        case 1:
          print("function 1")
          
        case 2:
          print("function 2")
          
        case 3:
          print("function 3")
          
        case 4:
          print("function 4")
          
        case 5:
          print("function 5")
          
        case 6:
          print("function 6")
          
        case 7:
          print("function 7")
          
        case 8:
          print("Kết thúc chương trình.")
          return
          
        case other:
          print("Số chức năng không hợp lệ. vui lòng nhập lại.\n")
          continue
          
    back = int(input("\nNhập 0 để hiển thị các chức năng hoặc nhập 8 để thoát chương trình: "))
    print("\n")
    
run()
  