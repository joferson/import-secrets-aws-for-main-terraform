Claro! Abaixo está o conteúdo formatado para um arquivo README.md. Esse arquivo pode ser colocado na raiz do projeto do script para oferecer uma documentação clara e acessível sobre o que o script faz e como usá-lo.

---

# Script de Importação de Segredos para Terraform 🗝

## O que esse script faz? 🤔

Esse script é tipo um "faz-tudo" pra quem está usando o AWS Secrets Manager junto com o Terraform. Ele faz três coisas principais:

1. **Lista os Segredos:**  
   Ele pede pra AWS listar todos os segredos que você tem lá no Secrets Manager.

2. **Gera o Arquivo Terraform:**  
   Com essa lista de segredos, ele cria um arquivo chamado `main.tf`. Esse arquivo é uma receitinha que diz pro Terraform como gerenciar esses segredos.

3. **Inicializa e Importa os Segredos pro Terraform:**  
   Ele prepara o Terraform pra trabalhar com esses segredos e manda o Terraform importar todos eles.

## Antes de Começar: O que você vai precisar 🛠

- Python 3 instalado no seu computador.
- Terraform instalado no seu computador.
- AWS CLI instalado e configurado no seu computador.
- Boto3, que é a biblioteca do Python para a AWS.

(Sem stress, tá tudo explicado mais pra baixo como instalar e configurar essas coisas.)

## Passo a Passo: Como Rodar esse Script 🚀

### Passo 1: Instalação das Ferramentas Necessárias

#### 1.1 [Instalar Python](https://www.python.org/downloads/)
- **Como instala?**  
   Baixa a versão mais recente e instala seguindo os passos que aparecem na tela. É bem tranquilo.

#### 1.2 [Instalar o Terraform](https://www.terraform.io/downloads.html)
- **Como instala?**  
   Escolhe o sistema operacional que você tá usando e segue as instruções.

#### 1.3 [Instalar o AWS CLI](https://aws.amazon.com/pt/cli/)
- **Como instala?**  
   Entra nesse link e segue os passos. É rapidinho.

#### 1.4 Instalar o Boto3
- **Como instala?**  
   Abre o terminal e digita:

   ```sh
   pip install boto3
   ```

### Passo 2: Configurar a AWS CLI

- **Como faz?**  
   Abre o terminal e digita:

   ```sh
   aws configure
   ```
   Ele vai pedir umas informações que você pega lá no teu painel da AWS (Access Key, Secret Key, etc).  
   Pra região, coloca `sa-east-1` (ou outra região que você prefira).

### Passo 3: Rodar o Script

- **Como faz?**  
   Navega no terminal até onde tá o nosso script e digita:
   ```sh
   python nome_do_script.py
   ```
   (troca `nome_do_script.py` pelo nome que tá o nosso script, tipo `python import_secrets.py`).

- **O que esperar?**  
   Se tudo deu certo, ele vai criar um arquivo `main.tf` com todas as configurações e vai mostrar umas mensagens tipo 'Arquivo main.tf gerado com sucesso.' e 'Todos os segredos foram importados.'.

## Detalhes da Construção do Script

### Configurações Iniciais

```python
AWS_REGION = 'sa-east-1'
bucket_name = "terraform-southrock-uat"
key_name = "secrets-manager/ledger-secrets-uat.state"
```

Define as constantes utilizadas ao longo do script, incluindo a região da AWS, o nome do bucket S3 e a chave para o estado do Terraform.

### Funções

#### `list_secrets()`

```python
def list_secrets():
    ...
```

**Objetivo:** Lista todos os segredos armazenados no AWS Secrets Manager.  
**Retorno:** Uma lista contendo os nomes de todos os segredos armazenados.  
**Detalhes:** Utiliza o cliente `boto3` para acessar a AWS Secrets Manager e lida com a paginação da resposta da API.

#### `generate_terraform_config(secret_names)`

```python
def generate_terraform_config(secret_names):
    ...
```

**Objetivo:** Gerar o arquivo `main.tf` do Terraform que contém as definições de recursos para cada segredo da AWS.  
**Parâmetros:** 
- `secret_names`: Lista contendo os nomes dos segredos que devem ser gerenciados pelo Terraform.

#### `initialize_terraform()`

```python
def initialize_terraform():
    ...
```

**Objetivo:** Inicializar o Terraform na diretoria atual.  
**Detalhes:** Executa o comando `terraform init` através de um subprocesso. Este comando prepara o Terraform para aplicar as configurações presentes nos arquivos.

#### `import_secrets_to_terraform(secret_names)`

```python
def import_secrets_to_terraform(secret_names):
    ...
```

**Objetivo:** Importar os segredos da AWS Secrets Manager para o estado do Terraform.  
**Parâmetros:** 
- `secret_names`: Lista contendo os nomes dos segredos que devem ser importados para o estado do Terraform.  
**Detalhes:** Para cada segredo, executa o comando `terraform import` através de um subprocesso para trazer o segredo da AWS para o gerenciamento do Terraform.

## Execução do Script

Quando o script é executado, ele:

1. Obtém a lista de segredos com `list_secrets()`;
2. Gera o arquivo de configuração `main.tf` com `generate_terraform_config()`;
3. Inicializa o Terraform com `initialize_terraform()`;
4. Importa os segredos para o estado do Terraform com `import_secrets_to_terraform()`.

## E isso é tudo, pessoal!

Depois disso, seu Terraform tá pronto pra gerenciar seus segredos na AWS. Se deu algum problema, respira fundo, lê a mensagem de erro e tenta de novo. Google é teu amigo nessas horas! 😉

---

Este arquivo README.md pode ser colocado no diretório do seu projeto de código. Ele será apresentado de forma bem formatada quando alguém abrir o repositório do seu projeto no GitHub, por exemplo, facilitando o entendimento do que o projeto faz e como utilizá-lo.
