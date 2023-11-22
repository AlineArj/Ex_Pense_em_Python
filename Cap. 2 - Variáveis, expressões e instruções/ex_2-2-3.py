# Se eu sair da minha casa às 6:52 e correr 1 quilômetro a um certo passo (8min e 15s por quilometro),
# então 3 quilômetros a um passo mais rápido (7min e 12s por quilômetro) e 1 quilômetro no mesmo passo 
# usado em primeiro lugar, que horas chego em casa para o café da manhã?

def TempoTrajeto(d, h, m, s):
    tempo_s = ((h * 3600) + (m * 60) + s) * d
    return tempo_s

def Conversão(s):
    if s >= 3600:
        h = int(s / 3600)
        s %= 3600
    else:
        h = 0
        
    if s >= 60:
        m = int(s / 60)
        s %= 60
    else:
        m = 0
    
    hora_str = str(h) + ":" + str(m) + ":" + str(s)
    return(hora_str)


t_inicial = TempoTrajeto(1, 6, 52, 0)
t_duracao = TempoTrajeto(1, 0, 8, 15)
t_duracao += TempoTrajeto(3, 0, 7, 12)

t_final = Conversão(t_inicial+t_duracao)
print(t_final)