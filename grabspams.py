#!/usr/bin/python
# -*- coding: utf-8 -*-
# Grabspams
# Coded by Nedi Senja
# Github: https://github.com/stepbystepexe/Grabspams

import os, sys, time, random

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

example = """\033[0;101;77;1m[        Grabspams OTP, My Github: @stepbystepexe        ]\033[0m"""

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

os.system('clear')
os.system('reset')
time.sleep(1)
print()
print(logo)
print(example)
print()
print("\033[0m[\033[1;96mあ\033[0m] \033[1;77mKirim Spam OTP")
print()
print("\033[0m[\033[93;1m&\033[0m] LISENSI")
print("\033[0m[\033[94;1m#\033[0m] Informasi")
print("\033[0m[\033[92;1m*\033[0m] Perbarui")
print("\033[0m[\033[91;1m-\033[0m] Keluar")
print()
option = input("\033[0m[\033[1;95m/\033[0m] \033[1;77mMasukan opsi: \033[0m")
if option.strip() in 'あ 1 kirim'.split():
    write("\n\n\033[0m[\033[91;1m!\033[0m] Membuka Server OTP ...\033[0m\n")
    time.sleep(1)
    os.system('php __otp__.php')
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
    time.sleep(1)
    print()
    input('[ Tekan Enter ]')
    restart()
elif option.strip() in '* 4 perbarui'.split():
    print()
    os.system('git pull origin master')
    print()
    input('\033[0m[ \033[92mTekan Enter \033[0m]')
    restart()
elif option.strip() in '- keluar 0'.split():
    print("\n\033[0m[\033[1;91m!\033[0m] \033[1;77mKeluar dari program!")
    print()
    sys.exit(1)
else:
    print("\n\033[0m[=\033[1;41;77m Pilihan Salah \033[0m=]")
    print()
    time.sleep(1)
    restart()
