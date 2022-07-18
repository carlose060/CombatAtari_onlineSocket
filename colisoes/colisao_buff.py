class ColisaoBuff:

    def iscoliding(tanque):
        if tanque.x > 120 and tanque.x <= 180:
            if tanque.y > 270 and tanque.y <= 330:
                return True
        return False
