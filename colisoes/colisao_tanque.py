class Colisao():

    def iscoliding0(tanque):
        if tanque.x + tanque.velocidade >= 730:
            return True
        elif tanque.y > 242 and tanque.y < 360:
            if tanque.x + tanque.velocidade >= 90\
            and tanque.x + tanque.velocidade <  140:
                return True
            elif tanque.x + tanque.velocidade >= 630\
            and tanque.x + tanque.velocidade < 680:
                return True
        tanque.x += tanque.velocidade
        return False

    def iscoliding45(tanque):
        if tanque.x + (tanque.velocidade/2) >= 730\
        or tanque.y - (tanque.velocidade/2) < 50:
            return True
            # 250 pela inclinação
        elif tanque.y - (tanque.velocidade/2) > 250\
        and tanque.y - (tanque.velocidade/2) < 360:
            if tanque.x + (tanque.velocidade/2) >= 90\
            and tanque.x + (tanque.velocidade/2) < 140:
                return True
            elif tanque.x + (tanque.velocidade/2) >= 630\
            and tanque.x + (tanque.velocidade/2) < 680:
                return True
        tanque.x += (tanque.velocidade/2)
        tanque.y -= (tanque.velocidade/2)
        return False
        
    def iscoliding90(tanque):
        if tanque.y - tanque.velocidade <= 50:
            return True
        elif tanque.y - tanque.velocidade < 360\
        and tanque.y - tanque.velocidade > 270:
            if tanque.x > 90 and tanque.x < 140:
                return True
            elif tanque.x > 630 and tanque.x < 680:
                return True
        tanque.y -= tanque.velocidade
        return False

    def iscoliding135(tanque):
        if tanque.x - (tanque.velocidade/2) <= 40\
            or tanque.y - (tanque.velocidade/2) <= 50:
            return True
            # 250 pela inclinação
        elif tanque.y - (tanque.velocidade/2) > 250\
        and tanque.y - (tanque.velocidade/2) < 360:
            if tanque.x - (tanque.velocidade/2) >= 90\
            and tanque.x - (tanque.velocidade/2) < 140:
                return True
            elif tanque.x - (tanque.velocidade/2) >= 630\
            and tanque.x - (tanque.velocidade/2) < 680:
                return True
        tanque.x -= (tanque.velocidade/2)
        tanque.y -= (tanque.velocidade/2)
        return False
    def iscoliding180(tanque):
        if tanque.x - tanque.velocidade <= 40:
            return True
        elif tanque.y > 242 and tanque.y < 360:
            if tanque.x - tanque.velocidade > 120\
            and tanque.x - tanque.velocidade <= 140:
                return True
            elif tanque.x - tanque.velocidade > 660\
            and tanque.x - tanque.velocidade <= 680:
                return True
        tanque.x -= tanque.velocidade
        return False
    def iscoliding225(tanque):
        if tanque.x - (tanque.velocidade/2) <= 40\
        or tanque.y + (tanque.velocidade/2) > 530:
            return True
        elif tanque.y + (tanque.velocidade/2) > 250\
        and tanque.y + (tanque.velocidade/2) < 360:
            if tanque.x - (tanque.velocidade/2) >= 90\
            and tanque.x - (tanque.velocidade/2) < 140:
                return True
            if tanque.x - (tanque.velocidade/2) >= 630\
            and tanque.x - (tanque.velocidade/2) < 680:
                return True
        tanque.x -= (tanque.velocidade/2)
        tanque.y += (tanque.velocidade/2)
        return False
    def iscoliding270(tanque):
        if tanque.y + tanque.velocidade >= 530:
            return True
        elif tanque.y + tanque.velocidade >= 240\
        and tanque.y + tanque.velocidade < 360:
            if tanque.x > 90 and tanque.x < 140:
                return True
            if tanque.x > 630 and tanque.x < 680:
                return True
        tanque.y += tanque.velocidade
        return False
    def iscoliding315(tanque):
        if tanque.x + (tanque.velocidade/2) >= 730\
        or tanque.y + (tanque.velocidade/2) >= 530:
            return True
        elif tanque.y + (tanque.velocidade/2) >= 240\
        and tanque.y + (tanque.velocidade/2) < 360:
            if tanque.x + (tanque.velocidade/2) >= 90\
            and tanque.x + (tanque.velocidade/2) < 140:
                return True
            if tanque.x + (tanque.velocidade/2) >= 630\
            and tanque.x + (tanque.velocidade/2) < 680:
                return True
        tanque.x += (tanque.velocidade/2)
        tanque.y += (tanque.velocidade/2)
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

class ColisaoMapa:


    def iscoliding0(tanque, mapa):
        if mapa == 1:
            if tanque.x + tanque.velocidade >= 220 and tanque.x + tanque.velocidade <= 280\
                and tanque.y + tanque.velocidade >= 70 and tanque.y + tanque.velocidade <= 200:
                return True
            if tanque.x + tanque.velocidade >= 480 and tanque.x + tanque.velocidade <= 540\
                and tanque.y + tanque.velocidade >= 380 and tanque.y + tanque.velocidade <= 510:
                return True
            if tanque.x + tanque.velocidade >= 345 and tanque.x + tanque.velocidade <= 425\
                and tanque.y + tanque.velocidade >= 250 and tanque.y + tanque.velocidade <= 330:
                return True
        # Mapa 2 
        else:
            if tanque.x + tanque.velocidade >= 320 and tanque.x + tanque.velocidade <= 450\
                and tanque.y > 225 and tanque.y < 355:
                return True
        return False
        

    def iscoliding45(tanque, mapa):
        if mapa == 1:
            if tanque.x + (tanque.velocidade/2) >= 250 and tanque.x + (tanque.velocidade/2) <= 280\
                and tanque.y - (tanque.velocidade/2) > 70 and tanque.y - (tanque.velocidade/2) < 200:
                return True
            if tanque.x + (tanque.velocidade/2) >= 480 and tanque.x + (tanque.velocidade/2) <= 540\
                and tanque.y - (tanque.velocidade/2) >= 380 and tanque.y - (tanque.velocidade/2) <= 510:
                return True
            if tanque.x + (tanque.velocidade/2) >= 345 and tanque.x + (tanque.velocidade/2) <= 425\
                and tanque.y - (tanque.velocidade/2) >= 250 and tanque.y - (tanque.velocidade/2) <= 330:
                return True
        # Mapa 2        
        else:
            if tanque.x + (tanque.velocidade/2) >= 320 and tanque.x + (tanque.velocidade/2) <= 450\
                and tanque.y - (tanque.velocidade/2) > 225 and tanque.y - (tanque.velocidade/2) < 355:
                return True
        return False
    def iscoliding90(tanque, mapa):
        if mapa == 1:
            if tanque.x  <= 220 and tanque.x  >= 280\
                and tanque.y - tanque.velocidade >= 70 and tanque.y - tanque.velocidade <= 200:
                return True
            if tanque.x  <= 480 and tanque.x  >= 540\
                and tanque.y - tanque.velocidade >= 380 and tanque.y - tanque.velocidade <= 510:
                return True
            if tanque.x  <= 345 and tanque.x  >= 425\
                and tanque.y - tanque.velocidade >= 250 and tanque.y - tanque.velocidade <= 330:
                return True
        # Mapa 2
        else:
            if tanque.y - tanque.velocidade >= 225 and tanque.y - tanque.velocidade <= 355\
                and tanque.x > 320 and tanque.x < 450:
                return True
        return False
    def iscoliding135(tanque, mapa):
        if mapa == 1:
            if tanque.x - (tanque.velocidade/2) >= 220 and tanque.x - (tanque.velocidade/2) <= 280\
                and tanque.y - (tanque.velocidade/2) >= 70 and tanque.y - (tanque.velocidade/2) <= 200:
                return True
            if tanque.x - (tanque.velocidade/2) >= 480 and tanque.x - (tanque.velocidade/2) <= 540\
                and tanque.y - (tanque.velocidade/2) >= 380 and tanque.y - (tanque.velocidade/2) <= 510:
                return True
            if tanque.x - (tanque.velocidade/2) >= 345 and tanque.x - (tanque.velocidade/2) <= 425\
                and tanque.y - (tanque.velocidade/2) >= 250 and tanque.y - (tanque.velocidade/2) <= 330:
                return True
        # Mapa 2     
        else:
            if tanque.x - (tanque.velocidade/2) >= 320 and tanque.x - (tanque.velocidade/2) <= 450\
                and tanque.y - (tanque.velocidade/2) > 225 and tanque.y - (tanque.velocidade/2) < 355:
                return True
        return False
    def iscoliding180(tanque, mapa):
        if mapa == 1:
            if tanque.x - tanque.velocidade >= 220 and tanque.x - tanque.velocidade <= 280\
                and tanque.y >= 70 and tanque.y <= 200:
                return True
            if tanque.x - tanque.velocidade >= 480 and tanque.x - tanque.velocidade <= 540\
                and tanque.y >= 380 and tanque.y <= 510:
                return True
            if tanque.x - tanque.velocidade >= 345 and tanque.x - tanque.velocidade <= 425\
                and tanque.y >= 250 and tanque.y <= 330:
                return True
        # Mapa 2 
        else:
            if tanque.x - tanque.velocidade >= 320 and tanque.x - tanque.velocidade <= 450\
                and tanque.y > 225 and tanque.y < 355:
                return True
        return False
    def iscoliding225(tanque, mapa):
        if mapa == 1:
            if tanque.x - (tanque.velocidade/2) > 230 and tanque.x - (tanque.velocidade/2) <= 280\
                and tanque.y + (tanque.velocidade/2) >= 70 and tanque.y + (tanque.velocidade/2) <= 200:
                return True
            if tanque.x - (tanque.velocidade/2) > 480 and tanque.x - (tanque.velocidade/2) <= 540\
                and tanque.y + (tanque.velocidade/2) >= 380 and tanque.y + (tanque.velocidade/2) <= 510:
                return True
            if tanque.x - (tanque.velocidade/2) > 345 and tanque.x - (tanque.velocidade/2) <= 425\
                and tanque.y + (tanque.velocidade/2) >= 250 and tanque.y + (tanque.velocidade/2) <= 330:
                return True
        # Mapa 2 
        else:
            if tanque.x - (tanque.velocidade/2) >= 320 and tanque.x - (tanque.velocidade/2) <= 450\
                and tanque.y + (tanque.velocidade/2) > 225 and tanque.y + (tanque.velocidade/2) < 355:
                return True
        return False
    def iscoliding270(tanque, mapa):
        if mapa == 1:
            if tanque.x >= 230 and tanque.x <= 280\
                and tanque.y + tanque.velocidade >= 70 and tanque.y + tanque.velocidade <= 200:
                return True
            if tanque.x >= 480 and tanque.x <= 540\
                and tanque.y + tanque.velocidade >= 380 and tanque.y + tanque.velocidade <= 510:
                return True
            if tanque.x >= 345 and tanque.x <= 425\
                and tanque.y + tanque.velocidade >= 250 and tanque.y + tanque.velocidade <= 330:
                return True
        # Mapa 2 
        else:
            if tanque.y + tanque.velocidade >= 225 and tanque.y + tanque.velocidade <= 355\
                and tanque.x > 320 and tanque.x < 450:
                return True
        return False
    def iscoliding315(tanque, mapa):
        if mapa == 1:
            if tanque.x + (tanque.velocidade/2) >= 220 and tanque.x + (tanque.velocidade/2) <= 280\
                and tanque.y + (tanque.velocidade/2) >= 70 and tanque.y + (tanque.velocidade/2) <= 200:
                return True
            if tanque.x + (tanque.velocidade/2) >= 480 and tanque.x + (tanque.velocidade/2) <= 540\
                and tanque.y + (tanque.velocidade/2) >= 380 and tanque.y + (tanque.velocidade/2) <= 510:
                return True
            if tanque.x + (tanque.velocidade/2) >= 345 and tanque.x + (tanque.velocidade/2) <= 425\
                and tanque.y + (tanque.velocidade/2) >= 250 and tanque.y + (tanque.velocidade/2) <= 330:
                return True
        # Mapa 2 
        else:
            if tanque.x + (tanque.velocidade/2) >= 320 and tanque.x + (tanque.velocidade/2) <= 450\
                and tanque.y + (tanque.velocidade/2) > 225 and tanque.y + (tanque.velocidade/2) < 355:
                return True
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