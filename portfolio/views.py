from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test  # Importar segurança
from .models import Projeto, Tecnologia, TFC, UnidadeCurricular
from .forms import ProjetoForm 

def e_gestor(user):
    return user.groups.filter(name='gestor-portfolio').exists()


def home_view(request):
    return render(request, 'portfolio/home.html')

def projetos_view(request):
    context = {'projetos': Projeto.objects.all()}
    return render(request, 'portfolio/projetos.html', context)

def tecnologias_view(request):
    context = {'tecnologias': Tecnologia.objects.all()}
    return render(request, 'portfolio/tecnologias.html', context)

def ucs_view(request):
    context = {'ucs': UnidadeCurricular.objects.all()}
    return render(request, 'portfolio/ucs.html', context)

def tfcs_view(request):
    context = {'tfcs': TFC.objects.all()}
    return render(request, 'portfolio/tfcs.html', context)

def sobre_view(request):
    return render(request, 'portfolio/sobre.html')


@login_required
@user_passes_test(e_gestor)  
def novo_projeto_view(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio:projetos') 
    else:
        form = ProjetoForm()
    return render(request, 'portfolio/novo_projeto.html', {'form': form})

@login_required
@user_passes_test(e_gestor)
def edita_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    form = ProjetoForm(request.POST or None, request.FILES or None, instance=projeto)
    if form.is_valid():
        form.save()
        return redirect('portfolio:projetos')
    return render(request, 'portfolio/edita_projeto.html', {'form': form, 'projeto': projeto})

@login_required
@user_passes_test(e_gestor)
def apaga_projeto_view(request, projeto_id):
    projeto = get_object_or_404(Projeto, id=projeto_id)
    if request.method == 'POST':
        projeto.delete()
        return redirect('portfolio:projetos')
    return render(request, 'portfolio/apaga_projeto.html', {'projeto': projeto})