def agregaColumnas(miPadron):
#agrega columna provincia y usando los numeros de la cedula convierte ese numero en nombre de provincias
    miPadron['Provincia'] = miPadron['Cedula'].astype(str)
    miPadron['Provincia'] = miPadron['Provincia'].str[0:1]
    miPadron['Provincia'] = miPadron['Provincia'].replace({'1':'San Jose', '2':'Alajuela', '3':'Cartago','4':'Heredia','5':'Guanacaste','6':'Puntarenas','7':'Limon','8':'Nacionalizado','9':'CasosEspeciales'})
    miPadron['Count'] = 1
    return (miPadron)

#agrega columna para conteo distritos        
def agregaColumnaDistrito (miDistrito):    
    miDistrito['Count'] = 1
    return (miDistrito)

#Calcula votantes por provincia
def votantesPorProvincia(miPadron):
    resultado = miPadron['Provincia'].value_counts().reset_index()
    resultado.columns = ['Provincia','Catidad de Votantes']
    return (resultado)

#ListaVotantes por variable selecionada
def ListaVotantesPorProvincia(miPadron):
    resultado = miPadron.loc[miPadron['Provincia'] == varProvincia]
    return (resultado)

def ListaVotantePorCedula(miPadron,CedId):
    resultado = miPadron.loc[miPadron['Cedula'] == CedId]
    return (resultado)

def ListaVotantePorDistrito(miPadron,Distrit):
    resultado = miPadron.loc[miPadron['Distrito'] == Distrit]
    return (resultado)


#Calcula vontantes por sexo
def votantesPorSexo(miPadron):
    miPadron['Sexo'] = miPadron['Sexo'].astype(str)
    miPadron['Sexo'] = miPadron['Sexo'].replace({'1':'Masculino','2':'Femenino'})
    resultado = miPadron['Sexo'].value_counts().reset_index()
    resultado.columns = ['Sexo','Cantidad']
    return (resultado)

#Lista Votantes Mujeres
def votantesFemenino(miPadron):
    miPadron['Sexo'] = miPadron['Sexo'].astype(str)
    miPadron['Sexo'] = miPadron['Sexo'].replace({'1':'Masculino','2':'Femenino'})
    resultado = miPadron.loc[miPadron['Sexo'] =="Femenino"]
    return (resultado.head(50))

#Lista Vontantes Hombres
def votantesMasculino(miPadron):
    miPadron['Sexo'] = miPadron['Sexo'].astype(str)
    miPadron['Sexo'] = miPadron['Sexo'].replace({'1':'Masculino','2':'Femenino'})
    resultado = miPadron.loc[miPadron['Sexo'] =="Masculino"]
    return (resultado.head(50))


#cuenta distritos electorales por provincia 
def DistritoPorProvincia(miDistrito):
    resultado = miDistrito['Provincia'].value_counts().reset_index()
    resultado.columns = ['Provincia','Cantidad Distritos']
    return (resultado)

#cuenta distritos electorales por Canton
def DistritoPorCanton(miDistrito):
    resultado = miDistrito['Canton'].value_counts().reset_index()
    resultado.columns = ['Canton','Distritos Electorales']
    return (resultado)





