import pandas as pd


df_dex = pd.read_csv("pokedex.csv")
print("\n",df_dex)

'''
Source: https://www.kaggle.com/datasets/rzgiza/pokdex-for-all-1025-pokemon-w-text-description

Id:
Name:
Height:
Weight:
Hp:
Attack:
Defense:
Special attack:
Special Defense:
Speed:
Type:
Evolution Set:
Info:
'''


df_leagues = pd.read_json("brasil-serie-b-2024.json")
print(df_leagues)

'''
Source: https://www.kaggle.com/datasets/rferreras/footballdata

Match date:
Round:
Home:
Away:
Goals Home:
Goals Away:
'''
