# do not change or move the following lines if you still want to use the box.py auto generator
from app import app, db
from models import Product, Category
import os
# you can freely change the lines below
from flask import render_template
from flask import json
from flask import session
from flask import url_for
from flask import redirect
from flask import request
from flask import abort
from flask import Response
from flask import flash
import logging
from forms import TambahBarang, RegTenant, TambahKategori
# define global variables here

# home root controller
@app.route('/')
@app.route('/index')
def index():
	# define your controller here
    products = Product.query.all()
    return render_template('mainpage.html', title='Online Shopper', products = products)
	

def allowedFile(filename):
        return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIIONS

def pathGbr(nmfile):
    return os.path.join(app.config['UPLOAD_FOLDER'], nmfile)

@app.route('/tambahBarang', methods = ['GET', 'POST'])
def tambahBarang():
    form = TambahBarang()
    if form.validate_on_submit():
        gambar = { 'gbrdpn' : form.img_front.data, 'gbrblkg' : form.img_back.data, 'gbrsamping' : form.img_side.data, 
                 'gbrutama' : form.img_main.data }
        for gbr in gambar:

            gambar[gbr].save(pathGbr(form.barang.data.split('.')[0] + '_'+ gbr + '.' + gambar[gbr].filename.split('.')[1]))


        tambah = Product(prod_name=form.barang.data, prod_price=form.harga.data, prod_stock=form.stock.data, 
                  prod_discount=form.disc.data, prod_image_main=form.barang.data + '_gbrutama.' + gambar['gbrutama'].filename.split('.')[-1:][0], 
                  prod_image_front=form.barang.data + '_gbrdpn.' + gambar['gbrdpn'].filename.split('.')[-1:][0], 
                  prod_image_back=form.barang.data + '_gbrblkg.' + gambar['gbrblkg'].filename.split('.')[-1:][0], 
                  prod_image_side=form.barang.data + '_gbrsamping.' + gambar['gbrsamping'].filename.split(',')[-1:][0], prod_desc=form.desc.data)
        db.session.add(tambah)
        db.session.commit()
        flash('Barang sudah ditambahkan')
        return redirect(url_for('tambahBarang'))
    return render_template('tambahBarang.html', title='Tambah Barang', form=form)

@app.route('/tambahTenant', methods = ['GET', 'POST'])
def tambahTenant():
	form = RegTenant()
	return render_template('regTenant.html', title='Registrasi Tenant', form=form)

@app.route('/tambahKategori', methods = ['GET', 'POST'])
def tambahKategori():
    cat = Category.query.all()
    existCat = [x.cat_name for x in cat]
    form = TambahKategori()
    if form.validate_on_submit():
        kategori = Category(cat_name=form.category.data)
        db.session.add(kategori)
        db.session.commit()
        flash('Kategori sudah ditambahkan')
        return redirect(url_for('tambahKategori'))

    return render_template('tambahKategori.html', title='Tambah Kategori', form=form, existCat=existCat)

@app.route('/dataBarang')
def dataBarang():
    tes = "tes"

@app.route('/Product')
def product():
    products = Product.query.all()
    if products == None:
        products = "Produk untuk kategori ini belum ada, silahkan pilih kategori yang lain"

    return render_template('kategori.html', title='Kategori', products = products)


