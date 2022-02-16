
def dict_fetchall(cursor):
    columns = [i[0] for i in cursor.description]
    return [
        dict(zip(columns, row)) for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    root = cursor.fetchone()
    if root is None:
        return None
    columns = [i[0] for i in cursor.description]
    return dict(zip(columns, root))