import os
from termcolor import colored
from spotipy_func import criar_playlist_artist, salvar_id_playlist, exibir_dicionario

def menu(sp):
  dicionario_playlists = {}
  while True:
    title = colored('♫ M', 'magenta', attrs=['bold']) + colored(' E', 'green', attrs=['bold']) + colored(' N', 'yellow', attrs=['bold']) + colored(' U ♫', 'magenta', attrs=['bold'])

    print(title)
    print("1. Criar nova playlist com base nos artistas")
    print("2. Criar nova playlist com base em gênero musical")
    print("3. Atualizar uma playlist dado um ID")
    print("4. Exibir playlists criadas")
    print("5. Sair")
    print("-"*42)
    opcao = input(colored("\nDigite uma opção: ", "white", attrs=["bold"]))
    print()

    if opcao == "1":
      p_id = criar_playlist_artist(sp)
      salvar_id_playlist(p_id, dicionario_playlists)
      limpar_terminal()
    elif opcao == "2":
      print("Em breve.\n")
      limpar_terminal()
      # criar_playlist_genero(sp)
      # salvar_id_playlist("ID_PLAYLIST_AQUI", dicionario_playlists)
    elif opcao == "3":
      print("Em breve.\n")
      limpar_terminal()
      # atualizar_playlist(sp)
    elif opcao == "4":
      exibir_dicionario(dicionario_playlists)
      limpar_terminal()
    elif opcao == "5":
      print("Saindo do menu...\n")
      break
    else:
      print("Opção inválida. Por favor, escolha novamente.\n")

def limpar_terminal():
  # Limpar o terminal de acordo com o sistema operacional
  if os.name == "posix":
    os.system("clear")  # No Unix/Linux/Mac
  elif os.name == "nt":
    os.system("cls")  # No Windows