class Student:
  def __init__(self, MSHS, ten, diemToan, diemVan, diemAnh, 
               hanhKiem):
    self.MSHS = MSHS
    self.ten = ten
    self.diemToan = float(diemToan)
    self.diemVan = float(diemVan)
    self.diemAnh = float(diemAnh)
    self.hanhKiem = hanhKiem
    self.DTB = self.calculateDTB()
    self.danhHieu = self.handleDanhHieu()

  def update(self, ten, diemToan, diemVan, diemAnh, 
             hanhKiem):
    self.ten = ten
    self.diemToan = float(diemToan)
    self.diemVan = float(diemVan)
    self.diemAnh = float(diemAnh)
    self.hanhKiem = hanhKiem
    self.DTB = self.calculateDTB()
    self.danhHieu = self.handleDanhHieu()

  def calculateDTB(self):
    return round(((self.diemToan + self.diemVan + 
                   self.diemAnh) / 3), 2)

  def handleDanhHieu(self):
    match self.hanhKiem:
      case 'T':
        if (self.hocSinhGioi()):
          return 'G'
        elif (self.hocSinhKha()):
          return 'K'
        elif (self.hocSinhTB()):
          return 'TB'
        elif (self.hocSinhYeu()):
          return 'Y'
        else:
          return 'Kem'
          
      case 'K':
        if (self.hocSinhKha()):
          return 'K'
        elif (self.hocSinhTB()):
          return 'TB'
        elif (self.hocSinhYeu()):
          return 'Y'
        else:
          return 'Kem'
          
      case 'TB':
        if (self.hocSinhTB()):
          return 'TB'
        elif (self.hocSinhYeu()):
          return 'Y'
        else:
          return 'Kem'
          
      case 'Y':
        if (self.hocSinhYeu()):
          return 'Y'
        else:
          return 'Kem'
          
      case 'Kem':
        return 'Kem'
      
      case other:
        return "Danh hiệu không hợp lệ."

  def __str__(self):
    return ("|  %-12s   %-18s   %-10s   %-10s   %-10s   %-11s   %-4s   %-23s |" % 
            (str(self.MSHS), str(self.ten), str(self.diemToan), str(self.diemVan), 
             str(self.diemAnh), str(hanh_kiem[self.hanhKiem]), str(self.DTB), 
             str(danh_hieu[self.danhHieu])))
  
  def hocSinhGioi(self) :
    if (self.DTB >= 8.0 and self.diemToan >= 6.5 and 
        self.diemVan >= 6.5 and 
        self.diemAnh >= 6.5):
      return True
    return False

  def hocSinhKha(self) :
    if (self.DTB >= 6.5 and self.diemToan >= 5.0 and 
        self.diemVan >= 5.0 and 
        self.diemAnh >= 5.0):
      return True
    return False
  
  def hocSinhTB(self) :
    if (self.DTB >= 5.0 and self.diemToan >= 3.5 and 
        self.diemVan >= 3.5 and 
        self.diemAnh >= 3.5):
      return True
    return False
  
  def hocSinhYeu(self) :
    if (self.DTB >= 3.5 and self.diemToan >= 2.0 and 
        self.diemVan >= 2.0 and 
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

