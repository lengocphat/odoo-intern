from openerp.osv import fields, osv
class SinhVien(osv.osv):
    _name = "sinhvien"
    _columns = {
        'name':fields.char('Ho Ten'),
        'ngaysinh':fields.date('Ngay Sinh'),
        'masv':fields.char('MSSV'),
        'gioitinh':fields.char('Gioi Tinh'),
        'diachi':fields.char('Dia Chi'),
        'sotinchinomon':fields.integer('So TC No Mon'),
        'm2m':fields.many2many('monhoc','rel_m2m',string='Many2Many'),
        'tugas':fields.many2many('ir.attachment','rel_tugas',string='Tugas')
    }
class monhoc(osv.osv):
    _name = "monhoc"
    _rec_name = "tenmh"
    _columns = {
        'id':fields.integer('ID'),
        'mamh':fields.char('Ma Mon Hoc'),
        'tenmh':fields.text('Ten Mon Hoc'),
        'sotinchi':fields.integer('So Tin Chi'),
    }
