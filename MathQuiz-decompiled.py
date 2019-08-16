import os
import time
import random
import datetime
from datetime import timedelta

os.system('clear')
logo = "\x1b[1;33m\n __  __       _   _ \n|  \\/  | __ _| |_| |__ \n| |\\/| |/ _` | __| '_ \\ \n| |  | | (_| | |_| | | | \n|_|  |_|\\__,_|\\__|_| |_| By JustAHacker"
print logo + '\n\x1b[1;35m\n\x1b[1;32m1.Easy\n\x1b[1;33m2.Normal\n\x1b[1;34m3.Hard\n\x1b[1;36m4.extreme'
mode = raw_input('\x1b[1;38mPilih Tingkat Kesulitan : ')

def main():
    if mode == '1':
        easy()
    elif mode == '2':
        normal()
    elif mode == '3':
        hard()
    elif mode == '4':
        extreme()
    else:
        print 'Pilihan Tidak ada'
        main()


def easy():
    soal = int(raw_input('\x1b[1;39mJumlah Soal = '))
    waktuawal = time.time()
    a = 0
    soal1 = 0
    score = 0
    benar = 0
    salah = 0
    scoreadd = 1
    for i in range(int(soal)):
        while int(soal) < 1:
            waktuakhir = time.time()
            lamawaktu = waktuakhir - waktuawal
            os.system('clear')
            print 'lama waktu anda mengerjakan ini ' + str(lamawaktu) + ' detik'
            print '\x1b[1;36mSoal Sudah Selesai\n'
            print '\x1b[1;33mJumlah Score anda = ', score
            print '\x1b[1;32mJumlah Benar anda = ', benar
            print '\x1b[1;36mJumlah Salah anda = ', salah
            print '\x1b[1;33mJumlah Soal = ', soal1
            print '\x1b[1;38mMode : Easy'
            os.sys.exit()

        while int(soal) > 0:
            a += 1
            soal1 += 1
            soal -= 1
            os.system('clear')
            ops = [' + ', ' - ']
            rand = random.randint(60, 90)
            rand2 = random.randint(30, 60)
            operation = random.choice(ops)
            maths = eval(str(rand) + operation + str(rand2))
            print '\x1b[1;32mScore Saat Ini = ' + str(score)
            print 'Soal Ke : ' + str(a)
            print '\x1b[1;33mHasil Dari ' + str(rand) + operation + str(rand2)
            ans = int(raw_input('\x1b[1;36mJawab = '))
            if ans == maths:
                scoreadd += 1
                os.system('clear')
                score += scoreadd
                benar += 1
                print '\x1b[1;32mJawaban anda benar'
                time.sleep(2)
            else:
                scoreadd = 0
                score -= 1
                salah += 1
                print 'jawaban anda salah \njawaban yang sebenarnya adalah : ' + str(maths)
                print '\x1b[1;35mScore Dikurangi 1'
                time.sleep(2)


def normal():
    soal = int(raw_input('\x1b[1;39mJumlah Soal = '))
    waktuawal = time.time()
    a = 0
    soal1 = 0
    score = 0
    benar = 0
    salah = 0
    scoreadd = 1
    for i in range(int(soal)):
        while int(soal) < 1:
            waktuakhir = time.time()
            lamawaktu = waktuakhir - waktuawal
            os.system('clear')
            print 'lama waktu anda mengerjakan ini ' + str(lamawaktu) + ' detik'
            print '\x1b[1;36mSoal Sudah Selesai\n'
            print '\x1b[1;33mJumlah Score anda = ', score
            print '\x1b[1;32mJumlah Benar anda = ', benar
            print '\x1b[1;36mJumlah Salah anda = ', salah
            print '\x1b[1;33mJumlah Soal = ', soal1
            print '\x1b[1;38mMode : Normal'
            os.sys.exit()

        while int(soal) > 0:
            a += 1
            soal -= 1
            soal1 += 1
            os.system('clear')
            ops = [' + ', ' - ']
            rand = random.randint(160, 190)
            rand2 = random.randint(90, 160)
            operation = random.choice(ops)
            maths = eval(str(rand) + operation + str(rand2))
            print '\x1b[1;32mScore Saat Ini = ' + str(score)
            print 'Soal Ke : ' + str(a)
            print '\x1b[1;33mHasil Dari ' + str(rand) + operation + str(rand2)
            ans = int(raw_input('\x1b[1;36mJawab = '))
            if ans == maths:
                scoreadd += 2
                os.system('clear')
                score += scoreadd
                benar += 1
                print '\x1b[1;32mJawaban anda benar'
                time.sleep(2)
            else:
                scoreadd = 0
                score -= 2
                salah += 1
                print 'jawaban anda salah \njawaban yang sebenarnya adalah : ' + str(maths)
                print '\x1b[1;35mScore Dikurangi 2'
                time.sleep(2)


def hard():
    soal = int(raw_input('\x1b[1;39mJumlah Soal = '))
    waktuawal = time.time()
    a = 0
    soal1 = 0
    score = 0
    benar = 0
    salah = 0
    scoreadd = 1
    for i in range(int(soal)):
        while int(soal) < 1:
            waktuakhir = time.time()
            lamawaktu = waktuakhir - waktuawal
            os.system('clear')
            print 'lama waktu anda mengerjakan ini ' + str(lamawaktu) + ' detik'
            print '\x1b[1;36mSoal Sudah Selesai\n'
            print '\x1b[1;33mJumlah Score anda = ', score
            print '\x1b[1;32mJumlah Benar anda = ', benar
            print '\x1b[1;36mJumlah Salah anda = ', salah
            print '\x1b[1;33mJumlah Soal = ', soal1
            print '\x1b[1;38mMode : Hard'
            os.sys.exit()

        while int(soal) > 0:
            a += 1
            soal -= 1
            soal1 += 1
            os.system('clear')
            ops = [' + ', ' - ']
            ops2 = [' - ', ' + ']
            rand = random.randint(260, 290)
            rand2 = random.randint(200, 260)
            rand3 = random.randint(160, 200)
            operation = random.choice(ops)
            operation2 = random.choice(ops2)
            maths = eval(str(rand) + operation + str(rand2) + operation2 + str(rand3))
            print '\x1b[1;32mScore Saat Ini = ' + str(score)
            print 'Soal Ke : ' + str(a)
            print '\x1b[1;33mHasil Dari ' + str(rand) + operation + str(rand2) + operation2 + str(rand3)
            ans = int(raw_input('\x1b[1;36mJawab = '))
            if ans == maths:
                scoreadd += 3
                os.system('clear')
                score += scoreadd
                benar += 1
                print '\x1b[1;32mJawaban anda benar'
                time.sleep(2)
            else:
                scoreadd = 0
                score -= 3
                salah += 1
                print 'jawaban anda salah \njawaban yang sebenarnya adalah : ' + str(maths)
                print '\x1b[1;35mScore Dikurangi 3'
                time.sleep(2)


def extreme():
    soal = int(raw_input('\x1b[1;39mJumlah Soal = '))
    waktuawal = time.time()
    a = 0
    score = 0
    benar = 0
    salah = 0
    soal1 = 0
    scoreadd = 1
    for i in range(int(soal)):
        while int(soal) < 1:
            waktuakhir = time.time()
            lamawaktu = waktuakhir - waktuawal
            os.system('clear')
            print 'lama waktu anda mengerjakan ini ' + str(lamawaktu) + ' detik'
            print '\x1b[1;36mSoal Sudah Selesai\n'
            print '\x1b[1;33mJumlah Score anda = ', score
            print '\x1b[1;32mJumlah Benar anda = ', benar
            print '\x1b[1;36mJumlah Salah anda = ', salah
            print '\x1b[1;33mJumlah Soal = ', soal1
            print '\x1b[1;38mMode : Extreme'
            os.sys.exit()

        while int(soal) > 0:
            a += 1
            soal1 += 1
            soal -= 1
            os.system('clear')
            ops = [' + ', ' - ']
            rand = random.randint(760, 790)
            rand2 = random.randint(630, 660)
            rand3 = random.randint(1, 50)
            ops2 = (' / ', ' * ')
            operation = random.choice(ops)
            operation2 = random.choice(ops2)
            maths = eval(str(rand) + operation + str(rand2) + operation2 + str(rand3))
            print '\x1b[1;32mScore Saat Ini = ' + str(score)
            print 'Soal Ke : ' + str(a)
            if operation2 == ' / ':
                print '\x1b[1;33mHasil Dari ' + str(rand) + operation + str(rand2) + ' : ' + str(rand3)
            if operation2 == ' * ':
                print '\x1b[1;33mHasil Dari ' + str(rand) + operation + str(rand2) + ' x ' + str(rand3)
            ans = int(raw_input('\x1b[1;36mJawab = '))
            if ans == maths:
                scoreadd += 4
                score += scoreadd
                benar += 1
                print '\x1b[1;32mJawaban anda benar'
                time.sleep(2)
            else:
                scoreadd = 0
                score -= 4
                salah += 1
                os.system('clear')
                print 'jawaban anda salah \njawaban yang sebenarnya adalah : ' + str(maths)
                print 'Karena Kalau Di Matematika, pembagian dan perkalian yang dijumlahkan duluan'
                print '\x1b[1;35mScore Dikurangi 4'
                time.sleep(4)


if __name__ == '__main__':
    main()
