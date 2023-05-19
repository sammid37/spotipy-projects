import base64
import spotipy
from termcolor import colored
from datetime import datetime
from spotipy.oauth2 import SpotifyOAuth
from secrets import user_id, client_id, client_secret, redirect_uri

def autenticar_spotify(client_id, client_secret, redirect_uri):
  scope = "playlist-modify-public"  # Escopo para permissão de modificação de playlists públicas

  try:
    sp = spotipy.Spotify(
      auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope=scope
      )
    )
    return sp
  # Mensagem de erro caso não consiga autenticar o usuário
  except spotipy.oauth2.SpotifyOAuthError as e:
      print("Erro ao autenticar no Spotify:", e)
      return None

def salvar_id_playlist(id_playlist, dicionario):
  novo_id = len(dicionario) + 1
  dicionario[novo_id] = id_playlist
  print(colored(f"Playlist criada com sucesso! ID: {novo_id}.", "yellow"))
  print("-"*42)

def exibir_dicionario(dicionario):
  print(colored("Playlists criadas:", "magenta", attrs=["bold"]))
  for chave, valor in dicionario.items():
    print(f"♫ ID: {chave} | Playlist ID: {valor}")
  print()

def upload_cover(playlist_id):
  scope = "ugc-image-upload"
  spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(
  scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))
  # reformat encoding jpg -> base64
  with open("spotipy_cover.jpg", 'rb') as image:
    cover_encoded = base64.b64encode(image.read()).decode("utf-8")

  return cover_encoded

def criar_playlist_artist(sp):
  if sp is None:
    print("Você não está autenticado. Por favor, faça a autenticação antes de criar uma playlist.")
    return
  
  print("Criando nova playlist...")
  
  # Abrindo o arquivo no modo de leitura
  arquivo = open("artistas.txt", "r")
  artista = [i.strip('\n') for i in arquivo.readlines()] # armazena o nome dos artistas
  qtd_artistas = len(artista) # contando quantos nomes há no arquivo

  # Definindo nome da playlist
  hoje = datetime.now()
  hoje_str = hoje.strftime("[%d/%b/%Y]")
  nome_playlist = "Python Spotipy " + hoje_str

  # Adicionando informações da playlist
  sp.user_playlist_create(
    user_id, 
    nome_playlist, 
    public=True, # playlist pública
    collaborative=False, 
    description='Esta playlist foi criada utilizando a API do Spotify e a biblioteca spotipy.'
  )

  # coletando o id da playlist, será usado posteriormente para adicionar as músicas na playlist
  playlist_info = sp.current_user_playlists(limit=1, offset=0)
  playlist_id = playlist_info["items"][0]["id"]

  artistas_id = [] # vai armazenar os ids de cada artista
  for i in artista:
    # realizando a busca, q="nome do artista atual na lista"
    busca_id = sp.search(q=i, limit=1, offset=0, type='artist', market=None)
    artistas_id.append(busca_id["artists"]["items"][0]["id"])

  # Buscando as top 3 músicas de cada artista
  qtd_fav = int(input("Quantas músicas favoritas de cada artista você deseja adicionar? "))
  print(f"Salvando as top {qtd_fav} músicas dos artistas")
  musica_info = [] # armazena a busca pelas top músicas
  musica_titulo = [] # armazena os títulos das músicas
  musica_uri = [] # armazena o uri de cada música

  for i in range(qtd_artistas):
    busca_top_musicas = sp.artist_top_tracks(artistas_id[i])
    # Buscando as top x músicas de cada artista
    for track in busca_top_musicas["tracks"][:qtd_fav]: # fatiamento
      musica_titulo.append(track["name"])
      musica_uri.append(track["uri"])

  # Adicionando as top x músicas de cada artista na playlist
  sp.playlist_add_items(playlist_id, musica_uri) 

  print(colored(f"♪ As seguintes músicas foram salvas:", "yellow", attrs=["bold"]))
  print('\n'.join(map(str, musica_titulo)))
  print("-"*42)

  return playlist_id
