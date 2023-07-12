import time

def waktu(menit, detik):
    total_waktu = menit*60 + detik
    sp = 1

    while total_waktu:
        mins,secd = divmod(total_waktu,60)
        print(f"{mins:02d}:{secd:02d}", end="\r")
        time.sleep(sp)
        total_waktu -= 1

waktu(2,30)