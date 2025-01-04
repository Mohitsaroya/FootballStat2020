import matplotlib.pyplot as plt
import pandas as pd

class Plots():
    def __init__(self):
        self.league_index = {1 : "premier_league", 2 : "serie_a", 3 : "la_liga", 4 : "ligue_1", 5 : "bundesliga"}
        
        
    def table_league(choice):
        if choice == 1:
            print(pd.DataFrame[["Football League", "Country", "Goals per Match"]])
        elif choice == 2:
            print(pd.DataFrame[["Football League", "Home goals per match", "Away goals per match"]])
        elif choice == 3:
            print(pd.DataFrame[["Football League", "Home Wins", "Away Wins"]])
    
    
        
        
    
