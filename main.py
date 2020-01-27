from app import app
from db_config import mysql
from flask import jsonify
from flask import request


@app.route('/')
def test():
    return "Estás ligado!"


@app.route('/adduser', methods=['POST'])
def add_user():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _user_name = _json['user_name']
        _user_email = _json['user_email']
        _user_password = _json['user_password']

        if _user_name and _user_email and _user_password and request.method == 'POST':
            sql = "INSERT INTO tbl_user(user_name, user_email, user_password) VALUES (%s, %s, %s)"
            data = (_user_name, _user_email, _user_password)
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Sala adicionada com sucesso!')
            resp.status_code = 200
            return resp
        else:
            resp1 = jsonify('Ocorreu um erro ao adicionar a sala!')
            return resp1
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()
        return 'Teste'


@app.route('/users')
def users():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM tbl_user")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#
@app.route('/user/<int:id>')
def user(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    try:

        cursor.execute("SELECT * FROM tbl_user WHERE user_id=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route('/update', methods=['POST'])
def update_user():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _user_id = _json['user_id']
        _user_name = _json['user_name']
        _user_email = _json['user_email']
        _user_password = _json['user_password']
        # validate the received values
        if _user_name and _user_email and _user_password and _user_id and request.method == 'POST':
            sql = "UPDATE tbl_user SET user_name=%s, user_email=%s, user_password=%s WHERE user_id=%s"
            data = (_user_name, _user_email, _user_password, _user_id,)

            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('User updated successfully!')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

#
# @app.route('/delete/<int:id>')
# def delete_user(id):
#     conn = pymysql.connect()
#     cursor = conn.cursor()
#     try:
#
#         cursor.execute("DELETE FROM tbl_user WHERE user_id=%s", (id,))
#         conn.commit()
#         resp = jsonify('User deleted successfully!')
#         resp.status_code = 200
#         return resp
#     except Exception as e:
#         print(e)
#     finally:
#         cursor.close()
#         conn.close()


@app.errorhandler(404)
def not_found(error=None):
    message = {
        'status': 404,
        'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == "__main__":
    app.run()