from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django import forms
from .forms import PersonCreationForm
from django.contrib import auth, messages
from .models import Person, Course
from django.contrib.auth.models import User
from  django.http import HttpResponseRedirect
from django.contrib.admin.widgets import AdminDateWidget
# class DTForm(forms.Form):
#     name=forms.CharField(max_length=124)
#     # dob=forms.DateField(widget=AdminDateWidget())
#     age =forms.IntegerField()
#     address =forms.TextInput()
#     gender =forms.CharField()
#     phn =forms.IntegerField
#     email =forms.EmailField()
#     department =forms.CharField()
#     course =forms.CharField()
# class DtModelForm(forms.ModelForm):
#
#     class Meta:
#         model=Person
#         fields="__all__"
#         widgets={
#             "dob":AdminDateWidget()
#         }
# def home(request):
#     return render(request,"home.html")
def index(request):
    return render(request,"index.html")
def login(request):
    if request.method=='POST':
        username=request.POST['name']
        password=request.POST['paswd']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dropdownapp:new_page')
        else:
            messages.info(request,"Invalied credentials")
            return redirect('login')
    return render(request,"login.html")

def logout(request):
    auth.logout(request)
    return render(request,"index.html")

def register(request):
    if request.method=='POST':
        username=request.POST['name']
        password=request.POST['paswd']
        cpassword=request.POST['cpaswd']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Token")
                return redirect('dropdownapp:register')
            else:
                user=User.objects.create_user(username=username,password=password)
                user.save()
                return redirect('dropdownapp:login')

        else:
            messages.info(request,"password not matching")
            return redirect('dropdownapp:register')
        return redirect('/')
    return render(request,"register.html")

def new_page(request):
    return render(request, "new_page.html")
def person_create_view(request):
    submitted=False
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/person_add?submitted=True')
    else:
        form=PersonCreationForm
        if 'submitted' in request.GET:
            submitted=True

    return render(request,'form.html',{'form':form,'submitted':submitted})
            # return redirect('dropdownapp:person_add')
    #
    # return render(request, 'form.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'form.html', {'form': form})


# AJAX
def load_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id).all()
    # return render(request, 'city_dropdown_list_options.html', {'courses': courses})
    return JsonResponse(list(courses.values('id', 'name')), safe=False)
