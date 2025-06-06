import os
from app import create_app

# Obter configuração do ambiente
config_name = os.environ.get('FLASK_CONFIG', 'default')

# Criar a aplicação
app = create_app(config_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
