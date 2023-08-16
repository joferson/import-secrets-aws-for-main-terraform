# Documentação - Como Rodar o Script de Importação de Segredos para Terraform

## Passo 1: Instalação das Ferramentas Necessárias

### 1.1 Instalar Python

1. **O que é?**  
   Python é a linguagem que a gente usou pra escrever esse script. Você precisa dele pra rodar o script.

2. **Como instala?**  
   Entra no site oficial (https://www.python.org/downloads/) e baixa a versão mais recente. Só seguir os passos que aparecem na tela, é bem tranquilo.

### 1.2 Instalar o Terraform

1. **O que é?**  
   O Terraform é o cara que vai cuidar de organizar nossos segredos na AWS.

2. **Como instala?**  
   Entra na página de downloads do Terraform (https://www.terraform.io/downloads.html), escolhe o sistema operacional que você tá usando e segue as instruções.

### 1.3 Instalar o AWS CLI

1. **O que é?**  
   É uma ferramenta que a gente usa pra conversar com os serviços da AWS direto do nosso terminal.

2. **Como instala?**  
   Entra nesse link (https://aws.amazon.com/pt/cli/) e segue os passos. É rapidinho.

### 1.4 Instalar o Boto3

1. **O que é?**  
   É a biblioteca do Python que a gente usa pra conversar com a AWS.

2. **Como instala?**  
   Abre o terminal e digita:
   ```
   pip install boto3
   ```
   (Se o `pip` não estiver instalado, ele é instalado junto com o Python. Se deu problema, googla "instalar pip" que é fácil de resolver).

## Passo 2: Configurar a AWS CLI

1. **O que é?**  
   Antes do script conversar com a AWS, ele precisa saber quem é você e quais permissões você tem.

2. **Como faz?**  
   Abre o terminal e digita:
   ```
   aws configure
   ```
   Ele vai pedir umas informações, que você pega lá no teu painel da AWS (Access Key, Secret Key, etc).  
   Pra região, coloca `sa-east-1` (ou outra região que você prefira).

## Passo 3: Rodar o Script

1. **O que é?**  
   Agora é a hora da verdade. Vamos rodar nosso script e ver a mágica acontecer!

2. **Como faz?**  
   Navega no terminal até onde tá o nosso script e digita:
   ```
   python nome_do_script.py
   ```
   (troca `nome_do_script.py` pelo nome que tá o nosso script, tipo `python import_secrets.py`).

3. **O que esperar?**  
   Se tudo deu certo, ele vai criar um arquivo `main.tf` com todas as configurações e vai mostrar umas mensagens tipo 'Arquivo main.tf gerado com sucesso.' e 'Todos os segredos foram importados.'.

## E isso é tudo, pessoal!

Depois disso, seu Terraform tá pronto pra gerenciar seus segredos na AWS. Se deu algum problema, respira fundo, lê a mensagem de erro e tenta de novo. Google é teu amigo nessas horas! 😉
