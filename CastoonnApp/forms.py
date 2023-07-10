from django import forms
from .models import CreatorUserProfile
from .models import ArtistUserProfile
# from .models import CreatorUser ,ArtistUser



 ###################################################################################<<<<<<<<< Creator Userform >>>>>>>>>>>>>>>>>
class CreatorUserProfileForm(forms.ModelForm):

    gender = forms.ChoiceField(choices=[
        ('Gender', 'Gender'),
        ('Female', 'Female'),
        ('Male', 'Male'),
    ], widget=forms.Select(attrs={'class': 'form-control item', 'id': 'Gender', 'placeholder': 'Gender'}))
    
    profession = forms.ChoiceField(choices=[
        ('Profession', 'Profession'),
        ('Actor', 'Actor'),
        ('Costume_Designer', 'Costume_Designer'),
        # Add more choices as needed
    ], widget=forms.Select(attrs={'class': 'form-control item', 'id': 'profession', 'placeholder': 'Profession'}))

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control item', 'id': 'birthday', 'placeholder': 'Date of Birth'}))

    username = forms.CharField(max_length=150, required=False)
    password = forms.CharField(max_length=128, widget=forms.PasswordInput, required=False)
    confirm_password = forms.CharField(max_length=128, widget=forms.PasswordInput, required=False)



    class Meta:
        model = CreatorUserProfile
        fields = ['name', 'lastname', 'nickname', 'gender', 'phone_number', 'email', 'profession', 'experience','username', 'password', 'confirm_password']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Lastname'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Nickname'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control item','placeholder':'phone number'}),
            'email': forms.EmailInput(attrs={'class': 'form-control item','placeholder':'Email'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control item','placeholder':'Experience'}),
            # 'username': forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control item', 'placeholder': 'Username'}), required=False)
            

        }
       
 ###################################################################################<<<<<<<<< Artist user profileForm >>>>>>>>>>>>>>>>>


class ArtistUserProfileForm(forms.ModelForm):

    gender = forms.ChoiceField(choices=[
        ('Gender', 'Gender'),
        ('Female', 'Female'),
        ('Male', 'Male'),
    ], widget=forms.Select(attrs={'class': 'form-control item', 'id': 'Gender', 'placeholder': 'Gender'}))
    
    profession = forms.ChoiceField(choices=[
        ('Profession', 'Profession'),
        ('Actor', 'Actor'),
        ('Costume_Designer', 'Costume_Designer'),
        # Add more choices as needed
    ], widget=forms.Select(attrs={'class': 'form-control item', 'id': 'profession', 'placeholder': 'Profession'}))

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control item', 'id': 'birthday', 'placeholder': 'Date of Birth'}))



    class Meta:
        model = ArtistUserProfile
        fields = ['name', 'lastname', 'nickname', 'gender', 'phone_number','phone_otp','email','email_otp', 'profession', 'experience']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Lastname'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Nickname'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control item','placeholder':'phone number'}),
            'phone_otp': forms.NumberInput(attrs={'class': 'form-control item','placeholder':'Enter Phone OTP'}),
            'email': forms.EmailInput(attrs={'class': 'form-control item','placeholder':'Email'}),
            'email_otp': forms.NumberInput(attrs={'class': 'form-control item','placeholder':'Enter Email OTP'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control item','placeholder':'Experience'})
        }
    

#  ###################################################################################<<<<<<<<< Creator login confirmation >>>>>>>>>>>>>>>>>
   


 ###################################################################################<<<<<<<<< Artist login confirmation >>>>>>>>>>>>>>>>>
   


