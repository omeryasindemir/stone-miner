import pyautogui
import keyboard
import time

# Botun çalışma durumunu kontrol eden değişken
bot_running = False

# Kullanıcıdan bir sayı girmesini iste
max_key = int(input("1 ile 9 arasında bir sayı girin: "))
sec = int(input("Saniyeyi girin : "))

# Girilen sayıdan 1'e kadar olan tuş listesini oluştur
keys = [str(i) for i in range(1, max_key + 1)]

def toggle_bot():
    global bot_running
    bot_running = not bot_running
    if bot_running:
        print("Bot başlatıldı.")
    else:
        print("Bot durduruldu.")

# F7 tuşuna basıldığında toggle_bot fonksiyonunu çağırır
keyboard.add_hotkey('F7', toggle_bot)

print("Botu başlatmak veya durdurmak için F7 tuşuna basın.")

while True:
    if bot_running:
        for key in keys:
            pyautogui.press(key)
            print(f'{key} tuşuna tıklandı.')
            time.sleep(sec)  # 2 saniye bekle
            if not bot_running:  # Bot durdurulmuşsa döngüden çık
                break
    time.sleep(0.1)  # CPU kullanımını düşürmek için kısa bir bekleme
