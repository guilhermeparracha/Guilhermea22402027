from django.shortcuts import render, redirect, get_object_or_404
from .models import Projeto, Tecnologia, TFC  
from .forms import ProjetoForm 

def home_view(request):
    return render(request, 'portfolio/home.html')

def projetos_view(request):
    context = {'projetos': Projeto.objects.all()}
    return render(request, 'portfolio/projetos.html', context)

def tecnologias_view(request):
    context = {'tecnologias': Tecnologia.objects.all()}
    return render(request, 'portfolio/tecnologias.html', context)

def novo_projeto_view(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio:home')
    else:
        form = ProjetoForm()
    return render(request, 'portfolio/novo_projeto.html', {'form': form})

def edita_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('portfolio:home')
    return render(request, 'portfolio/edita_projeto.html', {'form': form})

def apaga_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('portfolio:home')
    return render(request, 'portfolio/apaga_projeto.html', {'projeto': projeto})


def sobre_view(request):
    return render(request, 'portfolio/sobre.html')