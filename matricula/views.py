from cgi import print_arguments
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.db import models, connection
from matricula.models import Blog

# Create your views here.

def blogToDiccionary(blog):

    #funcion que formatea el resultado de un modelo en formato json, hay que tener los nombres de los campo para generar el json#
    output={}
    output['title']=blog.title
    output['description']=blog.description
    output['showcaseImage']=blog.showcaseImage.url
    output['dateTimeOfCreation']=blog.dateTimeOfCreation
    output['shareURL']=blog.shareURL
    output['likes']=blog.likes
    output['disLikes']=blog.disLikes
    output['bookmarks']=blog.bookmarks

    return output

def myView(request):
    ####################### prueba con cursor para bases sin modelo genera correctamente el json pero hay que pasarle los nombres de las columnas para formatear el json
    with connection.cursor() as cursor:
        #cursor.execute("UPDATE bar SET foo = 1 WHERE baz = %s", [self.baz])
        cursor.execute("select * from  matricula_blog")
        row = cursor.fetchall()
        json_data = []
        for obj in row:
            json_data.append({"title" : obj[0], "description" : obj[1], "showcaseImage" : obj[2], "dateTimeOfCreation" : obj[3], "shareURL" : obj[4], "disLikes" : obj[5],"bookmarks" : obj[6]})
        print("raw2",json_data)

    
    print('eddyrow',cursor.description)  
    ################################
    ##otro metodo para generar el json con consulta plana
    query = '''select * from matricula_blog'''
    asientocontable = connection.cursor()
    asientocontable.execute(query)
    print('eddy',asientocontable)##genera tuplas que es necesario formatear para genear json, no se hizo en este ejemplo
    

    blogs2 =Blog.objects.raw("select * from  matricula_blog")


    blog = Blog.objects.get(id=1)

    blogs = Blog.objects.all()
    print('eddy2',blogs)
    tempBlogs=[]

    blog=blogToDiccionary(blog)


    for i in range(len(blogs)):
        tempBlogs.append(blogToDiccionary(blogs[i]))
    
    blogs=tempBlogs

    tempBlogs=[]
    for i in range(len(blogs2)):
        tempBlogs.append(blogToDiccionary(blogs2[i]))
    
    blogs2=tempBlogs

    data ={
        "blog":blog,
        "blogs":blogs,
        "blog2":blogs2,
        "blog3":json_data
    }

    return JsonResponse(data)