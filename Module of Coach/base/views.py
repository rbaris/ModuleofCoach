from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Module
from django.urls import reverse_lazy


class CustomLoginView(LoginView):
    template_name = "base/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self) :
        return reverse_lazy('modules')

class RegisterPage(FormView):
    template_name = "base/register.html"
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('modules')

    def form_valid(self,form):
        user = form.save()
        if user is not None:
            login(self.request,user)
        return super(RegisterPage,self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('modules')
        return super(RegisterPage, self).get(*args, **kwargs)    


class ModuleList(LoginRequiredMixin, ListView):
    model = Module
    context_object_name = "modules"
    
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['modules']= context['modules'].filter(user=self.request.user)
        context['count']= context['modules'].count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['modules'] = context['modules'].filter(title__icontains=search_input)
        context['search_input'] = search_input    
        return context
        
class ModuleDetail(LoginRequiredMixin, DetailView):
    model = Module
    context_object_name = "module"


class ModuleCreate(LoginRequiredMixin, CreateView):
    model = Module
    fields = ['title','dataSheet','CVrate','kNeighbors','metric','isKNN','isDT','isNB']
    context_object_name = "module-create"
    success_url = reverse_lazy('modules')

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super(ModuleCreate, self).form_valid(form)

class ModuleUpdate(LoginRequiredMixin, UpdateView):
    model = Module
    fields = ['title','dataSheet','CVrate','kNeighbors','metric','isKNN','isDT','isNB']
    success_url = reverse_lazy('modules')

class ModuleDelete(LoginRequiredMixin, DeleteView):
    model = Module
    context_object_name = "module"
    success_url = reverse_lazy('modules')

