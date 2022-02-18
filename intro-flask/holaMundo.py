from os import abort
from flask import Flask, render_template, request, url_for, redirect, abort
app= Flask(__name__)

import psycopg2
import psycopg2.extras
conexion = psycopg2.connect("dbname=python_test01 user=postgres password=dr1234")
cursor = conexion.cursor(cursor_factory=psycopg2.extras.DictCursor)

@app.route('/')
def index():
    return 'hola mundo'

#GEST POST PUT PATCH DELETE
@app.route('/post/<post_id>', methods=['GET', 'POST'])
def lala(post_id):
    if request.method=='GET':
        return 'el id de post es '+post_id
    else:
        return 'no es metodo get'


@app.route('/lele', methods=['POST','GET'])
def lele():
    # abort(403)
    # return redirect(url_for('lala', post_id=2))
    # print (request.form)
    # print (request.form['llave1'])
    return {
        "username": 'chanchito feliz',
        "email": 'chanchitofeliz@felix.com'
    }

@app.route('/home', methods=['GET'])
def  home():
    cursor.execute( "SELECT nombre FROM estudiantes" )
    estudiantes= cursor.fetchall()
    return render_template('home.html', estudiantes=estudiantes)

@app.route('/crear', methods=['GET','POST'])
def crear():
    if request.method=="POST":
        cedula= request.form['cedula']
        nombre= request.form['nombre']
        fecha= request.form['fecha']
        sql= "INSERT INTO public.estudiantes(cedula, fecha, nombre) VALUES (%s,%s,%s)"
        values= (cedula,fecha,nombre)
        cursor.execute(sql,values)
        conexion.commit()
        return redirect(url_for('home'))
    return render_template ('crear.html')
