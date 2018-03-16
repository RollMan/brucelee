import pygame
import time
import pygame.midi
from pygame.locals import *

pygame.init()
pygame.display.set_mode([100,100])
            d r #m m f #s s r #s
c_note_table=[0, 2, 3, 4, 6, 9, 10, 12, 13]

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

print("ready")

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
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

            # c blues keymap
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
        if event.type == pygame.KEYUP:
            # c blues keymap
            if event.key == K_r:
                player.note_off(def_note + c_blues_table[8], 127, 1)
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
 
