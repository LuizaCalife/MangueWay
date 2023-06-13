import cv2 as video_player

# Leitor do arquivo contendo as direções da música
# em um dispositivo

arquivo = open('txt.txt', "wt+")

a = open(arquivo, "rt", encoding='utf8')
lista_musicas = a.read()
lista_musicas = lista_musicas.split('\n')

musicas_escolhidas = []

# Função 1: Sensor de presença
# O sensor de presença é ativado pela função sensor_presenca(),
# que imprime a mensagem "Sensor de presença ativado" 
# e chama a função reproduzir_video() para cada uma das músicas.
def sensor_presenca():
    print("Sensor de presença ativado")
    return True

# Função 2: Pause
# A função pause() pausa a apresentação do vídeo. 
# Ela imprime a mensagem "Apresentação de vídeo pausada"
# e chama o método pause() do objeto video_player para pausar a reprodução do vídeo.
def pause():
    print("Apresentação de vídeo pausada.")
    video_player.pause()

# Função 3: Continuar
# A função continuar() retoma a apresentação do vídeo após uma pausa.
# Ela imprime a mensagem "Apresentação de vídeo retomada"
# e chama o método play() do objeto 
def continuar():
    print("Apresentação de vídeo retomada.")
    video_player.play()

# Função 4: Reiniciar
# A função reiniciar() reinicia a apresentação do vídeo. 
# Ela imprime a mensagem "Apresentação de vídeo reiniciada"
# e chama o método seek(0) do objeto video_player para reiniciar o vídeo a partir do início.
def reiniciar():
    print("Apresentação de vídeo reiniciada.")
    video_player.seek(0)
def reiniciar():
    print("Apresentação de vídeo reiniciada.")
    video_player.seek(0)

# Função 5: Encerrar
# A função encerrar() encerra a apresentação do vídeo.
# Ela imprime a mensagem "Apresentação de vídeo encerrada"
# e chama o método pause() do objeto video_player para interromper a reprodução do vídeo.
def encerrar():
    print("Apresentação de vídeo encerrada.")
    video_player.pause()

# A função seletor_de_musicas(lista_musicas, musicas_escolhidas)
# permite que o usuário escolha até três músicas da lista lista_musicas.
# As músicas escolhidas são armazenadas na lista musicas_escolhidas.
def seletor_de_musicas(lista_musicas, musicas_escolhidas):
    cont = 1
    for i in lista_musicas:
        print(f'{cont} - {i}')
        cont += 1
    cont = 1

    try:
        for i in range(3):
            while True:
                try:
                    musica = int(input(f'Digite a {cont} música escolhida: '))
                    musica -= 1

                    if musica < 0 or musica >= len(lista_musicas):
                        print("Música inválida. Tente novamente.")
                    else:
                        musicas_escolhidas.append(lista_musicas[musica])
                        cont += 1
                        break
                except ValueError:
                    print("Entrada inválida. Digite um número válido.")
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário.")

    return musicas_escolhidas

# 
def reproduzir_video(caminho_arquivo):
    cap = video_player.VideoCapture(caminho_arquivo)

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        video_player.imshow('Reprodução de Vídeo', frame)

        if video_player.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    video_player.destroyAllWindows()

# Exemplo de uso:
while True:
    # Se o sensor de presença for ativado vai rodar as outras funções
    if (sensor_presenca()):
        # Primeiro a escolha das músicas
        file = seletor_de_musicas(lista_musicas, musicas_escolhidas)
        # Vai rodar o vídeo em sequencia de escolha
        print(file)
        for item in file:
            reproduzir_video(item)