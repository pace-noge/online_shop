from flask.ext.wtf import Form, TextField, BooleanField, FileField, SelectField, TextAreaField
from flask.ext.wtf import Required
#from flask.ext.uploads import UploadSet, IMAGES
from models import Category


class TambahBarang(Form):
    
    pilih_kategori = Category.query.all()
    isi_kategri = [(unicode(x.id), unicode(x.cat_name)) for x in pilih_kategori]
    barang = TextField('barang', validators = [Required()])
    harga = TextField('harga', validators = [Required()])
    stock = TextField('stock', validators=[Required()])
    desc = TextAreaField('desc')
    disc = TextField('disc', validators=[Required()])
    img_front= FileField('gambarDpn')
    img_back= FileField('gambarBlkg')
    img_side= FileField('gambarSamping')
    img_main= FileField('gambarUtama')
    warna = SelectField('warna', choices=[('Merah', 'Merah'), ('Biru', 'Biru'), ('Hitam', 'hitam')])
    kategori = SelectField('category', choices=isi_kategri)

class RegTenant(Form):
	tenant_name = TextField('nmTenant', validators=[Required])
	tenant_address  =  TextAreaField('almtTenant', validators=[Required])
	tenant_phone = TextField('tlpTenant')
	tenant_email = TextField('emailTenant')
	tenant_desc = TextAreaField('descTenant')

class TambahKategori(Form):
    category = TextField('category', validators=[Required()])




