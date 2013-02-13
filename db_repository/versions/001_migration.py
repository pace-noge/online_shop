from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
product = Table('product', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('cat_id', Integer),
    Column('prod_name', String(length=100)),
    Column('prod_price', Float),
    Column('prod_stock', Integer),
    Column('prod_image', Text),
    Column('add_date', Date),
    Column('prod_desc', UnicodeText),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=100)),
    Column('password', String(length=32)),
    Column('email', String(length=100)),
    Column('shop_name', String(length=255)),
    Column('is_active', SmallInteger),
    Column('is_admin', SmallInteger),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['product'].create()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['product'].drop()
    post_meta.tables['user'].drop()
