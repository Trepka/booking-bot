from booking.booking import Booking
import booking.constants as const

with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='USD')
    bot.select_place_to_go("New York")
    bot.select_dates("2022-11-15", "2022-12-17")
    bot.select_adults(3)
    bot.click_search()
    bot.apply_filtrations()