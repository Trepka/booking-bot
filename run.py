from booking.booking import Booking

try:
    with Booking() as bot:
        bot.land_first_page()
        bot.change_currency(currency='USD')
        bot.select_place_to_go(input('Укажите куда вы хотите поехать?(Например:"New York"): '))
        bot.select_dates("2022-11-17", "2022-12-17")
        bot.select_adults(3)
        bot.click_search()
        try:
            bot.close_pop_up()
        except:
            pass
        bot.apply_filtrations(input("Укажите количество звезд (Например: '4 звезды'): "))
        bot.refresh()
        bot.report_result()

except Exception as e:
    if 'in PATH' in str(e):
        print(
            'You trying to run bot from a command line \n'
            'Please add to PATH your Selenium Drivers \n'
            'Windows: \n'
            '   set PATH=%PATH%;C:\path-to-your-folder\n'
            )
    else:
        raise
