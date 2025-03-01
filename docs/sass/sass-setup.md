
### **Instalando Dart Sass na Sua Máquina**

#### **Para Windows (Usando Chocolatey)**

1. **Instalar o Chocolatey (se não tiver instalado):**
   Se você ainda não tem o **Chocolatey** instalado, siga os passos abaixo para instalá-lo.

   **Abra um terminal com permissões administrativas** e execute o comando correspondente:

   - **Para `cmd.exe`:**

     ```bash
     @"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "[System.Net.ServicePointManager]::SecurityProtocol = 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"
     ```

   - **Para `PowerShell.exe`:**

     1. Certifique-se de que a política de execução não esteja **Restrita**. Execute o comando:

        ```powershell
        Get-ExecutionPolicy
        ```

        Se retornar **Restricted**, altere a política com:

        ```powershell
        Set-ExecutionPolicy Bypass -Scope Process -Force
        ```

     2. Agora, execute o comando para instalar o **Chocolatey**:

        ```powershell
        Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
        ```

2. **Instalar o Dart Sass via Chocolatey:**
   Após instalar o **Chocolatey**, você pode instalar o **Dart Sass** com o seguinte comando:

   ```bash
   choco install sass
   ```

#### **Para Mac OS X ou Linux (Usando Homebrew)**

1. **Instalar o Dart Sass via Homebrew:**
   Se você estiver usando **Mac OS X** ou **Linux**, o Homebrew pode ser utilizado para instalar o **Dart Sass**. Execute o seguinte comando:

   ```bash
   brew install sass/sass/sass
   ```

---

### **Usando o Dart Sass no Projeto Django**

Agora que o **Dart Sass** está instalado na sua máquina, você pode utilizá-lo diretamente no seu projeto Django.

#### **1. Estrutura de Pastas**

Organize os arquivos **SCSS** dentro da pasta **`static/scss/`**. A estrutura deve ficar parecida com:

```
/static/
    ├── scss/
    │   ├── main.scss
    │   ├── _variables.scss
    ├── css/  (onde o CSS compilado será gerado)
```
[Clique aqui para ver o padrão de estrurura de pastas no sass](sass-estrutura.md)
#### **2. Compilando SCSS para CSS com Dart Sass**

Para compilar seus arquivos SCSS manualmente, execute o seguinte comando no terminal (dentro da pasta raiz do projeto):

```bash
sass static/scss/main.scss static/css/styles.css
```

Este comando converte o arquivo **`main.scss`** para o arquivo **`styles.css`** dentro da pasta **`static/css/`**.

#### **3. Configuração do Django para Usar o CSS Compilado**

No seu template HTML (por exemplo, **`base.html`**), inclua o arquivo CSS compilado:

```html
<link rel="stylesheet" href="{% static 'css/styles.css' %}">
```

#### **4. Automatizando a Compilação (Opcional)**

Para automatizar a compilação do SCSS sempre que você alterar um arquivo, você pode usar o comando de observação do Dart Sass:

```bash
sass --watch static/scss:static/css
```

Isso vai monitorar a pasta **`scss/`** e compilar automaticamente para **`css/`** sempre que um arquivo for alterado.

#### **5. Integrando a Compilação no Django (Opcional)**

Caso deseje integrar a compilação diretamente no fluxo de desenvolvimento do Django, você pode configurar um script **`post-save`** para executar o comando de compilação sempre que um arquivo SCSS for modificado.

---