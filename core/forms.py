from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['nome_cliente', 'telefone_cliente', 'barbeiro', 'data_hora', 'observacao']
        
        widgets = {
            'nome_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Seu nome completo'}),
            'telefone_cliente': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '(XX) 9XXXX-XXXX'}),
            'barbeiro': forms.Select(attrs={'class': 'form-select'}),
            'data_hora': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'observacao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        
        barbeiro_escolhido = cleaned_data.get('barbeiro')
        horario_escolhido = cleaned_data.get('data_hora')

        if horario_escolhido:
            # 1. Bloqueia datas no passado
            if horario_escolhido < timezone.now():
                raise ValidationError("Não dá pra voltar no tempo! Escolha uma data futura.")
            
            # 2. Bloqueia horário fora do expediente (09:30 às 20:30)
            # Truque de Engenharia: Converte tudo para minutos totais do dia
            minutos_totais = (horario_escolhido.hour * 60) + horario_escolhido.minute
            
            inicio_expediente = 570  # 09:30 (9*60 + 30)
            fim_expediente = 1230    # 20:30 (20*60 + 30)

            if minutos_totais < inicio_expediente or minutos_totais > fim_expediente:
                raise ValidationError(f"Estamos fechados! Atendemos das 09:30 às 20:30.")

        if barbeiro_escolhido and horario_escolhido:
            # 3. Bloqueia conflito de agenda
            conflito = Agendamento.objects.filter(
                barbeiro=barbeiro_escolhido,
                data_hora=horario_escolhido
            ).exists()

            if conflito:
                raise ValidationError("Ops! Esse horário já está ocupado para este barbeiro.")
        
        return cleaned_data