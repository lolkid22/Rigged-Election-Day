#No Name Corp.
#Sam Ni, Jeffery Wong, Eldon Wu
#Rigged:Election Day
#Hillary Clinton must go on a mission to stop Donald Trump from winning the
#election because she found out about Trump’s evil plans for America, you must
#rig the election!Use the spacebar, the right, and left arrow keys to play.
from gamelib import*
game = Game(1500,600,"Rigged:Election Day")
bk = Image("eldon.png",game)
bk.resizeTo(1600,600)
bk.draw()
hillary = Image("Hillaryclinton.png",game)
hillary.resizeBy(-50)
hillary.moveTo(500,360)
trump = Image("trump.png",game)
trump.moveTo(1100,360)
booth = Image("FotingBooth.png",game)
booth.moveTo(1300,370)
steve = Image("bodyguard.png",game)
steve.resizeBy(-75)
steve.moveTo(999,400)
vote = Image("Bullet.png",game)
vote.resizeBy(-96)
vote.setSpeed(5,90)
vote.visible = True
realvote = Image("realvote.png",game)
realvote.resizeTo(vote.width,vote.height)
realvote.setSpeed(4,randint(-10,180))
platform = Image("god.png",game)
platform.resizeTo(booth.width,100)
boomboom = Animation("explosjon3.png",16,game,512/16,512/16)
boomboom.visible = False
voter = Image("Voter.png",game)
voter.resizeBy(-75)
voter.moveTo(50,360)
titlebk2 = Image("trumhead.png",game)
titlebk2.moveTo(300,600)
titlebk1 = Image("hillhead.png",game)
titlebk1.moveTo(250,450)
titlebk1.resizeBy(-20)
mugshot = Image("headofgod.png",game)
mugshot.resizeTo(450,450)
mugshot.moveTo(1300,400)
shotmug = Image("headofdog.png",game)
shotmug.resizeTo(500,500)
shotmug.moveTo(900,350)
jeffrey = Image("Jeffrey.png",game)
jeffrey.resizeTo(game.width,game.height)
play = Image("experiment.png",game)
play.moveTo(190,418)
font = Image("helpme.png",game)
font.resizeBy(-50)
font.moveTo(977,70)
otherfont = Image("damnit.png",game)
otherfont.resizeTo(font.width,font.height)
otherfont.moveTo(977,118)
introductions = Image("dance.png",game)
introductions.resizeBy(-60)
introductions.moveTo(270,530)
spacebar = Image("otherdance.png",game)
spacebar.resizeBy(-65)
spacebar.moveTo(100,530)
win = Image("goodending.png",game)
win.resizeTo(font.width,font.height)
win.moveTo(977,70)
lose = Image("trueending.png",game)
lose.resizeTo(font.width,font.height)
lose.moveTo(977,70)
levelfont = Image("level2.png",game)
levelfont.moveTo(levelfont.x,50)
#Image Test
'''while not game.over:
    game.processInput()
    #hillary.draw()
    #trump.draw()
    #booth.draw()
    #steve.draw()
    #vote.draw()
    #platform.draw()
    #boomboom.draw()
    #voter.draw()
    
    game.update(30)'''
uranus = [] 
for index in range(100):
    uranus.append(Image("Bullet.png",game))    
for index in range(100):
    uranus[index].resizeBy(-96)
    x = randint(100,1500)
    y = randint(100,600)
    uranus[index].moveTo(x, -y)
    uranus[index].setSpeed(2,180)

saturn = []
for index in range(50):
    saturn.append(Image("Bullet.png",game))
for index in range(50):
    saturn[index].resizeBy(-96)
    saturn[index].setSpeed(5,180)

jupiter = []
for index in range(50):
    jupiter.append(Image("realvote.png",game))
for index in range(50):
    jupiter[index].resizeBy(-96)
    jupiter[index].setSpeed(5,180)

mars = []
for index in range(100):
    mars.append( Image( "god.png",game))
    mars[index].resizeTo(booth.width,100)
for index in range(100):
    x = randint(100,700)
    y = randint(100,4000)
    mars[index].moveTo(x, -y)
    mars[index].setSpeed(2,180)

venus = []
for index in range(50):
    venus.append(Image("Bullet.png",game))
for index in range(50):
    venus[index].resizeBy(-96)
    venus[index].setSpeed(2,90)

#Title Screen
game.over = False
while not game.over:
    game.processInput()

    jeffrey.draw()
    play.draw()
    font.draw()
    otherfont.draw()
    shotmug.draw()
    mugshot.draw()
    introductions.draw()
    spacebar.draw()
    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True

    game.update(30)

#Level 1
game.over = False
Tvotes = 20
Cvotes = 0
votecount = 1
timecount = 100
while not game.over:
    game.processInput()
    bk.draw()
    booth.draw()
    hillary.draw()
    vote.move(False)
    steve.move(True)
    realvote.move(True)
    'steve.visible = False'
    #Venus
    for index in range(50):
        if vote.collidedWith(steve,"rectangle"):
            venus[index].move(True)
    #Saturn
    for index in range(50):
        saturn[index].moveTo(hillary.x,hillary.y)
        saturn[index].visible = False
        saturn[index].move(True)
        if saturn[index].isOffScreen("top") and saturn[index].visible:
            saturn[index].visible = False
        if keys.Pressed[K_DOWN] and vote.move(False):
            vote.moveTo(hillary.x,hillary.y)
            vote.visible = True
            vote.setSpeed(1,-90)
    #Don't use Jupiter

    #mars and uranus having a blast!
    for index in range(100):
        #mars[index].move()
        uranus[index].move()
        '''if mars[index].isOffScreen("bottom") and mars[index].visible:
            #mars[index].visible = False'''
        if uranus[index].isOffScreen("bottom") and uranus[index].visible:
            uranus[index].visible = False
        '''if mars[index].collidedWith(vote):
            vote.visible = False
            boomboom.moveTo(mars[index].x,mars[index].y)
            boomboom.visible = True'''
        if uranus[index].collidedWith(hillary,"rectangle"):
            votecount += randint(1,2)
            uranus[index].visible = False
        if uranus[index].collidedWith(steve,"rectangle"):
            uranus[index].visible = False
    if vote.collidedWith(realvote):
        vote.visible = False
    if vote.collidedWith(steve,"rectangle"):
        vote.setSpeed(4,randint(-10,180))
        steve.health -= randint(10,30)
    if vote.collidedWith(hillary,"rectangle"):
        vote.visible = False
        hillary.health -= randint(0,40)
    if realvote.collidedWith(hillary,"rectangle"):
        realvote.visible = False
        hillary.health -= randint(0,40)
    if steve.health <=1:
        steve.moveTo(999999,999999)
        steve.visible = False
    if vote.collidedWith(booth):
        vote.visible = False
        Cvotes +=1
        Tvotes -=1
        realvote.visible = True
        realvote.moveTo(booth.x,booth.y)
        realvote.setSpeed(5,randint(10,180))
        realvote.visible = True
    if hillary.collidedWith(steve,"rectangle"):
        hillary.moveTo(500,360)
        hillary.health -= randint(10,40)
    if hillary.isOffScreen():
        hillary.moveTo(400,360)
    if Cvotes <= Tvotes-1:
        steve.visible = True
        steve.draw()
    if votecount <=0:
        game.over = True
    if Cvotes >= Tvotes+1:
        game.drawText("You Win!",100,5)
        game.over = True
    if hillary.health <=1:
        game.over = True
    '''if keys.Pressed[K_UP] and vote.isOffScreen():
        vote.moveTo(hillary.x,hillary.y+10)
        vote.visible = True
        vote.setSpeed(4,0)
        votecount -=1
    if keys.Pressed[K_DOWN] and vote.isOffScreen():
        vote.moveTo(hillary.x+10,hillary.y)
        vote.visible = True
        vote.setSpeed(4,-90)
        votecount -=1#votecount goes down by more than one'''
    if keys.Pressed[K_SPACE] and vote.isOffScreen():
        vote.moveTo(hillary.x+65,hillary.y)
        vote.visible = True
        vote.setSpeed(4,-90)
        votecount -=1
    if keys.Pressed[K_RIGHT]:
        hillary.y += 7
        hillary.x += 3
        hillary.y -= 7
    if keys.Pressed[K_LEFT]:
        hillary.y += 7
        hillary.x -= 3
        hillary.y -= 7

    game.drawText("Health: " + str(hillary.health),hillary.x - 40 ,hillary.y - 110)
    game.drawText("Health: " + str(steve.health),steve.x - 40 ,steve.y - 110)
    game.drawText("Ammo: " + str(votecount),50,550)
    game.drawText("Votes For Clinton: " + str(Cvotes),150,550)
    game.drawText("Votes For Trump: " + str(Tvotes),320,550)
    #game.displayTime(50,525)
    game.update(60)

#Level 2
game.over = False
hillary.health = 100
Tvotes = 25
while not game.over and hillary.health > 1:
    game.processInput()
    bk.draw()
    booth.draw()
    hillary.draw()
    vote.move(False)
    trump.move(True)
    realvote.move(True)
    levelfont.draw()
    'steve.visible = False'
    #Venus
    for index in range(50):
        if vote.collidedWith(steve,"rectangle"):
            venus[index].move(True)
    #Saturn
    for index in range(50):
        saturn[index].moveTo(hillary.x,hillary.y)
        saturn[index].visible = False
        saturn[index].move(True)
        if saturn[index].isOffScreen("top") and saturn[index].visible:
            saturn[index].visible = False
        if keys.Pressed[K_DOWN] and vote.move(False):
            vote.moveTo(hillary.x,hillary.y)
            vote.visible = True
            vote.setSpeed(1,-90)
    #Don't use Jupiter

    #mars and uranus having a blast!
    for index in range(50):
        #mars[index].move()
        uranus[index].move()
        if uranus[index].isOffScreen("bottom") and uranus[index].visible:
            uranus[index].visible = False
        if uranus[index].collidedWith(hillary,"rectangle"):
            votecount += randint(1,2)
            uranus[index].visible = False
        if uranus[index].collidedWith(steve,"rectangle"):
            uranus[index].visible = False
    if vote.collidedWith(realvote):
        vote.visible = False
    if vote.collidedWith(trump,"rectangle"):
        vote.setSpeed(4,randint(-10,180))
        trump.health -= randint(10,30)
    if vote.collidedWith(hillary,"rectangle"):
        vote.visible = False
        hillary.health -= randint(0,40)
    if realvote.collidedWith(hillary,"rectangle"):
        realvote.visible = False
        hillary.health -= randint(0,40)
    if trump.health <=1:
        trump.moveTo(999999,999999)
        trump.visible = False
    if vote.collidedWith(booth):
        vote.visible = False
        Cvotes +=1
        Tvotes -=1
        realvote.visible = True
        realvote.moveTo(booth.x,booth.y)
        realvote.setSpeed(5,randint(10,180))
        realvote.visible = True
    if hillary.collidedWith(steve,"rectangle"):
        hillary.moveTo(500,360)
        hillary.health -= randint(10,40)
    if hillary.isOffScreen():
        hillary.moveTo(400,360)
    if Cvotes <= Tvotes-1:
        steve.visible = True
        steve.draw()
    if votecount <=0:
        game.over = True
    if Cvotes >= Tvotes+1:
        game.drawText("You Win!",100,5)
        game.over = True
    if hillary.health <=1:
        game.over = True
    if keys.Pressed[K_SPACE] and vote.isOffScreen():
        vote.moveTo(hillary.x+65,hillary.y)
        vote.visible = True
        vote.setSpeed(4,-90)
        votecount -=1
    if keys.Pressed[K_RIGHT]:
        hillary.y += 7
        hillary.x += 3
        hillary.y -= 7
    if keys.Pressed[K_LEFT]:
        hillary.y += 7
        hillary.x -= 3
        hillary.y -= 7

    game.drawText("Health: " + str(hillary.health),hillary.x - 40 ,hillary.y - 110)
    game.drawText("Health: " + str(trump.health),trump.x - 40 ,trump.y - 110)
    game.drawText("Ammo: " + str(votecount),50,550)
    game.drawText("Votes For Clinton: " + str(Cvotes),150,550)
    game.drawText("Votes For Trump: " + str(Tvotes),320,550)
    #game.displayTime(50,525)
    game.update(60)

#End Screen
game.over = False
while not game.over:
    game.processInput()
    jeffrey.draw()
    if Cvotes >= Tvotes:
        titlebk1.draw()
        win.draw()
    if Cvotes <= Tvotes:
        titlebk2.draw()
        lose.draw()
    if keys.Pressed[K_SPACE]:
        game.over = True
    
    game.update(60)
game.quit()
