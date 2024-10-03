from django.shortcuts import render,redirect

from django.views.generic import View,TemplateView

from todo.forms import SignUpForm,SignInForm,TaskForm

from django.contrib.auth import authenticate,login,logout

from todo.models import Task


class SignupView(View):

    def get(self,request,*args,**kwargs):

        form_instance=SignUpForm()

        return render(request,'register.html',{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=SignUpForm(request.POST)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("signin")
        
        else:
            
            return render(request,'register.html',{"form":form_instance})


class SignInView(View):

    def get(self,request,*args,**kwargs):

        form_instance=SignInForm()

        return render(request,'login.html',{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_instance=SignInForm(request.POST)

        if form_instance.is_valid():
            
            data=form_instance.cleaned_data

            user_obj=authenticate(request,**data)

            if user_obj:

                login(request,user_obj)

                return redirect("task-add")

        return render(request,"login.html",{'form':form_instance})    
        

class IndexView(TemplateView):

    template_name="index.html"


class  TaskCreateView(View):

    def get(self,request,*args,**kwargs):

        form_instance=TaskForm()

        obj=Task.objects.filter(owner=request.user)

        count=Task.objects.filter(status="incomplete",owner=request.user).count()

        return render(request,'task_add.html',{"form":form_instance,"task":obj,"count":count})
    
    def post(self,request,*args,**kwargs):

        form_instance=TaskForm(request.POST)

        if form_instance.is_valid():

            form_instance.instance.owner=request.user

            form_instance.save()

            return redirect("task-add")
        
        else:

            return render(request,'task_add.html',{"form":form_instance})



class TaskUpdateView(View):
    def get(self,request,*args,**kwargs):
        

        id=kwargs.get("pk")

        obj=Task.objects.get(id=id)

        form_instance=TaskForm(instance=obj)


        return render(request,'task_update.html',{"form":form_instance})
    
    def post(self,request,*args,**kwargs):
        id=kwargs.get("pk")


        obj=Task.objects.get(id=id)

        form_instance=TaskForm(request.POST,instance=obj)

        if form_instance.is_valid():

            form_instance.instance.owner=request.user

            form_instance.save()

            return redirect("task-add")
        else:
            return render(request,'task_update.html',{"form":form_instance})
        

class TaskDeleteView(View):
    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Task.objects.get(id=id).delete()

        return redirect("task-add")
            
class LogoutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)   

        return redirect("signin")   




            




        
               

    
            