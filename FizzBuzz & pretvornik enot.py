# -*- coding: utf-8 -*-
import re

def pretvornik():
    while True:
        pozdrav = "Pozdravljen v pretvorniku (US / SLO) enot: **NAVIGACIJSKE ŠTEVILKE ZA IZBIRO PRETVORB** 1:razdalja  2:volumen (tekočin)  3:hitrost  4:teža  5:temperatura  9:Izhod"
        print pozdrav.center(200, ' ')
        izbira = raw_input()
        if not re.match("^[0-9]*$", izbira):
            print "SAMO ŠTEVILKE PROSIM!!! \n"
        elif izbira == "1":
            razdalja()
        elif izbira == "2":
            volumen()
        elif izbira == "3":
            hitrost()
        elif izbira == "4":
            teza()
        elif izbira == "5":
            temperatura()
        elif izbira == "9":
            break
        else:
            print "Vnesi samo eno številko! "

def razdalja():
    while True:
        pozdrav = "Pretvornik razdalje: **NAVIGACIJSKE ŠTEVILKE ZA IZBIRO** 1:km <-> mi  2:ft <-> m  3:in <-> cm  9:Izhod"
        print pozdrav.center(200, ' ')
        izbira = raw_input()
        if not re.match("^[0-9]*$", izbira):
            print "SAMO ŠTEVILKE PROSIM!!! \n"
        elif izbira == "1":
            print "Pretvori kilometre v milje in obratno"
            mi_km()
        elif izbira == "2":
            print "Pretvori metre v noge in obratno"
            ft_m()
        elif izbira == "3":
            print "Pretvori centimetre v inče in obratno"
            in_cm()
        elif izbira == "9":
            break
        else:
            print "Vnesi samo eno številko! "

def mi_km():
    vnos = float(raw_input())
    mi = vnos * 0.62137
    km = vnos / 0.62137
    print "Vnesel si %f kilometrov/milj, rezultat je:\n %fkm -> %.3fmi \n %fmi -> %.3fkm" % (vnos, vnos, mi, vnos, km)

def ft_m():
    vnos = float(raw_input())
    ft = vnos * 3.2808
    m = vnos / 3.2808
    print "Vnesel si %f metrov/nog, rezultat je:\n %fm -> %.3fft \n %fft -> %.3fm" % (vnos, vnos, ft, vnos, m)

def in_cm():
    vnos = float(raw_input())
    inch = vnos * 0.39370
    cm = vnos / 0.39370
    print "Vnesel si %f centimetrov/inčev, rezultat je:\n %fcm -> %.3fin \n %fin -> %.3fcm" % (vnos, vnos, inch, vnos, cm)

def volumen():
    while True:
        pozdrav = "Pretvornik volumna tekočin: **NAVIGACIJSKE ŠTEVILKE ZA IZBIRO** 1:ml <-> oz  2:L <-> gal  3:L <-> oz 4:EU prostorninske enote 9:Izhod"
        print pozdrav.center(200, ' ')
        izbira = raw_input()
        if not re.match("^[0-9]*$", izbira):
            print "SAMO ŠTEVILKE PROSIM!!! \n"
        elif izbira == "1":
            print "Pretvori mililitre v unče in obratno"
            ml_oz()
        elif izbira == "2":
            print "Pretvori litre v galone in obratno"
            l_gal()
        elif izbira == "3":
            print "Pretvori litre v unče in obratno"
            l_oz()
        elif izbira == "4":
            print "EU prostorninske enote"
            eu_enote()
        elif izbira == "9":
            break
        else:
            print "Vnesi samo eno številko! "

def ml_oz():
    vnos = float(raw_input())
    oz = vnos * 0.033814
    ml = vnos / 0.033814
    print "Vnesel si %f mililitrov/unč, rezultat je:\n %fml -> %.3foz \n %foz -> %.3fml" % (vnos, vnos, oz, vnos, ml)

def l_gal():
    vnos = float(raw_input())
    gal = vnos * 0.26417
    L = vnos / 0.26417
    print "Vnesel si %f litrov/galon, rezultat je:\n %fL -> %.3fgal \n %fgal -> %.3fL" % (vnos, vnos, gal, vnos, L)

def l_oz():
    vnos = float(raw_input())
    oz = vnos * 33.814
    L = vnos / 33.814
    print "Vnesel si %f litrov/unč, rezultat je:\n %fL -> %.3foz \n %foz -> %.3fL" % (vnos, vnos, oz, vnos, L)

def eu_enote():
    print "Konverzija je bazirana na L (liter) prostornine."
    vnos = float(raw_input())
    ml = vnos / 1000.0
    cl = vnos / 100.0
    dl = vnos / 10
    hl = vnos / 100
    kub_ml = vnos * 10**6
    kub_cm = vnos * 10**3
    kub_dm = vnos
    kub_m = vnos / 10**3
    print "Vnesel si %f litrov, rezultat je:\n %.3fml -> %.3fcl -> %.3fdl -> %.3fhl\n Kubi:\n %.3fml^3 -> %.3fcm^3 -> %.3fdl^3 -> %.3fm^3"  % (vnos, ml, cl, dl, hl, kub_ml,kub_cm, kub_dm, kub_m)

def hitrost():
    while True:
        pozdrav = "Pretvornik hitrosti: **NAVIGACIJSKE ŠTEVILKE ZA IZBIRO** 1:km/s <-> mp/s  2:km/min <-> mp/min  3:km/h <-> mp/h 4: km/(s,min,h) <-> m/(s,min,h) 9:Izhod"
        print pozdrav.center(200, ' ')
        izbira = raw_input()
        if not re.match("^[0-9]*$", izbira):
            print "SAMO ŠTEVILKE PROSIM!!! \n"
        elif izbira == "1":
            print "Pretvori (kilo)metre na sekundo v milje/noge na sekundo in obratno"
            kms()
        elif izbira == "2":
            print "Pretvori (kilo)metre na minuto v milje/noge na minuto in obratno"
            kmin()
        elif izbira == "3":
            print "Pretvori (kilo)metre na uro v milje/noge na uro in obratno"
            kmh()
        elif izbira == "4":
            print "Pretvori kilometre na uro v (kilo)metre na.."
            km_m()
        elif izbira == "9":
            break
        else:
            print "Vnesi samo eno številko! "

def kms():
    vnos = float(raw_input())
    m_sec = vnos * 1000
    mi_sec = vnos * 0.621371
    fps = vnos / 0.000304799
    print "Vnesel si %fkm/s, rezultat je:\n %.fkm/s -> %.6fm/s -> %.6fmi/s -> %.6ffp/s" % (vnos, vnos, m_sec, mi_sec, fps)

def kmin():
    vnos = float(raw_input())
    m_min = vnos / 0.06
    mi_min = vnos * 0.621371
    fpmin = vnos / 0.000304799
    print "Vnesel si %fkm/min, rezultat je:\n %.fkm/min -> %.6fm/min -> %.6fmi/min -> %.6ffp/min" % (vnos, vnos, m_min, mi_min, fpmin)

def kmh():
    vnos = float(raw_input())
    m_h = vnos / 3.6
    mi_h = vnos * 0.621371
    fph = vnos / 0.000304799
    print "Vnesel si %fkm/h, rezultat je:\n %.fkm/h -> %.6fm/h -> %.6fmi/h -> %.6ffp/h" % (vnos, vnos, m_h, mi_h, fph)

def km_m():
    vnos = float(raw_input())
    cm_sec = vnos / 0.036
    m_sec = vnos / 3.6
    km_sec = vnos / 3600
    cm_min = vnos / 0.0006
    m_min = vnos / 0.06
    km_min = vnos / 60
    cm_h = vnos * 10**5
    m_h = vnos * 1000
    print "Vnesel si %fkm/h, rezultat je:\n %.fkm/h -> %.6fcm/s -> %.6fm/s -> %.6fkm/s -> %.6fcm/min -> %.6fm/min -> %.3fkm/min -> %.6fcm/h -> %.3fcm/h -> %.3fm/h" % (vnos, vnos, cm_sec, m_sec, km_sec, cm_min, m_min, km_min, cm_min, cm_h, m_h)

def teza():
    while True:
        pozdrav = "Pretvornik teže: **NAVIGACIJSKE ŠTEVILKE ZA IZBIRO** 1:kg <-> lb  2:g <-> oz  3:oz <-> lb  9:Izhod"
        print pozdrav.center(200, ' ')
        izbira = raw_input()
        if not re.match("^[0-9]*$", izbira):
            print "SAMO ŠTEVILKE PROSIM!!! \n"
        elif izbira == "1":
            print "Pretvori kilograme v funte in obratno"
            kg_lb()
        elif izbira == "2":
            print "Pretvori grame v unče in obratno"
            g_oz()
        elif izbira == "3":
            print "Pretvori unče v funte in obratno"
            oz_lb()
        elif izbira == "9":
            break
        else:
            print "Vnesi samo eno številko! "

def kg_lb():
    vnos = float(raw_input())
    lb = vnos * 2.2046
    kg = vnos / 2.2046
    print "Vnesel si %f kilogramov/funtov, rezultat je:\n %fkg -> %.3flb \n %flb -> %.3fkg" % (vnos, vnos, lb, vnos, kg)

def g_oz():
    vnos = float(raw_input())
    oz = vnos * 0.035274
    g = vnos / 0.035274
    print "Vnesel si %f gramov/unč, rezultat je:\n %fg -> %.3foz \n %foz -> %.3fg" % (vnos, vnos, oz, vnos, g)

def oz_lb():
    vnos = float(raw_input())
    oz = vnos * 16.000
    lb = vnos / 16.000
    print "Vnesel si %f funtov/unč, rezultat je:\n %flb -> %.3foz \n %foz -> %.3flb" % (vnos, vnos, oz, vnos, lb)

def temperatura():
    while True:
        pozdrav = "Pretvornik temperature: **NAVIGACIJSKE ŠTEVILKE ZA IZBIRO** 1:C <-> F  2:C <-> K  3:F <-> K  9:Izhod"
        print pozdrav.center(200, ' ')
        izbira = raw_input()
        if not re.match("^[0-9]*$", izbira):
            print "SAMO ŠTEVILKE PROSIM!!! \n"
        elif izbira == "1":
            print "Pretvori temperatura Celzij v Farenheit in obratno"
            c_f()
        elif izbira == "2":
            print "Pretvori temperatura Celzij v Kelvin in obratno"
            c_k()
        elif izbira == "3":
            print "Pretvori temperatura Farenheit v Kelvin in obratno"
            f_k()
        elif izbira == "9":
            break
        else:
            print "Vnesi samo eno številko! "

def c_f():
    vnos = float(raw_input())
    tmp_f = vnos + 32
    tmp_c = vnos - 32
    print "Vnesel si %f stopinj C/F, rezultat je:\n %fC -> %.3fF \n %fF -> %.3fC" % (vnos, vnos, tmp_f, vnos, tmp_c)

def c_k():
    vnos = float(raw_input())
    tmp_k = vnos + 273.15
    tmp_c = vnos - 273.15
    print "Vnesel si %f stopinj C/F, rezultat je:\n %fC -> %.3fK \n %fK -> %.3fC" % (vnos, vnos, tmp_k, vnos, tmp_c)

def f_k():
    vnos = float(raw_input())
    tmp_f = vnos * 9/5 - 459.67
    tmp_k = (vnos + 459.67) * 5/9
    print "Vnesel si %f stopinj C/F, rezultat je:\n %fK -> %.3fF \n %fF -> %.3fK" % (vnos, vnos, tmp_f, vnos, tmp_k)

def fizzbuzz():
    print "Vnesi število med 1 in 100 za super izpis :) "
    izbira = raw_input()
    if not re.match("^[0-9]*$", izbira) and 0 <= int(izbira) <= 100:
        print "SAMO ŠTEVILKE PROSIM!!! \n"
    for izbira in range(1, int(izbira)+1):
        if izbira % 3 == 0 and izbira % 5 == 0:
            print "fizzbuzz"
        elif izbira % 3 == 0:
            print "fizz"
        elif izbira % 5 == 0:
            print "buzz"
        else:
            print izbira

def main():
    while True:
        pozdrav = "**NAVIGACIJSKE ŠTEVILKE ZA IZBIRO** 1:Pretvornik  2:FizzBuzz  9:Izhod "
        print pozdrav.center(200, ' ')
        izbira = raw_input()
        if not re.match("^[0-9]*$", izbira):
            print "SAMO ŠTEVILKE PROSIM!!! \n"
        elif izbira == "1":
            pretvornik()
        elif izbira == "2":
            fizzbuzz()
        elif izbira == "9":
            print "papa, se vidimo naslednjič :) !"
            break
        else:
            print "Vnesi samo eno številko! "

pozdrav = " Pozdravljen Uporabnik! Sem program, ki ima 2 funkciji - pretvornik enot in igra FizzBuzz "
print pozdrav.center(200, '*')
print "\n"
main()
