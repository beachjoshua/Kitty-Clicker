import pygame

class upgradeButton:
    def __init__(self, name, price, amtPerSec, x, y, imagePath=None):
        self.font=pygame.font.Font("PixelFont.ttf", 30)
        self.price = price
        self.amtPerSec = amtPerSec
        self.x = x
        self.y = y
        self.name = name
        self.text = self.font.render(str(f"{name} | Price:{self.price}"), True, "white")
        self.textRect = self.text.get_rect(topright=(x,y))
        
    #change methods   
    def changeXPos(self, x):
        self.x = x
        self.textRect = self.text.get_rect((self.x,self.y))
        
    def changeYPos(self, y):
        self.y = y
        self.textRect = self.text.get_rect((self.x,self.y))
        
    def updatePrice(self):
        self.price = int(self.price*1.5)
        self.text = self.font.render(str(f"{self.name} | Price:{self.price}"), True, "white")
        self.textRect = self.text.get_rect(topright=(self.x, self.y))
        
    #getter methods
    def getPrice(self):
        return self.price
    
    def getAmtPerSec(self):
        return self.amtPerSec
    
    def getTextRect(self):
        return self.textRect
    
    def getText(self):
        return self.text

#CAT ANIMATION IF MOUSE HOVERS
def catResizer(catRect, catResizeVal, catImage):
    mouseX, mouseY = pygame.mouse.get_pos()
    if catRect.collidepoint(mouseX, mouseY):
        if catResizeVal<10:
            catResizeVal += 1
    elif catResizeVal>0:
        catResizeVal -= 1
            
    resizedCat = pygame.transform.scale(catImage, (catImage.get_width() + catResizeVal, catImage.get_height() + catResizeVal))
    catRect = resizedCat.get_rect()
    catRect.x = (width - catRect.width) // 2
    catRect.y = (height - catRect.height) // 2
    
    return resizedCat, catRect, catResizeVal

if __name__ == "__main__":
    pygame.init()
    width, height = 1500, 800
    screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
    clock = pygame.time.Clock()
    pygame.display.set_caption("Kitty Clicker")
    running = True
    
    #cat vars
    catImagePath = "evil_cat.png"
    catImage = pygame.image.load(catImagePath)
    resizedCat = pygame.transform.scale(catImage, (catImage.get_width(), catImage.get_height()))
    catRect = resizedCat.get_rect()
    
    catRect.x = (width - catRect.width) // 2
    catRect.y = (height - catRect.height) // 2
    catResizeVal = 0
    
    font = pygame.font.Font("PixelFont.ttf", 52)
    catPointAmt = 0
    catPointText = font.render(str(catPointAmt), True, "white")
    catPointRect = catPointText.get_rect()
    catPointRect.x = (width - catPointRect.width)//2
    catPointRect.y = (height - catPointRect.height)
    
    #upgrades
    buttonWidth, buttonHeight = 150, 50
    upgradeX, upgradeY = width-25, 10
    upgradeList = []
    upgradeList.append(upgradeButton("Milk", 10, 1, upgradeX, upgradeY))
    upgradeList.append(upgradeButton("Kibble", 100, 2, upgradeX, upgradeY+buttonHeight))
    upgradeList.append(upgradeButton("Treats", 500, 4, upgradeX, upgradeY+buttonHeight*2))
    upgradeList.append(upgradeButton("Catnip", 1000, 6, upgradeX, upgradeY+buttonHeight*3))
    amtPerSec = 0
    
    fps = 120
    framesElapsed = 0
    
    while(running):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
                
            elif event.type == pygame.VIDEORESIZE:
                #set minimum possible window size
                width, height = event.size
                if(width<=2.5*catRect.width):
                    width = 2.5*catRect.width
                if(height<=2.5*catRect.height):
                    height = 2.5*catRect.height
                screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
                #resize cat object
                resizedCat = pygame.transform.scale(catImage, (catImage.get_width() + catResizeVal, catImage.get_height() + catResizeVal))
                catRect = resizedCat.get_rect()
                catRect.x = (width - catRect.width) // 2
                catRect.y = (height - catRect.height) // 2
                
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()
                if catRect.collidepoint(mouseX, mouseY):
                    catPointAmt += 1
                for upgrade in upgradeList:
                    if upgrade.getTextRect().collidepoint(mouseX, mouseY) and upgrade.getPrice()<=catPointAmt:
                        catPointAmt-=upgrade.getPrice()
                        amtPerSec += upgrade.getAmtPerSec()
                        upgrade.updatePrice()
        
        
        if(framesElapsed==fps):
            framesElapsed=0
            catPointAmt += amtPerSec
            
        
        screen.fill("tan")
        
        #cat animation
        resizedCat, catRect, catResizeVal = catResizer(catRect, catResizeVal, catImage)
        
        catPointText = font.render(str(catPointAmt), True, "white")
        catPointRect = catPointText.get_rect()
        catPointRect.x = (width - catPointRect.width)//2
        catPointRect.y = (height - catPointRect.height)//4
        
        screen.blit(catPointText, catPointRect)
        screen.blit(resizedCat, catRect)
        for upgrade in upgradeList:
            screen.blit(upgrade.getText(), upgrade.getTextRect())
        
        framesElapsed+=1
        pygame.display.flip()
        clock.tick(fps)
    
    pygame.quit()
