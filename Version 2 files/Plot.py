import matplotlib.pyplot as plt
import textwrap

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


    def plot_stats(self, df, title, choice):
        """Plots team statistics for a specific league."""
        if choice == 1:
            if df.columns[0] == "Club Name":
                for column in df.columns[1:]:
                    plt.plot(df["Club Name"], df[column], marker='o', linestyle='-', label=column)
                plt.xlabel("Club Name")
            else:
                for column in df.columns[1:]:
                    plt.plot(df["football league"], df[column], marker='o', linestyle='', label=column)
                plt.xlabel("League Name")
            plt.ylabel("Values")
            plt.title(title)
            plt.xticks(rotation=35)
            plt.legend()
            plt.grid(True)
            plt.show()
        elif choice == 2:
            df.plot(x="Club Name", kind='bar', title=title)
            plt.xlabel("Club Name")
            plt.ylabel("Values")
            plt.xticks(rotation=35)
            plt.legend(df.columns[1:])  
            plt.show()

    def plot_league_comparison(self, df, choice):
        """Plots comparison between two leagues."""
        if choice == 1:
            plt.plot(df["football league"], df["goals per match"], marker='o', linestyle='-', label="Goals per Match")
            plt.plot(df["football league"], df["home goals per match"], marker='s', linestyle='--', label="Home Goals per Match")
            plt.plot(df["football league"], df["away goals per match"], marker='^', linestyle='-.', label="Away Goals per Match")
            plt.xlabel("Football League")
            plt.ylabel("Goals")
            plt.title("League Comparison: Goals per Match")
            plt.xticks(rotation=35)
            plt.legend()
            plt.grid(True)
            plt.show()
            
        elif choice == 2:
            df.plot(x="football league", y=["goals per match", "home goals per match", "away goals per match"],
                    kind='bar', title="League Comparison: Goals per Match")
            plt.xlabel("Football League")
            plt.ylabel("Goals per Match")
            plt.xticks(rotation=35)
            plt.legend(["Overall Goals", "Home Goals", "Away Goals"])
            plt.show()

    def plot_team_comparison(self, df, choice):
        """Plots comparison between two teams."""
        if choice == 1:
            plt.plot(df["Club Name"], df["Points"], marker='o', linestyle='-', label="Points")
            plt.plot(df["Club Name"], df["Goals For"], marker='s', linestyle='--', label="Goals For")
            plt.plot(df["Club Name"], df["Goals Against"], marker='^', linestyle='-.', label="Goals Against")
            plt.xlabel("Club Name")
            plt.ylabel("Statistics")
            plt.title("Team Comparison")
            plt.xticks(rotation=35)
            plt.legend()
            plt.grid(True)
            plt.show()
        elif choice == 2:
            df.plot(x="Club Name", y=["Points", "Goals For", "Goals Against"], kind='bar', title="Team Comparison")
            plt.xlabel("Club Name")
            plt.ylabel("Statistics")
            plt.xticks(rotation=35)
            plt.legend(["Points", "Goals For", "Goals Against"])
            plt.show()


    def plot_table(self, data, title, columns):
        """Displays the data as a table using matplotlib."""
        fig, ax = plt.subplots(figsize=(12, 8))  
        ax.axis('tight')
        ax.axis('off')
        
        wrapped_columns = [textwrap.fill(col, width=15) for col in columns]
        table = ax.table(cellText=data, colLabels=wrapped_columns, cellLoc='center', loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.2, 1.2)
        cell_1 = table.get_celld()
        for i in range(len(columns)):
            cell_1[(0, i)].set_height(.1)
        plt.title(title)
        plt.show()
    