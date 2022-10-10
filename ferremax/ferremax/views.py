from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from modulos.models import PQRS
from .forms import PQRSForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
import threading
from products.models import Product
from users.models import User
from django.http import HttpResponseRedirect
from .mails import Mail

def index(request):
    return render(request,'index.html',{
    })

def contacto(request):
    return render(request,'contacto.html',{
        #context
    })

def contacto(request):
    if request.method == "POST":
        name = request.POST['name']
        surname = request.POST['surname']
        tel = request.POST['tel']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        template = render_to_string('email_template.html', {
            'name': name,
            'surname': surname,
            'tel': tel,
            'email': email,
            'message': message
        })
    
        email = EmailMessage(
            subject,
            template,
            settings.EMAIL_HOST_USER,
            ['ferre.maxcontacto45@gmail.com']
        )
    
        email.fail_silently = False
        email.send()
    
    return render(request, 'contacto.html',{

    })


def pedidos(request):
    return render (request,'pedidos.html',{
        #context
    })

def catalogo(request):

    return render (request,'catalogo.html',{
    })


def productos(request):

    products = Product.objects.all().order_by('-id')

    return render (request,'productos.html',{
        'message': 'Listado de Productos',
        'title': 'Productos',
        'products': products,
    })



def ofertas(request):
    return render (request,'ofertas.html',{
        #context
    })

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            login(request, user)

            if request.GET.get('next'):
                return HttpResponseRedirect(request.GET['next'])

            return redirect('index')
            
        else: 
            messages.error(request, 'Usuario o contraseña incorrectos')
    return render(request, 'login.html',{

    })

def logout_view(request):
    logout(request)
    messages.success(request, 'Sesión finalizada')
    return redirect('login')



def contacto(request):

    form = PQRSForm()

    if request.method == "POST":
        form = PQRSForm(request.POST)

        if form.is_valid():
            messages.success(request, 'Su PQRS ha sido enviada correctamente')
            # form.save()

            pqrs = PQRS()

            pqrs.name = form.cleaned_data['Nombre']
            pqrs.surname = form.cleaned_data['Apellido']
            pqrs.tel = form.cleaned_data['tel']
            pqrs.description = form.cleaned_data['Descripcion']
            pqrs.email = form.cleaned_data['email']
            pqrs.Tipopqrs = form.cleaned_data['Tipopqrs']

            pqrs.save()

            user = User.objects.last()

            thread = threading.Thread(target=Mail.send_complete_pqrs, args=(user, )) 

            thread.start()

        else:
            print("Invalido")


    return render(request, 'contacto.html',{
        'form' : form
})

def register(request):

    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            form.save()
            return redirect('register')

    else:
        form = UserRegisterForm()

    context = { 'form': form }
    return render(request, 'registro.html', context)