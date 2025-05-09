class Prompts():
    def __init__(self):
        pass
        
    def main_menu(self):
        print("---------------------------------------------------------------------------\n"
              "Main Menu\n"
              "1. View League-Wide Statistics\n"
              "2. View Team-Specific Statistics\n"
              "3. Compare Leagues or Teams\n"
              "4. Exit\n"
              "---------------------------------------------------------------------------\n"
              "0. Glossary\n")
        return int(input("Enter your choice: "))

    def display_glossary(self):
        print("============================================================\n"
              "GP: Games Played\n"
              "GF: Goals For (goals scored by the team)\n"
              "GA: Goals Against (goals scored against the team)\n"
              "GD: Goal Difference (difference between GF and GA)\n"
              "PPG: Points Per Game\n"
              "CS: Clean Sheets (matches with no goals conceded)\n"
              "FTS: Failed To Score (matches where the team did not score)\n"
              "============================================================")

    def choose_league_stat(self):
        print("\nSelect a League to View Statistics:\n"
              "1. Premier League\n"
              "2. Serie A\n"
              "3. La Liga\n"
              "4. Ligue 1\n"
              "5. Bundesliga\n")
        return int(input("Enter your choice: "))

    def choose_team_stat(self):
        print("\nChoose a League to View Team-Specific Statistics:\n"
              "1. Premier League\n"
              "2. Serie A\n"
              "3. La Liga\n"
              "4. Ligue 1\n"
              "5. Bundesliga\n")
        return int(input("Enter your choice: "))

    def compare_options(self):
        print("\nCompare Options:\n"
              "1. Compare Two Leagues\n"
              "2. Compare Two Teams\n"
              "3. Back")
        return int(input("Enter your choice: "))

    def compare_leagues(self):
        print("\nSelect Two Leagues to Compare:\n"
              "1. Premier League\n"
              "2. Serie A\n"
              "3. La Liga\n"
              "4. Ligue 1\n"
              "5. Bundesliga\n")
        leagues = []
        for i in range(2):
            leagues.append(int(input(f"Enter league {i+1}: ")))
        return leagues

    def compare_teams(self):
        print("\nSelect a League to Compare Two Teams From:\n"
              "1. Premier League\n"
              "2. Serie A\n"
              "3. La Liga\n"
              "4. Ligue 1\n"
              "5. Bundesliga\n")
        league_choice = int(input("Enter your choice: "))

        print("\nEnter Team Names as They Appear in the Dataset.")
        team1 = input("Enter the first team: ")
        team2 = input("Enter the second team: ")
        
        return league_choice, team1, team2

    def choices_for_plot_gen(self):
        print("\n1. Table\n"
              "2. Line Chart\n"
              "3. Bar Chart\n")
        return int(input("Enter your choice: "))
    
    def data_vals_prompt(self, header):
        print(f"\nChoose from the given options what you want you see (max allowed: {len(header)}), type 'end' to finish")
        retlist = []
        retlist_len_count = 0
        while len(retlist) < len(header):
            ind_val = input(f"Enter value {retlist_len_count + 1} for display: ")
            if str(ind_val) == "end":
                return retlist
            
            retlist_len_count += 1
            if int(ind_val) not in retlist and 0 <= int(ind_val) <= 6:
                retlist.append(int(ind_val))
            else:
                print(">> invalid input, please retry")
                retlist_len_count -= 1
                
        return retlist

    def choices_for_plot(self):
        print("\n1. Line Chart\n"
              "2. Bar Chart\n")
        return int(input("Enter your choice: "))
