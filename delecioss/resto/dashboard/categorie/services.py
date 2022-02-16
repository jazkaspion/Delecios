from collections import OrderedDict
from contextlib import closing

from django.db import connection

from base.db import dict_fetchall, dict_fetchone


def cat_list():
    sql = "select * from recipe_category"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        result = []
        for i in dict_fetchall(cursor):
            result.append(_format(i))

    return result


def cat_one(pk):
    sql = "select * from recipe_category where id=%s"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [pk])
        data = dict_fetchone(cursor)
        if data:
            result = _format(data)
        else:
            result = None

    return result


def cat_rec_delete(ctg_id):
    sql = "delete from recipe_recipe where ctg_id=%s"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [ctg_id])


def cat_delete(pk):
    sql = "delete from recipe_category where id=%s"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [pk])


def _format(data):
    return  OrderedDict([
        ('id', data['id']),
        ('slug', data['slug']),
        ('content', data['content'])
    ])