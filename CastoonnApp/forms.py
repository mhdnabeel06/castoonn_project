from django import forms
from .models import User_Registration


 ###################################################################################<<<<<<<<< Creator Userform >>>>>>>>>>>>>>>>>

class User_RegistrationForm(forms.ModelForm):

    gender = forms.ChoiceField(choices=[
        ('Gender', 'Gender'),
        ('Female', 'Female'),
        ('Male', 'Male'),
    ], widget=forms.Select(attrs={'class': 'form-control item', 'id': 'Gender', 'placeholder': 'Gender'}))
    
    profession = forms.ChoiceField(choices=[
        ('Profession', 'Profession'),
        ('Actor', 'Actor'),
        ('Costume_Designer', 'Costume_Designer'),
        
    ], widget=forms.Select(attrs={'class': 'form-control item', 'id': 'profession', 'placeholder': 'Profession'}))

    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control item', 'id': 'birthday', 'placeholder': 'Date of Birth'}))

    class Meta:
        model = User_Registration
        fields = '__all__'
    
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Name'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Lastname'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Nickname'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control item','placeholder':'phone number'}),
            'phone_otp': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Enter phone OTP'}),
            'email': forms.EmailInput(attrs={'class': 'form-control item','placeholder':'Email'}),
            'email_otp': forms.TextInput(attrs={'class': 'form-control item','placeholder':'Enter Email OTP'}),
            'experience': forms.NumberInput(attrs={'class': 'form-control item','placeholder':'Experience'}),
            'role': forms.TextInput(attrs={'class': 'form-control item','placeholder':'role'}),
            # 'username': forms.TextInput(attrs={'class': 'form-control item','placeholder': '&nbsp;&nbsp;Username'}),
            # 'password': forms.TextInput(attrs={'class': 'form-control item','placeholder': '&nbsp;&nbsp;Password'}),
            }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].required = False
        self.fields['password'].required = False




