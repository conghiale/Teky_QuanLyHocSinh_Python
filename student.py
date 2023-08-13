class Student:
  # MSSV 
  # ten 
  # diemToan
  # diemVan
  # diemAnh
  # DTB
  # hanhKiem
  # danhHieu
  
  def __init__(self, MSSV, ten, diemToan, diemVan, diemAnh, hanhKiem):
    self.MSSV = MSSV
    self.ten = ten
    self.diemToan = diemToan
    self.diemVan = diemVan
    self.diemAnh = diemAnh
    self.hanhKiem = hanh_kiem[hanhKiem]
    self.DTB = self.calculateDTB()
    self.danhHieu = self.handleDanhHieu(hanhKiem)

  def update(self, MSSV, ten, diemToan, diemVan, diemAnh, hanhKiem):
    self.MSSV = MSSV
    self.ten = ten
    self.diemToan = diemToan
    self.diemVan = diemVan
    self.diemAnh = diemAnh
    self.hanhKiem = hanh_kiem[hanhKiem]
    self.DTB = self.calculateDTB()
    self.danhHieu = self.handleDanhHieu(hanhKiem)

  def calculateDTB(self):
    return round(((self.diemToan + self.diemVan + self.diemAnh) / 3), 2)

  def handleDanhHieu(self, hanhKiem):
    match hanhKiem:
      case 'T':
        if (self.hocSinhGioi()):
          return danh_hieu['G']
        elif (self.hocSinhKha()):
          return danh_hieu['K']
        elif (self.hocSinhTB()):
          return danh_hieu['TB']
        elif (self.hocSinhYeu()):
          return danh_hieu['Y']
        else:
          return danh_hieu['Kem']
          
      case 'K':
        if (self.hocSinhKha()):
          return danh_hieu['K']
        elif (self.hocSinhTB()):
          return danh_hieu['TB']
        elif (self.hocSinhYeu()):
          return danh_hieu['Y']
        else:
          return danh_hieu['Kem']
          
      case 'TB':
        if (self.hocSinhTB()):
          return danh_hieu['TB']
        elif (self.hocSinhYeu()):
          return danh_hieu['Y']
        else:
          return danh_hieu['Kem']
          
      case 'Y':
        if (self.hocSinhYeu()):
          return danh_hieu['Y']
        else:
          return danh_hieu['Kem']
          
      case 'Kem':
        return danh_hieu['Kem']
      
      case other:
        return "Danh hiệu không hợp lệ."

  def __str__(self):
    return ("MSSV: " + str(self.MSSV) + 
            "\nten: " + str(self.ten) + 
            "\ndiemToan: " + str(self.diemToan) + 
            "\ndiemVan: " + str(self.diemVan) + 
            "\ndiemAnh: " + str(self.diemAnh) + 
            "\nhanhKiem: " + str(self.hanhKiem) + 
            "\nDTB: " + str(self.DTB) + 
            "\ndanhHieu: " + str(self.danhHieu))
  
  def hocSinhGioi(self) :
    if (self.DTB >= 8.0 and self.diemToan >= 6.5 and self.diemVan >= 6.5 and 
        self.diemAnh >= 6.5):
      return True
    return False

  def hocSinhKha(self) :
    if (self.DTB >= 6.5 and self.diemToan >= 5.0 and self.diemVan >= 5.0 and 
        self.diemAnh >= 5.0):
      return True
    return False
  
  def hocSinhTB(self) :
    if (self.DTB >= 5.0 and self.diemToan >= 3.5 and self.diemVan >= 3.5 and 
        self.diemAnh >= 3.5):
      return True
    return False
  
  def hocSinhYeu(self) :
    if (self.DTB >= 3.5 and self.diemToan >= 2.0 and self.diemVan >= 2.0 and 
        self.diemAnh >= 2.0):
      return True
    return False
    
danh_hieu = {
  'G': "Học sinh giỏi",
  'K': "Học sinh khá",
  'TB': "Học sinh trung bình",
  'Y': "Học sinh yếu",
  'Kem': "Học sinh kém"
}

hanh_kiem = {
  'T': "Tốt",
  'K': "Khá",
  'TB': "Trung bình",
  'Y': "Yếu",
  'Kem': "Kém"
}

