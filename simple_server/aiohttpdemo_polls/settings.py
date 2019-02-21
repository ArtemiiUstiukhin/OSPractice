import pathlib
import yaml

BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / 'config' / 'polls.yaml'

def get_config(path):
    with open(str(path),"r") as f:
        config = yaml.load(f)
    return config

config = get_config(config_path)
