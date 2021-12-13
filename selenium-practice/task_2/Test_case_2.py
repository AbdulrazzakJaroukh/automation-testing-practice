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
    bot.Go_to_Top_sellers()
    bot.choose_operating_system_Linux()
    bot.choose_number_of_players_LAN()
    bot.compare_num_of_games()
    a, b, c = bot.get_info_first_result()
    print(a, b, c)
    bot.click_first_result((a, b, c))


