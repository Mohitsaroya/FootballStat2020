########################
# Unfinished code (dont run)
# Statistical Analysis of Top European Football Leagues From year 2020-2021 version 2
########################
import matplotlib.pyplot as plt
from Prompts import Prompts
from Plot import Plots

class FootballAnalysis():
    def __init__(self):
        self.plot_data = Plots(base_folder)
        self.leagues = {1: "Premier League", 2: "Serie A", 3: "La Liga", 4: "Ligue 1", 5: "Bundesliga"}
           
    def choice_and_plot(self):
        choice = Prompts.choices_for_plot(self)
        if choice == 1:
            self.plot_data.table_league(choice)
        elif choice == 2:
            self.plot_data.bar_graph_league(choice)
        elif choice == 3:  
            self.plot_data.bar_graph_league(choice)
    
    def import_csv(self, filename):
        df = self.plot_data.dataframes.get(filename)
        if df is None or df.empty: 
            print("League statistics data is missing or empty!")
            return

     
    def display_general_details(self, choice):
        self.import_csv('league_stats')
        
        try:
            if choice == 1:
                self.choice_and_plot()
            elif choice == 2:
                self.choice_and_plot()     
            elif choice == 3:
                self.choice_and_plot()
            elif choice == 4:
                return
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except KeyError:
            print("Invalid input. Please enter a valid choice.")
            
    
    def display_league_specific(self):
        for i in self.leagues:
            print(f"{i}. {self.leagues[i]}")        


    def run(self):
        menu = Prompts()
        while True:
            choice = menu.main_menu()
            
            if choice == 0:
                menu.display_glossary()
            elif choice == 1:
                self.display_general_details(menu.display_general_prompt())
            elif choice == 2:
                menu.display_league_specific()
            elif choice == 3:
                print("Exiting program. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")



if __name__ == "__main__":
    base_folder = "D:\Macewan\semester 5\CMPT 200\GitHub\FootballStat2020\csv files"
    analysis = FootballAnalysis()
    analysis.run()
