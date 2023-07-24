from dotenv import load_dotenv, dotenv_values
import os

load_dotenv()

def setEnvConfig():
    env = os.environ.get('env')
    config = {}
    if env == 'local':
        config = dotenv_values('.env_local')
    elif env == 'dev':
        config = dotenv_values('.env_dev')
    elif env == 'prod':
        config = dotenv_values('.env_prod')
    elif env == 'stage':
        config = dotenv_values('.env_stage')
    elif env == 'unittest':
        config = dotenv_values('.env_unittest')

    return config