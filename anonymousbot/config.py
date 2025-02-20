import yaml
import sys


path = "config/config.yaml"
if len(sys.argv) == 2:
    path = sys.argv[1]
try:
    with open(path, 'r') as stream:
        conf = yaml.load(stream, Loader=yaml.FullLoader)
except FileNotFoundError:
    print("\n\WARNING:\n"
            "before of running anonymousbot you should create a file named `config.yaml`"
            " in `config`.\n\nOpen `config/config.example.yaml`\ncopy all\ncreate a file "
            "named `config.yaml`\nPaste and replace sample variables with true data."
            "\nIf the file is in another path, you can specify it as the first parameter."
            "\nExample: <anonymousbot /home/my_files/config.yaml>")
    sys.exit()

BOT_TOKEN = conf['bot_token']
DB_PATH = conf['db_path']
ADMINS = conf['admins']
