#!/usr/bin/python
# -*- coding: utf-8 -*-
# Grabspams
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Grabspams

import os, sys, time, random
from time import sleep

info = """
Nama        : Grabspams
Versi       : 1.1 (Update: 22 Juli 2020, 1:11 AM)
Tanggal     : 11 Januari 2019
Author      : Nedi Senja
Tujuan      : Untuk mengirim spam kepada
              mantan ASU hhe:v
Terimakasih : Allah SWT.
              FR13NDS, & seluruh
              manusia seplanet bumi
NB          : Manusia gax ada yang sempurna
              sama kaya tool ini.
              Silahkan laporkan kritik atau saran
              Ke - Email: d_q16x@outlook.co.id
                 - WhatsApp: +62 8577-5433-901

[ \033[4mGunakan tool ini dengan bijak \033[0m]\n """

example = """\033[0;101;77;1m[          Grabspams, My Github: @stepbystepexe          ]\033[0m"""

logo = """
 \033[0;36m█▀▀▀▀ █▀▀▀▄ █▀▀▀█ █▀▀▀▄ █▀▀▀▀ █▀▀▀█ █▀▀▀█ █▀▀█▀▀█ █▀▀▀▀
 \033[0;36m█   █ █▀▀▀▄ █▀▀▀█ █▀▀▀▄ ▀▀▀▀█ █▀▀▀▀ █▀▀▀█ █  █  █ ▀▀▀▀█
 \033[0;36m▀▀▀▀▀ ▀   ▀ ▀   ▀ ▀▀▀▀  ▀▀▀▀▀ ▀     ▀   ▀ ▀     ▀ ▀▀▀▀▀
"""

def restart():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    curdir = os.getcwd()

def write(o):
    for i in o + '\n':
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.03)

def serverotp():
    os.system('clear')
    os.system('reset')
    sleep(1)
    print()
    print(logo)
    print(example)
    print()
    write("\033[0m[ \033[32mINFO \033[0m] \033[3mSaya tidak real kalo code program saya ini ditiru")
    write("         Seburuk apaun itu tolong hargai karya milik orang\033[0m\n")
    os.system('php .otp')

os.system('clear')
os.system('reset')
sleep(1)
print()
print(logo)
print(example)
print()
print("\033[0m[\033[1;96;2m1\033[0m] \033[1;77mKirim Spam OTP")
print()
print("\033[0m[\033[93;1m&\033[0m] LISENSI")
print("\033[0m[\033[94;1m#\033[0m] Informasi")
print("\033[0m[\033[92;1m*\033[0m] Perbarui")
print("\033[0m[\033[91;1m-\033[0m] Keluar")
print()
option = input("\033[0m(\033[105;77;1m/\033[0m) \033[1;77mMasukan opsi: \033[0m")
if option.strip() in '1 kirim'.split():
    write("\n\033[0m[\033[32m●\033[0m] \033[77;1mSedang memproses ...\033[0m")
    sleep(1)
    serverotp()
elif option.strip() in '& 2 lisensi'.split():
    print()
    os.system('nano LICENSE')
    print()
    restart()
elif option.strip() in '# 3 info'.split():
    os.system('clear')
    print(example)
    os.system('toilet -f smslant Grab')
    print(info)
    sleep(1)
    print()
    input('[ Tekan Enter ]')
    restart()
elif option.strip() in '* 4 perbarui'.split():
    print()
    os.system('git pull origin master')
    print()
    input('\033[0m[ \033[32mTekan Enter \033[0m]')
    restart()
elif option.strip() in '- 0 keluar'.split():
    print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!")
    print()
    sys.exit(1)
else:
    print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
    print()
    sleep(1)
    restart()
