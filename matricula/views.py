from cgi import print_arguments
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.db import models, connection
from matricula.models import Blog

# Create your views here.

def blogToDiccionary(blog):
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

    ##metodo del codigo original
    query = '''select * from matricula_blog'''
    asientocontable = connection.cursor()
    asientocontable.execute(query)
    print('eddy',asientocontable)

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
        "blog2":blogs2
    }

    return JsonResponse(data)