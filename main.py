import data
import pandas as pd

TUB_LITRES = 10

paints_list = []

for colour, pigments in data.LIMEWASH_COLOURS.items():
    # print(f"Paint: {colour.title()}")
    pigment_list = []
    for pigment, amount in pigments.items():

        # print(f"Ing: {pigment}.........Amount: {amount}")
        if pigment in data.PIGMENT_BREAKDOWNS:
            quarter_value_per_tub_volume = ((data.PIGMENT_BREAKDOWNS[pigment] * 3) / 16) * TUB_LITRES
            grams_of_pigment = round((amount / .25) * quarter_value_per_tub_volume, 2)

            if grams_of_pigment.is_integer():
                grams_of_pigment = int(grams_of_pigment)
            pigment_list.append({pigment: grams_of_pigment})
            # print(f"Amount of {pigment} in {colour} for {TUB_LITRES}lt at ratio {amount} = {grams_of_pigment}g")
        else:
            print(f"Pigment {pigment} not located")

    paints_list.append([colour.title(), pigment_list])
    print("")


rows = []

for paint in paints_list:
    name, pigment_dict = paint
    for i, pig in enumerate(pigment_dict):
        for p, amnt in pig.items():
            rows.append([name if i == 0 else "", p, amnt])


pd.set_option("display.max_rows", None)
df = pd.DataFrame(rows, columns=[f"Colour", "Pigment", f"Amount(g) for {TUB_LITRES}lt"])
df.to_csv("paints.csv", index=False)
