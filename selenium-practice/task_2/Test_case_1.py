from STEAM.steam import Steam

while True:
    try:
        Width = int(input("Set integer of screen width above 1200: "))
        if Width < 1200:
            raise Exception
        Height = int(Width*(3/4))
        print("Height will be: ", Height)
        break
    except:
        print("Enter integers above 1200 for god sake")


with Steam.getInsctance(False, Width, Height) as bot:

    bot.load_first_page()
    bot.press_ABOUT()
    bot.compare_gamers()
    bot.go_to_store()





