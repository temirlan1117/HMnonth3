import sqlite3
from db import  queries

db = sqlite3.connect('db/store.sqlite3')
cursor = db.cursor()


async def sql_create():
    if db:
        print('База данных подключена!')

    cursor.execute(queries.CREATE_TABLE_PRODUCTS)
    cursor.execute(queries.CREATE_TABLE_PRODUCT_DETAIL)
    cursor.execute(queries.CREATE_TABLE_COLLECTION_PRODUCTS)
    db.commit()


async def sql_insert_products(name_product, size, price, product_id, photo):
    cursor.execute(queries.INSERT_PRODUCTS_QUERY, (
        name_product,
        size,
        price,
        product_id,
        photo
    ))
    db.commit()

async def  insert_product_detail(productid, category, info_product):
    cursor.execute(queries.INSERT_INTO_PRODUCT_DETAIL,(
        productid,
        category,
        info_product
    ))
    db.commit()

async def insert_collection_products(product_id, collection):
    cursor.execute(queries.INSERT_COLLECTION_PRODUCTS, (
        product_id,
        collection
    ))
    db.commit()