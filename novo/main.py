import pygame
import random
import time

# Inicialização
pygame.init()
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Batman: Fuga de Gotham")

PRETO = (0, 0, 0)
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (20, 20, 100)
VERDE = (0, 255, 0)

clock = pygame.time.Clock()
FPS = 60
fonte = pygame.font.SysFont("Arial", 30)

# Superfícies
batman = pygame.Surface((50, 50))
batman.fill(AZUL)

joker = pygame.Surface((40, 40))
joker.fill(VERMELHO)

boss = pygame.Surface((60, 60))
boss.fill(VERDE)

def esperar_tecla():
    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            if evento.type == pygame.KEYDOWN:
                esperando = False

def mostrar_texto(titulo, subtitulo=None, pausa=True):
    TELA.fill(PRETO)
    texto1 = fonte.render(titulo, True, BRANCO)
    TELA.blit(texto1, (LARGURA // 2 - texto1.get_width() // 2, ALTURA // 2 - 40))
    if subtitulo:
        texto2 = fonte.render(subtitulo, True, BRANCO)
        TELA.blit(texto2, (LARGURA // 2 - texto2.get_width() // 2, ALTURA // 2 + 10))
    pygame.display.update()
    if pausa:
        esperar_tecla()

def colisao(rect1, rect2):
    return rect1.colliderect(rect2)

def jogar_fase(nome_fase, tempo_fase, spawn_rapido=False, boss_final=False):
    batman_x = 100
    batman_y = ALTURA // 2
    vidas = 3
    inimigos = []
    spawn_timer = 0
    tempo_inicio = time.time()
    fase_ativa = True

    while fase_ativa:
        clock.tick(FPS)
        tempo_atual = time.time()
        tempo_restante = tempo_fase - int(tempo_atual - tempo_inicio)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

        # Controles
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] and batman_y > 0:
            batman_y -= 5
        if teclas[pygame.K_DOWN] and batman_y < ALTURA - 50:
            batman_y += 5

        # Spawna inimigos
        spawn_timer += 1
        if spawn_timer > (30 if spawn_rapido else 50):
            spawn_timer = 0
            novo = {
                "x": LARGURA,
                "y": random.randint(0, ALTURA - 40),
                "vel": random.randint(5, 9)
            }
            inimigos.append(novo)

        for inimigo in inimigos[:]:
            inimigo["x"] -= inimigo["vel"]
            rect_bat = pygame.Rect(batman_x, batman_y, 50, 50)
            rect_inimigo = pygame.Rect(inimigo["x"], inimigo["y"], 40, 40)

            if colisao(rect_bat, rect_inimigo):
                vidas -= 1
                inimigos.remove(inimigo)
                if vidas <= 0:
                    mostrar_texto("Você falhou!", "Pressione qualquer tecla para tentar novamente")
                    return False

            if inimigo["x"] < -50:
                inimigos.remove(inimigo)

        # Boss da fase final
        if boss_final and tempo_restante <= 10:
            boss_rect = pygame.Rect(LARGURA - 100, ALTURA // 2, 60, 60)
            batman_rect = pygame.Rect(batman_x, batman_y, 50, 50)
            if colisao(batman_rect, boss_rect):
                mostrar_texto("O chefe te derrotou!", "Pressione qualquer tecla para tentar novamente")
                return False
            TELA.blit(boss, (LARGURA - 100, ALTURA // 2))

        # Desenhar cena
        TELA.fill(PRETO)
        TELA.blit(batman, (batman_x, batman_y))
        for inimigo in inimigos:
            TELA.blit(joker, (inimigo["x"], inimigo["y"]))

        texto_vidas = fonte.render(f"Vidas: {vidas}", True, BRANCO)
        texto_tempo = fonte.render(f"Tempo: {max(0, tempo_restante)}", True, BRANCO)
        TELA.blit(texto_vidas, (10, 10))
        TELA.blit(texto_tempo, (10, 50))
        pygame.display.update()

        if tempo_restante <= 0:
            return True

# === NARRATIVA ===
mostrar_texto("GOTHAM ESTÁ EM PERIGO", "Um novo plano do Coringa ameaça a cidade.")
mostrar_texto("BATMAN TEM UMA MISSÃO", "Ele precisa atravessar as zonas dominadas por vilões...")

# === FASE 1 ===
mostrar_texto("Fase 1: Ruas de Gotham", "Sobreviva por 30 segundos")
fase1 = jogar_fase("Ruas de Gotham", tempo_fase=30)
if not fase1:
    exit()

mostrar_texto("Jornal: Coringa foge da emboscada do Batman!", "Distrito Químico agora está sob ataque...")

# === FASE 2 ===
mostrar_texto("Fase 2: Distrito Químico", "Inimigos mais rápidos. Sobreviva 45 segundos.")
fase2 = jogar_fase("Distrito Químico", tempo_fase=45, spawn_rapido=True)
if not fase2:
    exit()

mostrar_texto("Alerta: Último sinal do Coringa vem da Torre Wayne.", "Batman se prepara para o confronto final...")

# === FASE 3 ===
mostrar_texto("Fase 3: Torre Wayne", "Sobreviva 60 segundos. Chefe final no fim!")
fase3 = jogar_fase("Torre Wayne", tempo_fase=60, boss_final=True)
if not fase3:
    exit()

# === FINAL ===
mostrar_texto("GOTHAM ESTÁ A SALVO", "Mas o Coringa nunca desaparece por muito tempo...")
mostrar_texto("FIM", "Pressione qualquer tecla para sair.")
pygame.quit()
