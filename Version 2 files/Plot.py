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

    def plot_league_stats(self, df, choice):
        """Plots general league statistics."""
        if choice == 2:
            plt.plot(df["football league"], df["goals per match"], marker='o', linestyle='-')
            plt.xlabel("Football League")
            plt.ylabel("Goals per Match")
            plt.title("Goals per Match by League")
            plt.xticks(rotation=45)
            plt.grid(True)
            plt.show()
        elif choice == 3:
            df.plot(x="football league", y="goals per match", kind='bar', title="Goals per Match by League", legend=False)
            plt.xlabel("Football League")
            plt.ylabel("Goals per Match")
            plt.xticks(rotation=45)
            plt.show()

    def plot_team_stats(self, df, choice):
        """Plots team statistics for a specific league."""
        if choice == 2:
            plt.plot(df["Club Name"], df["Points"], marker='o', linestyle='-', color="blue", label="Points")
            plt.xlabel("Club Name")
            plt.ylabel("Points")
            plt.title("Team Points in League")
            plt.xticks(rotation=45)
            plt.legend()
            plt.grid(True)
            plt.show()
        elif choice == 3:
            df.plot(x="Club Name", y="Points", kind='bar', title="Team Points in League", legend=False, color="blue")
            plt.xlabel("Club Name")
            plt.ylabel("Points")
            plt.xticks(rotation=45)
            plt.show()

    def plot_league_comparison(self, df, choice):
        """Plots comparison between two leagues."""
        if choice == 2:
            plt.plot(df["football league"], df["goals per match"], marker='o', linestyle='-', label="Goals per Match")
            plt.plot(df["football league"], df["home goals per match"], marker='s', linestyle='--', label="Home Goals per Match")
            plt.plot(df["football league"], df["away goals per match"], marker='^', linestyle='-.', label="Away Goals per Match")
            plt.xlabel("Football League")
            plt.ylabel("Goals")
            plt.title("League Comparison: Goals per Match")
            plt.xticks(rotation=45)
            plt.legend()
            plt.grid(True)
            plt.show()
        elif choice == 3:
            df.plot(x="football league", y=["goals per match", "home goals per match", "away goals per match"], kind='bar', title="League Comparison: Goals per Match")
            plt.xlabel("Football League")
            plt.ylabel("Goals per Match")
            plt.xticks(rotation=45)
            plt.legend(["Overall Goals", "Home Goals", "Away Goals"])
            plt.show()

    def plot_team_comparison(self, df, choice):
        """Plots comparison between two teams."""
        if choice == 2:
            plt.plot(df["Club Name"], df["Points"], marker='o', linestyle='-', label="Points")
            plt.plot(df["Club Name"], df["Goals For"], marker='s', linestyle='--', label="Goals For")
            plt.plot(df["Club Name"], df["Goals Against"], marker='^', linestyle='-.', label="Goals Against")
            plt.xlabel("Club Name")
            plt.ylabel("Statistics")
            plt.title("Team Comparison")
            plt.xticks(rotation=45)
            plt.legend()
            plt.grid(True)
            plt.show()
        elif choice == 3:
            df.plot(x="Club Name", y=["Points", "Goals For", "Goals Against"], kind='bar', title="Team Comparison")
            plt.xlabel("Club Name")
            plt.ylabel("Statistics")
            plt.xticks(rotation=45)
            plt.legend(["Points", "Goals For", "Goals Against"])
            plt.show()

    def plot_table(self, df, title):
        """Displays the dataframe as a table using matplotlib."""
        fig, ax = plt.subplots(figsize=(12, 8))  # Adjust the figure size as needed
        ax.axis('tight')
        ax.axis('off')
        table = ax.table(cellText=df.values, colLabels=df.columns, cellLoc='center', loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.2, 1.2)
        plt.title(title)
        plt.show()

    def plot_table(self, df, title):
        """Displays the dataframe as a table using matplotlib."""
        fig, ax = plt.subplots(figsize=(12, 8))  # Adjust the figure size as needed
        ax.axis('tight')
        ax.axis('off')
        
        # Wrap text for column headers
        wrapped_columns = [textwrap.fill(col, width=15) for col in df.columns]
        
        table = ax.table(cellText=df.values, colLabels=wrapped_columns, cellLoc='center', loc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.2, 1.2)
        
        # Adjust row heights
        cell_dict = table.get_celld()
        for i in range(len(df.columns)):
            cell_dict[(0, i)].set_height(0.1)  # Set header row height
        for i in range(1, len(df) + 1):
            for j in range(len(df.columns)):
                cell_dict[(i, j)].set_height(0.03)  # Set data row height
        
        plt.title(title)
        plt.show()