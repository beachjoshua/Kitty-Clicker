import pygame

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
        
        
        if(framesElapsed==fps):
            framesElapsed=0
            
        
        screen.fill("tan")
        
        #cat animation
        resizedCat, catRect, catResizeVal = catResizer(catRect, catResizeVal, catImage)
        
        catPointText = font.render(str(catPointAmt), True, "white")
        catPointRect = catPointText.get_rect()
        catPointRect.x = (width - catPointRect.width)//2
        catPointRect.y = (height - catPointRect.height)//4
        
        screen.blit(catPointText, catPointRect)
        screen.blit(resizedCat, catRect)
        
        framesElapsed+=1
        pygame.display.flip()
        clock.tick(fps)
    
    pygame.quit()