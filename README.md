#  Barbearia System

Sistema de agendamento online para barbearias, desenvolvido em Django.
Permite que clientes agendem cortes e que o barbeiro gerencie a agenda do dia.

## Tecnologias

- **Backend:** Python e Django
- **Frontend:** HTML5, Bootstrap 5, CSS (Dark Mode)
- **Deploy:** PythonAnywhere

## Funcionalidades

-  Agendamento de horário com validação (impede conflitos).
-  Bloqueio de datas passadas e horários fora do expediente.
-  Dashboard restrito para o Barbeiro (visualização diária).
-  Login personalizado e seguro.
-  Envio de link de confirmação via WhatsApp.

## Prints
### Tela de Login
<img width="1919" height="1079" alt="Captura de tela 2025-11-28 224403" src="https://github.com/user-attachments/assets/1b13fa39-4c06-436f-a1c2-21e8f5694185" />

### Dashboard do Barbeiro
<img width="1919" height="1079" alt="Captura de tela 2025-11-28 224422" src="https://github.com/user-attachments/assets/2e411dcf-dab9-4fd5-85d4-c2de07d641d6" />

### Agendamento do Cliente
<img width="1919" height="1079" alt="Captura de tela 2025-11-28 224416" src="https://github.com/user-attachments/assets/0d88cc59-aa0f-4ee6-8332-03921cb7d508" />




## Como rodar localmente

1. Clone o repositório.
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o venv.
4. Instale as dependências: `pip install -r requirements.txt`
5. Rode as migrações: `python manage.py migrate`
6. Inicie o servidor: `python manage.py runserver`

---
Desenvolvido por Joao Antonio Bonfim Rodrigues ( @joaorodriguesss_ ) (https://github.com/joaorodriguesss2001)
