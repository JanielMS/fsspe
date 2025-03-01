# FSSPE - Frabrica de Software do IFSertãoPE Campus Petrolina

Projeto Django Sistema de Gerenciamento de Projetos e Acontecimentos (SGPA) para a Fábrica de Software do IFSertãoPE (FSSPE).

## Pré-requisitos

Certifique-se de que você tenha as seguintes ferramentas instaladas em seu ambiente:

- Python 3.10 ou superior
- Pip (Python package installer)
- Virtualenv (opcional, mas recomendado)

## Configuração do Ambiente

1. **Clone o repositório:**

   ```bash
   git clone https://fsspe.petrolina.ifsertaope.edu.br:9000/webfusion/sitefsspe.git
   cd sitefsspe
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado):**

   ```bash
   python -m venv venv
   source venv/bin/activate # Linux/macOS
   venv\Scripts\activate    # Windows
   ```

3. **Instale as dependências:**

   Execute o comando abaixo para instalar as dependências listadas no `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

   Caso não exista o arquivo `requirements.txt`, você pode criar um com o seguinte comando:

   ```bash
   pip freeze > requirements.txt
   ```

   **Dependências do projeto:**
   ```
   asgiref==3.8.1
   Django==5.1.6
   sqlparse==0.5.3
   ```


4. **Realize as migrações do banco de dados:**

   ```bash
   python manage.py migrate
   ```

5. **Execute o servidor de desenvolvimento:**

   ```bash
   python manage.py runserver
   ```

   O projeto estará disponível em [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Instruções de Configuração

- [Configuração do Dart Sass](docs/sass/sass-setup.md)

## Como contribuir

1. Faça um clone do repositório.
2. Crie uma branch para sua feature: `git checkout -b minha-feature`.
3. Faça commit das suas alterações: `git commit -m 'Adicionei uma nova feature'`.
4. Envie para o repositório remoto: `git push origin minha-feature`.
5. Abra um Merge Request (MR) no Gitlab.


---