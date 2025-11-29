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

*(Depois você edita aqui e cola os links das imagens que você me mandou)*

## Como rodar localmente

1. Clone o repositório.
2. Crie um ambiente virtual: `python -m venv venv`
3. Ative o venv.
4. Instale as dependências: `pip install -r requirements.txt`
5. Rode as migrações: `python manage.py migrate`
6. Inicie o servidor: `python manage.py runserver`

---
Desenvolvido por Joao Antonio Bonfim Rodrigues ( @joaorodriguesss_ ) (https://github.com/seusuer)