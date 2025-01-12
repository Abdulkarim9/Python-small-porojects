from forex_python.converter import CurrencyRates
from win10toast import ToastNotifier
from PIL import Image
from datetime import datetime


toast = ToastNotifier()


c = CurrencyRates()
# USD Dollar to Turkish Lira
USD_TO_TL = c.get_rate("USD", "TRY")
USD_TO_TL = str(USD_TO_TL)[:5]

# Turkish Lira to USD Dollar
TL_TO_USD = c.get_rate("TRY", "USD")
TL_TO_USD = str(TL_TO_USD)[:5]

# EUR to Turkish lira
EUR_TO_TL = c.get_rate("EUR", "TRY")
EUR_TO_TL = str(EUR_TO_TL)[:5]

# Turkish Lira to EUR
TL_TO_EUR = c.get_rate("TRY", "EUR")
TL_TO_EUR = str(TL_TO_EUR)[:5]


icon_file_path = "C:/Users/abdul/Saved-Pictures/money.png"
img = Image.open(icon_file_path)
img.save("money.ico")
file_name = "money.ico"


def notifier():
    toast.show_toast("Currency Rate",
                     f"USD :  {USD_TO_TL} ₺\nEUR :  {EUR_TO_TL} ₺\n",
                     duration=5,
                     icon_path=file_name,
                     threaded=True)


def main():
    time = datetime.now()
    if time.hour == 8 and time.minute == 00 and time.second == 00:
        notifier()
    if time.hour == 18 and time.minute == 00 and time.second == 00:
        notifier()



if __name__ == "__main__":

    while True:
        main()

