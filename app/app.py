from typing import List, Dict
import simplejson as json
from flask import Flask, request, Response, redirect
from flask import render_template
from flaskext.mysql import MySQL
from pymysql.cursors import DictCursor

app = Flask(__name__)
mysql = MySQL(cursorclass=DictCursor)

app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_PORT'] = 3306
app.config['MYSQL_DATABASE_DB'] = 'citiesData'
mysql.init_app(app)


@app.route('/', methods=['GET'])
def index():
    user = {'username': 'Hurricanes Project'}
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblCitiesImport')
    result = cursor.fetchall()
    return render_template('index.html', title='Home', user=user, hurricanes=result)


@app.route('/view/<int:month_id>', methods=['GET'])
def record_view(month_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblCitiesImport WHERE id=%s', month_id)
    result = cursor.fetchall()
    return render_template('view.html', title='View Form', month=result[0])


@app.route('/edit/<int:month_id>', methods=['GET'])
def form_edit_get(month_id):
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblCitiesImport WHERE id=%s', month_id)
    result = cursor.fetchall()
    return render_template('edit.html', title='Edit Form', month=result[0])


@app.route('/edit/<int:month_id>', methods=['POST'])
def form_update_post(month_id):
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('fldMonth'), request.form.get('fldAvg'),
                 request.form.get('fld2005'), request.form.get('fld2006'),
                 request.form.get('fld2007'), request.form.get('fld2008'),
                 request.form.get('fld2009'), request.form.get('fld2010'),
                 request.form.get('fld2011'), request.form.get('fld2012'),
                 request.form.get('fld2013'), request.form.get('fld2014'),
                 request.form.get('fld2015'),
                 month_id)
    sql_update_query = """UPDATE tblCitiesImport t SET t.fldMonth = %s, t.fldAvg = %s, t.fld2005 = %s, t.fld2006 = %s, t.fld2007 = 
    %s, t.fld2008 = %s, t.fld2009 = %s, t.fld2010 = %s , t.fld2011 = %s, t.fld2012 = %s, t.fld2013 = %s, t.fld2014 = %s, t.fld2015 = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)

@app.route('/hurricanes/new', methods=['GET'])
def form_insert_get():
    return render_template('new.html', title='New Month Form')


@app.route('/hurricanes/new', methods=['POST'])
def form_insert_post():
    cursor = mysql.get_db().cursor()
    inputData = (request.form.get('fldMonth'), request.form.get('fldAvg'), request.form.get('2005'),
                 request.form.get('fld2006'), request.form.get('fld2007'),
                 request.form.get('fld2008'), request.form.get('fld2009'),
                 request.form.get('fld2010'), request.form.get('fld2011'),
                 request.form.get('fld2012'), request.form.get('fld2013'),
                 request.form.get('fld2014'), request.form.get('fld2015')
                 )
    sql_insert_query = """INSERT INTO tblCitiesImport (fldMonth,fldAvg,fld2005,fld2006,fld2007,fld2008,fld2009,fld2010,fld2011,fld2012,fld2013,fld2014,fld2015) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) """
    cursor.execute(sql_insert_query, inputData)
    mysql.get_db().commit()
    return redirect("/", code=302)

@app.route('/delete/<int:month_id>', methods=['POST'])
def form_delete_post(month_id):
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM tblCitiesImport WHERE month = %s """
    cursor.execute(sql_delete_query, month_id)
    mysql.get_db().commit()
    return redirect("/", code=302)


@app.route('/api/v1/hurricanes', methods=['GET'])
def api_browse() -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblCitiesImport')
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/hurricanes/<int:month_id>', methods=['GET'])
def api_retrieve(month_id) -> str:
    cursor = mysql.get_db().cursor()
    cursor.execute('SELECT * FROM tblCitiesImport WHERE id=%s', month_id)
    result = cursor.fetchall()
    json_result = json.dumps(result);
    resp = Response(json_result, status=200, mimetype='application/json')
    return resp


@app.route('/api/v1/hurricanes/', methods=['POST'])
def api_add() -> str:
    try:
        content = request.json
        cursor = mysql.get_db().cursor()
        inputData = (content['fldMonth'], content['fldAvg'], content['fld2005'],
                     content['fld2006'], content['fld2007'],
                     content['fld2008'], content['fld2009'],
                     content['fld2010'], content['fld2011'],
                     content['fld2012'], content['fld2013'],
                     content['fld2014'], content['fld2015']
                     )
        sql_insert_query = """INSERT INTO tblCitiesImport (fldName,fldLat,fldLong,fldCountry,fldAbbreviation,fldCapitalStatus,fldPopulation) VALUES (%s, %s,%s, %s,%s, %s,%s) """
        cursor.execute(sql_insert_query, inputData)
        mysql.get_db().commit()
        resp = Response(status=201, mimetype='application/json')
        return resp
    except:
        resp = Response(status=201, mimetype='application/json')
        return resp


@app.route('/api/v1/hurricanes/<int:month_id>', methods=['PUT'])
def api_edit(month_id) -> str:
    cursor = mysql.get_db().cursor()
    content = request.json
    inputData = (content['fldMonth'], content['fldAvg'], content['fld2005'],
                 content['fld2006'], content['fld2007'],
                 content['fld2008'], content['fld2009'],
                 content['fld2010'], content['fld2011'],
                 content['fld2012'], content['fld2013'],
                 content['fld2014'], content['fld2015'],month_id
                 )
    sql_update_query = """UPDATE tblCitiesImport t SET t.fldMonth = %s, t.fldAvg = %s, t.fld2005 = %s, t.fld2006 = 
            %s, t.fld2007 = %s, t.fld2008 = %s, t.fld2009 = %s, t.fld2010 = %s, t.fld2011 = %s, t.fld2012 = %s, t.fld2013 = %s, t.fld2014 = %s, t.fld2015 = %s WHERE t.id = %s """
    cursor.execute(sql_update_query, inputData)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp


@app.route('/api/hurricanes/<int:month_id>', methods=['DELETE'])
def api_delete(month_id) -> str:
    cursor = mysql.get_db().cursor()
    sql_delete_query = """DELETE FROM tblCitiesImport WHERE id = %s """
    cursor.execute(sql_delete_query, month_id)
    mysql.get_db().commit()
    resp = Response(status=200, mimetype='application/json')
    return resp


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
