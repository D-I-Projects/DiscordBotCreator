import os
from dotenv import load_dotenv

class token:
    @staticmethod #ka. was das macht bzw. habe ich es vergessen gab es aber in C# auch :D
    def load_token():
        load_dotenv() #eig voll unnötig aber egal

    @staticmethod
    def read_token():
        return os.getenv('DISCORD_BOT_TOKEN')
    
    @staticmethod
    def create_token(token):
        with open('.env', 'a') as f:
            f.write(f'DISCORD_BOT_TOKEN={token}\n')
    
    @staticmethod
    def delete_token():
        if os.path.exists('.env'):
            with open('.env', 'r') as f:
                lines = f.readlines()
            with open('.env', 'w') as f:
                for line in lines:
                    if not line.startswith('DISCORD_BOT_TOKEN'):
                        f.write(line)

#Example
#Token.load_token() um die datei zu laden
#print(Token.read_token()) #um denn token zu lesen
#Token.create_token('your_token_here') #token datei erstellen
#Token.delete_token() #token löschen

#Soon
#switch_token 