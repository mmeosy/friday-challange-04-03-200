def writejsonfile(data):
    with open('coronainfo.json', 'w') as file:
        file.write('\n')
        file.write(data)
        