from django.shortcuts import render, redirect
from .forms import CreatorUserProfileForm
from .forms import ArtistUserProfileForm

# from .forms import ArtistUserForm


######################################################################### <<<<<<<<<< LANDING MODULE >>>>>>>>>>>>>>
def index(request):
    return render(request, 'index/index.html')

def login_main(request):
    return render(request,'index/login.html')

def user_type(request):
    return render(request, 'index/user_type.html')



######################################################################### <<<<<<<<<< CREATOR MODULE >>>>>>>>>>>>>>

#Creator Registration 

def creator_registration(request):
    if request.method =='POST':
        form = CreatorUserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index_creator_confirmation' )
    else:
        form = CreatorUserProfileForm()


    return render(request,'index\index_creator\index_creator_registraion.html',{'form':form})

#Artist Registration 
def index_artist_confirmation(request,):
    

    return render(request,'index\index_artist\index_artist_confirmation.html')

def artist_registration(request):
    if request.method =='POST':
        form = ArtistUserProfileForm(request.POST)
        if form.is_valid():
            test=form.save()
            mypk = test.pk
            print(mypk)
            return redirect('index_artist_confirmation')
    else:
        form = ArtistUserProfileForm()
    

    return render(request,'index\index_artist\index_artist_registraion.html',{'form':form})


def index_creator_confirmation(request):
    
    
    return render(request,'index\index_creator\index_creator_confirmation.html')


######################################################################### <<<<<<<<<< ARTIST MODULE >>>>>>>>>>>>>>>>

