
def setup_files():
    with open('./resources/dates', 'r') as f:
        text = f.read()
        text = text.replace(',', '')
        text = text.replace('" (', '", ')
        text = text.replace('1983)', '1983,')
        text = text.replace('1984)', '1984,')
        text = text.replace('1985)', '1985,')
        text = text.replace('1986)', '1986,')
        text = text.replace('1987)', '1987,')
        text = text.replace('1988)', '1988,')
        text = text.replace('1989)', '1989,')
        text = text.replace('1990)', '1990,')
        text = text.replace('1991)', '1991,')
        text = text.replace('1992)', '1992,')
        text = text.replace('1993)', '1993,')
        text = text.replace('1994)', '1994,')
        
    with open('./resources/modified_dates', 'w') as f:
        f.write(text)


if __name__ == '__main__':
    setup_files()
