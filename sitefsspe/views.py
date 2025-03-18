from django.shortcuts import render
from projetos.models import Projeto
from acontecimentos.models import Acontecimento
from django.contrib.auth.models import User

def dashboard(request):
    # Get the counts of various objects
    total_projects = Projeto.objects.count()
    total_acontecimentos = Acontecimento.objects.count()
    total_users = User.objects.count()

    # Get recent movements
    recent_movements = list(Projeto.objects.all()) + list(Acontecimento.objects.all())
    recent_movements.sort(key=lambda x: x.data_cadastro, reverse=True)
    recent_movements = recent_movements[:5]
    # Add the created_at attribute in the projects and events

    # Pass the counts and recent movements to the template
    context = {
        'total_projects': total_projects,
        'total_acontecimentos': total_acontecimentos,
        'total_users': total_users,
        'recent_movements': recent_movements,
    }
    return render(request, 'dashboard.html', context)

def custom_403(request, exception):
    """
    View para exibir a página de acesso negado (403).
    """
    return render(request, "core/403.html", status=403)