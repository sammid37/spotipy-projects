# Samantha Dantas Medeiros (28/10/2021)
# Cria uma playlist com as 3 principais músicas de cada artista presente em um arquivo.txt

import spotipy
from datetime import datetime
from spotipy.oauth2 import SpotifyOAuth
from secrets import user_id, client_id, client_secret, redirect_uri

# Abrindo o arquivo no modo de leitura
arquivo = open("artistas.txt", "r")
artista = [i.strip('\n') for i in arquivo.readlines()] # armazena o nome dos artistas
qtd_artistas = len(artista) # contando quantos nomes há no arquivo

# Autentificação de usuário
# Preencha o arquivo secrets.py com seus dados
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=client_id,
        client_secret=client_secret,
        redirect_uri=redirect_uri,
        scope="playlist-modify-public"
    )
)

# Criando uma playlist
hoje = datetime.now()
hoje_str = hoje.strftime("[%d/%b/%Y]")
print("Criando uma nova playlist...")
nome_playlist = "Python Spotipy " + hoje_str
sp.user_playlist_create(
    user_id, 
    nome_playlist, 
    public=True, 
    collaborative=False, 
    description='Esta playlist foi criada utilizando a API do Spotify e a biblioteca spotipy.'
)

# coletando o id da playlist, será usado posteriormente para adicionar as músicas na playlist
playlist_info = sp.current_user_playlists(limit=1, offset=0)
playlist_id = playlist_info["items"][0]["id"]

# Buscandos os artistas :D
print("Recolhendo id dos artistas")

artistas_id = [] # vai armazenar os ids de cada artista
for i in artista:
    # realizando a busca, q="nome do artista atual na lista"
    busca_id = sp.search(q=i, limit=1, offset=0, type='artist', market=None)
    artistas_id.append(busca_id["artists"]["items"][0]["id"])

# Buscando as top 3 músicas de cada artista
print("Salvando as top 3 músicas dos artistas")
musica_info = [] # armazena a busca pelas top músicas
musica_titulo = [] # armazena os títulos das músicas
musica_uri = [] # armazena o uri de cada música

for i in range(qtd_artistas):
    busca_top_musicas = sp.artist_top_tracks(artistas_id[i])
    for track in busca_top_musicas["tracks"][:3]:
        # musica_info.append(busca_top_musicas["tracks"][0]["name"])
        musica_titulo.append(track["name"])
        musica_uri.append(track["uri"])

# Adicionando as top 3 músicas de cada artista na playlist
sp.playlist_add_items(playlist_id, musica_uri) 
print(f"As seguintes músicas foram salvas: {musica_titulo}")