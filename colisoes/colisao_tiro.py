class ColisaoTiro:

    def colisao_tanque(tiro, tanque):
        
        if tiro.x - tanque.x < 30 and tiro.x - tanque.x >= -9\
        and tiro.y - tanque.y < 30 and tiro.y - tanque.y >= -9:
            return True

    def iscoliding0(tiro):
        if tiro.x + tiro.velocidade >=  760:
            return True
        elif tiro.y > 270 and tiro.y < 360:
            if tiro.x + tiro.velocidade >= 120\
            and tiro.x + tiro.velocidade <  140:
                return True
            elif tiro.x + tiro.velocidade >= 660\
            and tiro.x + tiro.velocidade < 680:
                return True  
        return False

    def iscoliding45(tiro):
        if tiro.x + (tiro.velocidade/2) >= 730\
        or tiro.y - (tiro.velocidade/2) < 50:
            return True
            # 250 pela inclinação
        elif tiro.y - (tiro.velocidade/2) > 270\
        and tiro.y - (tiro.velocidade/2) < 360:
            if tiro.x + (tiro.velocidade/2) >= 120\
            and tiro.x + (tiro.velocidade/2) < 140:
                return True
            elif tiro.x + (tiro.velocidade/2) >= 660\
            and tiro.x + (tiro.velocidade/2) < 680:
                return True
        tiro.x += (tiro.velocidade/2)
        tiro.y -= (tiro.velocidade/2)
        return False

    def iscoliding90(tiro):
        if tiro.y - tiro.velocidade <= 50:
            return True
        elif tiro.y - tiro.velocidade < 360\
        and tiro.y - tiro.velocidade > 270:
            if tiro.x > 120 and tiro.x < 140:
                return True
            elif tiro.x > 660 and tiro.x < 680:
                return 
        tiro.y -= tiro.velocidade
        return False

    def iscoliding135(tiro):
        if tiro.x - (tiro.velocidade/2) <= 40\
            or tiro.y - (tiro.velocidade/2) <= 50:
            return True
            # 250 pela inclinação
        elif tiro.y - (tiro.velocidade/2) > 270\
        and tiro.y - (tiro.velocidade/2) < 360:
            if tiro.x - (tiro.velocidade/2) >= 120\
            and tiro.x - (tiro.velocidade/2) < 140:
                return True
            elif tiro.x - (tiro.velocidade/2) >= 660\
            and tiro.x - (tiro.velocidade/2) < 680:
                return True
        tiro.x -= (tiro.velocidade/2)
        tiro.y -= (tiro.velocidade/2)
        return False

    def iscoliding180(tiro):
        if tiro.x - tiro.velocidade <= 40:
            return True
        elif tiro.y > 270 and tiro.y < 360:
            if tiro.x - tiro.velocidade > 120\
            and tiro.x - tiro.velocidade <= 140:
                return True
            elif tiro.x - tiro.velocidade > 660\
            and tiro.x - tiro.velocidade <= 680:
                return True
        tiro.x -= tiro.velocidade
        return False

    def iscoliding225(tiro):
        if tiro.x - (tiro.velocidade/2) <= 40\
        or tiro.y + (tiro.velocidade/2) > 560:
            return True
        elif tiro.y + (tiro.velocidade/2) > 270\
        and tiro.y + (tiro.velocidade/2) < 360:
            if tiro.x - (tiro.velocidade/2) >= 120\
            and tiro.x - (tiro.velocidade/2) < 140:
                return True
            if tiro.x - (tiro.velocidade/2) >= 660\
            and tiro.x - (tiro.velocidade/2) < 680:
                return True
        tiro.x -= (tiro.velocidade/2)
        tiro.y += (tiro.velocidade/2)
        return False

    def iscoliding270(tiro):
        if tiro.y + tiro.velocidade >= 560:
            return True
        elif tiro.y + tiro.velocidade >= 270\
        and tiro.y + tiro.velocidade < 360:
            if tiro.x > 120 and tiro.x < 140:
                return True
            if tiro.x > 660 and tiro.x < 680:
                return True
        tiro.y += tiro.velocidade
        return False
        
    def iscoliding315(tiro):
        if tiro.x + (tiro.velocidade/2) >= 760\
        or tiro.y + (tiro.velocidade/2) >= 560:
            return True
        elif tiro.y + (tiro.velocidade/2) >= 270\
        and tiro.y + (tiro.velocidade/2) < 360:
            if tiro.x + (tiro.velocidade/2) >= 120\
            and tiro.x + (tiro.velocidade/2) < 140:
                return True
            if tiro.x + (tiro.velocidade/2) >= 660\
            and tiro.x + (tiro.velocidade/2) < 680:
                return True
        tiro.x += (tiro.velocidade/2)
        tiro.y += (tiro.velocidade/2)
        return False

    iscoliding = {
        0: iscoliding0,
        45: iscoliding45,
        90: iscoliding90,
        135: iscoliding135,
        180: iscoliding180,
        225: iscoliding225,
        270: iscoliding270,
        315: iscoliding315

    }
class ColisaoTiroMapa:

    def iscoliding0(tiro, mapa):
        if mapa == 1:
            if tiro.x + tiro.velocidade >= 240 and tiro.x + tiro.velocidade < 280\
                and tiro.y > 90 and tiro.y < 200:
                return True
            if tiro.x + tiro.velocidade >= 500 and tiro.x + tiro.velocidade < 540\
                and tiro.y > 410 and tiro.y < 510:
                return True
            if tiro.x + tiro.velocidade >= 365 and tiro.x + tiro.velocidade < 425\
                and tiro.y > 280 and tiro.y < 330:
                return True
        else:
            if tiro.x + tiro.velocidade >= 340 and tiro.x + tiro.velocidade <= 450\
                and tiro.y > 245 and tiro.y < 355:
                return True
        return False
    def iscoliding45(tiro, mapa):
        if mapa == 1:
            if tiro.x + (tiro.velocidade/2) >= 240 and tiro.x + (tiro.velocidade/2) < 280\
                and tiro.y - (tiro.velocidade/2) > 90 and tiro.y - (tiro.velocidade/2) < 200:
                return True
            if tiro.x + (tiro.velocidade/2) >= 500 and tiro.x + (tiro.velocidade/2) < 540\
                and tiro.y- (tiro.velocidade/2) > 400 and tiro.y- (tiro.velocidade/2) < 510:
                return True
            if tiro.x + (tiro.velocidade/2) >= 365 and tiro.x + (tiro.velocidade/2) < 425\
                and tiro.y- (tiro.velocidade/2) > 270 and tiro.y- (tiro.velocidade/2) < 330:
                return True
        else:
            if tiro.x + (tiro.velocidade/2) >= 340 and tiro.x + (tiro.velocidade/2) <= 450\
                and tiro.y - (tiro.velocidade/2) > 245 and tiro.y - (tiro.velocidade/2) < 355:
                return True
        return False
    def iscoliding90(tiro, mapa):
        if mapa == 1:
            if tiro.y - tiro.velocidade >= 100 and tiro.y - tiro.velocidade <= 200\
                and tiro.x > 240 and tiro.x < 280:
                return True
            if tiro.y - tiro.velocidade >= 410 and tiro.y - tiro.velocidade <= 510\
                and tiro.x > 500 and tiro.x < 540:
                return True
            if tiro.y - tiro.velocidade >= 280 and tiro.y - tiro.velocidade <= 330\
                and tiro.x > 365 and tiro.x < 425:
                return True
        else:
            if tiro.y - tiro.velocidade >= 245 and tiro.y - tiro.velocidade <= 355\
                and tiro.x > 340 and tiro.x < 450:
                return True
        return False
    def iscoliding135(tiro, mapa):
        if mapa == 1:
            if tiro.x - (tiro.velocidade/2) >= 240 and tiro.x - (tiro.velocidade/2) <= 280\
                and tiro.y - (tiro.velocidade/2) > 90 and tiro.y - (tiro.velocidade/2) < 200:
                return True
            if tiro.x - (tiro.velocidade/2) >= 500 and tiro.x - (tiro.velocidade/2) <= 540\
                and tiro.y - (tiro.velocidade/2) > 400 and tiro.y - (tiro.velocidade/2) < 510:
                return True
            if tiro.x - (tiro.velocidade/2) >= 365 and tiro.x - (tiro.velocidade/2) <= 425\
                and tiro.y - (tiro.velocidade/2) > 270 and tiro.y - (tiro.velocidade/2) < 330:
                return True
        else:
            if tiro.x - (tiro.velocidade/2) >= 340 and tiro.x - (tiro.velocidade/2) <= 450\
                and tiro.y - (tiro.velocidade/2) > 245 and tiro.y - (tiro.velocidade/2) < 355:
                return True
        return False
    def iscoliding180(tiro, mapa):
        if mapa == 1:
            if tiro.x - tiro.velocidade >= 240 and tiro.x - tiro.velocidade < 280\
                and tiro.y > 90 and tiro.y < 200:
                return True
            if tiro.x - tiro.velocidade >= 500 and tiro.x - tiro.velocidade < 540\
                and tiro.y > 400 and tiro.y < 510:
                return True
            if tiro.x - tiro.velocidade >= 365 and tiro.x - tiro.velocidade < 425\
                and tiro.y > 270 and tiro.y < 330:
                return True
        else:
            if tiro.x - tiro.velocidade >= 340 and tiro.x - tiro.velocidade <= 450\
                and tiro.y > 245 and tiro.y < 355:
                return True
        return False
    def iscoliding225(tiro, mapa):
        if mapa == 1:
            if tiro.x - (tiro.velocidade/2) >= 240 and tiro.x - (tiro.velocidade/2) < 280\
                and tiro.y + (tiro.velocidade/2) > 90 and tiro.y + (tiro.velocidade/2) < 200:
                return True
            if tiro.x - (tiro.velocidade/2) >= 500 and tiro.x - (tiro.velocidade/2) < 540\
                and tiro.y + (tiro.velocidade/2) > 400 and tiro.y + (tiro.velocidade/2) < 510:
                return True
            if tiro.x - (tiro.velocidade/2) >= 365 and tiro.x - (tiro.velocidade/2) < 425\
                and tiro.y + (tiro.velocidade/2) > 270 and tiro.y + (tiro.velocidade/2) < 330:
                return True
        else:
            if tiro.x - (tiro.velocidade/2) >= 340 and tiro.x - (tiro.velocidade/2) <= 450\
                and tiro.y + (tiro.velocidade/2) > 245 and tiro.y + (tiro.velocidade/2) < 355:
                return True
        return False
    def iscoliding270(tiro, mapa):
        if mapa == 1:
            if tiro.y + tiro.velocidade >= 100 and tiro.y + tiro.velocidade < 200\
                and tiro.x > 240 and tiro.x < 280:
                return True
            if tiro.y + tiro.velocidade >= 410 and tiro.y + tiro.velocidade < 510\
                and tiro.x > 500 and tiro.x < 540:
                return True
            if tiro.y + tiro.velocidade >= 280 and tiro.y + tiro.velocidade < 330\
                and tiro.x > 365 and tiro.x < 425:
                return True
        else:
            if tiro.y + tiro.velocidade >= 245 and tiro.y + tiro.velocidade <= 355\
                and tiro.x > 340 and tiro.x < 450:
                return True
        return False
    def iscoliding315(tiro, mapa):
        if mapa == 1:
            if tiro.x + (tiro.velocidade/2) >= 240 and tiro.x + (tiro.velocidade/2) < 280\
                and tiro.y + (tiro.velocidade/2) > 90 and tiro.y + (tiro.velocidade/2) < 200:
                return True
            if tiro.x + (tiro.velocidade/2) >= 500 and tiro.x + (tiro.velocidade/2) < 540\
                and tiro.y + (tiro.velocidade/2) > 400 and tiro.y + (tiro.velocidade/2) < 510:
                return True
            if tiro.x + (tiro.velocidade/2) >= 365 and tiro.x + (tiro.velocidade/2) < 425\
                and tiro.y + (tiro.velocidade/2) > 270 and tiro.y + (tiro.velocidade/2) < 330:
                return True
        else:
            if tiro.x + (tiro.velocidade/2) >= 340 and tiro.x + (tiro.velocidade/2) <= 450\
                and tiro.y + (tiro.velocidade/2) > 245 and tiro.y + (tiro.velocidade/2) < 355:
                return True
    


    iscoliding = {
        0: iscoliding0,
        45: iscoliding45,
        90: iscoliding90,
        135: iscoliding135,
        180: iscoliding180,
        225: iscoliding225,
        270: iscoliding270,
        315: iscoliding315
    }
