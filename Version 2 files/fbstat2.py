########################
# stable version (mostly)
# Statistical Analysis of Top European Football Leagues From year 2020-2021 version 2
########################

from Prompts import Prompts
from Plot import Plots
import os
import pandas as pd

class FootballAnalysis:
    def __init__(self):
        self.prompts = Prompts()
        self.base_folder = os.path.join("csv files")
        self.plot_data = Plots(self.base_folder)
        self.file_names = {
            "league_stats": "leaguestatistics.csv",
            "premier_league": "premierleaguestat.csv",
            "serie_a": "seriastat.csv",
            "la_liga": "laligastat.csv",
            "ligue_1": "ligue1stat.csv",
            "bundesliga": "bundesligastat.csv"
        }

        self.leagues = {
            1: "Premier League",
            2: "Serie A",
            3: "La Liga",
            4: "Ligue 1",
            5: "Bundesliga"
        }

    def load_data(self, file_key):
        """Load CSV file based on the given key from file_names dictionary."""
        file_path = os.path.join(self.base_folder, self.file_names[file_key])
        try:
            df = pd.read_csv(file_path, encoding="ISO-8859-1")
            header = df.columns.tolist()
            header = header
            return df, header  
        except Exception as e:
            print(f"Error loading {file_path}: {e}")
            return None, None 
        
    def display_league_stats(self):
        """Display overall league statistics."""
        df, header = self.load_data("league_stats")
        header = header[2:-5]
        if df is not None:
            choice = self.prompts.choices_for_plot_gen()
            data = df.values.tolist()
            columns = df.columns.tolist()
            if choice == 1:
                self.plot_data.plot_table(data, "League Statistics Table", columns)
            if choice in [2, 3]:
                self.header_print(header=header)
                filtered_df = self.data_filter(df=df, header=header)
                if choice == 2:
                    self.plot_data.plot_stats(filtered_df, "Team Statistics Table", 1)
                if choice == 3:
                    self.plot_data.plot_stats(filtered_df, "Team Statistics Graph", 2)

    def display_team_stats(self):
        """Display team statistics for a selected league."""
        league_choice = self.prompts.choose_team_stat()
        league_key = list(self.file_names.keys())[league_choice] 
        
        df, header = self.load_data(league_key)
        header = header[3:-4]
        if df is not None:
            print(df)
            choice = self.prompts.choices_for_plot()
            if choice in [1, 2]:
                self.header_print(header=header)
                self.prompts.display_glossary()
                filtered_df = self.data_filter(df=df, header=header)
                if choice == 1:
                    self.plot_data.plot_stats(filtered_df, "Team Statistics Table", 1)
                elif choice == 2:
                    self.plot_data.plot_stats(filtered_df, "Team Statistics Graph", 2)
    
    def header_print(self, header):
        option_print = ""
        for i in range(len(header)):
            option_print += f'{i}: {header[i]}, '
        print(option_print[:-2])
    
    def data_filter(self, df, header):
        indices = self.prompts.data_vals_prompt(header)
        selected_columns = [header[int(index)] for index in indices]
        if df.columns[0] == "football league":
            filtered_df = df[["football league"] + selected_columns]
        else:
            filtered_df = df[["Club Name"] + selected_columns]
        return filtered_df

    def compare_leagues(self):
        """Compare statistics between two leagues."""
        leagues = self.prompts.compare_leagues()
        df = self.load_data("league_stats")

        if df is not None:
            league1 = self.leagues[leagues[0]]
            league2 = self.leagues[leagues[1]]
            df_filtered = df[df["football league"].isin([league1, league2])]
            print(df_filtered)

            choice = self.prompts.choices_for_plot()
            if choice in [1, 2]:
                self.plot_data.plot_league_comparison(df_filtered, choice)

    def compare_teams(self):
        """Compare statistics between two teams in the same league."""
        league_choice, team1, team2 = self.prompts.compare_teams()
        league_key = list(self.file_names.keys())[league_choice]

        df = self.load_data(league_key)
        if df is not None:
            df_filtered = df[df["Club Name"].isin([team1, team2])]
            print(df_filtered)

            choice = self.prompts.choices_for_plot()
            if choice in [1, 2]:
                self.plot_data.plot_team_comparison(df_filtered, choice)

    def run(self):
        """Main menu loop for user interaction."""
        while True:
            choice = self.prompts.main_menu()
            
            if choice == 0:
                self.prompts.display_glossary()
            elif choice == 1:
                self.display_league_stats()
            elif choice == 2:
                self.display_team_stats()
            elif choice == 3:
                compare_choice = self.prompts.compare_options()
                if compare_choice == 1:
                    self.compare_leagues()
                elif compare_choice == 2:
                    self.compare_teams()
            elif choice == 4:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid input. Please enter a valid choice.")

if __name__ == "__main__":
    analysis = FootballAnalysis()
    analysis.run()
