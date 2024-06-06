from environs import Env

env = Env()

API_ID = env.str('API_ID')
API_HASH = env.str('API_HASH')
