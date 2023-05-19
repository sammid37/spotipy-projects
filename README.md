# Criando playlists com spotipy

Com apenas um arquivo de texto que contém o nome de vários artistas, você pode criar uma playlist no Spotify que contém as top 3 músicas de cada um deles. 

## ✏️ Tecnologias utilizadas
* Python 3.10.9
* [Spotipy 2.23.0](https://spotipy.readthedocs.io/en/2.19.0/)

# ⚙️ Configurações
1. Instale as dependências `pip3 install -r requirements.txt`
2. Insira o nome dos artistas ou bandas no arquivo `artistas.txt`.
3. Altere as informações do arquivo ```secrets.py```
   1. O `user_id` é encontrado ao final da URL do seu perfil do Spotify, por exemplo: https://open.spotify.com/user/seu_user_está_aqui
   2. Para obter: `client_id`, `client_secret` e gerar um `redirect_uri` é necessário fazer no login em [**Spotify fo Developers**](https://developer.spotify.com/dashboard/login) utilizando sua conta do Spotify.
      1. Acessar o [Dashboard](https://developer.spotify.com/dashboard/applications) e criar uma uma aplicação/app 
         ![alt text](https://1.bp.blogspot.com/-2HyMxEQCMbg/YXwgSOWDLTI/AAAAAAAALcE/_9RoB0mnI0okZEWDrZyAREJJQ0lCi-Q_wCLcBGAsYHQ/s1347/Screenshot%2B2021-10-29%2Bat%2B13-12-09%2BMy%2BDashboard%2BSpotify%2Bfor%2BDevelopers.png)
         ![alt text](https://1.bp.blogspot.com/-omkrJ5ZkoAs/YXwgSHc3YlI/AAAAAAAALcI/8xudZoz3OTg7rdAdLpn6WVilUFCmYa8zwCLcBGAsYHQ/s793/Screenshot%2B2021-10-29%2Bat%2B13-13-44%2BMy%2BDashboard%2BSpotify%2Bfor%2BDevelopers.png)
      2. Acessar a aplicação e obter: `client_id` e o `client_secret`
         ![alt text](https://lh3.googleusercontent.com/-0upB7IdnhYw/YXwhwEuEoHI/AAAAAAAALcc/IN_dUfmvMJMZF9qjvobg_Unhbj_wCzfsACLcBGAsYHQ/pixelado_oficial.png)
      3. Editar as configurações do aplicativo e inserir uma **Redirect URI**, utilizei: *http://localhost:8080/callback*
         ![alt text](https://1.bp.blogspot.com/-QXHsGCKShOY/YXwgSNn6pqI/AAAAAAAALcQ/Of98UbeUnO0lcXQNowwCG4AJbufsXef6wCLcBGAsYHQ/s549/Screenshot%2B2021-10-29%2Bat%2B13-15-41%2BMy%2BDashboard%2BSpotify%2Bfor%2BDevelopers.png)
4. Executar a aplicação: `python3 spotipy-create-playlist.py`

# ✏️ Futuras implementações e funcionalidades
- Criar funções para a criação de diferentes tipos de playlist e um menu de opções;
   - [x] Playlist a partir de nome de artistas
   - [ ] Playlist a partir do gênero musical
   - [ ] Enriquecer playlist
- Adicionar uma capa automática para a playlist;
- Criar uma versão web do script;
