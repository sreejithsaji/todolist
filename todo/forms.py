from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from todo.models import Task



class SignUpForm(UserCreationForm):

    password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-2"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-2"}))


    class Meta:

        model=User

        fields=["username","email","password1","password2"]

        widgets={

            "username":forms.TextInput(attrs={"class":"form-control mb-2"}),
            "email":forms.EmailInput(attrs={"class":"form-control mb-2"}),
        }



class SignInForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control mb-2"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control mb-2"}))        


class TaskForm(forms.ModelForm):

    class Meta:

        model=Task

        fields=["title","status"]

        widgets={

             "title":forms.TextInput(attrs={"class":"form-control"}),
             "status":forms.Select(attrs={"class":"form-control form-select mb-2"})


        }

           