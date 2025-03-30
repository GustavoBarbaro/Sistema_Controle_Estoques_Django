[![OS - Windows](https://img.shields.io/badge/OS-Windows-blue?logo=windows&logoColor=white)](https://www.microsoft.com/ "Go to Microsoft homepage") [![GitHub Repo](https://img.shields.io/badge/GustavoBarbaro-Sistema__Controle__Estoques__Django-blue?style=flat&logo=github)](https://github.com/GustavoBarbaro/Sistema_Controle_Estoques_Django) [![License](https://img.shields.io/badge/License-MIT-yellow)](#license) [![Made with Python](https://img.shields.io/badge/Python-=3.12.3-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage") ![GitHub last commit](https://img.shields.io/github/last-commit/GustavoBarbaro/Sistema_Controle_Estoques_Django)

# Sistema de Controle de Estoque com Django


Este projeto é um Sistema de Controle de Estoque desenvolvido em Django e um ESP32 com interface responsiva em Bootstrap e suporte a leitura de RFID. Ele permite registrar movimentações de produtos (entradas e saídas), armazenando as informações em um banco de dados relacional.

Este repositório contém o projeto Web com o banco de dados.

Para o código fonte do hardware, com o ESP32 e o leitor RFID confira este repositório:


[![GitHub Repo](https://img.shields.io/badge/GustavoBarbaro-TCC__Leitor__RFID-blue?style=flat)](https://github.com/GustavoBarbaro/TCC-Leitor-RFID)


---



# Tecnologias Utilizadas

### Backend
* ![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)

### Frontend
* ![bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
* ![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
* ![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white
)

### Banco de Dados
* ![SQL_Lite](https://img.shields.io/badge/Sqlite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

### Hardware
* ![ESP](https://img.shields.io/badge/ESP32-E7352C?style=for-the-badge&logo=espressif&logoColor=white)

---

# Screenshots

![Homecomlogin](https://github.com/user-attachments/assets/00b9c2e1-201b-4c5b-8ddf-31642bf224ad)

![Log das Movimentacoes Menor](https://github.com/user-attachments/assets/0ebe9fda-f07e-479b-b3e4-14c9aded9e4a)

![Estoque Atual Menor](https://github.com/user-attachments/assets/2c6a9285-ce6e-4741-b18a-bcc75e4379e5)


# Funcionalidades

✅Cadastro de produto e usuários

✅Registro de entradas e saídas de produtos

✅Monitoramento de movimentações em tempo real com **WebSockets**

✅Integração com Leitor RFID por meio de *wi-fi* para leitura automática

✅Controle de usuários e permissões

---

# Instalação

1️⃣ Clonar o repositório:

```bash
git clone https://github.com/GustavoBarbaro/Sistema_Controle_Estoques_Django.git
cd Sistema_Controle_Estoques_Django
```

2️⃣ Criar ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```

3️⃣ Instalar dependências:

```bash
pip install -r requirements.txt
```

4️⃣ Aplicar migrações:

```bash
python manage.py migrate
```

5️⃣ Iniciar o servidor:

```bash
bash runserver.sh
```
 ou
 
```bash
daphne -b 0.0.0.0 -p 8000 core.asgi:application
```

Acesse o sistema em: 

* http://localhost:8000 caso esteja no Windows
* http://your_local_IP_Address:8000 caso esteja no WSL ou Linux


---

# Arquitetura do Sistema

O sistema segue uma estrutura MVC (Model-View-Controller) adaptada ao Django (MTV - Model, Template, View). Ele conta com:

* Modelos para representar os dados dos produtos e movimentações.
* Views baseadas em classes (CBV) para facilitar o desenvolvimento.
* Templates dinâmicos usando Bootstrap para uma interface amigável.


---

# Demonstração

[YouTube](https://youtu.be/2zCVcu27XJM)

# Palavras-chave


Django; Bootstrap; RFID; Banco de Dados; WebSockets; Backend Python; Fullstack Development; API REST


