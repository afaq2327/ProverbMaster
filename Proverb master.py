import pygame ,random

def generate_proverb():
        global get
        get=list(master_it(lista))
        global quest
        quest=get[0].copy()
        global sol
        sol=get[1]
        print(quest)
        print(sol)

def quest_2():
    global quest2
    quest2=get[0]

def generate_test():
        get1=test_file[test_list[0]].split()
        global ans_test
        ans_test=get1.copy()
        global quest3
        quest3=ans_test.copy()
        random.shuffle(quest3)
                
                
def display_test_result():
        display.blit(background_image2,background_position)
        global test_list
        test_list=[0,1,2,3,4,5,6,7,8,9]
        opt=True
        while opt:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        opt=False
                        pygame.quit()
                        quit()
                total_master=wel_font.render(("Total Marks Gained:"+str(marks)),True,black)
                trect=total_master.get_rect()
                trect.midtop=(display_width/2,display_height/2)
                display.blit(total_master,trect)

                text=wel_font.render("MAIN MENU",True,black)
                trect=text.get_rect()
                trect.midtop=(400,500)
                
                pygame.draw.rect(display,(0,17,17),[320,500,160,50])
                display.blit(text,trect)

                pos=list(pygame.mouse.get_pos())
                
                if (pos[0]>=320 and pos[0]<=480) and pos[1]>=500 and pos[1]<=550:
                    pygame.draw.rect(display,black,[320,500,160,50],3)
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        pygame.mixer.Sound.play(click)
                        opt=False
                        welcome_screen()
                        
                pygame.display.update()
        
def display_result(sol,user_list):
    global ans
    ans=True
    global mastered
    if len(sol)==len(user_list):
        for x in range(0,len(sol)):
            if sol[x] == user_list[x]:
                if x==len(sol)-1:
                    checking_text=font.render("well done! you master it..",True,black)
                    pygame.mixer.Sound.play(sad)
                    display.blit(checking_text,(300,250))
                    
                    
                            
            else:
                checking_text=font.render("Sorry! you didn't master it..",True,black)
                pygame.mixer.Sound.play(sad)
                display.blit(checking_text,(320,250))
                ans=False
                break
    elif len(sol)!=len(user_list):
        checking_text=font.render("Sorry! you didn't master it..",True,black)
        ans=False
        pygame.mixer.Sound.play(sad)
        display.blit(checking_text,(300,250))
def reset_it():
        
        display.blit(background_image2,background_position)
        with open("proverb.txt","r") as text_file3:
                a1=text_file3.readlines()
                        
                reseting=a1.copy()
                print(len(reseting))
        with open("proverb2.txt","w") as again3:
                again3.writelines("".join(reseting))
                
        opt=True
        while opt:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        opt=False
                        pygame.quit()
                        quit()
                master_it(a)
                total_master=wel_font.render(("Total Proverbs Mastered:"+str(1000-total)),True,black)
                trect=total_master.get_rect()
                trect.midtop=(display_width/2,display_height/2)
                display.blit(total_master,trect)

                text=wel_font.render("MAIN MENU",True,black)
                trect=text.get_rect()
                trect.midtop=(400,500)
                reset=wel_font.render("RESET",True,black)
                trect3=text.get_rect()
                pygame.draw.rect(display,(0,17,17),[320,400,160,50])
                trect3.midtop=(430,400)
                
                pygame.draw.rect(display,(0,17,17),[320,500,160,50])
                display.blit(text,trect)
                display.blit(reset,trect3)
                

                pos=list(pygame.mouse.get_pos())
                
                if (pos[0]>=320 and pos[0]<=480) and pos[1]>=500 and pos[1]<=550:
                    pygame.draw.rect(display,black,[320,500,160,50],3)
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        pygame.mixer.Sound.play(click)
                        opt=False
                        welcome_screen()
        
                
                pygame.display.update()  

def stats():
        master_it(a)
        display.blit(background_image2,background_position)
        opt=True
        while opt:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        opt=False
                        pygame.quit()
                        quit()
                master_it(a)
                total_master=wel_font.render(("Total Proverbs Mastered:"+str(1000-total)),True,black)
                trect=total_master.get_rect()
                trect.midtop=(display_width/2,display_height/2)
                display.blit(total_master,trect)

                text=wel_font.render("MAIN MENU",True,black)
                trect=text.get_rect()
                trect.midtop=(400,500)
                reset=wel_font.render("RESET",True,black)
                trect3=text.get_rect()
                pygame.draw.rect(display,(0,17,17),[320,400,160,50])
                trect3.midtop=(430,400)
                
                pygame.draw.rect(display,(0,17,17),[320,500,160,50])
                display.blit(text,trect)
                display.blit(reset,trect3)
                

                pos=list(pygame.mouse.get_pos())
                
                if (pos[0]>=320 and pos[0]<=480) and pos[1]>=500 and pos[1]<=550:
                    pygame.draw.rect(display,black,[320,500,160,50],3)
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        pygame.mixer.Sound.play(click)
                        opt=False
                        welcome_screen()
                if (pos[0]>=320 and pos[0]<=480) and pos[1]>=400 and pos[1]<=450:
                    pygame.draw.rect(display,black,[320,400,160,50],3)
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        pygame.mixer.Sound.play(click)
                        reset_it()
                       
                
                pygame.display.update()

def test():
        test=True
        user_list2=[]
        generate_test()
        global marks
        marks=0
        while test:
                for event in pygame.event.get():
                        if event.type==pygame.QUIT:
                                pygame.quit()
                                quit()
                        if event.type==pygame.KEYDOWN:
                                if event.key==pygame.K_BACKSPACE:
                                        if len(user_list2)>=1:
                                                a=user_list2.pop()
                                                quest3.append(a)
                display.blit(background_image,background_position)
                
                lis=[10,20,130,50]
                for x in range(0,len(quest3)):
                    text=font.render(quest3[x],True,black)
                    trect=text.get_rect()
                    if x==5 or x==10:
                        lis[1]+=100
                        lis[0]=10
                    trect.midtop=(lis[0]+lis[2]/2,lis[1]+10)    
                    
                    pygame.draw.rect(display,color,lis,3)
                    display.blit(text,trect)
                    lis[0]+=150
                pos=list(pygame.mouse.get_pos())#generating list of current cursor position.....
    ####    
                if len(quest3)<=5:
                    if (pos[0]>=10 and pos[0]<=140) and (pos[1]>=20 and pos[1]<=70) and (len(quest3)>=1):
                        pygame.draw.rect(display,white,[10,20,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN :
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[0])
                            del quest3[0]
                    elif (pos[0]>=160) and (pos[0]<=290) and (pos[1]>=20 and pos[1]<=70) and (len(quest3)>=2):
                        pygame.draw.rect(display,white,[160,20,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[1])
                            del quest3[1]
                    elif (pos[0]>=310 and pos[0]<=440) and (pos[1]>=20 and pos[1]<=70) and (len(quest3)>=3):
                        pygame.draw.rect(display,white,[310,20,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[2])
                            del quest3[2]
                            
                    elif (pos[0]>=460 and pos[0]<=590) and (pos[1]>=20 and pos[1]<=70) and (len(quest3)>=4):
                        pygame.draw.rect(display,white,[460,20,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[3])
                            del quest3[3]
                            
                    elif (pos[0]>=610 and pos[0]<=740 )and (pos[1]>=20 and pos[1]<=70) and (len(quest3)>=5):
                        pygame.draw.rect(display,white,[610,20,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[4])
                            del quest3[4]
                            
            ####
                elif len(quest3)<=10 and len(quest3)>5:
                    if (pos[0]>=10 and pos[0]<=140) and (pos[1]>=20 and pos[1]<=70) and (len(quest3)>=1):
                        pygame.draw.rect(display,white,[10,20,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN :
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[0])
                            del quest3[0]
                    elif (pos[0]>=160) and (pos[0]<=290) and (pos[1]>=20 and pos[1]<=70) and (len(quest3)>=2):
                        pygame.draw.rect(display,white,[160,20,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[1])
                            del quest3[1]
                    elif (pos[0]>=310 and pos[0]<=440) and (pos[1]>=20 and pos[1]<=70) and (len(quest3)>=3):
                        pygame.draw.rect(display,white,[310,20,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[2])
                            del quest3[2]
                            
                    elif (pos[0]>=460 and pos[0]<=590) and (pos[1]>=20 and pos[1]<=70) and (len(quest3)>=4):
                        pygame.draw.rect(display,white,[460,20,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[3])
                            del quest3[3]
                            
                    elif (pos[0]>=610 and pos[0]<=740 )and (pos[1]>=20 and pos[1]<=70) and (len(quest3)>=5):
                        pygame.draw.rect(display,white,[610,20,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[4])
                            del quest3[4]

                        
                    elif (pos[0]>=10 and pos[0]<=140) and (pos[1]>=120 and pos[1]<=170) and (len(quest3)>=6):
                        pygame.draw.rect(display,white,[10,120,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[5])
                            del quest3[5]
                    elif (pos[0]>=160 and pos[0]<=290) and (pos[1]>=120 and pos[1]<=170) and (len(quest3)>=7):
                        pygame.draw.rect(display,white,[160,120,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[6])
                            del quest3[6]
                    elif (pos[0]>=310 and pos[0]<=440) and (pos[1]>=120 and pos[1]<=170) and (len(quest3)>=8):
                        pygame.draw.rect(display,white,[310,120,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[7])
                            del quest3[7]
                    elif (pos[0]>=460 and pos[0]<=590) and (pos[1]>=120 and pos[1]<=170)  and (len(quest3)>=9):
                        pygame.draw.rect(display,white,[460,120,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[8])
                            del quest3[8]
                    elif (pos[0]>=610 and pos[0]<=740) and (pos[1]>=120 and pos[1]<=170)  and (len(quest3)>=10):
                        pygame.draw.rect(display,white,[610,120,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[9])
                            del quest3[9]
            ####
                elif len(quest3)<=15 and len(quest3)>10:
                    if (pos[0]>=10 and pos[0]<=140) and (pos[1]>=20 and pos[1]<=70) and (len(quest3)>=1):
                        pygame.draw.rect(display,white,[10,20,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN :
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[0])
                            del quest3[0]
                    elif (pos[0]>=160) and (pos[0]<=290) and (pos[1]>=20 and pos[1]<=70) and (len(quest3)>=2):
                        pygame.draw.rect(display,white,[160,20,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[1])
                            del quest3[1]
                    elif (pos[0]>=310 and pos[0]<=440) and (pos[1]>=20 and pos[1]<=70) and (len(quest3)>=3):
                        pygame.draw.rect(display,white,[310,20,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[2])
                            del quest3[2]
                            
                    elif (pos[0]>=460 and pos[0]<=590) and (pos[1]>=20 and pos[1]<=70) and (len(quest3)>=4):
                        pygame.draw.rect(display,white,[460,20,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[3])
                            del quest3[3]
                            
                    elif (pos[0]>=610 and pos[0]<=740 )and (pos[1]>=20 and pos[1]<=70) and (len(quest3)>=5):
                        pygame.draw.rect(display,white,[610,20,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[4])
                            del quest3[4]

                        
                    elif (pos[0]>=10 and pos[0]<=140) and (pos[1]>=120 and pos[1]<=170) and (len(quest3)>=6):
                        pygame.draw.rect(display,white,[10,120,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[5])
                            del quest3[5]
                    elif (pos[0]>=160 and pos[0]<=290) and (pos[1]>=120 and pos[1]<=170) and (len(quest3)>=7):
                        pygame.draw.rect(display,white,[160,120,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[6])
                            del quest3[6]
                    elif (pos[0]>=310 and pos[0]<=440) and (pos[1]>=120 and pos[1]<=170) and (len(quest3)>=8):
                        pygame.draw.rect(display,white,[310,120,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[7])
                            del quest3[7]
                    elif (pos[0]>=460 and pos[0]<=590) and (pos[1]>=120 and pos[1]<=170)  and (len(quest3)>=9):
                        pygame.draw.rect(display,white,[460,120,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[8])
                            del quest3[8]
                    elif (pos[0]>=610 and pos[0]<=740) and (pos[1]>=120 and pos[1]<=170)  and (len(quest3)>=10):
                        pygame.draw.rect(display,white,[610,120,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[9])
                            del quest3[9]

                    elif (pos[0]>=10 and pos[0]<=140) and (pos[1]>=220 and pos[1]<=270) and (len(quest3)>=11):
                        pygame.draw.rect(display,white,[10,220,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[10])
                            del quest3[10]
                    elif (pos[0]>=160 and pos[0]<=290) and (pos[1]>=220 and pos[1]<=270) and (len(quest3)>=12):
                        pygame.draw.rect(display,white,[160,220,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[11])
                            del quest3[11]
                    elif (pos[0]>=310 and pos[0]<=440) and (pos[1]>=220 and pos[1]<=270) and (len(quest3)>=13):
                        pygame.draw.rect(display,white,[310,220,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[12])
                            del quest3[12]
                    elif (pos[0]>=460 and pos[0]<=590) and (pos[1]>=220 and pos[1]<=270)  and (len(quest3)>=14):
                        pygame.draw.rect(display,white,[460,220,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[13])
                            del quest3[13]
                    elif (pos[0]>=610 and pos[0]<=740) and (pos[1]>=220 and pos[1]<=270)  and (len(quest3)>=15):
                        pygame.draw.rect(display,white,[610,220,130,50],3)
                        if event.type==pygame.MOUSEBUTTONDOWN:
                            pygame.mixer.Sound.play(click)
                            user_list2.append(quest3[14])
                            del quest3[14]
        #enter button...
                display.fill(color,rect=[700,450,91,50])
                enter=font.render("NEXT",True,black)
                display.blit(enter,(710,460))

                if (pos[0]>=700 and pos[0]<=790) and pos[1]>=450 and pos[1]<=500:
                    display.fill(white,rect=[700,450,91,50])
                    display.blit(enter,(710,460))
                    if event.type==pygame.MOUSEBUTTONDOWN:
                        pygame.mixer.Sound.play(click)
                        if len(ans_test)==len(user_list2):
                                for x in range(0,len(ans_test)):
                                    if ans_test[x] == user_list2[x]:
                                        if x==len(ans_test)-1:
                                            user_list2=[]
                                            marks+=1
                                    else:
                                        user_list2=[]
                                        break
                        elif len(ans_test)!=len(user_list2):
                            user_list2=[]
                        del test_list[0]    
                        if len(test_list)>=1:
                                generate_test()
                        else:
                                
                                test=False
                                display_test_result()
                                
                                

                    
                        
        ###printing ans....
                lis2=[10,400,780,50]
                text=font.render(" ".join(user_list2),True,black)
                trect2=text.get_rect()
                trect2.midtop=(lis2[0]+lis2[2]/2,lis2[1]+10)
                pygame.draw.rect(display,color,lis2,3)
                display.blit(text,trect2)
                
                pygame.display.update()
                clock.tick(fps)
def welcome_screen():
    pygame.mixer.music.play(-1)
    welcome=True
    while welcome:

        font2=pygame.font.SysFont("monaco",95)
        font3=pygame.font.SysFont("monaco",40)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        
        display.blit(background_image2,background_position)
        welcome_text=font2.render("THE PROVERB MASTER",True,(255,102,0))
        perceeding_text=font3.render("The Objective Of The Game Is To Master 1000 Proverbs!!",True,(255,102,0))
        perceeding_text2=font3.render("Only Sincere Players Can MASTER IT!!",True,(255,102,0))
        
        display.blit(welcome_text,(10,50))
        display.blit(perceeding_text,(10,150))
        display.blit(perceeding_text2,(120,190))
        

        options_list=[40,300,200,50]
        options=["MASTER IT","TAKE TEST","STATISTICS","QUIT"]
        for x in range(0,len(options)):
            text=wel_font.render(options[x],True,black)
            trect=text.get_rect()
            trect.midtop=(options_list[0]+options_list[2]/2,options_list[1]+10)    
            
            pygame.draw.rect(display,(0,17,17),options_list)
            display.blit(text,trect)
            options_list[1]+=70

        pos=list(pygame.mouse.get_pos())
        if (pos[0]>=40 and pos[0]<=240) and pos[1]>=300 and pos[1]<=350:
            pygame.draw.rect(display,black,[40,300,200,50],3)
            if event.type==pygame.MOUSEBUTTONDOWN:
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(click)
                welcome=False
                gameloop()
        elif (pos[0]>=40 and pos[0]<=240) and pos[1]>=440 and pos[1]<=490:
            pygame.draw.rect(display,black,[40,440,200,50],3)
            if event.type==pygame.MOUSEBUTTONDOWN:
                pygame.mixer.music.stop()
                pygame.mixer.Sound.play(click)
                welcome=False
                stats()

        elif (pos[0]>=40 and pos[0]<=240) and pos[1]>=370 and pos[1]<=420:
            pygame.draw.rect(display,black,[40,370,200,50],3)
            if event.type==pygame.MOUSEBUTTONDOWN:
                    if len(test_file)>=10:
                        pygame.mixer.music.stop()
                        pygame.mixer.Sound.play(click)
                        welcome=False
                        test()
                    else:
                        text2=wel_font.render("(Master at least 10 proverbs!!)",True,black)
                        trect2=text2.get_rect()
                        trect2.midtop=(430,380)
                        display.blit(text2,trect2)
                        
                    
        elif (pos[0]>=40 and pos[0]<=240) and pos[1]>=510 and pos[1]<=560:
            pygame.draw.rect(display,black,[40,510,200,50],3)
            if event.type==pygame.MOUSEBUTTONDOWN:
                welcome=False
                pygame.quit()
                quit()
                
        

        pygame.display.update()
    
            
            
def gameloop():
#function for checking ans...
    user_list=[]
    
#game variables....
    crashed=False
    after_crashing=False
    if ans:
        generate_proverb()
        quest_2()
    else:
        global quest
        quest_2()
        quest=quest2.copy()
    

    pygame.display.update()
    
    while not crashed:
        

        while after_crashing:
    
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    after_crashing=False
                    crashed=True
                    pygame.quit()
                    quit()
                    
            
            
            display.blit(background_image3,background_position)

            display_result(sol,user_list)
#descion buttons...            
            
            display.fill(color,rect=[580,530,140,50])
            if ans:
                yes=font.render("MASTER NEXT",True,black)
                configuring_text=font.render("PUT IN REVIEW",True,black)
                display.fill(color,rect=[400,530,160,50])
            else:
                yes=font.render("TRY AGAIN",True,black)
                configuring_text=font.render("PUT IN REVIEW",True,black)
                display.fill(color,rect=[400,530,140,50])

            no=font.render("MAIN MENU",True,black)
            display.fill(color,rect=[100,530,180,50])
            display.blit(configuring_text,(110,540))
            display.blit(yes,(410,540))
            display.blit(no,(590,540))

            pos=list(pygame.mouse.get_pos())

            if (pos[0]>=580 and pos[0]<=720) and pos[1]>=530 and pos[1]<=580:
                display.fill(white,rect=[580,530,140,50])
                display.blit(no,(590,540))
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.stop(sad)
                    pygame.mixer.music.play(-1)
                    if ans:
                            test_file.append(lista[b])
                            del lista[b]
                            with open("proverb2.txt","w")as again:
                                again.writelines("".join(lista))
                            with open("test.txt","w")as again2:
                                again2.writelines("".join(test_file))
                    after_crashing=False
                    crashed=True
                    welcome_screen()
                    
                    
            elif (pos[0]>=400 and pos[0]<=540) and pos[1]>=530 and pos[1]<=580:
                if ans:
                    display.fill(white,rect=[400,530,160,50])
                else:
                    display.fill(white,rect=[400,530,140,50])
                display.blit(yes,(410,540))
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.stop(sad)
                    pygame.mixer.Sound.play(click)
                    if ans:
                            test_file.append(lista[b])
                            del lista[b]
                            with open("proverb2.txt","w")as again:
                                again.writelines("".join(lista))
                    gameloop()
                    
            else:
                if ans:
                        if (pos[0]>=100 and pos[0]<=280) and pos[1]>=530 and pos[1]<=580:
                                display.fill(white,rect=[100,530,180,50])
                                display.blit(configuring_text,(110,540))
                                if event.type==pygame.MOUSEBUTTONDOWN:
                                    pygame.mixer.Sound.stop(sad)
                                    pygame.mixer.Sound.play(click)
                                    gameloop()
                                
                
            

            pygame.display.update()


        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                crashed=True
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_BACKSPACE:
                        if len(user_list)>=1:
                                a=user_list.pop()
                                quest.append(a)
            
        display.blit(background_image,background_position)
#drawing the rectangles and text in them...
        lis=[10,20,130,50]
        for x in range(0,len(quest)):
            text=font.render(quest[x],True,black)
            trect=text.get_rect()
            if x==5 or x==10:
                lis[1]+=100
                lis[0]=10
            trect.midtop=(lis[0]+lis[2]/2,lis[1]+10)    
            
            pygame.draw.rect(display,color,lis,3)
            display.blit(text,trect)
            lis[0]+=150
    
#proverbs button logic....        
        pos=list(pygame.mouse.get_pos())#generating list of current cursor position.....
    ####    
        if len(quest)<=5:
            if (pos[0]>=10 and pos[0]<=140) and (pos[1]>=20 and pos[1]<=70) and (len(quest)>=1):
                pygame.draw.rect(display,white,[10,20,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN :
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[0])
                    del quest[0]
            elif (pos[0]>=160) and (pos[0]<=290) and (pos[1]>=20 and pos[1]<=70) and (len(quest)>=2):
                pygame.draw.rect(display,white,[160,20,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[1])
                    del quest[1]
            elif (pos[0]>=310 and pos[0]<=440) and (pos[1]>=20 and pos[1]<=70) and (len(quest)>=3):
                pygame.draw.rect(display,white,[310,20,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[2])
                    del quest[2]
                    
            elif (pos[0]>=460 and pos[0]<=590) and (pos[1]>=20 and pos[1]<=70) and (len(quest)>=4):
                pygame.draw.rect(display,white,[460,20,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[3])
                    del quest[3]
                    
            elif (pos[0]>=610 and pos[0]<=740 )and (pos[1]>=20 and pos[1]<=70) and (len(quest)>=5):
                pygame.draw.rect(display,white,[610,20,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[4])
                    del quest[4]
                    
    ####
        elif len(quest)<=10 and len(quest)>5:
            if (pos[0]>=10 and pos[0]<=140) and (pos[1]>=20 and pos[1]<=70) and (len(quest)>=1):
                pygame.draw.rect(display,white,[10,20,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN :
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[0])
                    del quest[0]
            elif (pos[0]>=160) and (pos[0]<=290) and (pos[1]>=20 and pos[1]<=70) and (len(quest)>=2):
                pygame.draw.rect(display,white,[160,20,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[1])
                    del quest[1]
            elif (pos[0]>=310 and pos[0]<=440) and (pos[1]>=20 and pos[1]<=70) and (len(quest)>=3):
                pygame.draw.rect(display,white,[310,20,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[2])
                    del quest[2]
                    
            elif (pos[0]>=460 and pos[0]<=590) and (pos[1]>=20 and pos[1]<=70) and (len(quest)>=4):
                pygame.draw.rect(display,white,[460,20,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[3])
                    del quest[3]
                    
            elif (pos[0]>=610 and pos[0]<=740 )and (pos[1]>=20 and pos[1]<=70) and (len(quest)>=5):
                pygame.draw.rect(display,white,[610,20,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[4])
                    del quest[4]

                
            elif (pos[0]>=10 and pos[0]<=140) and (pos[1]>=120 and pos[1]<=170) and (len(quest)>=6):
                pygame.draw.rect(display,white,[10,120,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[5])
                    del quest[5]
            elif (pos[0]>=160 and pos[0]<=290) and (pos[1]>=120 and pos[1]<=170) and (len(quest)>=7):
                pygame.draw.rect(display,white,[160,120,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[6])
                    del quest[6]
            elif (pos[0]>=310 and pos[0]<=440) and (pos[1]>=120 and pos[1]<=170) and (len(quest)>=8):
                pygame.draw.rect(display,white,[310,120,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[7])
                    del quest[7]
            elif (pos[0]>=460 and pos[0]<=590) and (pos[1]>=120 and pos[1]<=170)  and (len(quest)>=9):
                pygame.draw.rect(display,white,[460,120,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[8])
                    del quest[8]
            elif (pos[0]>=610 and pos[0]<=740) and (pos[1]>=120 and pos[1]<=170)  and (len(quest)>=10):
                pygame.draw.rect(display,white,[610,120,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[9])
                    del quest[9]
    ####
        elif len(quest)<=15 and len(quest)>10:
            if (pos[0]>=10 and pos[0]<=140) and (pos[1]>=20 and pos[1]<=70) and (len(quest)>=1):
                pygame.draw.rect(display,white,[10,20,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN :
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[0])
                    del quest[0]
            elif (pos[0]>=160) and (pos[0]<=290) and (pos[1]>=20 and pos[1]<=70) and (len(quest)>=2):
                pygame.draw.rect(display,white,[160,20,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[1])
                    del quest[1]
            elif (pos[0]>=310 and pos[0]<=440) and (pos[1]>=20 and pos[1]<=70) and (len(quest)>=3):
                pygame.draw.rect(display,white,[310,20,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[2])
                    del quest[2]
                    
            elif (pos[0]>=460 and pos[0]<=590) and (pos[1]>=20 and pos[1]<=70) and (len(quest)>=4):
                pygame.draw.rect(display,white,[460,20,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[3])
                    del quest[3]
                    
            elif (pos[0]>=610 and pos[0]<=740 )and (pos[1]>=20 and pos[1]<=70) and (len(quest)>=5):
                pygame.draw.rect(display,white,[610,20,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[4])
                    del quest[4]

                
            elif (pos[0]>=10 and pos[0]<=140) and (pos[1]>=120 and pos[1]<=170) and (len(quest)>=6):
                pygame.draw.rect(display,white,[10,120,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[5])
                    del quest[5]
            elif (pos[0]>=160 and pos[0]<=290) and (pos[1]>=120 and pos[1]<=170) and (len(quest)>=7):
                pygame.draw.rect(display,white,[160,120,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[6])
                    del quest[6]
            elif (pos[0]>=310 and pos[0]<=440) and (pos[1]>=120 and pos[1]<=170) and (len(quest)>=8):
                pygame.draw.rect(display,white,[310,120,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[7])
                    del quest[7]
            elif (pos[0]>=460 and pos[0]<=590) and (pos[1]>=120 and pos[1]<=170)  and (len(quest)>=9):
                pygame.draw.rect(display,white,[460,120,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[8])
                    del quest[8]
            elif (pos[0]>=610 and pos[0]<=740) and (pos[1]>=120 and pos[1]<=170)  and (len(quest)>=10):
                pygame.draw.rect(display,white,[610,120,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[9])
                    del quest[9]

            elif (pos[0]>=10 and pos[0]<=140) and (pos[1]>=220 and pos[1]<=270) and (len(quest)>=11):
                pygame.draw.rect(display,white,[10,220,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[10])
                    del quest[10]
            elif (pos[0]>=160 and pos[0]<=290) and (pos[1]>=220 and pos[1]<=270) and (len(quest)>=12):
                pygame.draw.rect(display,white,[160,220,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[11])
                    del quest[11]
            elif (pos[0]>=310 and pos[0]<=440) and (pos[1]>=220 and pos[1]<=270) and (len(quest)>=13):
                pygame.draw.rect(display,white,[310,220,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[12])
            elif (pos[0]>=460 and pos[0]<=590) and (pos[1]>=220 and pos[1]<=270)  and (len(quest)>=14):
                pygame.draw.rect(display,white,[460,220,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[13])
                    del quest[13]
            elif (pos[0]>=610 and pos[0]<=740) and (pos[1]>=220 and pos[1]<=270)  and (len(quest)>=15):
                pygame.draw.rect(display,white,[610,220,130,50],3)
                if event.type==pygame.MOUSEBUTTONDOWN:
                    pygame.mixer.Sound.play(click)
                    user_list.append(quest[14])
                    del quest[14]
#enter button...
        display.fill(color,rect=[700,450,91,50])
        enter=font.render("CHECK",True,black)
        display.blit(enter,(710,460))

        if (pos[0]>=700 and pos[0]<=790) and pos[1]>=450 and pos[1]<=500:
            display.fill(white,rect=[700,450,91,50])
            display.blit(enter,(710,460))
            if event.type==pygame.MOUSEBUTTONDOWN:
                pygame.mixer.Sound.play(click)
                after_crashing=True

##hint button....
        display.fill(color,rect=[20,540,120,50])
        hint=font.render("ANSWER:",True,black)
        hint_text=font.render(" ".join(sol),True,black)
        grect=hint_text.get_rect()
        grect.midtop=(495,550)
        display.blit(hint,(30,550))

        if (pos[0]>=20 and pos[0]<=140) and pos[1]>=540 and pos[1]<=590:
            display.fill(white,rect=[20,540,120,50])
            display.blit(hint,(30,550))
            display.blit(hint_text,grect)
            
                
###printing ans....
        lis2=[10,400,780,50]
        text=font.render(" ".join(user_list),True,black)
        trect2=text.get_rect()
        trect2.midtop=(lis2[0]+lis2[2]/2,lis2[1]+10)
        pygame.draw.rect(display,color,lis2,3)
        display.blit(text,trect2)
        
                
        pygame.display.update()
        clock.tick(fps)


#main program.........
with open("proverb2.txt","r") as text_file:
    a=text_file.readlines()
lista=a.copy()
#total=len(lista)
def master_it(a):
    global total
    total=len(lista)
    global b
    b=random.randint(0,total-1)
    proverb=lista[b]
    ans=proverb.split()
    question=proverb.split()
    random.shuffle(question)
    return question,ans
with open("test.txt","r") as text_file2:
        file=text_file2.readlines()
test_file=file.copy()
random.shuffle(test_file)
#gui interface*********
#initialize the pygame module...
pygame.init()
#initializing sounds.....
pygame.mixer.music.load("Bounce_Ball.wav")
sad=pygame.mixer.Sound("sad.wav")
click=pygame.mixer.Sound("Click.wav")
#display parameters...
display_width=800
display_height=600
#background settings....
background_position=(0,0)
background_image=pygame.image.load("background.jpg")
background_image2=pygame.image.load("background2.jpg")
background_image3=pygame.image.load("background3.jpg")
#text and background colors....
color=(250,187,25)
white=(136,0,34)
black=(170,170,170)
green=(0,170,0)

display=pygame.display.set_mode((display_width,display_height))#setting the canvas of the pygame screen...
pygame.display.set_caption("**Proverb Master**")#display the name of the game...
clock=pygame.time.Clock()#initialize the system clock..
fps=8#setting theframes per second...

test_list=[0,1,2,3,4,5,6,7,8,9]
ans=True

#setting the fonts...
font=pygame.font.SysFont("arial",25)
wel_font=pygame.font.SysFont("arial",30)
        
welcome_screen()#starting game....
pygame.quit()#uninitialize the pygame modules...
quit()#quiting from idle....
            

