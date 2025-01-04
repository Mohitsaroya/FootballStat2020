import matplotlib.pyplot as plt
import pandas as pd

class Plots():
    def __init__(self, base_folder):
        self.base_folder = base_folder
        self.file_names = {
            "league_stats": "leaguestatistics.csv",
            "premier_league": "premierleaguestat.csv",
            "serie_a": "seriastat.csv",
            "la_liga": "laligastat.csv",
            "ligue_1": "ligue1stat.csv",
            "bundesliga": "bundesligastat.csv"
        }
        self.dataframes = {}
        self.load_data()
        
            
    def load_data(self):
        for name, file_name in self.file_names.items():
            file_path = f"{self.base_folder}/{file_name}"
            try:
                self.dataframes[name] = pd.read_csv(file_path, encoding='ISO-8859-1')
                print(f"Loaded {file_name} successfully.")
            except FileNotFoundError:
                print(f"File not found: {file_path}")
            except UnicodeDecodeError:
                print(f"Encoding error in file: {file_path}")
        
        
    def table_league(self, choice):
        df = self.dataframes.get('league_stats')
        if choice == 1:
            print(df[["football league", "country", "goals per match"]])
        elif choice == 2:
            print(df[["football league", "home goals per match", "goals per match"]])
        elif choice == 3:
            print(df[["football league", "home wins", "away wins"]])
    
    def bar_graph_league(self, choice):
        if choice == 1:
            df = pd.DataFrame[["football league", "goals per match"]]
            plt.bar(df["football league"], df["goals per match"])
            plt.title("goals per match by League")
            plt.show()
        elif choice == 2:
            df = pd.DataFrame[["football league", "home goals per match", "away goals per match"]]
            plt.bar(df["football league"], df["home goals per match"], label="home Goals")
            plt.bar(df["football league"], df["away goals per match"], label="away Goals")
            plt.title("home and away goals per match by League")
            plt.legend()
            plt.show()
        elif choice == 3:
            df = pd.DataFrame[["football league", "home wins", "away wins"]]
            plt.bar(df["football league"], df["home wins"], label="home wins")
            plt.bar(df["football league"], df["away wins"], label="away wins")
            plt.title("home and away wins by League")
            plt.legend()
            plt.show()
    
    def line_graph_league(self, choice):
        if choice == 1:
            df = pd.DataFrame[["football league", "goals per match"]]
            plt.plot(df["football league"], df["goals per match"])
            plt.title("goals per match by League")
            plt.show()
        elif choice == 2:
            df = pd.DataFrame[["football league", "home goals per match", "away goals per match"]]
            plt.plot(df["football league"], df["home goals per match"], label="home Goals")
            plt.plot(df["football league"], df["away goals per match"], label="away Goals")
            plt.title("home and away goals per match by League")
            plt.legend()
            plt.show()
        elif choice == 3:
            df = pd.DataFrame[["football league", "home wins", "away wins"]]
            plt.plot(df["football league"], df["home wins"], label="home wins")
            plt.plot(df["football league"], df["away wins"], label="away wins")
            plt.title("home and away wins by League")
            plt.legend()
            plt.show()
