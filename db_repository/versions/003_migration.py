from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
category = Table('category', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('genre', String(length=50)),
    Column('age_cat', String(length=50)),
    Column('category', String(length=50)),
)

customer = Table('customer', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('cust_username', String(length=100)),
    Column('cust_password', String(length=32)),
    Column('cust_firstname', String(length=100)),
    Column('cust_lastname', String(length=50)),
    Column('cust_address', Text),
    Column('cust_shipping_address', Text),
    Column('cust_city', String(length=100)),
    Column('cust_postal', String(length=5)),
    Column('cust_email', String(length=100)),
    Column('cust_phone', String(length=50)),
)

order_detail = Table('order_detail', post_meta,
    Column('order_id', Integer, primary_key=True, nullable=False),
    Column('order_qty', Integer),
    Column('product_color', String(length=255)),
)

orders = Table('orders', post_meta,
    Column('order_id', Integer, primary_key=True, nullable=False),
    Column('payment_id', Integer),
    Column('order_timeStamp', DateTime),
    Column('transaction_status', String(length=100)),
    Column('order_paid', String(length=50)),
    Column('order_paymentDate', Date),
)

payment = Table('payment', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('payment_method', String(length=255)),
    Column('is_allowed', SmallInteger),
)

shipper = Table('shipper', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('shipper_name', String(length=100)),
    Column('shipper_address', String(length=255)),
    Column('shipper_cost', Float),
    Column('shipper_phone', String(length=100)),
)

tenant = Table('tenant', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('tenant_name', String(length=100)),
    Column('tenant_address', String(length=255)),
    Column('tenant_desc', Text),
    Column('tenant_phone', String(length=50)),
    Column('tenant_city', String(length=100)),
    Column('tenant_postal_code', String(length=5)),
)

product = Table('product', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('cat_id', Integer),
    Column('prod_name', String),
    Column('prod_price', Float),
    Column('prod_stock', Integer),
    Column('prod_image', Text),
    Column('add_date', Date),
    Column('prod_desc', Text),
)

product = Table('product', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('prod_name', String(length=100)),
    Column('prod_price', Float),
    Column('prod_size', String(length=3)),
    Column('prod_stock', Integer),
    Column('prod_discount', Float),
    Column('prod_image_main', Text),
    Column('prod_image_front', Text),
    Column('prod_image_back', Text),
    Column('prod_image_side', Text),
    Column('add_date', Date),
    Column('prod_desc', UnicodeText),
)

user = Table('user', pre_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String),
    Column('password', String),
    Column('email', String),
    Column('shop_name', String),
    Column('is_active', SmallInteger),
    Column('is_admin', SmallInteger),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=100)),
    Column('password', String(length=32)),
    Column('first_name', String(length=100)),
    Column('last_name', String(length=50)),
    Column('email', String(length=100)),
    Column('tenant_id', String(length=255)),
    Column('user_address', Text),
    Column('is_admin', SmallInteger),
    Column('is_staff', SmallInteger),
    Column('is_active', SmallInteger),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['category'].create()
    post_meta.tables['customer'].create()
    post_meta.tables['order_detail'].create()
    post_meta.tables['orders'].create()
    post_meta.tables['payment'].create()
    post_meta.tables['shipper'].create()
    post_meta.tables['tenant'].create()
    pre_meta.tables['product'].columns['cat_id'].drop()
    pre_meta.tables['product'].columns['prod_image'].drop()
    post_meta.tables['product'].columns['prod_discount'].create()
    post_meta.tables['product'].columns['prod_image_back'].create()
    post_meta.tables['product'].columns['prod_image_front'].create()
    post_meta.tables['product'].columns['prod_image_main'].create()
    post_meta.tables['product'].columns['prod_image_side'].create()
    post_meta.tables['product'].columns['prod_size'].create()
    pre_meta.tables['user'].columns['shop_name'].drop()
    post_meta.tables['user'].columns['first_name'].create()
    post_meta.tables['user'].columns['is_staff'].create()
    post_meta.tables['user'].columns['last_name'].create()
    post_meta.tables['user'].columns['tenant_id'].create()
    post_meta.tables['user'].columns['user_address'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['category'].drop()
    post_meta.tables['customer'].drop()
    post_meta.tables['order_detail'].drop()
    post_meta.tables['orders'].drop()
    post_meta.tables['payment'].drop()
    post_meta.tables['shipper'].drop()
    post_meta.tables['tenant'].drop()
    pre_meta.tables['product'].columns['cat_id'].create()
    pre_meta.tables['product'].columns['prod_image'].create()
    post_meta.tables['product'].columns['prod_discount'].drop()
    post_meta.tables['product'].columns['prod_image_back'].drop()
    post_meta.tables['product'].columns['prod_image_front'].drop()
    post_meta.tables['product'].columns['prod_image_main'].drop()
    post_meta.tables['product'].columns['prod_image_side'].drop()
    post_meta.tables['product'].columns['prod_size'].drop()
    pre_meta.tables['user'].columns['shop_name'].create()
    post_meta.tables['user'].columns['first_name'].drop()
    post_meta.tables['user'].columns['is_staff'].drop()
    post_meta.tables['user'].columns['last_name'].drop()
    post_meta.tables['user'].columns['tenant_id'].drop()
    post_meta.tables['user'].columns['user_address'].drop()
