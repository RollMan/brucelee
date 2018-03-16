import pygame
import time
import pygame.midi
from pygame.locals import *

pygame.init()
pygame.display.set_mode([100,100])


pygame.midi.init()
print(pygame.midi.get_count())
player= pygame.midi.Output(2)
# player.set_instrument(48,1)
inst = 0
player.set_instrument(inst,1)

major=[0,4,7,12]
keys_horizontal = [K_a, K_w, K_s, K_e, K_d, K_f, K_t, K_g, K_y, K_h, K_u, K_j, K_k]


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

class Lefthand:

    def __init__(self):
        self.major = [0, 7]
        self.scale = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
        self.top = [K_q, K_w, K_e]
        self.med = [K_a, K_s, K_d]
        self.bot = [K_z, K_x, K_c]
        self.back = [def_note + self.scale['C'], def_note + self.scale['F'],  def_note + self.scale['G']]
        pass

    def note_onoff(self, key, on):
        switch_note = player.note_on if on == True else player.note_off
        for i, k in enumerate(self.top):
            if k == key:
                switch_note(self.back[i], 127, 1)
                switch_note(self.back[i] + major[1], 127, 1)
        
        for i, k in enumerate(self.med):
            if k == key:
                switch_note(self.back[i] + 2, 127, 1)
                switch_note(self.back[i] + major[1] + 2, 127, 1)


print("ready")

lefthand = Lefthand()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            lefthand.note_onoff(event.key, True)
            if event.key == pygame.K_BACKSPACE:
                del player
                end()
            if event.key == K_UP:
                inst = inst + 1
                player.set_instrument(inst,1)
            if event.key == K_DOWN:
                inst = max(0, inst - 1)
                player.set_instrument(inst,1)
            if event.key == K_RIGHT:
                inst = 0
                player.set_instrument(inst, 1)


            pass
        if event.type == pygame.KEYUP:
            lefthand.note_onoff(event.key, False)
            pass

