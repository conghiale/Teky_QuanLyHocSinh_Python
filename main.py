import studentController
from student import Student
from data import students

def menu():
  print('-'*15, 'Chương Trình Quản Lý Học Sinh', '-'*15, end='\n')
  print('| ', '1. Hiển thị danh sách học sinh', ' '*26, end='|\n')
  print('| ', '2. Thêm một học sinh vào danh sách', ' '*22, end='|\n')
  print('| ', '3. Cập nhật một sinh viên trong danh sách', ' '*15, end='|\n')
  print('| ', '4. Xoá một sinh viên trong danh sách', ' '*20, end='|\n')
  print('| ', '5. Hiển thị danh sách học sinh theo Hành Kiểm', ' '*11, end='|\n')
  print('| ', '6. Hiển thị danh sách học sinh theo Danh Hiệu', ' '*11, end='|\n')
  print('| ', '7. Thoát chương trình', ' '*35, end='|\n')
  print('-'*61, end='\n')

def run() :
  back = '0'
  while (True):
    if (back != '7' and back != '0'):
      print("Nhập sai chức năng. Vui lòng nhập lại.")
    elif (back == '7'):
      print("Kết thúc chương trình.")
      return
    elif (back == '0'): 
      menu()
      func = int(input("\nChọn chức năng bạn muốn thực hiện: "))
      print("\n")
      match func:
        case 1:
          studentController.getStudents()
          
        case 2:
          studentController.addStudent()
          
        case 3:
          studentController.updateStudent()
          
        case 4:
          studentController.removeStudent()
          
        case 5:
          studentController.getStudentsByHanhKiem()
          
        case 6:
          studentController.getStudentsByDanhHieu()
          
        case 7:
          print("Kết thúc chương trình.")
          return
          
        case other:
          print("Số chức năng không hợp lệ. vui lòng nhập lại.\n")
          continue
          
    back = input("\nNhập 0 để hiển thị các chức năng hoặc nhập 7 để thoát chương trình: ")
    print("\n")
    
run()
  