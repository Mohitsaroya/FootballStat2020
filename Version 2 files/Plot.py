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
            
    
    def plot_goals_per_match(self, df):
        choice = self.choices_for_plot()

        if choice == 1:
            print(df[["Football League", "Goals per match"]])
        elif choice == 2:
            plt.plot(df["Football League"], df["Goals per match"])
            plt.title("Goals per Match by League")
            plt.show()
        elif choice == 3:
            df.plot(x="Football League", y="Goals per match", kind='bar', title="Goals per Match by League")
            plt.show()
    

