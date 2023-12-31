from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request):
    return render(request, 'home.html')

# Formulário de Cadastro
def create(request):
    return render(request, 'create.html')

# Inserção dos dados dos usuários no banco
def store(request):
    data = {}
    if (request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senha e confirmação de senha diferentes'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        data['msg'] = 'Usuário Cadastrado com Sucesso'
        data['class'] = 'alert-success'

        
    return render(request, 'create.html', data)

# Formuçário do Painel de Login
def painel(request):
    return render(request, 'painel.html')

# Processa o Login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Login ou Senha Inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html', data)
    
# Página inicial do Dashboard
def dashboard(request):
    return render(request, 'dashboard/home.html')

# Logout do Sistema
def logouts(request):
    logout(request)
    return redirect('/painel/')
