price_rubles = int(input("Стоимость пирожка (рубли): "))
price_kopecks = int(input("Стоимость пирожка (копейки): "))
quantity = int(input("Сколько пирожков: "))

total_kopecks = price_rubles * 100 + price_kopecks
total_payment_kopecks = total_kopecks * quantity

total_rubles = total_payment_kopecks // 100
total_kopecks_final = total_payment_kopecks % 100

print(f"К оплате: {total_rubles} руб. {total_kopecks_final} коп.")