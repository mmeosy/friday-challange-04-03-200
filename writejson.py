def writejsonfile(data):
    with open('coronainfo.json', 'a') as file:
        file.write('\n')
        file.write(data)
        