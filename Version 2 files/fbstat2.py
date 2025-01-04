########################
# Unfinished code (dont run)
# Statistical Analysis of Top European Football Leagues From year 2020-2021 version 2
########################
import matplotlib.pyplot as plt
import pandas as pd
from Prompts import Prompts
from Plot import Plots

class FootballAnalysis:
    def __init__(self):
        self.plot_data = Plots()
    
    def choice_and_plot(self):
        choice = Prompts.choices_for_plot()
        Plots().table_league(choice) 

     
    def display_general_details(self, choice):
        df = self.plot_data.dataframes.get('league_stats')
        if df is None or df.empty: 
            print("League statistics data is missing or empty!")
            return
        
        try:
            if choice == 1:
                self.plot_data.table_league(1)
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

        

    def run(self):
        menu = Prompts()
        while True:
            choice = menu.main_menu()
            if choice == 3:
                print("Exiting program. Goodbye!")
                break
            elif choice == 0:
                menu.display_glossary()
            elif choice == 1:
                self.display_general_details(menu.display_general_prompt())
            elif choice == 2:
                menu.display_league_specific()
            else:
                print("Invalid choice. Please try again.")



if __name__ == "__main__":
    base_folder = input("Enter the folder path containing the CSV files: ")
    analysis = FootballAnalysis(base_folder)
    analysis.run()
