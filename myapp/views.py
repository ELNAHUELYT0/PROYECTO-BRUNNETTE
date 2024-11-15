from django.shortcuts import render
from MiPrimerApp.models import Usuario

# Create your views here.
def AppIndex(request):
    datos={
        'mensaje': ''
    }
    return render(request,'login.html', datos)

def ValidarLogin(request):
    if request.method == 'POST':
        username = request.POST.get('inputUsername', None)
        password = request.POST.get('inputPassword', None)
        print(username)
        print(password)
        try:
            usuario = Usuario.objects.get(username=username, password=password)
            datos={
                'usuario': usuario
            }
            return render(request,'bienvenido.html', datos)
        except Usuario.DoesNotExist:
            datos={
                'mensaje': 'Usuario y/o contraseña incorrectos'
            }
            return render(request,'login.html',datos)      
    else:
        datos={
            'mensaje': ''
        }
        return render(request,'login.html', datos)
