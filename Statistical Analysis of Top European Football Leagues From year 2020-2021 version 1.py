import matplotlib.pyplot as plt
import pandas as pd

df =pd.read_csv(r'C:\Users\user\AppData\Local\Programs\Python\Python38\proj\stats\leaguestatistics.csv')
df1 =pd.read_csv(r'C:\Users\user\AppData\Local\Programs\Python\Python38\proj\stats\premierleaguestat.csv')
df2 = pd.read_csv(r'C:\Users\user\AppData\Local\Programs\Python\Python38\proj\stats\seriastat.csv')
df3 = pd.read_csv(r'C:\Users\user\AppData\Local\Programs\Python\Python38\proj\stats\laligastat.csv')
df4 = pd.read_csv(r'C:\Users\user\AppData\Local\Programs\Python\Python38\proj\stats\ligue1stat.csv')
df5 = pd.read_csv(r'C:\Users\user\AppData\Local\Programs\Python\Python38\proj\stats\bundesligastat.csv')
df6 = pd.read_csv(r'C:\Users\user\AppData\Local\Programs\Python\Python38\proj\stats\topplayerstat.csv')
df7 = pd.read_csv(r'C:\Users\user\AppData\Local\Programs\Python\Python38\proj\stats\topclubpayment.csv')
df8 = pd.read_csv(r'C:\Users\user\AppData\Local\Programs\Python\Python38\proj\stats\Comparisonfile.csv')
df9 = pd.read_csv(r'C:\Users\user\AppData\Local\Programs\Python\Python38\proj\stats\Comparisonfile1.csv')


while True:

##########################################################################################

    print("---------------------------------------------------------------------------\n"
        "Home Menu\n"
      "1. Display general details about the prominant Europian football Leagues and terminology\n"
      "2. Display the details for the different leagues\n"
      "3. Display the stats for the clubs in each league\n"
      "4. Statistical analysis of top 56 football players in history of football\n"
      "5. Market Value and Revenue(in million US dollars) of top 10 football clubs\n"
      "6. Comparing Clubs\n"
      "7. Exit\n"
      "---------------------------------------------------------------------------\n"
      "NOTE: the given data is from the year 2020-2021\n"
      "---------------------------------------------------------------------------")
    n = int(input("Enter the number: "))

    
##########################################################################################

    if n == 7:
        break
    if n == 1:
        print('============================================================\n'
              'For glossary, press zero(0)\n'
              "1. League Names\n"
              "2. League Country Names\n"
              "3. League with average goal scored per match\n"
              "4. Back\n"
              '============================================================')
        n1 = int(input("Enter the number here: "))
        if n1 == 1:
            print(df["Football League"])
        elif n1 == 2:
            print(df[["Football League","Country"]])
        elif n1 == 3:
            print('1. Tabular form\n'
                  '2. Line graph\n'
                  '3. Bar chart form\n')
            n11 = int(input("In what manner shall the data be presented?: "))
            if n11 == 1:
                print(df[["Football League", "Goals per match"]])
            elif n11 == 2:
                plt.plot(df["Football League"], df["Goals per match"])
                plt.legend(["Goals per match"])
                plt.ylabel('goals per match')
                plt.xlabel('League')
                plt.title('Football leagues and goals per match')
                plt.show()
            elif n11 == 3:
                df.plot(x = "Football League", y = "Goals per match", kind = 'bar')
                plt.title('Football leagues and goals per match')
                plt.show()
        elif n1 == 0:
            print('ok\n'
              '============================================================\n'
              'GF: Goals For (goals scores for the team)\n'
              'GA: Goals Against (goals scored against the team)\n'
              'GD: Goal Difference (difference between the goals scored by and against the team)\n'
              'PPG: Points Per Game\n'
              'CS: Clean Sheet (matches with no goals conceded)\n'
              'FTS: Failed To Score (no goals for the team)\n'
              '============================================================\n')
        else:
            print('ok')


##########################################################################################

    elif n == 2:
        
        print('============================================================\n'
             'ok..\n'
             '1. League name with country names\n'
             '2. Home win/draw/away win percentage in each league\n'
             '3. Goal tally, Goals per match, times goals scored over 1.5, over 2.5, and over 3.5\n'
             '4. Home goal, away goal and percentage of both teams scoring a goal\n'
             '5. Back')
        
        n2 = int(input('Enter the number: '))
        for i in range(1):

            if 1<n2<5:
                print('What format would you prefer?\n'
                                '1. Tabular form\n'
                                '2. Line Chart form\n'
                                '3. Bar chart form\n'
                                '4. Back\n')

            if n2 == 1:
                print(df[["Football League","Country"]])
                
            elif n2 == 2:
                
                n21 = int(input('Enter the number: '))
                if n21 == 1:
                    print(df[["Football League",'Home Wins ptg', 'Draws ptg','Away Wins ptg']])
                elif n21 == 2:
                    plt.plot(df['Football League'], df[['Home Wins ptg','Draws ptg','Away Wins ptg']])
                    plt.legend(['Home Wins ptg','Draws ptg','Away Wins ptg'])
                    plt.ylabel('Goal details')
                    plt.xlabel('League')
                    plt.xticks(rotation = 15)
                    plt.title('Home win/draw/away win percentage in each league')
                    plt.show()
                elif n21 == 3:
                    df.plot(x = "Football League", y = ['Home Wins ptg', 'Draws ptg','Away Wins ptg'],kind = 'bar', color = ['r','c','b'],
                                    title = "Win/draw/lose percentage chart", edgecolor = 'black', rot = 12)
                    plt.show()
                else:
                    print('ok')

            elif n2 == 3:

                n22 = int(input('Enter the number: '))
                if n22 == 1:
                    print(df[['Football League','Goals', 'Goals per match','Over 1.5 goal ptg','Over 2.5 goals ptg', 'Over     3.5 goals ptg']])
                
                elif n22 == 2:
                    plt.plot(df['Football League'], df[['Over 1.5 goal ptg','Over 2.5 goals ptg', 'Over 3.5 goals ptg']])
                    plt.legend(['Over 1.5 goal ptg','Over 2.5 goals ptg', 'Over 3.5 goals ptg'])
                    plt.ylabel('Goal details')
                    plt.xlabel('League')
                    plt.xticks(rotation = 15)
                    plt.title('Goals per match, times goals scored over 1.5, over 2.5, and over 3.5')
                    plt.show()
                elif n22 == 3:
                    df.plot(x = "Football League", y = ['Goals per match', 'Over 1.5 goal ptg','Over 2.5 goals ptg', 'Over 3.5 goals ptg'],kind = 'bar',
                            color = ['r','c','b'], title = "times goals scored over 1.5, over 2.5, and over 3.5", edgecolor = 'black', rot = 12)
                    plt.show()
                else:
                    print('ok')
            
            elif n2 == 4:
                n23 = int(input('Enter the number: '))
                if n23 == 1:
                    print(df[['Football League','Home goals per match', 'Away goals per match', 'Both teams scored ptg']])
                elif n23 == 2:
                    plt.plot(df['Football League'], df[['Home goals per match', 'Away goals per match']])
                    plt.legend(['Home goals per match', 'Away goals per match'])
                    plt.ylabel('Goal details')
                    plt.xlabel('League')
                    plt.title('Home goal, away goal of both teams scoring a goal')
                    plt.xticks(rotation = 15)
                    plt.show()
                    
                elif n23 == 3:
                    df1.plot(x = ["Football League"], y = ['Home goals per match', 'Away goals per match'],kind = 'bar',                                                         color = ['r','c','b'], title = "Home goal, away goal of both teams scoring a goal", edgecolor = 'black', rot = 12)
                    plt.show()


##########################################################################################



    elif n == 3:
        print('============================================================\n'
              "What league stats do you want to see\n"
              "1. Premier League\n"
              "2. Serie A\n"
              "3. La Liga\n"
              "4. Ligue 1\n"
              "5. Bundesliga\n"
              "6. Back\n"
              '============================================================\n')
        n3 = int(input("Enter the number here: "))

        for i in range(1):
            if 1<=n3<6:
                print("ok")
            if n3 == 1:
                print(df1['Club Name'])
                print("1. Club Points, points per game and standings\n"
                  "2. Win/draw/lose chart with points per match\n"
                  "3. Goals for/goals against and goal difference\n"
                  "4. other details\n"
                  '============================================================\n')
                n31 = int(input('Enter number: '))
                if n31 == 1:
                    print(df1[['Club Name', 'Points', 'PPG', 'Standing']])
                elif n31 == 2:
                    print('What format would you prefer?\n'
                              '1. Tabular form\n'
                              '2. Line Chart form\n'
                              '3. Bar chart form\n'
                              '4. Back\n')
                    n311 = int(input('Enter number: '))
                    if n311 == 1:
                        print(df1[['Club Name', 'Win', 'Draw', 'Lose']])
                    elif n311 == 2:
                        plt.plot(df1["Club Name"], df1[['Win', 'Draw', 'Lose']])
                        plt.legend(['Win', 'Draw', 'Lose'])
                        plt.title('Win/draw/lose chart with points per match')
                        plt.xlabel('Club')
                        plt.ylabel('Win/draw/lose')
                        plt.xticks(rotation = 15)
                        plt.show()
                        
                    elif n311 == 3:
                         df1.plot(x = "Club Name", y = ['Win', 'Draw', 'Lose'],kind = 'bar', color = ['r','c','b'],
                                  title = "Win/draw/lose chart with points per match", edgecolor = 'black', rot = 12)
                         plt.show()
                    else:
                        print('ok')
                elif n31 == 3:
                    print('What format would you prefer?\n'
                              '1. Tabular form\n'
                              '2. Line Chart form\n'
                              '3. Bar chart form\n'
                              '4. Back\n')
                    n312 = int(input('Enter Number: '))
                    if n312 == 1:
                        print(df1[['Club Name', 'GF', 'GA', 'GD']])
                    elif n312 == 2:
                        plt.plot(df1["Club Name"], df1[['GF', 'GA', 'GD']])
                        plt.legend(['GF', 'GA', 'GD'])
                        plt.title('Goals for/goals against and goal difference')
                        plt.xlabel('Club')
                        plt.ylabel('Goals for/goals against and goal difference details')
                        plt.xticks(rotation = 15)
                        plt.show()
                        
                    elif n312 == 3:
                         df1.plot(x = "Club Name", y = ['GF', 'GA', 'GD'],kind = 'bar', color = ['r','c','b'],
                                  title = "Goals for/goals against and goal difference", edgecolor = 'black', rot = 12)
                         plt.show()
                    else:
                        print('ok')
                    

            elif n3 == 2:
                print(df2['Club Name'])
                print("1. Club Points, points per game and standings\n"
                  "2. Win/draw/lose chart with points per match\n"
                  "3. Goals for/goals against and goal difference\n"
                  "4. back\n"
                  '============================================================\n')
                n32 = int(input('Enter number: '))
                if n32 == 1:
                    print(df2[['Club Name', 'Points', 'PPG', 'Standing']])
                elif n32 == 2:
                    print('What format would you prefer?\n'
                              '1. Tabular form\n'
                              '2. Line Chart form\n'
                              '3. Bar chart form\n'
                              '4. Back\n')
                    n321 = int(input('Enter number: '))
                    if n321 == 1:
                        print(df2[['Club Name', 'Win', 'Draw', 'Lose']])
                    elif n321 == 2:
                        plt.plot(df2["Club Name"], df2[['Win', 'Draw', 'Lose']])
                        plt.legend(['Win', 'Draw', 'Lose'])
                        plt.title('Win/draw/lose chart with points per match')
                        plt.xlabel('Club')
                        plt.ylabel('Win/draw/lose')
                        plt.xticks(rotation = 15)
                        plt.show()
                        
                    elif n321 == 3:
                         df2.plot(x = "Club Name", y = ['Win', 'Draw', 'Lose'],kind = 'bar', color = ['r','c','b'],
                                  title = "Win/draw/lose chart with points per match", edgecolor = 'black', rot = 12)
                         plt.show()
                    else:
                        print('ok')
                elif n32 == 3:
                    print('What format would you prefer?\n'
                              '1. Tabular form\n'
                              '2. Line Chart form\n'
                              '3. Bar chart form\n'
                              '4. Back\n')
                    n322 = int(input('Enter Number: '))
                    if n322 == 1:
                        print(df2[['Club Name', 'GF', 'GA', 'GD']])
                    elif n322 == 2:
                        plt.plot(df2["Club Name"], df2[['GF', 'GA', 'GD']])
                        plt.legend(['GF', 'GA', 'GD'])
                        plt.title('Goals for/goals against and goal difference')
                        plt.xlabel('Club')
                        plt.ylabel('Goals for/goals against and goal difference details')
                        plt.xticks(rotation = 15)
                        plt.show()
                        
                    elif n322 == 3:
                         df2.plot(x = "Club Name", y = ['GF', 'GA', 'GD'],kind = 'bar', color = ['r','c','b'],
                                  title = "Goals for/goals against and goal difference", edgecolor = 'black', rot = 12)
                         plt.show()
                    else:
                        print('ok')
            elif n3 == 3:
                print(df3['Club Name'])
                print("1. Club Points, points per game and standings\n"
                  "2. Win/draw/lose chart with points per match\n"
                  "3. Goals for/goals against and goal difference\n"
                  "4. back\n"
                  '============================================================\n')
                n33 = int(input('Enter number: '))
                if n33 == 1:
                    print(df3[['Club Name', 'Points', 'PPG', 'Standing']])
                elif n33 == 2:
                    print('What format would you prefer?\n'
                              '1. Tabular form\n'
                              '2. Line Chart form\n'
                              '3. Bar chart form\n'
                              '4. Back\n')
                    n331 = int(input('Enter number: '))
                    if n331 == 1:
                        print(df3[['Club Name', 'Win', 'Draw', 'Lose']])
                        
                    elif n331 == 2:
                        plt.plot(df3["Club Name"], df3[['Win', 'Draw', 'Lose']])
                        plt.legend(['Win', 'Draw', 'Lose'])
                        plt.title('Win/draw/lose chart with points per match')
                        plt.xticks(rotation = 15)
                        plt.xlabel('Club')
                        plt.ylabel('Win/draw/lose')
                        plt.show()
                        
                    elif n331 == 3:
                         df3.plot(x = "Club Name", y = ['Win', 'Draw', 'Lose'],kind = 'bar', color = ['r','c','b'],
                                  title = "Win/draw/lose chart with points per match", edgecolor = 'black', rot = 12)
                         plt.show()
                    else:
                        print('ok')
                elif n33 == 3:
                    print('What format would you prefer?\n'
                              '1. Tabular form\n'
                              '2. Line Chart form\n'
                              '3. Bar chart form\n'
                              '4. Back\n')
                    n332 = int(input('Enter Number: '))
                    if n332 == 1:
                        print(df3[['Club Name', 'GF', 'GA', 'GD']])
                        
                    elif n332 == 2:
                        plt.plot(df3["Club Name"], df3[['GF', 'GA', 'GD']])
                        plt.legend(['GF', 'GA', 'GD'])
                        plt.title('Goals for/goals against and goal difference')
                        plt.xlabel('Club')
                        plt.ylabel('Goals for/goals against and goal difference details')
                        plt.xticks(rotation = 15)
                        plt.show()
                        
                    elif n332 == 3:
                         df3.plot(x = "Club Name", y = ['GF', 'GA', 'GD'],kind = 'bar', color = ['r','c','b'],
                                  title = "Goals for/goals against and goal difference", edgecolor = 'black', rot = 12)
                         plt.show()
                    else:
                        print('ok')


                
            elif n3 == 4:
                print(df4['Club Name'])
                print("1. Club Points, points per game and standings\n"
                  "2. Win/draw/lose chart with points per match\n"
                  "3. Goals for/goals against and goal difference\n"
                  "4. other details\n"
                  '============================================================\n')
                n34 = int(input('Enter number: '))
                if n34 == 1:
                    print(df4[['Club Name', 'Points', 'PPG', 'Standing']])
                elif n34 == 2:
                    print('What format would you prefer?\n'
                              '1. Tabular form\n'
                              '2. Line Chart form\n'
                              '3. Bar chart form\n'
                              '4. Back\n')
                    n341 = int(input('Enter number: '))
                    if n341 == 1:
                        print(df4[['Club Name', 'Win', 'Draw', 'Lose']])
                    elif n341 == 2:
                        plt.plot(df4["Club Name"], df4[['Win', 'Draw', 'Lose']])
                        plt.legend(['Win', 'Draw', 'Lose'])
                        plt.title('Win/draw/lose chart with points per match')
                        plt.xlabel('Club')
                        plt.ylabel('Win/draw/lose')
                        plt.xticks(rotation = 15)
                        plt.show()
                        
                    elif n341 == 3:
                         df4.plot(x = "Club Name", y = ['Win', 'Draw', 'Lose'],kind = 'bar', color = ['r','c','b'],
                                  title = "Win/draw/lose chart with points per match", edgecolor = 'black', rot = 12)
                         plt.show()
                    else:
                        print('ok')
                elif n34 == 3:
                    print('What format would you prefer?\n'
                              '1. Tabular form\n'
                              '2. Line Chart form\n'
                              '3. Bar chart form\n'
                              '4. Back\n')
                    n342 = int(input('Enter Number: '))
                    if n342 == 1:
                        print(df4[['Club Name', 'GF', 'GA', 'GD']])
                    elif n342 == 2:
                        plt.plot(df4["Club Name"], df4[['GF', 'GA', 'GD']])
                        plt.legend(['GF', 'GA', 'GD'])
                        plt.title('Goals for/goals against and goal difference')
                        plt.xlabel('Club')
                        plt.ylabel('Goals for/goals against and goal difference details')
                        plt.xticks(rotation = 15)
                        plt.show()
                        
                    elif n342 == 3:
                         df4.plot(x = "Club Name", y = ['GF', 'GA', 'GD'],kind = 'bar', color = ['r','c','b'],
                                  title = "Goals for/goals against and goal difference", edgecolor = 'black', rot = 12)
                         plt.show()
                    else:
                        print('ok')
                        
            elif n3 == 5:
                print(df5['Club Name'])
                print("1. Club Points, points per game and standings\n"
                  "2. Win/draw/lose chart with points per match\n"
                  "3. Goals for/goals against and goal difference\n"
                  "4. back\n"
                  '============================================================\n')
                n31 = int(input('Enter number: '))
                if n31 == 1:
                    print(df5[['Club Name', 'Points', 'PPG', 'Standing']])
                elif n31 == 2:
                    print('What format would you prefer?\n'
                              '1. Tabular form\n'
                              '2. Line Chart form\n'
                              '3. Bar chart form\n'
                              '4. Back\n')
                    n311 = int(input('Enter number: '))
                    if n311 == 1:
                        print(df5[['Club Name', 'Win', 'Draw', 'Lose']])
                        
                    elif n311 == 2:
                        plt.plot(df5["Club Name"], df5[['Win', 'Draw', 'Lose']])
                        plt.legend(['Win', 'Draw', 'Lose'])
                        plt.title('Win/draw/lose chart with points per match')
                        plt.xlabel('Club')
                        plt.ylabel('Win/draw/lose')
                        plt.xticks(rotation = 15)
                        plt.show()
                        
                    elif n311 == 3:
                         df5.plot(x = "Club Name", y = ['Win', 'Draw', 'Lose'],kind = 'bar', color = ['r','c','b'],
                                  title = "Win/draw/lose chart with points per match", edgecolor = 'black', rot = 12)
                         plt.show()
                    else:
                        print('ok')
                elif n31 == 3:
                    print('What format would you prefer?\n'
                              '1. Tabular form\n'
                              '2. Line Chart form\n'
                              '3. Bar chart form\n'
                              '4. Back\n')
                    n342 = int(input('Enter Number: '))
                    if n342 == 1:
                        print(df5[['Club Name', 'GF', 'GA', 'GD']])
                    elif n342 == 2:
                        plt.plot(df5["Club Name"], df5[['GF', 'GA', 'GD']])
                        plt.legend(['GF', 'GA', 'GD'])
                        plt.title('Goals for/goals against and goal difference')
                        plt.xlabel('Club')
                        plt.ylabel('Goals for/goals against and goal difference details')
                        plt.xticks(rotation = 15)
                        plt.show()
                        
                    elif n342 == 3:
                         df5.plot(x = "Club Name", y = ['GF', 'GA', 'GD'],kind = 'bar', color = ['r','c','b'],
                                  title = "Goals for/goals against and goal difference", edgecolor = 'black', rot = 12)
                         plt.show()
                    else:
                        print('ok')

##########################################################################################

    elif n == 4:
        print(df6[['Player', 'Goals', 'Matches', 'Ratio', 'Years', 'Rank']])

    elif n == 5:
        print('What format would you prefer?\n'
                '1. Tabular form\n'
                '2. Line Chart form\n'                          
                '3. Bar chart form\n'
                '4. Back\n')
        n51 = int(input('Enter the Number: '))
        if n51 == 1:
            print('M.D = Million Dollars')
            print(df7[['Footbal Club','MarketValue(M.D.)','Revenue(M.D.)']])
                  
        elif n51 == 2:
            plt.plot(df7["Footbal Club"], df7[['MarketValue(M.D.)', 'Revenue(M.D.)']])
            plt.legend(['MarketValue(M.D.)', 'Revenue(M.D.)'])
            plt.title('Market Value and Revenue(in million US dollars) of top 10 football clubs')
            plt.xlabel('Club')
            plt.ylabel('Market Value and Revenue(in million US dollars)')
            plt.xticks(rotation = 15)
            plt.show()
            
        elif n51 == 3:
            df7.plot(x = "Footbal Club", y = ['MarketValue(M.D.)', 'Revenue(M.D.)'],kind = 'bar', color = ['r','c','b'],
                    title = "Market Value and Revenue(in million US dollars", edgecolor = 'black', rot = 12)
            plt.show()   
        
        else:
            print('ok')
##########################################################################################

    elif n == 6:

        print('Pick one of the below options:\n'
              '1. Comparison of the chart topping clubs from each league\n'
              '2. Comparison of the losing clubs from each club\n')

        n61 = int(input('Enter the number here: '))

            
        if n61 == 1:
            print(df8['Club Name'])
            print("1. Club Points, points per game\n"
              "2. Win/draw/lose chart with points per match\n"
              "3. Goals for/goals against and goal difference\n"
              "4. other details\n"
              '============================================================\n')
            n611 = int(input('Enter number: '))
            if n611 == 1:
                print(df8[['Club Name', 'Points', 'PPG']])
            elif n611 == 2:
                print('What format would you prefer?\n'
                          '1. Tabular form\n'
                          '2. Line Chart form\n'
                          '3. Bar chart form\n'
                          '4. Back\n')
                n6111 = int(input('Enter number: '))
                if n6111 == 1:
                    print(df8[['Club Name', 'Win', 'Draw', 'Lose']])
                elif n6111 == 2:
                    plt.plot(df8["Club Name"], df8[['Win', 'Draw', 'Lose']])
                    plt.legend(['Win', 'Draw', 'Lose'])
                    plt.title('Win/draw/lose chart with points per match')
                    plt.xlabel('Club')
                    plt.ylabel('Win/draw/lose')
                    plt.xticks(rotation = 15)
                    plt.show()
                    
                elif n6111 == 3:
                     df8.plot(x = "Club Name", y = ['Win', 'Draw', 'Lose'],kind = 'bar', color = ['r','c','b'],
                              title = "Win/draw/lose chart with points per match", edgecolor = 'black', rot = 12)
                     plt.show()
                else:
                    print('ok')
            elif n611 == 3:
                print('What format would you prefer?\n'
                          '1. Tabular form\n'
                          '2. Line Chart form\n'
                          '3. Bar chart form\n'
                          '4. Back\n')
                n612 = int(input('Enter Number: '))
                if n612 == 1:
                    print(df8[['Club Name', 'GF', 'GA', 'GD']])
                elif n612 == 2:
                    plt.plot(df8["Club Name"], df8[['GF', 'GA', 'GD']])
                    plt.legend(['GF', 'GA', 'GD'])
                    plt.title('Goals for/goals against and goal difference')
                    plt.xlabel('Club')
                    plt.ylabel('Goals for/goals against and goal difference details')
                    plt.xticks(rotation = 15)
                    plt.show()
                    
                elif n612 == 3:
                     df8.plot(x = "Club Name", y = ['GF', 'GA', 'GD'],kind = 'bar', color = ['r','c','b'],
                              title = "Goals for/goals against and goal difference", edgecolor = 'black', rot = 12)
                     plt.show()
                else:
                    print('ok')
            

        elif n61 == 2:
            print(df9['Club Name'])
            print("1. Club Points, points per game\n"
              "2. Win/draw/lose chart with points per match\n"
              "3. Goals for/goals against and goal difference\n"
              "4. other details\n"
              '============================================================\n')
            n612 = int(input('Enter number: '))
            if n612 == 1:
                print(df9[['Club Name', 'Points', 'PPG']])
            elif n612 == 2:
                print('What format would you prefer?\n'
                          '1. Tabular form\n'
                          '2. Line Chart form\n'
                          '3. Bar chart form\n'
                          '4. Back\n')
                n6112 = int(input('Enter number: '))
                if n6112 == 1:
                    print(df8[['Club Name', 'Win', 'Draw', 'Lose']])
                elif n6112 == 2:
                    plt.plot(df9["Club Name"], df9[['Win', 'Draw', 'Lose']])
                    plt.legend(['Win', 'Draw', 'Lose'])
                    plt.title('Win/draw/lose chart with points per match')
                    plt.xlabel('Club')
                    plt.ylabel('Win/draw/lose')
                    plt.xticks(rotation = 15)
                    plt.show()
                    
                elif n6112 == 3:
                     df9.plot(x = "Club Name", y = ['Win', 'Draw', 'Lose'],kind = 'bar', color = ['r','c','b'],
                              title = "Win/draw/lose chart with points per match", edgecolor = 'black', rot = 12)
                     plt.show()
                else:
                    print('ok')
            elif n612 == 3:
                print('What format would you prefer?\n'
                          '1. Tabular form\n'
                          '2. Line Chart form\n'
                          '3. Bar chart form\n'
                          '4. Back\n')
                n6122 = int(input('Enter Number: '))
                if n6122 == 1:
                    print(df8[['Club Name', 'GF', 'GA', 'GD']])
                elif n6122 == 2:
                    plt.plot(df9["Club Name"], df9[['GF', 'GA', 'GD']])
                    plt.legend(['GF', 'GA', 'GD'])
                    plt.title('Goals for/goals against and goal difference')
                    plt.xlabel('Club')
                    plt.ylabel('Goals for/goals against and goal difference details')
                    plt.xticks(rotation = 15)
                    plt.show()
                    
                elif n6122 == 3:
                     df9.plot(x = "Club Name", y = ['GF', 'GA', 'GD'],kind = 'bar', color = ['r','c','b'],
                              title = "Goals for/goals against and goal difference", edgecolor = 'black', rot = 12)
                     plt.show()
                else:
                    print('ok')
            
    elif n > 7:
        print('============================================================\n'
            'error...try again\n'
            '============================================================\n')
        
    else:
        break
