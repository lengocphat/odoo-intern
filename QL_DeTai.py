from openerp.osv import osv, fields

class ql_de_tai(osv.osv):
    _name = 'ql.detai'
    _columns = {
        'ten': fields.char('Ten mon hoc '),
        'sotiet': fields.integer('So tiet '),
        'songuoi': fields.integer('So nguoi dang ki '),
        'ghichu': fields.char('Ghi chu '),
        'ngaybatdau': fields.date('Ngay bat dau '),
        'ngayketthuc': fields.date('Ngay ket thuc '),
        'nhanvien': fields.many2many('hr.employee',string='Chon nhan vien',invertse="name")
    }
