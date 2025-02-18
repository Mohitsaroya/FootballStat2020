class Prompts():
    def __init__(self):
        pass
        
    def main_menu(self):
        print("---------------------------------------------------------------------------\n"
            "Home Menu\n"
            "1. General Details About Football Leagues\n"
            "2. League-Specific Details\n"
            "3. Exit\n"
            "---------------------------------------------------------------------------\n"
            "0. Glossary\n"
            "---------------------------------------------------------------------------")
        return int(input("Enter the number: "))

    
    def display_glossary(self):
        print('ok\n'
            '============================================================\n'
            'GF: Goals For (goals scores for the team)\n'
            'GA: Goals Against (goals scored against the team)\n'
            'GD: Goal Difference (difference between the goals scored by and against the team)\n'
            'PPG: Points Per Game\n'
            'CS: Clean Sheet (matches with no goals conceded)\n'
            'FTS: Failed To Score (no goals for the team)\n'
            '============================================================\n')
    
    def choices_for_plot(self):
        print("1. Table\n"
              "2. Line Chart\n"
              "3. Bar Chart\n")
        return int(input("Enter your choice: "))
    
    def display_general_prompt(self):
        print("1. League Names and Goals per Match\n"
            "2. Total goals, Home goals per match, away goals per match\n"
            "3. Home wins vs away wins\n"
            "4. Back\n")
        return int(input("Enter your choice: "))
    
    
    def display_league_compare(self):
        print("1. Premier League\n"
            "2. Serie A\n"
            "3. La Liga\n"
            "4. Ligue 1\n"
            "5. Bundesliga\n")
        number = []
        for i in range(1,2):
            number.append(int(input(f"Enter the display number for any two leagues you want to compare ({i} more): \n")))     
        return number
    
    def display_league_prompt(self):
        print("1. Display league table\n"
            "2. Display league statistics\n"
            "3. Display league fixtures\n"
            "4. Back\n")
        return int(input("Enter your choice: "))
    
    
    
    