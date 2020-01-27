from app import app
from db_config import mysql
from flask import jsonify
from flask import request


@app.route('/')
def test():
    return "Estás ligado!"


# --------------- ADICIONAR REGISTOS À TABELA ---------------------


@app.route('/addcasa', methods=['POST'])
def add_casa():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _num_divisoes = _json['num_divisoes']
        _garagem = _json['garagem']

        if _num_divisoes and _garagem and request.method == 'POST':
            sql = "INSERT INTO casa(num_divisoes, garagem) VALUES (%s, %s)"
            data = (_num_divisoes, _garagem)
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Casa adicionada com sucesso!')
            resp.status_code = 200
            return resp
        else:
            resp1 = jsonify('Ocorreu um erro ao adicionar a Casa!')
            return resp1
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# ------------------ VER TODOS OS REGISTOS DA TABELA ----------


@app.route('/casas')
def casas():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM casa")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# -------------- VER REGISTO EXPECIFICO --------------------------------


@app.route('/casa/<int:id>')
def casa(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    try:

        cursor.execute("SELECT * FROM casa WHERE id_casa=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# -------------------------- ALTERAR REGISTO ---------------------


@app.route('/updatecasa', methods=['POST'])
def update_casa():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _id_casa = _json['id_casa']
        _num_divisoes = _json['num_divisoes']
        _garagem = _json['garagem']
        # validar valores recebidos
        if _num_divisoes and _garagem and _id_casa and request.method == 'POST':
            sql = "UPDATE casa SET num_divisoes=%s, garagem=%s WHERE id_casa=%s"
            data = (_num_divisoes, _garagem, _id_casa,)

            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Registo alterado com sucesso')
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

# ----------------- APAGAR REGISTO ----------------------

@app.route('/deletecasa/<int:id>')
def delete_casa(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    try:

        cursor.execute("DELETE FROM casa WHERE id_casa=%s", (id,))
        conn.commit()
        resp = jsonify('registo apagado com sucesso!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


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