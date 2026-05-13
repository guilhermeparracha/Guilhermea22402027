from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Artigo, Comentario

def lista_artigos_view(request):
    artigos = Artigo.objects.all().order_by('-data_criacao')
    return render(request, 'artigos/lista.html', {'artigos': artigos})

# 2. View de detalhe
def detalhe_artigo_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    return render(request, 'artigos/detalhe.html', {'artigo': artigo})

# 3. View de Likes
@login_required
def like_artigo_view(request, artigo_id):
    artigo = get_object_or_404(Artigo, id=artigo_id)
    if request.user in artigo.likes.all():
        artigo.likes.remove(request.user)
    else:
        artigo.likes.add(request.user)
    return redirect('artigos:detalhe', artigo_id=artigo.id)

# 4. View de Comentários
@login_required
def comentar_view(request, artigo_id):
    if request.method == 'POST':
        artigo = get_object_or_404(Artigo, id=artigo_id)
        texto = request.POST.get('texto')
        if texto:
            Comentario.objects.create(
                artigo=artigo,
                autor=request.user,
                texto=texto
            )
    return redirect('artigos:detalhe', artigo_id=artigo_id)