from collections import OrderedDict
from contextlib import closing

from django.conf import settings
from django.db import connection

from base.db import dict_fetchall, dict_fetchone
from base.sqlpaginator import SqlPaginator


def cat_list(requests):
    try:
        page = int(requests.GET.get('page', 1))
    except:
        page = 1

    PER_PAGE = settings.PAGINATE_BY

    offset = PER_PAGE * (page-1)

    print(page, PER_PAGE)

    sql = """ 
    select * from recipe_category
    order by id 
    limit %s offset %s
    """
    with closing(connection.cursor()) as cursor:
        cursor.execute(sql, [PER_PAGE, offset])
        result = []
        for i in dict_fetchall(cursor):
            result.append(_format(i))
    with closing(connection.cursor()) as cursor:
        cursor.execute("select count(1) as cnt from recipe_category")
        cnt = dict_fetchone(cursor)['cnt']

    meta = SqlPaginator(requests, page=page, per_page=PER_PAGE, count=cnt)
    meta = meta.get_paginated_response(PER_PAGE, page)

    return OrderedDict([
        ('items', result),
        ('meta', meta)
    ])


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