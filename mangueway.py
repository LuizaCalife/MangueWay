import cv2 as video_player

# Leitor do arquivo contendo as direções da música
# em um dispositivo
fileloc = 'file_loc.txt'
a = open(fileloc, "rt", encoding='utf8')
lista_musicas = a.read()
lista_musicas = lista_musicas.split('\n')
a.close()
print(lista_musicas)
musicas_escolhidas = []


# Função 1: Sensor de presença
# O sensor de presença é ativado pela função sensor_presenca(),
# que imprime a mensagem "Sensor de presença ativado" 
# e chama a função reproduzir_video() para cada uma das músicas.
def sensor_presenca():
    print("Sensor de presença ativado")
    return True

# Função 2: Pause e Continuar
# A função pausar_e_continuar() pausa a apresentação do vídeo. 
# Ela imprime a mensagem "Apresentação de vídeo pausada"
# e chama o método pausar_e_continuar() do objeto video_player para pausar a reprodução do vídeo.
def pausar_e_continuar():
    print("Apresentação de vídeo pausada.")
    while True:
        key = video_player.waitKey(1) & 0xFF
        if key == ord('p'):
            break

# Função 3: Reiniciar
# A função reiniciar(cap) reinicia a apresentação do vídeo. 
# Ela imprime a mensagem "Apresentação de vídeo reiniciada"
# e chama o método set(video_player.CAP_PROP_POS_FRAMES, 0) do objeto video_player para reiniciar o vídeo a partir do início.
def reiniciar(cap):
    print("Apresentação de vídeo reiniciada.")
    cap.set(video_player.CAP_PROP_POS_FRAMES, 0)

# Função 4: Encerrar
# A função encerrar() encerra a apresentação do vídeo.
# Ela imprime a mensagem "Apresentação de vídeo encerrada"
# e chama o método destroyAllWindows() do objeto video_player para interromper a reprodução do vídeo.
def encerrar():
    print("Apresentação de vídeo encerrada manualmente.")
    video_player.destroyAllWindows()

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

# Função para reprodução do vídeo com uso do módulo cv2
def reproduzir_video(caminho_arquivo):
    cap = video_player.VideoCapture(caminho_arquivo)
    encerrar_video = False

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        video_player.imshow('Reprodução de Vídeo', frame)

        key = video_player.waitKey(1) & 0xFF
        if key == ord('p'):
            pausar_e_continuar()
        elif key == ord('r'):
            reiniciar(cap)
        elif key == ord('q'):
            encerrar_video = True
            break

    cap.release()
    video_player.destroyAllWindows()

    if encerrar_video:
        encerrar()

# Exemplo de uso:
while True:
    # Se o sensor de presença for ativado, vai rodar as outras funções
    if sensor_presenca():
        # Primeiro a escolha das músicas 
        file = seletor_de_musicas(lista_musicas, musicas_escolhidas)
        # Vai rodar o vídeo em sequência de escolha
        for item in file:
            reproduzir_video(item)

        break

print('Apresentação de vídeo encerrada')