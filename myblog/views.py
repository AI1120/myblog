from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import RedirectView

class tutorial(RedirectView):
    url = 'https://data-flair.training/blogs/category/django/'
    
def index(request):
    html = """<h1>Data Flair Django</h1>Hello, you just configured you First URL"""
    return HttpResponse(html)
    
def data_flair(request):
    return redirect('/dataflair')

def setcookie(request):
    html = HttpResponse("<h1>Dataflair Django Tutorial</h1>")
    if request.COOKIES.get('visits'):
        html.set_cookie('dataflair', 'Welcome Back')
        value = int(request.COOKIES.get('visits'))
        html.set_cookie('visits', value + 1)
    else:
        value = 1
        text = 'Welcome for the first time'
        html.set_cookie('visits', value)
        html.set_cookie('dataflair', text)
    return html

def showcookie(request):
    if request.COOKIES.get('visits') is not None:
        value = request.COOKIES.get('visits')
        text = request.COOKIES.get('dataflair')
        html = HttpResponse("<center><h1>{0}<br>You have requested this page {1} times</h1></center>".format(text, value))
        html.set_cookie('visits', int(value) + 1)
        return html
    else :
        return redirect('/setcookie')
    
def delete_co(request):
    if request.COOKIES.get('visits'):
        response = HttpResponse("<h1>dataflair<br>Cookie deleted</h1>")
        response.delete_cookie("visits")
    else:
        response = HttpResponse("<h1>dataflair</h1>need to create cookie before deleting")
    return response

def cookie_session(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>dataflair</h1>")

def cookie_delete(request):
    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        response = HttpResponse("dataflair<br> cookie createed")
    else:
        response = HttpResponse("Dataflair <br> Your browser doesnot accept cookies")
    return response