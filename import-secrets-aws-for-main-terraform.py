import boto3
import json
import subprocess

# Configura a região da AWS aqui. 
# Por exemplo, para São Paulo, o código é 'sa-east-1'.
AWS_REGION = 'sa-east-1'

def list_secrets():
    # Conecta com o serviço Secrets Manager da AWS e pega a lista de segredos.
    client = boto3.client('secretsmanager', region_name=AWS_REGION)
    response = client.list_secrets()
    secret_names = [secret['Name'] for secret in response['SecretList']]
    return secret_names

def get_secret_value(secret_name):
    # Pega o valor de um segredo específico pelo nome dele.
    client = boto3.client('secretsmanager', region_name=AWS_REGION)
    response = client.get_secret_value(SecretId=secret_name)
    return response['SecretString']

def format_secret_string(secret_value_json):
    # Formata o JSON do segredo para um formato bonito e fácil de ler.
    secret_dict = json.loads(secret_value_json)
    formatted_string = '{\n'
    for key, value in secret_dict.items():
        formatted_string += f'    "{key}": "{value}",\n'
    formatted_string = formatted_string.rstrip(',\n') + '\n  }'
    return formatted_string

def generate_terraform_config(secret_names):
    # Gera o arquivo main.tf do Terraform.
    # Esse arquivo vai conter todas as configurações pra gerenciar os segredos na AWS.
    with open('main.tf', 'w') as file:
        file.write('provider "aws" {\n')
        file.write(f'  region = "{AWS_REGION}"\n')
        file.write('}\n\n')

        for secret in secret_names:
            secret_value = get_secret_value(secret)
            formatted_secret_string = format_secret_string(secret_value)
            resource_name = secret.replace('-', '_').lower()
            
            file.write(f'resource "aws_secretsmanager_secret" "{resource_name}" {{\n')
            file.write(f'  name = "{secret}"\n')
            file.write('}\n\n')
            
            file.write(f'resource "aws_secretsmanager_secret_version" "{resource_name}_version" {{\n')
            file.write(f'  secret_id     = aws_secretsmanager_secret.{resource_name}.id\n')
            file.write('  secret_string = <<EOT\n')
            file.write(f'{formatted_secret_string}\n')
            file.write('  EOT\n')
            file.write('}\n\n')

def initialize_terraform():
    # Inicializa o Terraform. Isso prepara o Terraform pra executar comandos.
    subprocess.run(["terraform", "init"])

def import_secrets_to_terraform(secret_names):
    # Importa os segredos pra o estado do Terraform.
    # Isso faz o Terraform "saber" sobre os segredos que já existem na AWS.
    for secret in secret_names:
        resource_name = secret.replace('-', '_').lower()
        print(f"Importing secret: {secret}")
        subprocess.run(["terraform", "import", f"aws_secretsmanager_secret.{resource_name}", secret])

if __name__ == '__main__':
    # Inicia a bagunça! :)
    secrets = list_secrets()
    generate_terraform_config(secrets)
    print('Arquivo main.tf gerado com sucesso.')
    initialize_terraform()
    import_secrets_to_terraform(secrets)
    print('Todos os segredos foram importados.')
