from bson import is_valid
from django.shortcuts import render
from . import forms

# Create your views here.
def regform(request):
    form = forms.SignUp()
    if request.method == 'POST':
        form = forms.SignUp(request.POST)
        html = 'we have recieved this form again'
        if form.is_valid():
            html = html + "This Form is Valid"
    else:
        html = 'welcome for first time'
    return render(request, 'signup.html', {'html':html, 'form':form})
