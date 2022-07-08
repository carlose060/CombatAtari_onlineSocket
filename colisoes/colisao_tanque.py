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
