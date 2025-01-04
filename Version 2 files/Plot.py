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
        if choice == 1:
            print(pd.DataFrame[["Football League", "Country", "Goals per Match"]])
        elif choice == 2:
            print(pd.DataFrame[["Football League", "Home goals per match", "Away goals per match"]])
        elif choice == 3:
            print(pd.DataFrame[["Football League", "Home Wins", "Away Wins"]])
    
    def bar_graph_league(self, choice):
        if choice == 1:
            df = pd.DataFrame[["Football League", "Goals per Match"]]
            plt.bar(df["Football League"], df["Goals per Match"])
            plt.title("Goals per Match by League")
            plt.show()
        elif choice == 2:
            df = pd.DataFrame[["Football League", "Home goals per match", "Away goals per match"]]
            plt.bar(df["Football League"], df["Home goals per match"], label="Home Goals")
            plt.bar(df["Football League"], df["Away goals per match"], label="Away Goals")
            plt.title("Home and Away Goals per Match by League")
            plt.legend()
            plt.show()
        elif choice == 3:
            df = pd.DataFrame[["Football League", "Home Wins", "Away Wins"]]
            plt.bar(df["Football League"], df["Home Wins"], label="Home Wins")
            plt.bar(df["Football League"], df["Away Wins"], label="Away Wins")
            plt.title("Home and Away Wins by League")
            plt.legend()
            plt.show()
    
    def line_graph_league(self, choice):
        if choice == 1:
            df = pd.DataFrame[["Football League", "Goals per Match"]]
            plt.plot(df["Football League"], df["Goals per Match"])
            plt.title("Goals per Match by League")
            plt.show()
        elif choice == 2:
            df = pd.DataFrame[["Football League", "Home goals per match", "Away goals per match"]]
            plt.plot(df["Football League"], df["Home goals per match"], label="Home Goals")
            plt.plot(df["Football League"], df["Away goals per match"], label="Away Goals")
            plt.title("Home and Away Goals per Match by League")
            plt.legend()
            plt.show()
        elif choice == 3:
            df = pd.DataFrame[["Football League", "Home Wins", "Away Wins"]]
            plt.plot(df["Football League"], df["Home Wins"], label="Home Wins")
            plt.plot(df["Football League"], df["Away Wins"], label="Away Wins")
            plt.title("Home and Away Wins by League")
            plt.legend()
            plt.show()
