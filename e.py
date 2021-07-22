import random
import pygame
__author__ = 'Noah Vendrig'
__license__ = 'MIT'  # copy of the license available @ https://prodicus.mit-license.org/
__version__ = '1.0.1'
__email__ = 'noah.vendrig@education.nsw.gov.au'
__github__ = "github.com/noahvendrig"  # @noahvendrig
__course__ = 'Software Design and Development'
__date__ = '10/07/2021'
__description__ = 'Modern Recreation of text-based adventure game Hunt the Wumpus (1973)'
__specifications__ = "noahvendrig.com/#about"  # specifications available here

print('# ' + '=' * 78)
print('Author: ' + __author__)
print('License: ' + __license__)
print('Version: ' + __version__)
print('Email: ' + __email__)
print('Course: ' + __course__)
print('Date: ' + __date__)
print('Description: ' + __description__)
print('# ' + '=' * 78)


#   L. 521       336  LOAD_STR                 'yes'
# ->             338_0  COME_FROM            74  '74'
#                  338  STORE_GLOBAL             wumpusPoisoned
#                  340  JUMP_FORWARD        366  'to 366'
#                342_0  COME_FROM           326  '326'
pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((960, 600))
pygame.display.set_caption('Hunt the Wumpus Pro')
caves = {}
randRooms = {}
caveIDs = {}
cheats = False
cheatCount = 0
bestTime = []
tally = {'win': 0,
 'wumpus': 0,  'pit': 0}
playerPrefs = {'rooms': 20,
 'lightStrength': 4,
 'pitStrength': 50,
 'arrows': 3,
 'arrowRange': 2,
 'wumpusMove': 75,
 'wumpusWarning': 35,
 'wumpusRampage': 45}
startTime = None
programState = 'menu'
time = 0
arrows = playerPrefs['arrows']
wumpusPoisoned = 'no'
wumpusActive = 'inactive'
treasureFound = 'unfound'
CaveIdle = pygame.image.load('data/screens/Cave/cave_00.png')
CaveExit = pygame.image.load('data/screens/Cave/exit.png')
CaveTreasure = pygame.image.load('data/screens/Cave/treasure.png')
PlayerReminders = {'NoTreasure': pygame.image.load(
    'data/screens/Cave/noTreasure.png'),  'NoWumpus': pygame.image.load('data/screens/Cave/noWumpus.png')}
CaveAnim = [
 pygame.image.load('data/screens/Cave/cave_00.png'),
 pygame.image.load('data/screens/Cave/cave_01.png'),
 pygame.image.load('data/screens/Cave/cave_02.png'),
 pygame.image.load('data/screens/Cave/cave_03.png'),
 pygame.image.load('data/screens/Cave/cave_04.png'),
 pygame.image.load('data/screens/Cave/cave_05.png'),
 pygame.image.load('data/screens/Cave/cave_06.png'),
 pygame.image.load('data/screens/Cave/cave_07.png'),
 pygame.image.load('data/screens/Cave/cave_08.png'),
 pygame.image.load('data/screens/Cave/cave_08.png'),
 pygame.image.load('data/screens/Cave/cave_08.png'),
 pygame.image.load('data/screens/Cave/cave_08.png'),
 pygame.image.load('data/screens/Cave/cave_08.png'),
 pygame.image.load('data/screens/Cave/cave_08.png'),
 pygame.image.load('data/screens/Cave/cave_08.png'),
 pygame.image.load('data/screens/Cave/cave_08.png'),
 pygame.image.load('data/screens/Cave/cave_08.png'),
 pygame.image.load('data/screens/Cave/cave_08.png'),
 pygame.image.load('data/screens/Cave/cave_09.png'),
 pygame.image.load('data/screens/Cave/cave_10.png'),
 pygame.image.load('data/screens/Cave/cave_11.png'),
 pygame.image.load('data/screens/Cave/cave_12.png'),
 pygame.image.load('data/screens/Cave/cave_13.png'),
 pygame.image.load('data/screens/Cave/cave_14.png'),
 pygame.image.load('data/screens/Cave/cave_15.png'),
 pygame.image.load('data/screens/Cave/cave_16.png'),
 pygame.image.load('data/screens/Cave/cave_17.png')]
ShootPrompt = pygame.image.load('data/screens/Cave/Shoot.png')
ShootAnim = [
 pygame.image.load('data/screens/Shoot/Shoot_00.png'),
 pygame.image.load('data/screens/Shoot/Shoot_01.png'),
 pygame.image.load('data/screens/Shoot/Shoot_02.png'),
 pygame.image.load('data/screens/Shoot/Shoot_03.png'),
 pygame.image.load('data/screens/Shoot/Shoot_04.png'),
 pygame.image.load('data/screens/Shoot/Shoot_05.png'),
 pygame.image.load('data/screens/Shoot/Shoot_06.png'),
 pygame.image.load('data/screens/Shoot/Shoot_07.png'),
 pygame.image.load('data/screens/Shoot/Shoot_08.png'),
 pygame.image.load('data/screens/Shoot/Shoot_09.png'),
 pygame.image.load('data/screens/Shoot/Shoot_10.png'),
 pygame.image.load('data/screens/Shoot/Shoot_11.png'),
 pygame.image.load('data/screens/Shoot/Shoot_12.png'),
 pygame.image.load('data/screens/Shoot/Shoot_13.png'),
 pygame.image.load('data/screens/Shoot/Shoot_14.png'),
 pygame.image.load('data/screens/Shoot/Shoot_15.png'),
 pygame.image.load('data/screens/Shoot/Shoot_16.png'),
 pygame.image.load('data/screens/Shoot/Shoot_17.png'),
 pygame.image.load('data/screens/Shoot/Shoot_18.png')]
Menus = {'main': pygame.image.load('data/screens/Menu/Main.png'),
 'play': pygame.image.load('data/screens/Menu/Play.png'),
 'quit': pygame.image.load('data/screens/Menu/Quit.png'),
 'rule': pygame.image.load('data/screens/Menu/Rules.png'),
 'setting': pygame.image.load('data/screens/Menu/Settings.png'),
 'tally': pygame.image.load('data/screens/Menu/Tally.png')}
TallyScreen = pygame.image.load('data/screens/Screens/Tally.png')
WinScreen = pygame.image.load('data/screens/Endgames/Win/Win.png')
SettingsPrompts = {'rooms': pygame.image.load('data/screens/Screens/Settings/Room.png'),
 'lightStrength': pygame.image.load('data/screens/Screens/Settings/LightStrength.png'),
 'pitStrength': pygame.image.load('data/screens/Screens/Settings/PitStrength.png'),
 'arrows': pygame.image.load('data/screens/Screens/Settings/Arrow.png'),
 'arrowRange': pygame.image.load('data/screens/Screens/Settings/ArrowRange.png'),
 'wumpusMove': pygame.image.load('data/screens/Screens/Settings/WumpusMove.png'),
 'wumpusWarning': pygame.image.load('data/screens/Screens/Settings/WumpusWarning.png'),
 'wumpusRampage': pygame.image.load('data/screens/Screens/Settings/WumpusRampage.png')}
Instructions = [pygame.image.load('data/screens/Screens/Instructions/Instruction_00.png'),
 pygame.image.load('data/screens/Screens/Instructions/Instruction_01.png'),
 pygame.image.load('data/screens/Screens/Instructions/Instruction_02.png'),
 pygame.image.load('data/screens/Screens/Instructions/Instruction_03.png'),
 pygame.image.load('data/screens/Screens/Instructions/Instruction_04.png'),
 pygame.image.load('data/screens/Screens/Instructions/Instruction_05.png'),
 pygame.image.load('data/screens/Screens/Instructions/Instruction_06.png'),
 pygame.image.load('data/screens/Screens/Instructions/Instruction_07.png'),
 pygame.image.load('data/screens/Screens/Instructions/Instruction_08.png')]
WumpusWarning = pygame.image.load('data/screens/Cave/Wumpus.png')
WumpusAnim = [pygame.image.load('data/screens/Endgames/Wumpus/wumpus_00.png'),
 pygame.image.load('data/screens/Endgames/Wumpus/wumpus_01.png'),
 pygame.image.load('data/screens/Endgames/Wumpus/wumpus_02.png')]
PitWarning = pygame.image.load('data/screens/Cave/Pit.png')
PitAnim = [pygame.image.load('data/screens/Endgames/Pit/pit_00.png'),
 pygame.image.load('data/screens/Endgames/Pit/pit_01.png'),
 pygame.image.load('data/screens/Endgames/Pit/pit_02.png'),
 pygame.image.load('data/screens/Endgames/Pit/pit_03.png'),
 pygame.image.load('data/screens/Endgames/Pit/pit_04.png'),
 pygame.image.load('data/screens/Endgames/Pit/pit_05.png'),
 pygame.image.load('data/screens/Endgames/Pit/pit_06.png'),
 pygame.image.load('data/screens/Endgames/Pit/pit_07.png'),
 pygame.image.load('data/screens/Endgames/Pit/pit_08.png')]
BatWarning = pygame.image.load('data/screens/Cave/Bat.png')
BatAnim = [pygame.image.load('data/screens/Endgames/Bat/bat_00.png'),
 pygame.image.load('data/screens/Endgames/Bat/bat_01.png'),
 pygame.image.load('data/screens/Endgames/Bat/bat_02.png'),
 pygame.image.load('data/screens/Endgames/Bat/bat_03.png'),
 pygame.image.load('data/screens/Endgames/Bat/bat_04.png'),
 pygame.image.load('data/screens/Endgames/Bat/bat_05.png'),
 pygame.image.load('data/screens/Endgames/Bat/bat_06.png'),
 pygame.image.load('data/screens/Endgames/Bat/bat_07.png'),
 pygame.image.load('data/screens/Endgames/Bat/bat_08.png'),
 pygame.image.load('data/screens/Endgames/Bat/bat_09.png'),
 pygame.image.load('data/screens/Endgames/Bat/bat_10.png')]


def Draw(pic):
    win.blit(pic, (0, 0))
    pygame.display.update()


def CaveDrawInfo(pos):
    global arrows
    global treasureFound
    global wumpusPoisoned
    if wumpusPoisoned == 'no':
        wumpCheck = '>'
    else:
        wumpCheck = '<'
    if treasureFound == 'unfound':
        tresureCheck = '>'
    else:
        tresureCheck = '<'
    font = pygame.font.Font('data/pixel.ttf', 20)
    bigFont = pygame.font.Font('data/pixel.ttf', 25)
    win.blit(bigFont.render('current room: ' + str(pos), 1, (120, 120, 120)), (340,
                                                                               45))
    win.blit(font.render('wumpus: ' + str(wumpCheck),
             1, (120, 120, 120)), (730, 50))
    win.blit(font.render('treasure: ' + str(tresureCheck), 1, (120, 120, 120)), (710,
                                                                                 110))
    win.blit(font.render('radio strength: ' + str(SignalCalculator(pos)) + ' %', 1, (120,
                                                                                     120,
                                                                                     120)), (20,
                                                                                             50))
    win.blit(font.render(str(arrows) + ' arrows left',
             1, (120, 120, 120)), (70, 550))
    win.blit(font.render(
        'cave ' + str(caves[pos][0]), 1, (120, 120, 120)), (210, 200))
    win.blit(font.render(
        'cave ' + str(caves[pos][1]), 1, (120, 120, 120)), (450, 113))
    win.blit(font.render(
        'cave ' + str(caves[pos][2]), 1, (120, 120, 120)), (670, 205))
    win.blit(font.render(
        'cave ' + str(caves[pos][3]), 1, (120, 120, 120)), (450, 497))
    pygame.display.update()


def DrawWinInfo(millisec):
    totalTime = int(millisec / 1000)
    sec = totalTime % 60
    min = totalTime // 60
    bigFont = pygame.font.Font('data/pixel.ttf', 30)
    win.blit(bigFont.render(str(min) + ' min: ' + str(sec) + ' sec', 1, (120, 120,
                                                                         120)), (650,
                                                                                 280))
    pygame.display.update()


def DrawTallyInfo():
    global bestTime
    font = pygame.font.Font('data/pixel.ttf', 25)
    bigFont = pygame.font.Font('data/pixel.ttf', 27)
    win.blit(bigFont.render(str(tally['win']) + ' times', 1, (120, 120, 120)), (440,
                                                                                225))
    win.blit(bigFont.render(str(tally['wumpus']) + ' times', 1, (120, 120, 120)), (440,
                                                                                   320))
    win.blit(bigFont.render(str(tally['pit']) + ' times', 1, (120, 120, 120)), (440,
                                                                                415))
    i = 0
    while i < len(bestTime):
        min = bestTime[i] // 60
        sec = bestTime[i] % 60
        win.blit(font.render(str(min) + ' min: ' + str(sec) + ' sec', 1, (120, 120,
                                                                          120)), (670, 48 * i + 130))
        i += 1

    pygame.display.update()


def MoveCaveAnim(pos):
    global playerPos
    i = 0
    while i < len(CaveAnim) * 3:
        Draw(CaveAnim[(i // 3)])
        i += 1

    playerPos = pos
    CaveDrawInfo(pos)
    WumpusCheck(hazardRooms[0], pos, 1)
    Hazard(pos)
    if pos == exitPos:
        if wumpusPoisoned != 'yes':
            Draw(PlayerReminders['NoWumpus'])
        if treasureFound != 'found':
            Draw(PlayerReminders['NoTreasure'])


def DrawShootAnim():
    programState = 'Submenu'
    i = 0
    while i < len(ShootAnim) * 3:
        Draw(ShootAnim[(i // 3)])
        i += 1


def DrawWinAnim():
    global endTime
    global programState
    global startTime
    programState = 'Submenu'
    Draw(WinScreen)
    endTime = int((pygame.time.get_ticks() - startTime) / 1000)
    DrawWinInfo(pygame.time.get_ticks() - startTime)


def SignalCalculator(player):
    global playerPrefs
    cavesInXPathLength = {}
    nextToPit = 0
    cavesInXPathLength[1] = caves[exitPos]
    i = 2
    while i < playerPrefs['lightStrength'] + 1:
        cavesInXPathLength[i] = []
        i += 1

    if player == exitPos:
        pathLength = 0
    else:
        if player in caves[exitPos]:
            pathLength = 1
        else:
            x = 2
            while x < playerPrefs['lightStrength'] + 1:
                i = 0
                while i < len(cavesInXPathLength[(x - 1)]):
                    cavesInXPathLength[x] = cavesInXPathLength[x] + \
                        caves[cavesInXPathLength[(x - 1)][i]]
                    i += 1

                if player in cavesInXPathLength[x]:
                    pathLength = x
                    break
                else:
                    pathLength = playerPrefs['lightStrength'] + 1
                x += 1

    if hazardRooms[3] in caves[player] or hazardRooms[4] in caves[player]:
        nextToPit = 1
    signalLevel = int(-100 /
                      (playerPrefs['lightStrength'] + 1) * pathLength + 100)
    signalLevel = int(signalLevel - signalLevel *
                      nextToPit * playerPrefs['pitStrength'] / 100)
    if signalLevel < 0:
        signalLevel = 0
    return signalLevel


def RemindPlayer(what, pos):
    i = 0
    while i < 3:
        Draw(PlayerReminders[what])
        pygame.time.delay(100)
        Draw(CaveAnim[17])
        WarningCheck(pos)
        pygame.time.delay(100)
        i += 1


def Hazard(pos):
    global playerPos
    global programState
    global treasureFound
    if pos == hazardRooms[0]:
        i = 0
        while i < len(WumpusAnim) * 15:
            Draw(WumpusAnim[(i // 15)])
            i += 1

        programState = 'Tally'
        TallyUpdate(0, 'wumpus')
    else:
        if pos == hazardRooms[3] or pos == hazardRooms[4]:
            i = 0
            while i < len(PitAnim) * 9:
                Draw(PitAnim[(i // 9)])
                i += 1

            programState = 'Tally'
            TallyUpdate(0, 'pit')
        else:
            if pos == hazardRooms[1] or pos == hazardRooms[2]:
                playerPos = safeRooms[random.randint(0, len(safeRooms) - 1)]
                i = 0
                while i < len(BatAnim) * 6:
                    Draw(BatAnim[(i // 6)])
                    i += 1

                CaveDrawInfo(playerPos)
            else:
                if pos == treasurePos:
                    treasureFound = 'found'
                else:
                    if pos == exitPos:
                        if treasureFound == 'found':
                            if wumpusPoisoned == 'yes':
                                DrawWinAnim()
                    if programState == 'game':
                        WarningCheck(playerPos)


def WarningCheck(pos):
    wumpusDirect = caves[hazardRooms[0]]
    wumpusIndirect = []
    i = 0
    while i < 3:
        x = 0
        while x < 3:
            wumpusIndirect.append(caves[wumpusDirect[i]][x])
            x += 1

        i += 1

    if pos in wumpusDirect:
        Draw(WumpusWarning)
        CaveDrawInfo(pos)
    else:
        if pos in wumpusIndirect:
            if random.randint(1, 100) < playerPrefs['wumpusWarning']:
                Draw(WumpusWarning)
    if pos in caves[hazardRooms[3]] or pos in caves[hazardRooms[4]]:
        Draw(PitWarning)
        CaveDrawInfo(pos)
    if pos in caves[hazardRooms[1]] or pos in caves[hazardRooms[2]]:
        Draw(BatWarning)
        CaveDrawInfo(pos)
    if pos == exitPos:
        Draw(CaveExit)
        CaveDrawInfo(pos)
    if pos == treasurePos:
        Draw(CaveTreasure)
        CaveDrawInfo(pos)


def WumpusCheck(pos, player, moveNumber):
    global wumpusActive
    if wumpusActive == 'active':
        if random.randint(1, 100) <= playerPrefs['wumpusMove']:
            rooms = caves[int(pos)]
            newPos = rooms[random.randint(0, 2)]
            hazardRooms[0] = newPos
        if wumpusPoisoned == 'yes':
            if moveNumber == 1:
                if random.randint(1, 100) <= playerPrefs['wumpusRampage']:
                    WumpusCheck(newPos, player, moveNumber + 1)


def GetRooms():
    global exitPos
    global hazardRooms
    global playerPos
    global safeRooms
    global treasurePos
    RoomGen()
    safeRooms = []
    playerPos = int
    playerPos = int
    playerPos = int
    hazardRooms = []
    wumpusRoom = random.randint(1, playerPrefs['rooms'])
    bat1Room = random.randint(1, playerPrefs['rooms'])
    pit1Room = random.randint(1, playerPrefs['rooms'])
    bat2Room = random.randint(1, playerPrefs['rooms'])
    pit2Room = random.randint(1, playerPrefs['rooms'])
    while bat2Room == bat1Room:
        bat2Room = random.randint(1, playerPrefs['rooms'])

    while pit2Room == pit1Room:
        pit2Room = random.randint(1, playerPrefs['rooms'])

    hazardRooms = [wumpusRoom, bat1Room, bat2Room, pit1Room, pit2Room]
    i = 1
    while i < playerPrefs['rooms'] + 1:
        if i != wumpusRoom:
            if i != bat1Room:
                if i != bat2Room:
                    if i != pit1Room:
                        if i != pit2Room:
                            safeRooms.append(i)
        i += 1

    playerPos = safeRooms[random.randint(0, len(safeRooms) - 1)]
    treasurePos = safeRooms[random.randint(0, len(safeRooms) - 1)]
    exitPos = safeRooms[random.randint(0, len(safeRooms) - 1)]
    SaveData()


def RoomGen():
    roomsRemaining = []
    i = 1
    while i < playerPrefs['rooms'] + 1:
        roomsRemaining.append(i)
        i += 1

    i = 1
    while i < playerPrefs['rooms'] + 1:
        randRooms[i] = roomsRemaining[random.randint(
            0, len(roomsRemaining) - 1)]
        roomsRemaining.remove(randRooms[i])
        i += 1

    i = 1
    while i < playerPrefs['rooms'] + 1:
        temp = [
         0, 0, 0, 0]
        if i - 5 > 0:
            temp[0] = i - 5
        else:
            temp[0] = i + playerPrefs['rooms'] - 5
        if i % 5 == 1:
            temp[1] = i + 4
        else:
            temp[1] = i - 1
        if i % 5 == 0:
            temp[2] = i - 4
        else:
            temp[2] = i + 1
        if i + 5 > playerPrefs['rooms']:
            temp[3] = i - playerPrefs['rooms'] + 5
        else:
            temp[3] = i + 5
        caveIDs[i] = temp
        i += 1

    i = 1
    while i < playerPrefs['rooms'] + 1:
        caves[randRooms[i]] = [
         randRooms[caveIDs[i][0]], randRooms[caveIDs[i][1]], randRooms[caveIDs[i][2]], randRooms[caveIDs[i][3]]]
        i += 1


def SaveData():
    global lastGameData
    lastGameData = []
    i = 1
    while i < playerPrefs['rooms'] + 1:
        if i == playerPos:
            lastGameData.append('Player')
        else:
            if i == treasurePos:
                lastGameData.append('Treasure')
            else:
                if i == exitPos:
                    lastGameData.append('Exit')
                else:
                    if i in safeRooms:
                        lastGameData.append('Safe')
                    else:
                        if i == hazardRooms[0]:
                            lastGameData.append('Wumpus')
                        else:
                            if i == hazardRooms[3] or i == hazardRooms[4]:
                                lastGameData.append('Pit')
                            else:
                                if i == hazardRooms[1] or i == hazardRooms[2]:
                                    lastGameData.append('Bat')
        i += 1


def Shoot(pos, shot, original):
    global arrows
    global programState
    global wumpusActive
    if shot < playerPrefs['arrowRange']:
        Draw(ShootPrompt)
        CaveDrawInfo(pos)
        clicked = False
        while not clicked:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    clicked = True
                    ShootSelect(pygame.mouse.get_pos(), original, shot, pos)

    else:
        arrows -= 1
        wumpusActive = 'active'
    programState = 'game'


def ShootSelect--- This code section failed: ---

 L. 494         0  LOAD_FAST                'pos'
                2  LOAD_CONST               0
                4  BINARY_SUBSCR
                6  STORE_FAST               'x'

 L. 495         8  LOAD_FAST                'pos'
               10  LOAD_CONST               1
               12  BINARY_SUBSCR
               14  STORE_FAST               'y'

 L. 497        16  LOAD_FAST                'x'
               18  LOAD_CONST               260
               20  BINARY_SUBTRACT
               22  LOAD_CONST               2
               24  BINARY_POWER
               26  LOAD_FAST                'y'
               28  LOAD_CONST               325
               30  BINARY_SUBTRACT
               32  LOAD_CONST               2
               34  BINARY_POWER
               36  BINARY_ADD
               38  LOAD_CONST               7000
               40  COMPARE_OP <=
               42  POP_JUMP_IF_FALSE   104  'to 104'

 L. 498        44  LOAD_GLOBAL              caves
               46  LOAD_FAST                'room'
               48  BINARY_SUBSCR
               50  LOAD_CONST               0
               52  BINARY_SUBSCR
               54  LOAD_GLOBAL              hazardRooms
               56  LOAD_CONST               0
               58  BINARY_SUBSCR
               60  COMPARE_OP ==
               62  POP_JUMP_IF_FALSE    76  'to 76'

 L. 499        64  LOAD_GLOBAL              DrawShootAnim
               66  CALL_FUNCTION_0       0  '0 positional arguments'
               68  POP_TOP

 L. 500        70  LOAD_STR                 'yes'
               72  STORE_GLOBAL             wumpusPoisoned
               74  JUMP_FORWARD        366  'to 366'
             76_0  COME_FROM            62  '62'

 L. 502        76  LOAD_GLOBAL              Shoot
               78  LOAD_GLOBAL              caves
               80  LOAD_FAST                'room'
               82  BINARY_SUBSCR
               84  LOAD_CONST               0
               86  BINARY_SUBSCR
               88  LOAD_FAST                'shot'
               90  LOAD_CONST               1
               92  BINARY_ADD
               94  LOAD_FAST                'original'
               96  CALL_FUNCTION_3       3  '3 positional arguments'
               98  POP_TOP
          100_102  JUMP_FORWARD        366  'to 366'
            104_0  COME_FROM            42  '42'

 L. 504       104  LOAD_FAST                'x'
              106  LOAD_CONST               500
              108  BINARY_SUBTRACT
              110  LOAD_CONST               2
              112  BINARY_POWER
              114  LOAD_FAST                'y'
              116  LOAD_CONST               240
              118  BINARY_SUBTRACT
              120  LOAD_CONST               2
              122  BINARY_POWER
              124  BINARY_ADD
              126  LOAD_CONST               7000
              128  COMPARE_OP               <=
              130  POP_JUMP_IF_FALSE   190  'to 190'

 L. 505       132  LOAD_GLOBAL              caves
              134  LOAD_FAST                'room'
              136  BINARY_SUBSCR
              138  LOAD_CONST               1
              140  BINARY_SUBSCR
              142  LOAD_GLOBAL              hazardRooms
              144  LOAD_CONST               0
              146  BINARY_SUBSCR
              148  COMPARE_OP               ==
              150  POP_JUMP_IF_FALSE   164  'to 164'

 L. 506       152  LOAD_GLOBAL              DrawShootAnim
              154  CALL_FUNCTION_0       0  '0 positional arguments'
              156  POP_TOP

 L. 507       158  LOAD_STR                 'yes'
              160  STORE_GLOBAL             wumpusPoisoned
              162  JUMP_FORWARD        188  'to 188'
            164_0  COME_FROM           150  '150'

 L. 509       164  LOAD_GLOBAL              Shoot
              166  LOAD_GLOBAL              caves
              168  LOAD_FAST                'room'
              170  BINARY_SUBSCR
              172  LOAD_CONST               1
              174  BINARY_SUBSCR
              176  LOAD_FAST                'shot'
              178  LOAD_CONST               1
              180  BINARY_ADD
              182  LOAD_FAST                'original'
              184  CALL_FUNCTION_3       3  '3 positional arguments'
              186  POP_TOP
            188_0  COME_FROM           162  '162'
              188  JUMP_FORWARD        366  'to 366'
            190_0  COME_FROM           130  '130'

 L. 511       190  LOAD_FAST                'x'
              192  LOAD_CONST               720
              194  BINARY_SUBTRACT
              196  LOAD_CONST               2
              198  BINARY_POWER
              200  LOAD_FAST                'y'
              202  LOAD_CONST               330
              204  BINARY_SUBTRACT
              206  LOAD_CONST               2
              208  BINARY_POWER
              210  BINARY_ADD
              212  LOAD_CONST               7000
              214  COMPARE_OP               <=
          216_218  POP_JUMP_IF_FALSE   278  'to 278'

 L. 512       220  LOAD_GLOBAL              caves
              222  LOAD_FAST                'room'
              224  BINARY_SUBSCR
              226  LOAD_CONST               2
              228  BINARY_SUBSCR
              230  LOAD_GLOBAL              hazardRooms
              232  LOAD_CONST               0
              234  BINARY_SUBSCR
              236  COMPARE_OP               ==
              238  POP_JUMP_IF_FALSE   252  'to 252'

 L. 513       240  LOAD_GLOBAL              DrawShootAnim
              242  CALL_FUNCTION_0       0  '0 positional arguments'
              244  POP_TOP

 L. 514       246  LOAD_STR                 'yes'
              248  STORE_GLOBAL             wumpusPoisoned
              250  JUMP_FORWARD        276  'to 276'
            252_0  COME_FROM           238  '238'

 L. 516       252  LOAD_GLOBAL              Shoot
              254  LOAD_GLOBAL              caves
              256  LOAD_FAST                'room'
              258  BINARY_SUBSCR
              260  LOAD_CONST               2
              262  BINARY_SUBSCR
              264  LOAD_FAST                'shot'
              266  LOAD_CONST               1
              268  BINARY_ADD
              270  LOAD_FAST                'original'
              272  CALL_FUNCTION_3       3  '3 positional arguments'
              274  POP_TOP
            276_0  COME_FROM           250  '250'
              276  JUMP_FORWARD        366  'to 366'
            278_0  COME_FROM           216  '216'

 L. 518       278  LOAD_FAST                'x'
              280  LOAD_CONST               500
              282  BINARY_SUBTRACT
              284  LOAD_CONST               2
              286  BINARY_POWER
              288  LOAD_FAST                'y'
              290  LOAD_CONST               400
              292  BINARY_SUBTRACT
              294  LOAD_CONST               2
              296  BINARY_POWER
              298  BINARY_ADD
              300  LOAD_CONST               7000
              302  COMPARE_OP               <=
          304_306  POP_JUMP_IF_FALSE   366  'to 366'

 L. 519       308  LOAD_GLOBAL              caves
              310  LOAD_FAST                'room'
              312  BINARY_SUBSCR
              314  LOAD_CONST               3
              316  BINARY_SUBSCR
              318  LOAD_GLOBAL              hazardRooms
              320  LOAD_CONST               0
              322  BINARY_SUBSCR
              324  COMPARE_OP               ==
          326_328  POP_JUMP_IF_FALSE   342  'to 342'

 L. 520       330  LOAD_GLOBAL              DrawShootAnim
              332  CALL_FUNCTION_0       0  '0 positional arguments'
              334  POP_TOP

 L. 521       336  LOAD_STR                 'yes'
            338_0  COME_FROM            74  '74'
              338  STORE_GLOBAL             wumpusPoisoned
              340  JUMP_FORWARD        366  'to 366'
            342_0  COME_FROM           326  '326'

 L. 523       342  LOAD_GLOBAL              Shoot
              344  LOAD_GLOBAL              caves
              346  LOAD_FAST                'room'
              348  BINARY_SUBSCR
              350  LOAD_CONST               3
              352  BINARY_SUBSCR
              354  LOAD_FAST                'shot'
              356  LOAD_CONST               1
              358  BINARY_ADD
              360  LOAD_FAST                'original'
              362  CALL_FUNCTION_3       3  '3 positional arguments'
              364  POP_TOP
            366_0  COME_FROM           340  '340'
            366_1  COME_FROM           304  '304'
            366_2  COME_FROM           276  '276'
            366_3  COME_FROM           188  '188'
            366_4  COME_FROM           100  '100'

 L. 525       366  LOAD_STR                 'game'
              368  STORE_GLOBAL             programState

Parse error at or near `COME_FROM' instruction at offset 338_0


def Reset():
    global arrows
    global treasureFound
    global wumpusActive
    global wumpusPoisoned
    arrows = playerPrefs['arrows']
    treasureFound = 'unfound'
    wumpusActive = 'inactive'
    wumpusPoisoned = 'no'


def Menu(action):
    global programState
    global startTime
    i = 0
    while i < 3:
        Draw(Menus[action])
        pygame.time.delay(100)
        Draw(Menus['main'])
        pygame.time.delay(100)
        i += 1

    if action == 'play':
        Reset()
        GetRooms()
        programState = 'game'
        startTime = pygame.time.get_ticks()
        MoveCaveAnim(playerPos)
    if action == 'tally':
        TallyUpdate(0, '')
        programState = 'Tally'
    if action == 'setting':
        programState = 'setting'
        SettingUpdate('rooms')
    if action == 'rule':
        programState = 'rule'
        PlayInstructions(0)


def SettingUpdate(pref):
    global programState
    bigFont = pygame.font.Font('data/pixel.ttf', 30)
    valueEntered = False
    tempString = str(playerPrefs[pref])
    Draw(SettingsPrompts[pref])
    while valueEntered == False:
        keys = pygame.key.get_pressed()
        win.blit(bigFont.render('your choice: ' + str(tempString), 1, (120, 120, 120)), (370,
                                                                                         350))
        win.blit(bigFont.render('current: ' + str(playerPrefs[pref]), 1, (120, 120,
                                                                          120)), (370,
                                                                                  400))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if pref == 'rooms':
                        if int(tempString) % 5 == 0:
                            valueEntered = True
                            playerPrefs[pref] = int(tempString)
                        else:
                            Draw(SettingsPrompts[pref])
                            tempString = 'must be multiple of 5'
                            win.blit(bigFont.render('Your Choice: ' + str(tempString), 1, (120,
                                                                                           120,
                                                                                           120)), (370,
                                                                                                   350))
                            pygame.display.update()
                            pygame.time.delay(500)
                            Draw(SettingsPrompts[pref])
                            tempString = ''
                    else:
                        valueEntered = True
                        playerPrefs[pref] = int(tempString)
                if event.key == pygame.K_BACKSPACE:
                    Draw(SettingsPrompts[pref])
                    tempString = tempString[:-1]
                else:
                    tempString += event.unicode

    if pref == 'rooms':
        SettingUpdate('lightStrength')
    else:
        if pref == 'lightStrength':
            SettingUpdate('pitStrength')
        else:
            if pref == 'pitStrength':
                SettingUpdate('arrows')
            else:
                if pref == 'arrows':
                    SettingUpdate('arrowRange')
                else:
                    if pref == 'arrowRange':
                        SettingUpdate('wumpusWarning')
                    else:
                        if pref == 'wumpusWarning':
                            SettingUpdate('wumpusMove')
                        else:
                            if pref == 'wumpusMove':
                                SettingUpdate('wumpusRampage')
                            else:
                                if pref == 'wumpusRampage':
                                    Draw(Menus['main'])
                                    programState = 'menu'


def PlayInstructions(slide):
    global programState
    next = False
    if slide < len(Instructions):
        Draw(Instructions[slide])
        while next == False and programState == 'rule':
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_x:
                        PlayInstructions(99)
                    else:
                        next = True
                        PlayInstructions(slide + 1)

    else:
        programState = 'menu'
        Draw(Menus['main'])


def TallyUpdate(time, why):
    global bestTime
    bestTime = TimeFileUpdate('read')
    if time != 0:
        bestTime.append(time)
        bestTime.sort()
        if len(bestTime) > 10:
            bestTime.remove(bestTime[10])
    if why == 'wumpus':
        tally['wumpus'] += 1
    if why == 'pit':
        tally['pit'] += 1
    if why == 'win':
        tally['win'] += 1
    TimeFileUpdate('write')
    Draw(TallyScreen)
    DrawTallyInfo()


def TimeFileUpdate(action):
    temp = []
    if action == 'read':
        timeLog = open('data/Times.txt', 'r')
        for line in timeLog:
            temp.append(int(line))

        return temp
    if action == 'write':
        for i in range(0, 10):
            temp.append(str(bestTime[i]) + ' \n')

        timeLog = open('data/Times.txt', 'w+')
        timeLog.writelines(temp)
    if action == 'clear':
        clear = [
         '5999 \n', '5999 \n', '5999 \n', '5999 \n', '5999 \n', '5999 \n', '5999 \n', '5999 \n', '5999 \n', '5999 \n']
        timeLog = open('data/Times.txt', 'w')
        timeLog.seek(0)
        timeLog.writelines(clear)


Draw(Menus['main'])
run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if programState == 'Submenu':
                TallyUpdate(endTime, 'win')
                pygame.time.delay(100)
                programState = 'Tally'
        if event.type == pygame.MOUSEBUTTONDOWN:
            if programState == 'Tally':
                Draw(Menus['main'])
                programState = 'menu'
            if event.type == pygame.MOUSEBUTTONDOWN and programState == 'menu':
                cheatCount += 1
                if cheatCount >= 5:
                    cheats = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_p]:
        if programState == 'menu':
            Menu('play')
    if keys[pygame.K_t]:
        if programState == 'menu':
            Menu('tally')
    if keys[pygame.K_s]:
        if programState == 'menu':
            Menu('setting')
    if keys[pygame.K_r]:
        if programState == 'menu':
            Menu('rule')
    if keys[pygame.K_q]:
        if programState == 'menu':
            Menu('quit')
            run = False
    if keys[pygame.K_x]:
        programState = 'menu'
        Draw(Menus['main'])
    if keys[pygame.K_c]:
        if programState == 'game':
            if cheats == True:
                print(hazardRooms)
                print(treasurePos)
                print(exitPos)
    if keys[pygame.K_c]:
        if programState == 'Tally':
            TimeFileUpdate('clear')
            TallyUpdate(0, '')
    if keys[pygame.K_LEFT]:
        if programState == 'game':
            MoveCaveAnim(caves[playerPos][0])
    if keys[pygame.K_UP]:
        if programState == 'game':
            MoveCaveAnim(caves[playerPos][1])
    if keys[pygame.K_RIGHT]:
        if programState == 'game':
            MoveCaveAnim(caves[playerPos][2])
    if keys[pygame.K_DOWN]:
        if programState == 'game':
            MoveCaveAnim(caves[playerPos][3])
    if keys[pygame.K_SPACE] and programState == 'game':
        programState = 'shoot'
        Shoot(playerPos, 0, playerPos)
        MoveCaveAnim(playerPos)
        if arrows == 0:
            i = 0
            while i < len(WumpusAnim) * 15:
                Draw(WumpusAnim[(i // 15)])
                i += 1

            programState = 'Tally'
            TallyUpdate(0, 'wumpus')

pygame.quit()
# global run ## Warning: Unused global

# file wumpuspy.pyc
# Deparsing stopped due to parse error
