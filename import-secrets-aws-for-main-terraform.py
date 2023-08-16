import boto3
import json
import subprocess

# Configurações
AWS_REGION = 'sa-east-1'
bucket_name = "my-bucket-45646" #lembre de criar o bucket antes de rodar para evitar erros.
key_name = "secrets-manager/my-secrets.state"

def list_secrets():
    """Lista todos os segredos usando a paginação da AWS."""
    client = boto3.client('secretsmanager', region_name=AWS_REGION)
    response = client.list_secrets()
    secret_names = [secret['Name'] for secret in response['SecretList']]

    # Tratar paginação
    while 'NextToken' in response:
        response = client.list_secrets(NextToken=response['NextToken'])
        secret_names.extend(secret['Name'] for secret in response['SecretList'])
    
    print(f"Listados {len(secret_names)} secrets.")
    return secret_names

def get_secret_value(secret_name):
    """Pega o valor de um segredo específico pelo nome."""
    client = boto3.client('secretsmanager', region_name=AWS_REGION)
    response = client.get_secret_value(SecretId=secret_name)
    return response['SecretString']

def format_secret_string(secret_value_json):
    """Formata o JSON do segredo para um formato legível."""
    secret_dict = json.loads(secret_value_json)
    formatted_string = '{\n'
    for key, value in secret_dict.items():
        formatted_string += f'    "{key}": "{value}",\n'
    formatted_string = formatted_string.rstrip(',\n') + '\n  }'
    return formatted_string

def generate_terraform_config(secret_names):
    """Gera o arquivo main.tf do Terraform."""
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

def generate_backend_config():
    """Gera o arquivo backend.tf do Terraform."""
    with open('backend.tf', 'w') as file:
        file.write('terraform {\n')
        file.write('  backend "s3" {\n')
        file.write(f'    bucket = "{bucket_name}"\n')
        file.write(f'    key    = "{key_name}"\n')
        file.write(f'    region  = "{AWS_REGION}"\n')        
        file.write('  }\n')
        file.write('}\n')

def initialize_terraform():
    """Inicializa o Terraform."""
    subprocess.run(["terraform", "init"])

def import_secrets_to_terraform(secret_names):
    """Importa os segredos para o estado do Terraform."""
    for secret in secret_names:
        resource_name = secret.replace('-', '_').lower()
        print(f"Importando segredo: {secret}")
        subprocess.run(["terraform", "import", f"aws_secretsmanager_secret.{resource_name}", secret])

if __name__ == '__main__':
    secrets = list_secrets()
    generate_terraform_config(secrets)
    generate_backend_config()
    print('Arquivos main.tf e backend.tf gerados com sucesso.')
    initialize_terraform()
    import_secrets_to_terraform(secrets)
    print('Todos os segredos foram importados.')
