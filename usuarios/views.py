from django.shortcuts import render,redirect, get_object_or_404
from usuarios.forms import UsuarioForm, TipoUsuarioForm
from usuarios.models import Usuario, TipoUsuario
from django.contrib.auth.decorators import permission_required
# Create your views here.




def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarUsuarios')
    else:
        form = UsuarioForm()
        
    return render(request, 'templateUsuarios/usuarioAdd.html', {'form': form})


def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    tipos = TipoUsuario.objects.all()
    
    data = {
        'usuarios': usuarios,
        'tipos': tipos
    }
    
    return render(request, 'templateUsuarios/usuarios.html', data)

def cargar_editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    form = UsuarioForm(instance=usuario)
    
    return render(request, 'templateUsuarios/usuarioEdit.html', {'form': form, 'usuario': usuario})

def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listarUsuarios')
    else:
        form = UsuarioForm(instance=usuario)
        
    return render(request, 'templateUsuarios/usuarios.html', {'form': form})

def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listarUsuarios')

    return render(request, 'templateUsuarios/usuarioDelete.html', {'usuario': usuario})
