from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
order_detail = Table('order_detail', post_meta,
    Column('order_id', Integer, primary_key=True, nullable=False),
    Column('product_id', Integer),
    Column('order_qty', Integer),
    Column('product_color', String(length=255)),
)

product = Table('product', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('cat_id', Integer),
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
    Column('add_user', Integer),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=100)),
    Column('password', String(length=32)),
    Column('first_name', String(length=100)),
    Column('last_name', String(length=50)),
    Column('email', String(length=100)),
    Column('tenant_id', String(length=255)),
    Column('user_tenant', Integer),
    Column('user_address', Text),
    Column('is_admin', SmallInteger),
    Column('is_staff', SmallInteger),
    Column('is_active', SmallInteger),
)

orders = Table('orders', post_meta,
    Column('order_id', Integer, primary_key=True, nullable=False),
    Column('cust_id', Integer),
    Column('order_detailId', Integer),
    Column('payment_id', Integer),
    Column('order_timeStamp', DateTime),
    Column('transaction_status', String(length=100)),
    Column('order_paid', String(length=50)),
    Column('order_paymentDate', Date),
    Column('order_paymentMethode', Integer),
    Column('shipper_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['order_detail'].columns['product_id'].create()
    post_meta.tables['product'].columns['add_user'].create()
    post_meta.tables['product'].columns['cat_id'].create()
    post_meta.tables['user'].columns['user_tenant'].create()
    post_meta.tables['orders'].columns['cust_id'].create()
    post_meta.tables['orders'].columns['order_detailId'].create()
    post_meta.tables['orders'].columns['order_paymentMethode'].create()
    post_meta.tables['orders'].columns['shipper_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['order_detail'].columns['product_id'].drop()
    post_meta.tables['product'].columns['add_user'].drop()
    post_meta.tables['product'].columns['cat_id'].drop()
    post_meta.tables['user'].columns['user_tenant'].drop()
    post_meta.tables['orders'].columns['cust_id'].drop()
    post_meta.tables['orders'].columns['order_detailId'].drop()
    post_meta.tables['orders'].columns['order_paymentMethode'].drop()
    post_meta.tables['orders'].columns['shipper_id'].drop()
