from django.http import HttpResponse
import datetime
from django.template import Template, Context

class Persona(object):

    def __init__(self, nombre, apellido):

        self.nombre=nombre

        self.apellido=apellido

def saludo(request): #Primera vista

    p1=Persona("Profesor Juan", "Diaz")

    #nombre="Juan"

    #apellido="Diaz"

    temasDelCurso=["Plantillas", "Modelos", "Formularios", "Vistas", "Despliegue"]

    ahora=datetime.datetime.now()

    doc_externo=open("C:/Users/PC/Desktop/DJANGO/plantillas/miplantilla.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "momento_actual":ahora, "temas":temasDelCurso})

    documento=plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):

    return HttpResponse('Hasta luego amigos')


def damefecha(request):

    fecha_actual=datetime.datetime.now()

    documento="""<html>
    <body>
    <h2>
    Fecha y hora actuales %s
    </h1>
    </body>
    </html>""" % fecha_actual

    return HttpResponse(documento)

def calculaedad(request, edad, agno):

    #edadActual=18
    periodo=agno-2022
    edadFutura=edad+periodo
    documento="<html><body><h2> En el agno %s tendras %s agnos" %(agno, edadFutura)

    return HttpResponse(documento)