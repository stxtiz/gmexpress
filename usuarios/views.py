from django.shortcuts import render,redirect
from usuarios.forms import UsuarioForm, TipoUsuarioForm

# Create your views here.




def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('templateUsuarios/usuarios.html')
        else:
            form = UsuarioForm()
    return render(request, 'templateUsuarios/usuarioAdd.html', {'form': form})