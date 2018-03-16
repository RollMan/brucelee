import pygame
import time
import pygame.midi
from pygame.locals import *

pygame.init()
pygame.display.set_mode([100,100])
c_blues_table=[0, 2, 3, 4, 5, 6, 7, 8, 9]

pygame.midi.init()
print(pygame.midi.get_count())
player= pygame.midi.Output(2)
# player.set_instrument(48,1)
inst = 0
player.set_instrument(inst,1)

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
def_note_a = def_note + 6

class Lefthand:

    def __init__(self):
        self.def_note = 60 - 24
        self.major = [0, 7]
        self.scale = {'C': 0, 'D': 2, 'E': 4, 'F': 5, 'G': 7, 'A': 9, 'B': 11}
        self.top = [K_q, K_w, K_e]
        self.med = [K_a, K_s, K_d]
        self.bot = [K_z, K_x, K_c]
        self.back = [self.def_note + self.scale['C'], self.def_note + self.scale['F'],  self.def_note + self.scale['G']]
        pass

    def note_onoff(self, key, on):
        switch_note = player.note_on if on == True else player.note_off
        for i, k in enumerate(self.top):
            if k == key:
                switch_note(self.back[i], 127, 1)
                switch_note(self.back[i] + major[1], 127, 1)
        
        for i, k in enumerate(self.med):
            if k == key:
                switch_note(self.back[i], 127, 1)
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

        if event.type == pygame.KEYUP:
            lefthand.note_onoff(event.key, False)
            # c blues keymap
        if event.type == pygame.KEYDOWN:
            if event.key == K_r:
                player.note_on(def_note + c_blues_table[0], 127, 1)
            if event.key == K_t:
                player.note_on(def_note + c_blues_table[1], 127, 1)
            if event.key == K_y:
                player.note_on(def_note + c_blues_table[2], 127, 1)
            if event.key == K_u:
                player.note_on(def_note + c_blues_table[3], 127, 1)
            if event.key == K_i:
                player.note_on(def_note + c_blues_table[4], 127, 1)
            if event.key == K_o:
                player.note_on(def_note + c_blues_table[5], 127, 1)
            if event.key == K_p:
                player.note_on(def_note + c_blues_table[6], 127, 1)
            if event.key == K_LEFTBRACKET:
                player.note_on(def_note + c_blues_table[7], 127, 1)
            if event.key == K_RIGHTBRACKET:
                player.note_on(def_note + c_blues_table[8], 127, 1)
             # a blues keymap
            if event.key == K_f:
                player.note_on(def_note_a + c_blues_table[0], 127, 1)
            if event.key == K_g:
                player.note_on(def_note_a + c_blues_table[1], 127, 1)
            if event.key == K_h:
                player.note_on(def_note_a + c_blues_table[2], 127, 1)
            if event.key == K_j:
                player.note_on(def_note_a + c_blues_table[3], 127, 1)
            if event.key == K_k:
                player.note_on(def_note_a + c_blues_table[4], 127, 1)
            if event.key == K_l:
                player.note_on(def_note_a + c_blues_table[5], 127, 1)
            if event.key == K_SEMICOLON:
                player.note_on(def_note_a + c_blues_table[6], 127, 1)
            if event.key == K_QUOTE:
                player.note_on(def_note_a + c_blues_table[7], 127, 1)
        if event.type == pygame.KEYUP:
            # c blues keymap
            if event.key == K_r:
                player.note_off(def_note + c_blues_table[0], 127, 1)
            if event.key == K_t:
                player.note_off(def_note + c_blues_table[1], 127, 1)
            if event.key == K_y:
                player.note_off(def_note + c_blues_table[2], 127, 1)
            if event.key == K_u:
                player.note_off(def_note + c_blues_table[3], 127, 1)
            if event.key == K_i:
                player.note_off(def_note + c_blues_table[4], 127, 1)
            if event.key == K_o:
                player.note_off(def_note + c_blues_table[5], 127, 1)
            if event.key == K_p:
                player.note_off(def_note + c_blues_table[6], 127, 1)
            if event.key == K_LEFTBRACKET:
                player.note_off(def_note + c_blues_table[7], 127, 1)
            if event.key == K_RIGHTBRACKET:
                player.note_off(def_note + c_blues_table[8], 127, 1)
              # a blues keymap
            if event.key == K_f:
                player.note_off(def_note_a + c_blues_table[0], 127, 1)
            if event.key == K_g:
                player.note_off(def_note_a + c_blues_table[1], 127, 1)
            if event.key == K_h:
                player.note_off(def_note_a + c_blues_table[2], 127, 1)
            if event.key == K_j:
                player.note_off(def_note_a + c_blues_table[3], 127, 1)
            if event.key == K_k:
                player.note_off(def_note_a + c_blues_table[4], 127, 1)
            if event.key == K_l:
                player.note_off(def_note_a + c_blues_table[5], 127, 1)
            if event.key == K_SEMICOLON:
                player.note_off(def_note_a + c_blues_table[6], 127, 1)
            if event.key == K_QUOTE:
                player.note_off(def_note_a + c_blues_table[7], 127, 1)
