from data import students
from student import Student
from student import danh_hieu
from student import hanh_kiem


def getStudents():
  print('|', '-' * 47, "Danh sách các sinh viên", '-' * 48, '|')
  print('|', ' ' * 120, '|')

  print(
      f"|  {'MSHS':<12}   {'tên':<18}   {'Điểm Toán':<10}   {'Điểm Văn':<10}",
      f"  {'Điểm Anh':<10}   {'Hành Kiểm':<11}   {'DTB':<4}   {'Danh Hiệu':<23}",
      '|')
  print('|', ' ' * 120, '|')

  for student in students:
    print(student.__str__())
    print("|", "-" * 120, "|")


def addStudent():
  MSHS = input("Nhập MSHS: ")
  ten = input("\nNhập tên: ")
  diemToan = input("\nNhập Điểm Toán: ")
  diemVan = input("\nNhập Điểm Văn: ")
  diemAnh = input("\nNhập Điểm Anh: ")
  hanhKiem = input("\nNhập Hành Kiểm: ")

  student = Student(MSHS, ten, diemToan, diemVan, diemAnh, hanhKiem)

  oldLengh = len(students)
  students.append(student)
  newLengh = len(students)

  if (newLengh > oldLengh):
    print("\nĐã thêm sinh viên %s thành công." % MSHS)


def updateStudent():
  MSHS = input("Nhập MSHS của học sinh muốn cập nhật: ")

  while (len(list(filter(lambda s: s.MSHS == MSHS, students))) == 0):
    MSHS = input(
        "\nHọc sinh không tồn tại. Vui lòng Nhập lại MSHS của học sinh muốn cập nhật: "
    )

  student = list(filter(lambda s: s.MSHS == MSHS, students))[0]
  print("\nVui lòng nhập thông tin mới.")
  ten = input(f"\nTên hiện tại {student.ten}. Nhập tên mới: ")
  diemToan = input(
      f"\nĐiểm Toán hiện tại {student.diemToan}. Nhập Điểm Toán mới: ")
  diemVan = input(
      f"\nĐiểm Văn hiện tại {student.diemVan}. Nhập Điểm Văn mới: ")
  diemAnh = input(
      f"\nĐiểm Anh hiện tại {student.diemAnh}. Nhập Điểm Anh mới: ")
  hanhKiem = input(
      f"\nHành Kiểm hiện tại {student.hanhKiem}. Nhập Hành Kiểm mới: ")

  student.update(ten, diemToan, diemVan, diemAnh, hanhKiem)
  print(f"\nĐã cập nhật học sinh có MSHS: {student.MSHS} thành công.")


def removeStudent():
  MSHS = input("Nhập MSHS của học sinh muốn xoá: ")

  while (len(list(filter(lambda s: s.MSHS == MSHS, students))) == 0):
    MSHS = input(
        "\nMSHS không tồn tại. Vui lòng nhập lại MSHS của học sinh muốn xoá: ")

  student = list(filter(lambda s: s.MSHS == MSHS, students))[0]
  students.remove(student)
  print(f"\nHọc sinh có MSHS: {student.MSHS} đã được xoá thành công.")


def getStudentsByHanhKiem():
  hanhKiem = input(
      "Nhập loại Hành kiểm học sinh muốn tìm kiếm (T, K, TB, Y, Kem): ")

  while (hanhKiem != 'T' and hanhKiem != 'K' and hanhKiem != 'TB'
         and hanhKiem != 'Y' and hanhKiem != 'kem'):
    hanhKiem = input(
        "\nLoại Hành Kiểm không hợp lệ. Vui lòng nhập lại loại Hành Kiểm học sinh muốn tìm kiếm (T, K, TB, Y, Kem): "
    )

  findStudentsByHK = list(filter(lambda s: s.hanhKiem == hanhKiem, students))
  if (len(findStudentsByHK) == 0):
    print(f"\nKhông tồn tại học sinh nào có Hành Kiểm {hanhKiem}")
  else:
    print("\n|", "-" * 43,
          f"Danh sách học sinh có Hành Kiểm {hanh_kiem[hanhKiem]}", "-" * 42,
          "|")
    print('|', ' ' * 120, '|')

    print(
        f"|  {'MSHS':<12}   {'tên':<18}   {'Điểm Toán':<10}   {'Điểm Văn':<10}",
        f"  {'Điểm Anh':<10}   {'Hành Kiểm':<11}   {'DTB':<4}   {'Danh Hiệu':<23}",
        '|')
    print('|', ' ' * 120, '|')

    for student in findStudentsByHK:
      print(student.__str__())
      print("|", "-" * 120, "|")


def getStudentsByDanhHieu():
  danhHieu = input(
      "Nhập loại Danh Hiệu học sinh muốn tìm kiếm (G, K, TB, Y, kem): ")

  while (danhHieu != 'G' and danhHieu != 'K' and danhHieu != 'TB'
         and danhHieu != 'Y' and danhHieu != 'kem'):
    danhHieu = input(
        "\nLoại Danh Hiệu không hợp lệ. Vui lòng nhập lại loại Danh Hiệu học sinh muốn tìm kiếm (G, K, TB, Y, Kem): "
    )

  findStudentsByDH = list(filter(lambda s: s.danhHieu == danhHieu, students))
  if (len(findStudentsByDH) == 0):
    print(f"\nKhông tồn tại học sinh nào có Danh Hiệu {danh_hieu[danhHieu]}")
  else:
    print("\n|", "-" * 43, f"Danh sách học sinh có Danh Hiệu {danhHieu}",
          "-" * 42, "|")
    print('|', ' ' * 120, '|')

    print(
        f"|  {'MSHS':<12}   {'tên':<18}   {'Điểm Toán':<10}   {'Điểm Văn':<10}",
        f"  {'Điểm Anh':<10}   {'Hành Kiểm':<11}   {'DTB':<4}   {'Danh Hiệu':<23}",
        '|')
    print('|', ' ' * 120, '|')

    for student in findStudentsByDH:
      print(student.__str__())
      print("|", "-" * 120, "|")
