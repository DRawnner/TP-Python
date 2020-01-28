from app import app
from db_config import mysql
from flask import jsonify
from flask import request


@app.route('/')
def test():
    return "Estás ligado!"


# --------------- TABELA CASA ---------------------


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
            resp = jsonify('registo adicionado com sucesso!')
            resp.status_code = 200
            return resp
        else:
            resp1 = jsonify('Ocorreu um erro ao adicionar o registo!')
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


# ----------------- TABELA TELEVISAO --------------

# --------------- ADICIONAR REGISTOS À TABELA ---------------------

@app.route('/addtv', methods=['POST'])
def add_tv():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _id_casa_tv = _json['id_casa_tv']
        _consumo = _json['consumo']
        _descricao = _json['descricao']

        if _id_casa_tv and _consumo and _descricao and request.method == 'POST':
            sql = "INSERT INTO televisao(id_casa_tv, consumo, descricao) VALUES (%s, %s, %s)"
            data = (_id_casa_tv, _consumo, _descricao)
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('resgisto adicionado com sucesso!')
            resp.status_code = 200
            return resp
        else:
            resp1 = jsonify('Ocorreu um erro ao adicionar o registo!')
            return resp1
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# ------------------ VER TODOS OS REGISTOS DA TABELA ----------

@app.route('/tvs')
def tvs():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM televisao")
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


@app.route('/tv/<int:id>')
def tv(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    try:

        cursor.execute("SELECT * FROM televisao WHERE id_tv=%s", id)
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


@app.route('/updatetv', methods=['POST'])
def update_tv():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _id_tv = _json['id_tv']
        _id_casa_tv = _json['id_casa_tv']
        _consumo = _json['consumo']
        _descricao = _json['descricao']
        # validar valores recebidos
        if _id_casa_tv and _consumo and _descricao and _id_tv and request.method == 'POST':
            sql = "UPDATE televisao SET id_casa_tv=%s, consumo=%s, descricao=%s WHERE id_tv=%s"
            data = (_id_casa_tv, _consumo, _descricao, _id_tv)

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


@app.route('/deletetv/<int:id>')
def delete_tv(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    try:

        cursor.execute("DELETE FROM televisao WHERE id_tv=%s", (id,))
        conn.commit()
        resp = jsonify('registo apagado com sucesso!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# ------------------ TABELA CONTADOR ----------------------

# --------------- ADICIONAR REGISTOS À TABELA ---------------------

@app.route('/addcontador', methods=['POST'])
def add_contador():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _tipo_contador = _json['tipo_contador']
        _descricao = _json['descricao']

        if _tipo_contador and _descricao and request.method == 'POST':
            sql = "INSERT INTO contador(tipo_contador, descricao) VALUES (%s, %s)"
            data = (_tipo_contador, _descricao)
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('resgisto adicionado com sucesso!')
            resp.status_code = 200
            return resp
        else:
            resp1 = jsonify('Ocorreu um erro ao adicionar o registo!')
            return resp1
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# ------------------ VER TODOS OS REGISTOS DA TABELA ----------

@app.route('/contadores')
def contadores():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM contador")
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

@app.route('/contador/<int:id>')
def contador(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    try:

        cursor.execute("SELECT * FROM contador WHERE id_contador=%s", id)
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


@app.route('/updatecontador', methods=['POST'])
def update_contador():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _id_contador = _json['id_contador']
        _tipo_contador = _json['tipo_contador']
        _descricao = _json['descricao']
        # validar valores recebidos
        if _tipo_contador and _descricao and _id_contador and request.method == 'POST':
            sql = "UPDATE contador SET tipo_contador=%s, descricao=%s WHERE id_contador=%s"
            data = (_tipo_contador, _descricao, _id_contador,)

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


@app.route('/deletecontador/<int:id>')
def delete_contador(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    try:

        cursor.execute("DELETE FROM contador WHERE id_contador=%s", (id,))
        conn.commit()
        resp = jsonify('registo apagado com sucesso!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# --------------- TABELA REGISTO ---------------------------------

# --------------- ADICIONAR REGISTOS À TABELA ---------------------

@app.route('/addregisto', methods=['POST'])
def add_registo():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _id_contador = _json['id_contador']
        _id_casa_registo = _json['id_casa_registo']
        _valor = _json['valor']

        if _id_contador and _id_casa_registo and _valor and request.method == 'POST':
            sql = "INSERT INTO registo_consumo(id_contador, id_casa_registo, valor ) VALUES (%s, %s, %s)"
            data = (_id_contador, _id_casa_registo, _valor)
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Registo adicionado com sucesso!')
            resp.status_code = 200
            return resp
        else:
            resp1 = jsonify('Ocorreu um erro ao adicionar o registo!')
            return resp1
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# ------------------ VER TODOS OS REGISTOS DA TABELA ----------

@app.route('/registos')
def registos():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM registo_consumo")
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

@app.route('/registo/<int:id>')
def registo(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    try:

        cursor.execute("SELECT * FROM registo_consumo WHERE id_registo_consumo=%s", id)
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

@app.route('/updateregisto', methods=['POST'])
def update_registo():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _id_registo_consumo = _json['id_registo_consumo']
        _id_contador = _json['id_contador']
        _id_casa_registo = _json['id_casa_registo']
        _valor = _json['valor']
        # validar valores recebidos
        if _id_contador and _id_casa_registo and _valor and _id_registo_consumo and request.method == 'POST':
            sql = "UPDATE registo_consumo SET id_contador=%s, id_casa_registo=%s, valor=%s WHERE id_registo_consumo=%s"
            data = (_id_contador, _id_casa_registo, _valor, _id_registo_consumo)

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


@app.route('/deleteregisto/<int:id>')
def delete_registo(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    try:

        cursor.execute("DELETE FROM registo_consumo WHERE id_registo_consumo=%s", (id,))
        conn.commit()
        resp = jsonify('registo apagado com sucesso!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# ------------------- TABELA AR CONDICIONADO -------------------------------


# --------------- ADICIONAR REGISTOS À TABELA ---------------------

@app.route('/addar', methods=['POST'])
def add_ar():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _id_casa_ar = _json['id_casa_ar']
        _temperatura = _json['temperatura']
        _consumo = _json['consumo']
        _humidade = _json['humidade']
        _descricao = _json['descricao']

        if _id_casa_ar and _temperatura and _consumo and _humidade and _descricao and request.method == 'POST':
            sql = "INSERT INTO ar_condicionado(id_casa_ar, temperatura, consumo, humidade, descricao ) VALUES (%s, %s, %s, %s, %s)"
            data = (_id_casa_ar, _temperatura, _consumo, _humidade, _descricao)
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Registo adicionado com sucesso!')
            resp.status_code = 200
            return resp
        else:
            resp1 = jsonify('Ocorreu um erro ao adicionar o registo!')
            return resp1
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# ------------------ VER TODOS OS REGISTOS DA TABELA ----------

@app.route('/ares')
def ares():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM ar_condicionado")
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

@app.route('/ar/<int:id>')
def ar(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    try:

        cursor.execute("SELECT * FROM ar_condicionado WHERE id_ar_condicionado=%s", id)
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

@app.route('/updatear', methods=['POST'])
def update_ar():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _id_ar_condicionado = _json['id_ar_condicionado']
        _id_casa_ar = _json['id_casa_ar']
        _temperatura = _json['temperatura']
        _consumo = _json['consumo']
        _humidade = _json['humidade']
        _descricao = _json['descricao']

        # validar valores recebidos
        if _id_casa_ar and _temperatura and _consumo and _humidade and _descricao and _id_ar_condicionado and request.method == 'POST':
            sql = "UPDATE ar_condicionado SET id_casa_ar=%s, temperatura=%s, consumo=%s, humidade=%s, descricao=%s WHERE id_ar_condicionado=%s"
            data = (_id_casa_ar, _temperatura, _consumo, _humidade, _descricao, _id_ar_condicionado)

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


@app.route('/deletear/<int:id>')
def delete_ar(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    try:

        cursor.execute("DELETE FROM ar_condicionado WHERE id_ar_condicionado=%s", (id,))
        conn.commit()
        resp = jsonify('registo apagado com sucesso!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# ----------------------- TABELA PORTA PRINCIPAL

# --------------- ADICIONAR REGISTOS À TABELA ---------------------


@app.route('/addporta', methods=['POST'])
def add_porta():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _id_casa_porta = _json['id_casa_porta']

        if _id_casa_porta and request.method == 'POST':
            sql = "INSERT INTO porta_principal(id_casa_porta) VALUES (%s)"
            data = (_id_casa_porta)
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Registo adicionado com sucesso!')
            resp.status_code = 200
            return resp
        else:
            resp1 = jsonify('Ocorreu um erro ao adicionar registo!')
            return resp1
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# ------------------ VER TODOS OS REGISTOS DA TABELA ----------

@app.route('/portas')
def portas():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM porta_principal")
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


@app.route('/porta/<int:id>')
def porta(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    try:

        cursor.execute("SELECT * FROM porta_principal WHERE id_porta_principal=%s", id)
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


@app.route('/updateporta', methods=['POST'])
def update_porta():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _id_porta_principal = _json['id_porta_principal']
        _id_casa_porta = _json['id_casa_porta']
        # validar valores recebidos
        if _id_casa_porta and _id_porta_principal and request.method == 'POST':
            sql = "UPDATE porta_principal SET id_casa_porta=%s WHERE id_porta_principal=%s"
            data = (_id_casa_porta , _id_porta_principal ,)

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


@app.route('/deleteporta/<int:id>')
def delete_porta(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    try:

        cursor.execute("DELETE FROM porta_principal WHERE id_porta_principal=%s", (id,))
        conn.commit()
        resp = jsonify('registo apagado com sucesso!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# ------------------ TABELA GARAGEM --------------


# --------------- ADICIONAR REGISTOS À TABELA ---------------------


@app.route('/addgaragem', methods=['POST'])
def add_garagem():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _id_casa_garagem = _json['id_casa_garagem']

        if _id_casa_garagem and request.method == 'POST':
            sql = "INSERT INTO garagem(id_casa_garagem) VALUES (%s)"
            data = (_id_casa_garagem)
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify('Registo adicionado com sucesso!')
            resp.status_code = 200
            return resp
        else:
            resp1 = jsonify('Ocorreu um erro ao adicionar registo!')
            return resp1
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


# ------------------ VER TODOS OS REGISTOS DA TABELA ----------

@app.route('/garagens')
def garagens():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM garagem")
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


@app.route('/garagem/<int:id>')
def garagem(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    try:

        cursor.execute("SELECT * FROM garagem WHERE id_garagem=%s", id)
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


@app.route('/updategaragem', methods=['POST'])
def update_garagem():
    conn = mysql.connect()
    cursor = conn.cursor()
    try:
        _json = request.json
        _id_garagem = _json['id_garagem']
        _id_casa_garagem = _json['id_casa_garagem']
        # validar valores recebidos
        if _id_casa_garagem and _id_garagem and request.method == 'POST':
            sql = "UPDATE garagem SET id_casa_garagem=%s WHERE id_garagem=%s"
            data = (_id_casa_garagem, _id_garagem)

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


@app.route('/deletegaragem/<int:id>')
def delete_garagem(id):
    conn = mysql.connect()
    cursor = conn.cursor()
    try:

        cursor.execute("DELETE FROM garagem WHERE id_garagem=%s", (id,))
        conn.commit()
        resp = jsonify('registo apagado com sucesso!')
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()









# ---------------------------- ERROR HANDLER ------------------------


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
