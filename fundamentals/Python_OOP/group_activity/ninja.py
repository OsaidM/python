class snowBall:
    def __init__(self, damage, speed, x, y):
        self.damage = damage # 15 minus points if hit for example
        self.speed = speed # 3 for example
    
    def range():
        rng = 70
        newP = player.position + rng
        return newP
        
    def position(x,y):
        x = self.x
        y = self.y
        return x,y
        
    def hit():
        if enemy.position == self.position:
                enemy.health = enemy.health - self.damage
        return enemy.health        

class ninja:
    def __init__(self, health, lives):
        self.health = health # default 100 point  
        self.lives = lives # 3 lives for starter
    
    def position(x,y):
        pass
    def moving(x,y):
        pass
    
    def throwing(self, range):
        newP = self.position + range
        return newP
       

player = ninja(100,3)
enemy = ninja(100,1)
ball = snowBall(15, 3, 35,35)
