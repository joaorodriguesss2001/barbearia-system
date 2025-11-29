from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.utils.timezone import now
from .forms import AgendamentoForm
from .models import Agendamento  # Importação essencial!

# --- 1. TELA DE AGENDAMENTO (CLIENTE) ---
def agendar_corte(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            agendamento_criado = form.save()
            return render(request, 'core/sucesso.html', {'agendamento': agendamento_criado})
    else:
        form = AgendamentoForm()

    return render(request, 'core/agenda.html', {'form': form})

# --- 2. DASHBOARD (BARBEIRO) ---
@login_required
def dashboard(request):

    # Ordenado por data (do mais antigo pro mais novo)
    agendamentos_todos = Agendamento.objects.all().order_by('data_hora')
    
    return render(request, 'core/dashboard.html', {'agendamentos': agendamentos_todos})

# --- 3. LOGOUT (SAIR) ---
def fazer_logout(request):
    logout(request)
    return redirect('login')