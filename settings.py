import os
from dotenv import load_dotenv, find_dotenv

env = os.getenv('PYTHON_ENV', 'development')

files = {
    'production': '.env',
    'development': '.env.development'
}

file = files.get(env)

try:
    dotenv_path = find_dotenv(file)
    if dotenv_path:
        load_dotenv(dotenv_path)
    else:
        raise FileNotFoundError(f'File {file} not found')
except Exception as e:
    print(f'Error load file: {e}')

URL = os.getenv('URL')
