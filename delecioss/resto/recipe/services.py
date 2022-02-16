from contextlib import closing

from django.db import connection
from typing_extensions import OrderedDict

from base.db import dict_fetchall, dict_fetchone


def get_recipes_all():
    sql = "select * from recipe_category"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        result = []
        for i in dict_fetchall(cursor):
            result.append(_format(i))

    return result


def get_recipes_one(pk):
    sql = "select * from recipe_category where id=%s"
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [pk])
        data = dict_fetchone(cursor)
        if data:
            result = _format(data)
        else:
            result = None

    return result


def _format(data):
    return OrderedDict([
        ('id', data['id']),
        ('s', data['slug']),
        ('c', data['content']),
    ])





