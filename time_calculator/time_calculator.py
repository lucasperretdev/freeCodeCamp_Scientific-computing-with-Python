def add_time(start, duration, starting_day=None):
    new_time = None

    # création d'une variable change_ampm, si le resultat est pair, alors on change sinon on garde
    change_ampm = 0

    # Déclaration des variables de base - heures et minutes de départ
    start_hours = int(start.split()[0].split(':')[0])
    start_minutes = int(start.split()[0].split(':')[1])
    AMorPM = start.split()[1]

    # Déclaration des variables de bases pour la durée
    duration_hours = int(duration.split(':')[0])
    duration_minutes = int(duration.split(':')[1])

    # Réalisation des calculs
    new_minutes_raw = start_minutes + duration_minutes
    new_minutes = new_minutes_raw
    add_hours = 0
    # calculs des minutes
    if new_minutes_raw >= 60:
        add_hours = int(new_minutes_raw/60)
        new_minutes = new_minutes_raw % 60

    # print('{:0>2}'.format(new_minutes), add_hours) <== pour formatter avec un 0 à gauche
    # calculs de l'heure finale
    new_hour_raw = start_hours + duration_hours + add_hours
    new_hour = new_hour_raw

    if new_hour_raw >= 12:
        change_ampm = int(new_hour_raw/12)
        new_hour = new_hour_raw % 12
        if new_hour == 0:
            new_hour = 12

        # calcul de AM ou PM
    new_AMorPM = AMorPM
    if (change_ampm % 2) != 0:
        if AMorPM == 'AM':
            new_AMorPM = 'PM'
        else:
            new_AMorPM = 'AM'

    # calcul du jour si != None
    # création d'un dic avec les jours de la semaine

    week = {'monday': 1, 'tuesday': 2, 'wednesday': 3,
            'thursday': 4, 'friday': 5, 'saturday': 6, 'sunday': 7}

    new_day_index = None

    new_hour_raw_day = new_hour_raw
    new_day_raw = int(new_hour_raw_day/24)
    if AMorPM == 'PM':
        new_hour_raw_day = new_hour_raw + 12
    if new_hour_raw_day >= 24:
        new_day_raw = int(new_hour_raw_day/24)

    if starting_day != None:
        starting_day_index = week[starting_day.lower()]
        new_day_index = starting_day_index

        new_hour_raw_day = new_hour_raw
        if AMorPM == 'PM':
            new_hour_raw_day = new_hour_raw + 12

        if new_hour_raw_day >= 24:
            new_day_raw = int(new_hour_raw_day/24)
            new_day_index = ((new_day_raw + starting_day_index) % 7)
            if new_day_index == 0:
                new_day_index = 7

        result_day = None
        for name, day in week.items():
            if day == new_day_index:
                result_day = name

    # mise en forme de new time
    if starting_day != None:

        if new_day_raw == 0:
            new_time = str(new_hour) + ':' + '{:0>2}'.format(new_minutes)+" " + new_AMorPM + ", " + \
                result_day.capitalize()
        if new_day_raw == 1:
            new_time = str(new_hour) + ':' + '{:0>2}'.format(new_minutes)+" " + new_AMorPM + ", " + \
                result_day.capitalize()+" (next day)"

        if new_day_raw >= 2:
            new_time = str(new_hour) + ':' + '{:0>2}'.format(new_minutes)+" " + new_AMorPM + ", " + \
                result_day.capitalize() + " (" + str(new_day_raw)+" days later"+")"

    else:
        if new_day_raw == 0:
            new_time = str(new_hour) + ':' + '{:0>2}'.format(new_minutes) + \
                " " + new_AMorPM
        if new_day_raw == 1:
            new_time = str(new_hour) + ':' + '{:0>2}'.format(new_minutes) + \
                " " + new_AMorPM + "" + " (next day)"

        if new_day_raw >= 2:
            new_time = str(new_hour) + ':' + '{:0>2}'.format(new_minutes)+" " + \
                new_AMorPM + "" + " (" + str(new_day_raw)+" days later"+")"

    return new_time
