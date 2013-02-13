from app import db

ROLE_USER = 0
ROLE_ADMIN = 1

class Product(db.Model):
    '''
        Detail untuk tabel produk
    '''
    id = db.Column(db.Integer, primary_key = True)
    cat_id = db.Column(db.Integer, index=True)
    prod_name = db.Column(db.String(100), index=True)
    prod_price = db.Column(db.Float, index=True)
    prod_size = db.Column(db.String(3), index=True)
    prod_stock = db.Column(db.Integer, index=True)
    prod_discount = db.Column(db.Float, index=True)
    prod_image_main = db.Column(db.Text, index=True)
    prod_image_front = db.Column(db.Text, index=True)
    prod_image_back = db.Column(db.Text, index=True)
    prod_image_side = db.Column(db.Text, index=True)
    add_date = db.Column(db.Date, index=True)
    prod_desc = db.Column(db.UnicodeText, index=True)
    add_user = db.Column(db.Integer, index=True)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), index=True)
    password = db.Column(db.String(32), index=True)
    first_name = db.Column(db.String(100), index=True)
    last_name = db.Column(db.String(50), index=True)
    email = db.Column(db.String(100), index=True)
    tenant_id = db.Column(db.String(255), index=True)
    user_tenant = db.Column(db.Integer, index=True)
    user_address = db.Column(db.Text, index=True)
    is_admin = db.Column(db.SmallInteger, index=True)
    is_staff = db.Column(db.SmallInteger, index=True)
    is_active = db.Column(db.SmallInteger, index=True)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat_name = db.Column(db.String(50), index=True)

class Tenant(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    tenant_name = db.Column(db.String(100), index=True)
    tenant_address = db.Column(db.String(255), index=True)
    tenant_desc = db.Column(db.Text, index=True)
    tenant_phone = db.Column(db.String(50), index=True)
    tenant_city = db.Column(db.String(100), index=True)
    tenant_postal_code = db.Column(db.String(5), index=True)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cust_username = db.Column(db.String(100), index=True)
    cust_password = db.Column(db.String(32), index=True)
    cust_firstname = db.Column(db.String(100), index=True)
    cust_lastname = db.Column(db.String(50), index=True)
    cust_address = db.Column(db.Text, index=True)
    cust_shipping_address = db.Column(db.Text, index=True)
    cust_city = db.Column(db.String(100), index=True)
    cust_postal = db.Column(db.String(5), index=True)
    cust_email = db.Column(db.String(100), index=True)
    cust_phone = db.Column(db.String(50), index=True)

class Orders(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    cust_id = db.Column(db.Integer, index=True)
    order_detailId = db.Column(db.Integer, index=True)
    payment_id = db.Column(db.Integer, index=True)
    order_timeStamp = db.Column(db.DateTime, index=True)
    transaction_status = db.Column(db.String(100), index=True)
    order_paid = db.Column(db.String(50), index=True)
    order_paymentDate = db.Column(db.Date, index=True)
    order_paymentMethode = db.Column(db.Integer, index=True)
    shipper_id = db.Column(db.Integer, index=True)

class OrderDetail(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, index=True)
    order_qty = db.Column(db.Integer, index=True)
    product_color = db.Column(db.String(255), index=True)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    payment_method = db.Column(db.String(255), index=True)
    is_allowed = db.Column(db.SmallInteger, index=True)

class Shipper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    shipper_name = db.Column(db.String(100), index=True)
    shipper_address = db.Column(db.String(255), index=True)
    shipper_cost = db.Column(db.Float, index=True)
    shipper_phone = db.Column(db.String(100), index=True)


