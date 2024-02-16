def prevod_sekund():
    try:
        sekundy = int(input("Zadejte počet sekund pro převod: "))
        minuty = sekundy / 60
        hodiny = sekundy / 3600
        dny = sekundy / 86400

        print(f"{sekundy} sekund = {minuty} minut")
        print(f"{sekundy} sekund = {hodiny} hodin")
        print(f"{sekundy} sekund = {dny} dnů")
    except ValueError:
        print("Neplatný vstup. Zadejte prosím číslo.")

prevod_sekund()
