from booking.booking import Booking


with Booking() as bot:
    bot.load_first_page()
    bot.change_currency(currency='USD')




