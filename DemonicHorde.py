import time
import random
from tqdm import tqdm
#Options for players to select are named here
answer_A = ["a", "A"]
answer_B = ["b", "B"]
answer_C = ["c", "C"]
boss_weapon_choiceFists = ["Fists", "fists"]
boss_weapon_choicePistol = ["pistol", "Pistol"]
boss_weapon_choiceShotgun = ["shotgun", "Shotgun"]
boss_weapon_choiceMinigun = ["minigun", "Minigun"]
boss_weapon_choiceRocket = ["Rocket Launcher", "rocket launcher"]
boss_weapon_choiceLaser = ["laser cannon", "Laser Cannon", "laser", "Laser"]
yes = ["Y", "y", "yes", "Yes", "YES"]
no = ["N", "n", "no", "No", "NO"]
cheat_code = ["IDDQD", "iddqd"]
cheat_code2 = ["IDKFA", "idkfa"]
shotgun = 0
minigun = 0
rocket = 0
laser = 0
boss_health = 2500
multiplier = 0

#in-game RNG specifications
def RNG():
    x = random.randint(1,10)
    return x
def StartUpRNG():
    y = random.randint(0, 255)
    return y
def mimic_attackRNG():
    m = random.randint(1, 3)
    return m
def weaponboxRNG():
    w = random.randint(1, 2)
    return w
def bruiser_attackRNG():
    b = random.randint(1, 4)
    return b
required = ("\n Use only A, B, or C\n")

#Game over animation
def GameOver():
    spaces = 0
    while spaces <= 10:
        print(" ")
        time.sleep(0.5)
        spaces += 1
    print("                                 You Are Dead")
    while spaces <= 20:
        print(" ")
        time.sleep(0.5)
        spaces += 1
    print("Do you want to try again?")
    choice = input(">>> ")
    if choice in yes:
        first_encounter()
    if choice in no:
        print("Hahahahahahahahahahaha ragequitter")
        time.sleep(1000000000000000)
#Beginning of story
def first_encounter():
        print("Yet another reason to hate this security job, some nutty scientist over "
              "in Lazarus opened a portal to hell itself! Most of the detail are "
              "already dead or possesed, and all you have is a crappy old pistol. "
              "Your odds aren't great, and one of the possesed soldiers blasts "
              "open the locked door with a shotgun! You respond by:")
        time.sleep(1)
        print("A. Putting some bullets in him")
        time.sleep(1)
        print("B. Rushing him and tearing him apart with your bare hands")
        time.sleep(1)
        print("C. Begging for mercy")
        choice = input(">>> ")
        if choice in answer_A:
            if RNG() <= 2:
                print("The possessed soldier was a faster shot than you, tough luck!")
                GameOver()
            else :
                shotgun_choice()
        elif choice in answer_B:
            if RNG() >= 4:
                berserk()
            else:
                print("The possesed soldier paints the wall behind you a nice crimson with a hint of brain, what were you thinking?")
                GameOver()
        elif choice in answer_C:
            print("Did you seriously try to ask a demon for mercy? You get blown into little pieces, idiot")
            GameOver()
def berserk():
    print("You rip that shotgun out of that idiot's hands, and break that stupid gun over his stupid head, the soldier is very dead")
    time.sleep(4)
    print("WARNING, by following this path, your likelihood of success drops dramaticly, and you will not recieve weapons, are sure you want to proceed?")
    choice = input(">>> ")
    if choice in yes:
        print("Don't say I didn't warn you, welcome to hell!")
        time.sleep(3)
        print("OK, imma be real, there is no 'hard mode', sorry to dissapoint, back to the main story...")
        time.sleep(3)
        print("You still don't get the shotgun though.")
        shotgun_no()
    if choice in no:
        print("Ok wuss, go back to the beginning, and have a loading screen.")
        time.sleep(1)
        print("Loading...")
        time.sleep(5)
        print("You should probably get some coffee, the developer of this game is sadistic, we'll be here a while.") 
        time.sleep(10)
        print("So... hows the family? I'm a program, I don't have a family, must be nice.")
        time.sleep(15)
        print("Are you going to see the new James Bond movie, it looks pretty good.")
        time.sleep(25)
        print("OK, this is getting ridulous, I'm telling the dev to hurry it up.")
        time.sleep(5)
        print("Alrighty, should start up any second now")
        time.sleep(3)
        first_encounter()
def mimic_encounter():
    print("A column of flame shoots towards you, and you barely dodge in time. The wall behind you gets blasted to shrapnel, thinking quickly, you:")
    time.sleep(1)
    if shotgun == 1:
        print("A. Blast it with your shotgun")
    elif shotgun == 0:
        print("A. Shoot it with your pistol")
    time.sleep(1)
    if minigun == 1:
        print("B. Fire your minigun at it")
    elif minigun == 0:
        print("B. Charge it with your bare hands")
    time.sleep(1)
    print("C. Turn around and run")
    choice = input(">>> ")
    if choice in answer_A:
        if shotgun == 1:
            if RNG() <= 4:
                print("You shoot it again and again, but the demon wont go down, it raises its arms, and blasts you with a gout of fire. There isn't even a corpse left at the end.")
                GameOver()
            else:
                print("After several shells are pumped into that abomination, it falls over, wounded")
                time.sleep(1)
                mimic_attack()
        elif shotgun == 0:
                if RNG() <= 6:
                    print("Your pistol rounds bounce harmlessly off the demon, it shoots you with fire, you die.")
                    GameOver()
                elif RNG() >= 7:
                    print("One of your rounds find a chink in the demons armour, and it goes down, and it looks angry.")
                    time.sleep(1)
                    mimc_attack()
    elif choice in answer_B:
        if minigun == 1:
            if RNG() <= 2:
                print("While revving up that minigun, you erupt in flames, and are blown apart by an internal explosion.")
                GameOver()
            else:
                print("You rain lead on the creature that tried to trick you, but it only falls over wounded") 
                time.sleep(1)
                mimic_attack()
        elif minigun == 0:
            if RNG() >= 7:
                print("While charging the demon, a pillar of flame erupts underneath you, you die an agonizing death")
                GameOver()
            else:
                print("You slam into the demon, it looks you in the eyes, and throws you off, and it looks angry")
                time.sleep(1)
                mimic_attack()
    elif choice in answer_C:
        print("While trying to run away, the demon blasts your legs off. you try to crawl away, but the demon walks up to you and picks you up. ot grabs both shoulders, and rips you in half.")
        GameOver()
def mimic_attack():
    if mimic_attackRNG() == 1:
        print("The demon stands up, and raises it's hands in the air, the floor beneath you rumbles, you decide to:")
        time.sleep(1)
        print("A. Jump away from where you're standing")
        time.sleep(1)
        print("B. Charge the demon")
        time.sleep(1)
        print("C. Try and tank the attack")
        choice = input(">>> ")
        if choice in answer_A:
            if RNG() <= 4:
                print("You jumped too late! An eruption of hellfire blasts you from underneath, you die")
                GameOver()
            else:
                print("You manage to jump just before the hellfire erupts from underneath you")
                time.sleep(1)
                mimic_counter()
        elif choice in answer_B:
            if RNG() <= 6:
                print("While charging forward, the demon thrusts it's hand out and impales you, nice one.")
                GameOver()
            else:
                print("You plough into the demon, and tackle it to the ground, and pump some pistol rounds into it's arms, leaving it nearly unable to attack.")
                time.sleep(1)
                mimic_counter()
        elif choice in answer_C:
            if RNG() <= 8:
                print("In trying to take a literal gout of hellfire, you get melted, moron")
                GameOver()
            else:
                print("You take the blast of hellfire, and damn well nearly died trying, you take one of your emergency stimpacks and struggle to your feet. The demon looks surprised, and starts charging it's next attack. Before it can finish, you unload a clip into it's arms.")
                time.sleep(1)
                mimic_counter()
    elif mimic_attackRNG() == 2:
        print("The cretaure stands, and fire eprupts out of its hands and streaks towards you, you proceed to:")
        time.sleep(1)
        print("A. Get behind cover")
        time.sleep(1)
        print("B. Dodge and weave")
        time.sleep(1)
        print("C. Take the hit, momma didn't raise no wuss")
        choice = input(">>> ")
        if choice in answer_A:
            if RNG() <= 3:
                print("The fireball burns through your cover, and your chest")
                GameOver()
            else:
                print("Your cover holds, and the attack clearly taxed the demon, blood is spurting out of it's mouth and back")
                time.sleep(1)
                mimic_counter()
        elif choice in answer_B:
            if RNG() <= 5:
                print("You fail to dodge the fireball, should've stuck with boxing training")
                GameOver()
            else:
                print("The fireball streaks past you, and that demon doesn't look too good, blood is coming out of it's mouth and back")
                mimic_counter()
        elif choice in answer_C:
            if RNG() <= 8:
                print("You take the hit head on, and now you're a bunch of little bits of charred flesh on the ground, gross")
                GameOver()
            else:
                print("Ouch, that really hurt, but you're alive! The demon drops to it's knees, that attack is going to be it's last")
                time.sleep(1)
                mimic_counter()
    elif mimic_attackRNG() == 3:
        print("The demon tries to start an attack, but can't. It coughs up a lot of blood, and drops to its knees.")
        mimic_counter()
        
def mimic_counter():
    time.sleep(1)
    print("The demon won't be able to fight anymore, but you can't leave that thing alive, you choose to:")
    time.sleep(1)
    if shotgun == 0:
        print("A. Snap its neck")
    elif shotgun == 1:
        print("A. Put a slug in it")
    time.sleep(1)
    if minigun == 0:
        print("B. Choke it out")
    elif minigun == 1:
        print("B. Blast it with the minigun")
    time.sleep(1)
    print("C. Shoot it with your pistol")
    choice = input(">>> ")
    if choice in answer_A:
        if shotgun == 0:
            print("You kill the demon by violently breaking its neck.")
        elif shotgun == 1:
            print("You shoot the demon's head off with the shotgun.")
    elif choice in answer_B:
        if minigun == 0:
            print("You wrap an arm around its throat, and choke it to death.")
        elif minigun == 1:
            print("You turn that demon into mincemeat with your minigun.")
    elif choice in answer_C:
        print("You put your pistol in its mouth, and unload a clip in it.")
    break_()

def shotgun_choice():
    global shotgun
    print("You blast that demon with that pistol of yours, he drops like a rock, and that shotgun looks really nice, do you take the shotgun?")
    choice = input(">>> ")
    if choice in yes:
        shotgun_yes()
    elif choice in no:
        shotgun_no()
def minigun_choice():
    print("You blast that demon with a well placed shot to the head, and that is one smexy looking gun. Do you take the minigun?")
    choice = input(">>> ")
    if choice in yes:
        minigun_yes()
    elif choice in no:
        minigun_no()


def shotgun_yes():
    global shotgun
    shotgun = 1
    print("You pick up that shotgun, you feel like it might come in handy later")
    time.sleep(1)
    print("You start making your way to the command center, when bullets spark off the corner you were just abound to turn past"
          "A soldier with a minigun of all things block your path, and he looks mighty unhappy with you, You respond by:")
    time.sleep(1)
    print("A. Rush him with that new shotgun")
    time.sleep(1)
    print("B. Stay back and use your pistol")
    time.sleep(1)
    print("C. Challenge him to a dance-off")
    choice = input(">>> ")
    if choice in answer_A:
        if RNG() <= 3:
            print("You round the corner in full sprint, and the soldier helps you with your swiss cheese cosplay.")
            GameOver()
        elif RNG() >= 4:
            print("You charge around the corner, and by some miracle you don't get shot to pieces.")
            minigun_choice()
    elif choice in answer_B:
        if RNG() <= 2:
            print("You suck at hiding behind corners, you lose your arm to a volley of bullets, you bleed out.")
            GameOver()
        else:
            minigun_choice()
    elif choice in answer_C:
        print("Surprisingly, the demon accepts, but your dancing sucks, and you get torn to shreds by that minigun.")
        GameOver()
def minigun_yes():
    global minigun
    minigun = 1
    print("You take the minigun out of the soldiers cold dead hands, and hear another living soldier, and he sounds like he's in trouble. You proceed to:")
    time.sleep(1)
    print("A. Go see your fellow soldier, you need all the help you can get")
    time.sleep(1)
    print("B. Take a different route, he'll only slow you down")
    time.sleep(1)
    print("C. Play it safe, and peek into the room before rushing in")
    choice = input(">>> ")
    if choice in answer_A:
        if RNG() <= 6:
            print("While rushing the corner to help your fellow soldier, a fireball burns a hole through your chest, a creature looks down on your dying body, rips your arm off, and knocks your lights out.")
            GameOver()
        else:
            mimic_encounter()
    elif choice in answer_B:
        
        if RNG() <= 3:
            print("You decide that the soldier needs to fend for himself, when a clawed hand rips through your back, be more thoughtful of your fellow man, ya twit") 
            GameOver()
        else:
            mimic_encounter()
    elif choice in answer_C:
        if RNG() <= 2:
            print("You peek through a hole in the wall, when a stinger shoots through and stabs your brain stem, you die a painful death")
            GameOver()
        else:
            mimic_encounter()
def shotgun_no():
    print("Who needs a stupid shotgun anyway?")
    time.sleep(1)
    print("After a lot of fighting, you make it to the command center, but inside is a soldier with a minigun! He has yet to see you, Do you")
    time.sleep(1)
    print("A. Sneak up and throttle him")
    time.sleep(1)
    print("B. Shoot him in the back of the head")
    time.sleep(1)
    print("C. Wait for him to leave, don't feel like fighting him right now")
    choice = input(">>> ")
    if choice in answer_A:
        if RNG() <= 6:
            print("You sneak up and grab it's neck, but demons don't need oxygen, it throws you over it's shoulder. While you're dazed, it laughs and pumps you full of lead.")
            GameOver()
        else:
            print("You put an arm around his neck, and he goes down quick. He must've been a smoker. There's the mandatory PSA for ya, kids, don't smoke.")
            minigun_choice()
    elif choice in answer_B:
        if RNG() <= 2:
            print("You fire a bullet his way, and miss. The demon turns around and doesn't miss.")
            GameOver()
        else:            
            print("He goes down in one go, excellent, that minigun looks nice, too.")
            minigun_choice()
    elif choice in answer_C:
        print("While waiting, a bigger demon walks into you, and it doesn't seem to like you")
        bruiser_encounter()

def break_():
    print("After fighting that abomination, you take a well earned break, maybe catch a few Z's...")
    time.sleep(3)
    print("You awaken suddenly to the sound of the emergency bulkheads caving in, looks like your break is ending prematurely, hell isn't done with you yet")
    time.sleep(0.5)
    print("you look around the room, and see a weapon case, do you open the case?")
    choice = input(">>> ")
    if choice in yes:
        weaponbox1()
    if choice in no:
        print("Your loss buddy")
        time.sleep(1)
        bruiser_encounter()
        
        
def weaponbox1():
    global rocket
    rocket += 1
    print("You open the case and see the sleek, black barrel of a rocket launcher, with an experimental replicator for making a theorectical unlimeted supply of ammunition, nice.")
    bruiser_encounter()

def bruiser_encounter():
    time.sleep(1)
    print("You turn to see a hulking red demon behind you, it jumps into the air and starts careening towards you. You proceed to:")
    time.sleep(1)
    bruiser_evade()
def bruiser_evade():
    print("A. Run out of the blast zone")
    time.sleep(1)
    if rocket == 1:
        print("B. Fire a rocket at it")
    else:
        print("B. Pump lead into it with your pistol")
    time.sleep(1)
    print("C. Tank the hit, the demon doesn't look THAT strong")
    choice = input(">>> ")
    if choice in answer_A:
        if RNG() <= 4:
            print("You try to get out of the blast zone, but just can't get out in time, you get flattened by the demon.")
            GameOver()
        else:
            print("You barely manage to avoid certain death, the demon's hand is stuck in the ground. You shoot it with your pistol, and it falls over on it's side")
            bruiser_counter()
    elif choice in answer_B:
        if rocket == 1:
            if RNG() == 1:
                print("You pull the trigger, and your rocket explodes inside the barrel, you have been reduced to a pair of legs. Yikes.")
                GameOver()
            elif RNG() >= 4:
                print("You fire a rocket and knock the demon out of the air, good shooting")
                bruiser_counter()
            else:
                print("You fire too late, and get caught in the blast, you're now a pile of gibs, too bad.")
        else:
            if RNG() <= 8:
                print("Did you think that a pistol would be enough for this? The bullets don't even slow it down, and you get flattened.")
                GameOver()
            else:
                print("Your pistol is getting things done, the demon falls over on it's side")
                bruiser_counter()
    elif choice in answer_C:
        print("You get turned into a nice pancake, you're dead as dirt, you utter moron.")
        GameOver()

def bruiser_counter():
    print("You see a prime oppurtunity to strike, you attack by:")
    time.sleep(1)
    if shotgun == 1:
        print("A. Firing a slug into him")
    else:
        print("A. Fire some pistol rounds into him")
    time.sleep(1)
    if minigun == 1:
        print("B. Use that minigun on him")
    else:
        print("B. Punch it with the force of a thousand suns")
    time.sleep(1)
    if rocket == 1:
        print("C. Fire a rocket at him")
    else:
        print("C. Hit it over the head with a chair")
    choice = input(">>> ")
    if choice in answer_A:
        if shotgun == 1:
            print("You blast the demon, but the demon clearly didn't hear a bell")
            bruiser_attack2()
        else:
            print("You unload a clip into the demon, but he isn't going down that easy")
            bruiser_attack2()
    elif choice in answer_B:
        if minigun == 1:
            print("You rev up your gun, and fire a huge burst of bullets, but he isn't giving up that easy")
            bruiser_attack2()
        else:
            print("You run up and slam a fist into its head, you must have hit it hard, but it ain't done yet")
            bruiser_attack2()
    elif choice in answer_C:
        if rocket == 1:
            print("You pump a rocket into its side, but it ain't done yet")
            bruiser_attack2()
        else:
            print("You grab the nearest chair, and break it over the demon's head, but it's just not enough")
            bruiser_attack2()
def bruiser_attack2():
    if bruiser_attackRNG() == 1:
        print("The demon charges at you with it's head down, and those horns looks sharp. You quickly:")
        time.sleep(1)
        print("A. Jump to the side")
        time.sleep(1)
        print("B. Vault the demon")
        time.sleep(1)
        print("C. Overpower the demon")
        choice = input(">>> ")
        if choice in answer_A:
            if RNG() <= 4:
                print("The demon anticipated your move! You are slammed into the wall, and your torso is crushed.")
                GameOver()
            else:
                print("You barely avoid getting run down by that demon, it slams into the wall, and stumbles backward.")
        elif choice in answer_B:
            if RNG() <= 7:
                print("While trying to look insanely cool, you mess up, and get flattened,")
                GameOver()
            else:
                print("You roll over the back of the charging demon, causing it to slam into the wall")
                bruiser_kill()
        elif choice in answer_C:
            if RNG() <= 8:
                print("You try to overpower the demon, but it tosses you aside like a ragdoll. As you try to recover, the demon stomps your skull in. Ouch.")
                GameOver()
            else:
                print("You grab the demon by those sharp looking horns, and pull it to the ground.")
                bruiser_kill()
    elif bruiser_attackRNG() == 2:
        print("The demon launches itself into the air, with clear intent of flattening you. You evade by:")
        time.sleep(1)
        if rocket == 1:
            print("A. Shoot a rocket at it")
        else:
            print("A. Jump and punch it out of the sky")
        time.sleep(1)
        if minigun == 1:
            print("B. Gun it down with the minigun")
        else:
            print("B. Unload a clip into it")
        time.sleep(1)
        print("C. Dodge and weave")
        choice = input(">>> ")
        if choice in answer_A:
            if rocket == 1:
                if RNG() <= 3:
                    print("You missed, I think we both know where how this ends.")
                    GameOver()
                else:
                    print("Your rocket slams into the demon, the explosion knocks it onto its back")
                    bruiser_kill()
            else:
                if RNG <= 6:
                    print("You don't hit hard enough to pull that off, good try though.")
                    GameOver()
                else:
                    print("You slam into the demon, and bring it to the ground")
                    bruiser_kill()
        elif choice in answer_B:
            if minigun == 1:
                if RNG() <= 4:
                    print("The bullets just don't slow it down enough, you get grabbed and thrown against the wall. Your ribcage shatters")
                    GameOver()
                else:
                    print("The bullets rip through the demon, and it falls to the ground")
                    bruiser_kill()
            else:
                if RNG() <= 6:
                    print("The bullets bounce off the demon harmlessly, and you get flattened")
                    GameOver()
                else:
                    print("The bullets pierce the demon's abdomen, and it drops to the floor, but it isn't done yet")
                    bruiser_kill()
        elif choice in answer_C:
            if RNG() <= 4:
                print("You don't dodge well enough, and get freaking destroyed. You are super dead")
                GameOver()
            else:
                print("Good dodging, you manage to roll away in time")
                bruiser_kill()
    elif bruiser_attackRNG() == 3:
        print("Green flames erupt out of the demon's hand, it swings it's arm at you, and three fireballs blaze towards you. You have to move fast:")
        time.sleep(1)
        print("A. Slide under")
        time.sleep(1)
        print("B. Dodge left")
        time.sleep(1)
        print("C. Dodge right")
        choice = input(">>> ")
        if choice in answer_A:
            if RNG() <= 5:
                print("You don't go low enough! Your soul is blasted out of your body, yikes.")
                GameOver()
            else:
                print("The fireballs shoot over your head")
                bruiser_kill()
        elif choice in answer_B:
            if RNG() <= 3:
                print("You take a fireball right in the gut. Your soul flies into the wall, you see your body disintegrate before your eyes, you are dead.")
                GameOver()
            else:
                print("The fireballs streak past you, good dodging")
                bruiser_kill()
        elif choice in answer_C:
            if RNG() <= 4:
                print("You take a fireball in the chest, as your soul goes flying, you see a nasty hole where your left lung used to be.")
                GameOver()
            else:
                print("The fireballs streak past you, good dodging")
                bruiser_kill()
    elif bruiser_attackRNG() == 4:
        print("The demon slams its foot into the ground and heaves a piece of the floor over its head and throws it at you. ")
        time.sleep(1)
        print("A. Jump to the side")
        time.sleep(1)
        print("B. Hit the deck")
        time.sleep(1)
        print("C. Punch the rock")
        choice = input(">>> ")
        if choice in answer_A:
            if RNG() <= 4:
                print("You get hit by the rock! You have become a well-cooked crepe.")
                GameOver()
            else:
                print("Nice dodge! The rock sails past you and slams into the wall")
                bruiser_kill()
        elif choice in answer_B:
            if RNG <= 3:
                print("You drop too late! Your head gets taken off at the neck, that's quite the death you just had.")
                GameOver()
            else:
                print("You drop just in time. The rock sails over your head and destroys the wall behind you")
                bruiser_kill()
        elif choice in answer_C:
            print("You get flattened, what did you expect? Did you think you could just punch the rock and NOT die? This may be a game about shooting demons, but we have to have SOME realism, you absolute buffoon.")
            GameOver()
def bruiser_kill():
    print("You jump away from the demon, anticpating further assault. The demon tries to muster another attack, its arm erupts in green flames, and explodes. The demon screams in agony, and drops to its knees. You see a fallen soldiers knife on the floor, do you put the demon out of its misery?")
    choice = input(">>> ")
    if choice in yes:
        print("You walk up to the demon, and plunge the knife into the demons throat. It tries to grab at the knife, jerks, and goes limp, the flame in the demons eyes go out.")
        laser_get()
    
    if choice in no:
        print("You turn to leave the room, when a green fireball cuts through your chest, as your soul is ripped from you body and falls apart, you see the demon look with satisfaction, before going limp. In its last act, it killed you.")
        GameOver()
def laser_get():
    global laser
    laser += 1
    print("After killing that massive demon, you find yourself in the courtyard of the base, a once beautiful place to rest and socialize, now reduced to rubble. You note strange, perfectly circular holes in the walls. You hear a voice, definatly human.")
    time.sleep(1)
    print("One of the elite guards! Thank God! Those guys are nearly invincible! Those laser cannons can turn a demon into crimson rain in a single shot, but... he's wounded. Badly wounded.")
    time.sleep(1)
    print("'Get out of here! That thing... it's still alive! The other elites, they're all gone!' screams the guard.")
    time.sleep(1)
    print("You hear a faint humming sound, slowly getting louder...")
    time.sleep(0.5)
    print("'Damn it! It's back! TAKE MY GUN! KILL IT!' the guard screams")
    time.sleep(0.1)
    print("Right after the guard throws you the laser cannon, an orb of pure darkness shoots through the rubble, and goes through the soldier. All that's left are his arms...")
    finalboss()

def finalboss():
    print("The orb stops, and dissipates, and a lean yet muscular humanoid demon emerges from the orb")
    time.sleep(1)
    print("It looks around the room, and it spots you. It opens its fang-lined mouth, and the head of the lead scientist of the Lazarus project emerges.")
    time.sleep(1)
    print("'Look upon my new form, controlling one of the long extinct Miasma demons. I can become a portal to the region between dimensions! I have attained perfection! I am invincible, and the dark ones have promised me even more power! I am almost a god, who are you to try and stop me!'")
    time.sleep(1)
    print("The scientist becomes void once more, and careens towards you. You dodge before it hits you. The miasma emerges from the void again, and looks around the room.")
    finalbossfight()
def finalbossfight():
    global boss_health
    if boss_health >= 1:
        print("The miasma has " +str(boss_health)+ " health remaining")
        print("The miasma makes a pass towards you, you dodge...")
        time.sleep(1)
        print("A. Left")
        time.sleep(1)
        print("B. Right")
        choice = input(">>> ")
        if weaponboxRNG() == 1:
            if choice in answer_A:
                print("The miasma hits you, you get ripped from this dimension, to face a fate far worse than death.")
                time.sleep(1)
                print("The develloper is being merciful, do you want to go back to the start of this fight?")
                choice = input(">>> ")
                if choice in yes:
                    print("Alright, rewinding...")
                    print("Loading...")
                    time.sleep(6)
                    boss_health = 2500
                    finalbossfight()
                if choice in no:
                    print("Damn, I respect the choice man, but this game ain't exactly a cakewalk. Back ya go then!")
                    first_encounter()
            elif choice in answer_B:
                print("The miasma streaks past you, good prediction")
                if RNG() <= 3:
                     miasmahit()
                else:
                     finalbossfight()
        else:
            if choice in answer_A:
                print("The miasma streaks past you, good prediction")
                if RNG() <= 3:
                     miasmahit()
                else:
                     finalbossfight()
            elif choice in answer_B:
                print("The miasma hits you, you get ripped out of this dimension, to face a fate far worse than death.")
                time.sleep(1)
                print("The develloper is being merciful, do you want to go back to the start of this fight?")
                choice = input(">>> ")
                if choice in yes:
                    print("Alright, rewinding...")
                    print("Loading...")
                    time.sleep(6)
                    boss_health = 2500
                    finalbossfight()
                if choice in no:
                    print("Damn, I respect the choice man, but this game ain't exactly a cakewalk. Back ya go then!")
                    first_encounter()
    else:
        print("The Miasma drops to the floor, and the head of the scientist emerges from the miamsa's mouth. The scientist begs for mercy. You tell him...")
        time.sleep(1)
        print("A. There is no mercy")
        time.sleep(1)
        print("B. You are already dead")
        time.sleep(1)
        print("C. Go to hell, and tell the devil, I'm coming for him next")
        choice = input(">>> ")
        if choice in answer_A:
            print("After saying that, you fire your laser cannon in his head")
        elif choice in answer_B:
            print("After saying that, you stomp the scientists head in")
        elif choice in answer_C:
            print("After saying that, you rip the head off of the appendige.")

def miasmahit():
    global Multiplier
    global boss_health
    print("The miasma comes out of the void, and has yet to see you, what weapon will you use on the miasma?")
    print("Bare Hands")
    time.sleep(0.3)
    print("Pistol")
    time.sleep(0.3)
    if shotgun == 1:
        print("Shotgun")
    else:
        print("Should've picked up that shotgun")
    time.sleep(0.3)
    if minigun == 1:
        print("Minigun")
    else:
        print("Should've picked up that minigun")
    time.sleep(0.3)
    if rocket == 1:
        print("Rocket Launcher")
    else:
        print("Should've opened that weapon case")
    time.sleep(0.3)
    print("Laser Cannon")
    choice = input(">>> ")
    if choice in boss_weapon_choiceFists:
        Multiplier = 1
    elif choice in boss_weapon_choicePistol:
        Multiplier = 3
    elif choice in boss_weapon_choiceShotgun:
        if shotgun == 1:
            Multiplier = 5
        else:
            print("You don't have this weapon")
            time.sleep(1)
            miasmahit()
    elif choice in boss_weapon_choiceMinigun:
        if minigun == 1:
            Multiplier = 8
        else:
            print("You don't have this weapon")
            time.sleep(1)
            miasmahit()
    elif choice in boss_weapon_choiceRocket:
        if rocket == 1:
            Multiplier = 25
        else:
            print("You don't have this weapon")
            time.sleep(1)
            miasmahit()
    elif choice in boss_weapon_choiceLaser:
        Multiplier = 50
    P = boss_health
    boss_health = P - Multiplier * RNG()
    finalbossfight()
#startup sequence
if StartUpRNG() == 69:
    print("Whoops! You accidentally downloaded deathmatch! Idiot.")
else:
    print("Welcome to Demonic Hordes, an action-packed text game that totally isn't a DOOM ripoff. Every decision you make will either allow you to fight another day, or die a horrible and brutal death, do you have what it takes? Type Yes if you're an absolute chad, and ready to fight hell head-on, and type No if you're a coward who gets scared by a small child's halloween costume.")       
choice = input (">>> ")
if choice in yes:
    first_encounter()
elif choice in no:
    print("Ok bud, you read the text from before, coward")
elif choice in cheat_code:
    print("Demons! They've invaded your research base! No one survived! That includes you! You died in the initial assault, cheaters never prosper.")
elif choice in cheat_code2:
   print("You thought this was going to be a cheat code, but it was me! DIO!")
   
