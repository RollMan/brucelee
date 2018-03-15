import pygame
import time
import pygame.midi

pygame.init()
pygame.display.set_mode([100,100])


pygame.midi.init()
print(pygame.midi.get_count())
player= pygame.midi.Output(2)
player.set_instrument(48,1)

major=[0,4,7,12]


def go(note):
    player.note_on(note, 127,1)
    time.sleep(1)
    player.note_off(note,127,1)

def arp(base,ints):
    for n in ints:
        go(base+n)

def chord_on(base, ints):
    player.note_on(base,127,1)
    player.note_on(base+ints[1],127,1)
    player.note_on(base+ints[2],127,1)
    player.note_on(base+ints[3],127,1)
def chord_off(base, ints):
    player.note_off(base,127,1)
    player.note_off(base+ints[1],127,1)
    player.note_off(base+ints[2],127,1)
    player.note_off(base+ints[3],127,1)
def end():
    pygame.quit()

def_note = 60

print("ready")

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                del player
                end()
            if event.key == pygame.K_a:
                print("K_a downed")
                chord_on(def_note, major)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                print("K_a uped")
                chord_off(def_note, major)

