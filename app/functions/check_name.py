def is_valid_name(name):
    names = ["Jan", "Piet", "Kees", "David"]
    if name.capitalize() in names:
        return True
    else:
        return False
