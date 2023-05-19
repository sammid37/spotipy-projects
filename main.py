# dependências
import menu
from termcolor import colored
from spotipy_func import autenticar_spotify
from secrets import client_id, client_secret, redirect_uri
 
# Programa principal
sp = autenticar_spotify(client_id, client_secret, redirect_uri)
if sp:
  print(colored("Autenticação bem-sucedida!\n", "green",attrs=["bold"]))
  menu.menu(sp) # menu de opções
else:
  print("Falha na autenticação. Verifique suas credenciais e a configuração da biblioteca Spotipy.")
