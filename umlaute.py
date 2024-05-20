# Für newline und Umlaute und SZ zu ändern
#special_char_map = {'Ã„':'Ae', 'Ã–':'Ue', 'Ãœ':'Oe', 'Ã¤':'ae', 'Ã¶':'ue', 'Ã¼':'oe', 'ÃŸ':'sz'}
def umlaute(wort):
    wort = wort.strip()
    length = len(wort)
    neuesWort = ""
    i = 0
    while i < length:
        firstchar = wort[i]
        if firstchar == "Ã":
            try:
                secondchar = wort[i+1]
            except:
                print("Es kamm zu einer Fehlermeldung bei diesem Wort: " + wort)
                i+=1
                continue
            if secondchar == "„":
                neuesWort = neuesWort + "Ae"
                i+=1
            elif secondchar == "–":
                neuesWort = neuesWort + "Oe"
                i+=1
            elif secondchar == "œ":
                neuesWort = neuesWort + "Ue"
                i+=1
            elif secondchar == "¤":
                neuesWort = neuesWort + "ae"
                i+=1
            elif secondchar == "¶":
                neuesWort = neuesWort + "oe"
                i+=1
            elif secondchar == "¼":
                neuesWort = neuesWort + "ue"
                i+=1
            elif secondchar == "Ÿ":
                neuesWort = neuesWort + "sz"
                i+=1
        else:
            neuesWort = neuesWort + firstchar
        i+=1
    return neuesWort
