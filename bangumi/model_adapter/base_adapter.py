def item_to_document(obje, item):
    for key in item:
        setattr(obje, key, item[key])
    return obje
