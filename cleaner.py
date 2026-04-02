def clean_data(data):
    clean_data = []
    for flt in data[1:]:
        flt = float(flt.replace("\n", ""))
        clean_data.append(flt)
    return clean_data