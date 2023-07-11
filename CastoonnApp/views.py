from django.shortcuts import render, redirect
from .forms import User_RegistrationForm
from .models import User_Registration
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate
from django.contrib import messages




# from .forms import ArtistUserForm


######################################################################### <<<<<<<<<< LANDING MODULE >>>>>>>>>>>>>>
def index(request):
    return render(request, 'index/index.html')

def user_type(request):
    return render(request, 'index/user_type.html')

def login_main(request):
    if request.method == 'POST':
        username  = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            return redirect('user_type')
        
        if User_Registration.objects.filter(username=request.POST['username'], password=request.POST['password'],role="user1").exists():

            member = User_Registration.objects.get(username=request.POST['username'],password=request.POST['password'])
            
            request.session['userid'] = member.id
            
            return redirect('user_type')


       

        elif User_Registration.objects.filter(username=request.POST['username'], password=request.POST['password'],role="user2").exists():
            member = User_Registration.objects.get(username=request.POST['username'],password=request.POST['password'])
            request.session['userid'] = member.id

            return redirect('user_type')
        else:
            messages.error(request, 'Invalid username or password')
            #  error_message = 'Invalid username or password'
            # return redirect(request,'')
    return render(request,'index/login.html')





######################################################################### <<<<<<<<<< CREATOR MODULE >>>>>>>>>>>>>>
def creator_registration(request):
    if request.method =='POST':
        form = User_RegistrationForm(request.POST)
        if form.is_valid():

            user_model=form.save()
            user_id = user_model.pk

            return redirect('index_creator_confirmation',user_id=user_id)
    else:
        form = User_RegistrationForm()
    return render(request,'index/index_creator/index_creator_registraion.html',{'form':form})


def index_creator_confirmation(request,user_id):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            print("sucess")
            creator_object = User_Registration.objects.get(pk=user_id)
            creator_object.username=username
            creator_object.password = password
            creator_object.save()
            return redirect('user_type')
        else:
            error_message = 'Password and Confirm Password do not match.'
            return render(request,'index\index_creator\index_creator_confirmation.html',{'error_message':error_message})

    return render(request,'index\index_creator\index_creator_confirmation.html',{'user_id':user_id})








######################################################################### <<<<<<<<<< ARTIST MODULE >>>>>>>>>>>>>>>>

