import time
import random

items = []
pizza = ["Margherita", "Neapolitan", "Marinara", "Focaccia"]


def print_pause(text):
    print(text)
    time.sleep(1)


def intro():
    print_pause("Setelah sekian lama berpacaran dengan kekasihmu")
    print_pause("Akhirnya hari ini kamu akan bertamu ke rumahnya")
    print_pause("Disana terdapat orang tuanya juga.\n")
    print_pause("Saat ini kamu sudah bersiap untuk pergi, "
                "ada 2 pilihan yang akan kamu lakukan selanjutnya:")


def choice():
    print_pause("1. Pergi ke rumah kekasihmu")
    print_pause("2. Pergi ke Toko Pizza untuk memesan "
                "Pizza " + random.choice(pizza) + " untuk oleh-oleh"
                "kekasihmu dan keluarganya")
    print_pause("Pilih pilihan 1 atau 2.")


def come_to_girl_home():
    print_pause("Kamupun datang ke rumah kekasihmu")
    if "pizza" in items:
        print_pause("Kamu pun sampai di rumah kekasihmu")
        print_pause("Banyak obrolan")
        print_pause("Apa yang akan kamu lakukan selanjutnya?")
    else:
        print_pause("Sesampainya disana, obrolannya flat "
                    "dan kekasihmu muram dan nampaknya merasa lapar")
        print_pause("Apa yang kamu lakukan:")
    print_pause("1. tetap melanjutkan obrolan")
    print_pause("2. Pergi keluar")


def come_to_pizza_store():
    if "pizza" in items:
        print_pause("Kamu sudah membeli pizza")
        print_pause("Dan uangmu habis")
        print_pause("Kamu tidak bisa membeli Pizza lagi")
        print_pause("Kamupun keluar")
    else:
        print_pause("Akhirnya kamu memutuskan untuk membeli pizza")
        print_pause("Sesampainya di toko pizza, "
                    "kamu memesan Pizza " + random.choice(pizza))
        print_pause("Selesai dari Toko Pizza, kamu keluar")
        print_pause("Apa yang akan kamu lakukan selanjutnya?")
        items.append("pizza")


def result():
    if "pizza" in items:
        print_pause("Kamu baru ingat kamu membawakan "
                    "Pizza " + random.choice(pizza) + " kesukaan kekasihmu")
        print_pause("Tak hanya satu, kamupun membawakan "
                    "beberapa untuk keluarganya juga")
        print_pause("Yap, kekasihmu terlihat senang "
                    "melihat caramu memperlakukannya")
        print_pause("Orang tua kekasihmu juga ikut "
                    "senang karena kamu sangat baik")
        print_pause("Selamat kamu menjadi kekasih yang sangat baik! CONGRATS!")
    else:
        print_pause("Tak berselang lama obrolan membosankan, "
                    "dan kekasihmu kesal karena kamu tidak peka")
        print_pause("Akhirnya kekasihmu ngambek, dan kamu "
                    "tidak obrolanmu tidak ditanggapi kekasihmu")
        print_pause("GAME OVER")


def exit_from_girl_home():
    print_pause("Kamu akhirnya keluar dari rumah kekasihmu")
    print_pause("Ada beberapa pilihan berikut yang harus kamu pilih")


def play_again():
    print_pause("Mau bermain lagi? Y/N")
    pilihan = input("")
    if pilihan == "Y" or pilihan == "y":
        print_pause("OK, mari coba lagi!\n")
        play_game()
    elif pilihan == "N" or pilihan == "n":
        print_pause("Ok, terima kasih sudah mencoba game ini!")
    else:
        print("Input Y atau N ya..")
        play_again()


def condition():
    while True:
        choice()
        pilihan = input("")
        if pilihan == "1":
            come_to_girl_home()
            pilihan = input("")

            if pilihan == "1":
                result()
                break

            if pilihan == "2":
                exit_from_girl_home()

        elif pilihan == "2":
            come_to_pizza_store()


def play_game():
    intro()
    condition()
    play_again()


if __name__ == "__main__":
    play_game()
