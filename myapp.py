
from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd
import manipuladatos


app = Flask(__name__)

# este es nuestro home page
@app.route("/")
def index():
    return render_template('home.html')

#este app despliega distritos por provincia
@app.route('/disxprovincia', methods=("POST", "GET"))
def html_disxprovincia():
    df1 = pd.read_csv('./Data/Distelec.csv',encoding='ISO-8859-1')
    df1 = manipuladatos.agregaColumnaDistrito(df1)
    df1 = manipuladatos.DistritoPorProvincia(df1)
    return render_template('disxprovincia.html',  tables=[df1.to_html(classes='table table-striped')], titles=df1.columns.values)

#este app despliega distritos por canton
@app.route('/disxcanton', methods=("POST", "GET"))
def html_disxcanton():
    df1 = pd.read_csv('./Data/Distelec.csv',encoding='ISO-8859-1')
    df1 = manipuladatos.agregaColumnaDistrito(df1)
    df1 = manipuladatos.DistritoPorCanton(df1)
    return render_template('disxcanton.html',  tables=[df1.to_html(classes='table table-striped')], titles=df1.columns.values)    

#este app despliega el total de hombres y el total de mujeres
@app.route('/xSexo', methods=("POST", "GET"))
def html_xSexo():
    df1 = pd.read_csv('./Data/padron.csv',encoding='ISO-8859-1')
    df1 = manipuladatos.agregaColumnas(df1)
    df1 = manipuladatos.votantesPorSexo(df1)
    return render_template('xSexo.html',  tables=[df1.to_html(classes='table table-striped')], titles=df1.columns.values) 

#este app despliega el total votantes por provincia
@app.route('/xProvincia', methods=("POST", "GET"))
def html_xProvinca():
    df1 = pd.read_csv('./Data/padron.csv',encoding='ISO-8859-1')
    df1 = manipuladatos.agregaColumnas(df1)
    df1 = manipuladatos.votantesPorProvincia(df1)
    return render_template('xProvincia.html',  tables=[df1.to_html(classes='table table-striped')], titles=df1.columns.values) 

#este app despliega solo las mujeres votantes
@app.route('/xFemenino', methods=("POST", "GET"))
def html_xFemenino():
    df1 = pd.read_csv('./Data/padron.csv',encoding='ISO-8859-1')
    df1 = manipuladatos.agregaColumnas(df1)
    df1 = manipuladatos.votantesFemenino(df1)
    return render_template('xFemenino.html',  tables=[df1.to_html(classes='table table-striped')], titles=df1.columns.values) 

#este app despliega solo los hombres votantes
@app.route('/xMasculino', methods=("POST", "GET"))
def html_xMasculino():
    df1 = pd.read_csv('./Data/padron.csv',encoding='ISO-8859-1')
    df1 = manipuladatos.agregaColumnas(df1)
    df1 = manipuladatos.votantesMasculino(df1)
    return render_template('xMasculino.html',  tables=[df1.to_html(classes='table table-striped')], titles=df1.columns.values) 

#este app despliega la pagina de acerca de nosotros, los que trabajamos en el examen
@app.route('/about', methods=("POST", "GET"))
def html_about():
    return render_template('about.html') 

#este app solicita un numero de cedula y busca en el padron.csv y despliega los datos de la persona dueña del ese numero de cedula
@app.route('/xBusca',  methods=("POST", "GET"))
def html_xBusca():
    try:
        if request.method == 'POST':
            Ced = request.form["Cedula"]
            intCed = int(Ced)
            df1 = pd.read_csv('./Data/padron.csv',encoding='ISO-8859-1')
            df1 = manipuladatos.agregaColumnas(df1)
            df1 = manipuladatos.ListaVotantePorCedula(df1,intCed)
            return render_template('xResultado.html',  tables=[df1.to_html(classes='table table-striped')], titles=df1.columns.values) 
    
        return render_template('xBusca.html')
    
    except Exception as e:    
    
        return render_template('xBusca.html')

#este app solicita el nombre del distrito y displiega los votantes que estan en ese distrito.
@app.route('/xBuscaDis',  methods=("POST", "GET"))
def html_xBuscaDis():
    try:
        if request.method == 'POST':
            Distrito = request.form["Distrito"]
            df1 = pd.read_csv('./Data/padrond.csv',encoding='ISO-8859-1')
            df1 = manipuladatos.agregaColumnas(df1)
            df1 = manipuladatos.ListaVotantePorDistrito(df1,Distrito)
            return render_template('xResulDis.html',  tables=[df1.to_html(classes='table table-striped')], titles=df1.columns.values) 
    
        return render_template('xBuscaDis.html')
    
    except Exception as e:    
    
        return render_template('xBuscaDis.html')


if __name__ == '__main__':
    app.run()
