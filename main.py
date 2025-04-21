import data

TUB_LITRES = 10

for colour, pigments in data.LIMEWASH_COLOURS.items():
    print(f"Paint: {colour.title()}")
    for pigment, amount in pigments.items():
        # print(f"Ing: {pigment}.........Amount: {amount}")
        if pigment in data.PIGMENT_BREAKDOWNS:
            quarter_value_per_tub_volume = ((data.PIGMENT_BREAKDOWNS[pigment] * 3 ) / 16) * TUB_LITRES
            grams_of_pigment = round((amount / .25) * quarter_value_per_tub_volume, 2)

            if grams_of_pigment.is_integer():
                grams_of_pigment = int(grams_of_pigment)

            print(f"Amount of {pigment} in {colour} for {TUB_LITRES}lt at ratio {amount} = {grams_of_pigment}g")
        else:
            print(f"Pigment {pigment} not located")
    print("")

