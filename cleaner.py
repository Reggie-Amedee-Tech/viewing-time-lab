def clean_data(data):
    clean_data = []
    for flt in data[1:]:
        flt = float(flt.replace("\n", ""))
        clean_data.append(flt)
        print('you have cleaned the data')
    return clean_data