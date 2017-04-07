def convert(wh):
    result = 0
    if len(str(wh)) >= 10:
        result = str(wh / 1000 / 1000 / 1000)[:6] + 'MWh'
    elif len(str(wh)) >= 7:
        result = str(wh / 1000 / 1000)[:6] + 'kWh'
    elif len(str(wh)) >= 4:
        result = str(wh / 1000)[:6] + 'Wh'
    elif len(str(wh)) <= 3:
        result = str(wh)[:6] + 'mWh'

    return result
