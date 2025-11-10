from django.shortcuts import render,redirect, get_object_or_404
from usuarios.forms import UsuarioForm, TipoUsuarioForm
from usuarios.models import Usuario, TipoUsuario
from django.contrib.auth.decorators import permission_required
# Create your views here.



@permission_required('usuarios.add_usuario')
def crear_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarUsuarios')
    else:
        form = UsuarioForm()
        
    return render(request, 'templateUsuarios/usuarioAdd.html', {'form': form})

@permission_required('usuarios.view_usuario')
def listar_usuarios(request):
    usuarios = Usuario.objects.all()
    tipos = TipoUsuario.objects.all()
    
    data = {
        'usuarios': usuarios,
        'tipos': tipos
    }
    
    return render(request, 'templateUsuarios/usuarios.html', data)

@permission_required('usuarios.change_usuario')
def cargar_editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    form = UsuarioForm(instance=usuario)
    form.fields.pop('contrasenia', None)
    
    return render(request, 'templateUsuarios/usuarioEdit.html', {'form': form, 'usuario': usuario})
@permission_required('usuarios.change_usuario')
def editar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        form.fields.pop('contrasenia', None)
        if form.is_valid():
            form.save()
            return redirect('listarUsuarios')
    else:
        form = UsuarioForm(instance=usuario)
        form.fields.pop('contrasenia', None)
        
    return render(request, 'templateUsuarios/usuarioEdit.html', {'form': form, 'usuario': usuario})

@permission_required('usuarios.delete_usuario')
def eliminar_usuario(request, usuario_id):
    usuario = get_object_or_404(Usuario, id=usuario_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listarUsuarios')

    return render(request, 'templateUsuarios/usuarioDelete.html', {'usuario': usuario})

@permission_required('usuarios.add_tipousuario')
def crear_tipo_usuario(request):
    if request.method == 'POST':
        form = TipoUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarTipoUsuarios')
        else:
            # Si el formulario no es válido, mostrar errores
            print("Errores en el formulario:", form.errors)
    else:
        form = TipoUsuarioForm()
        
    return render(request, 'templateUsuarios/tipousuarioAdd.html', {'form': form})

@permission_required('usuarios.view_tipousuario')
def listar_tipo_usuarios(request):
    tipos = TipoUsuario.objects.all()
    
    data = {
        'tipos': tipos
    }
    return render(request, 'templateUsuarios/tipoUsuarios.html', data)

@permission_required('usuarios.change_tipousuario')
def cargar_editar_tipo_usuario(request, tipo_id):
    tipo = get_object_or_404(TipoUsuario, id=tipo_id)
    form = TipoUsuarioForm(instance=tipo)

    return render(request, 'templateUsuarios/tipoUsuarioEdit.html', {'form': form, 'tipo': tipo})
@permission_required('usuarios.change_tipousuario')
def editar_tipo_usuario(request, tipo_id):
    tipo = get_object_or_404(TipoUsuario, id=tipo_id)
    
    if request.method == 'POST':
        form = TipoUsuarioForm(request.POST, instance=tipo)
        if form.is_valid():
            form.save()
            return redirect('listarTipoUsuarios')
    else:
        form = TipoUsuarioForm(instance=tipo)
        
    return render(request, 'templateUsuarios/tipoUsuarioEdit.html', {'form': form, 'tipo': tipo})
@permission_required('usuarios.delete_tipousuario')
def eliminar_tipo_usuario(request, tipo_id):
    tipo = get_object_or_404(TipoUsuario, id=tipo_id)
    if request.method == 'POST':
        tipo.delete()
        return redirect('listarTipoUsuarios')

    return render(request, 'templateUsuarios/tipoUsuarioDelete.html', {'tipo': tipo})
