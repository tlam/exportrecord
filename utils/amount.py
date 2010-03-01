import locale

def decimal_separator(amount):
    return locale.format('%.2f', amount, grouping=True)
