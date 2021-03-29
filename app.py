# Stock Market Data Analysis Project

# Importing Necessary Libraries
import pandas as pd
import matplotlib.pyplot as plot
import numpy as np
from functions import *


# Initializing the Main Loop
while True:
    print('*******************************')
    print("Stocks")
    print("1. Apple")
    print("2. Google")
    print("3. EXIT")
    print('*******************************')
    
    print()
    stock = input("Stock: ") # User Input for Stock
    print()
    
    if stock == '1':
        print('Apple')
        while True:
            print('*******************************')
            print("Plot Options")
            print("1. Specific Year")
            print("2. All Years")
            print("3. Specific Month")
            print("4. Half Yearly")
            print("5. Quarterly")
            print("6: Exit")
            print('*******************************')
            
            print()
            option = input("Option: ") # User Input for Plot Option
            print()
            
            # Specific Year
            if option == '1':
                print ("Year options: 2019, 2020")
                year = input('Enter the year: ') # User Input for Year Option
                if year == '2019':
                    print("Columns: Low, High, Adj Close, Volume")
                    print('1: Specific Column')
                    print('2: All Columns')
                    cols = input("Enter the type: ") # User Input for Column type
                        
                    # Specific Column for Specific Year
                    if cols == '1':
                        column = input('Enter the Column name: ')
                        Apple_SpecificYear_OneColumn19(colName= column)
        
                    # All Columns for Specific Year
                    if cols == '2':
                        Apple_SpecificYear_AllColumns19()
                    
                if year == '2020':
                    print("Columns: Low, High, Adj Close, Volume")
                    print('1: Specific Column')
                    print('2: All Columns')
                    cols = input("Enter the type: ") # User Input for Column type
                        
                    # Specific Column for Specific Year
                    if cols == '1':
                        column = input('Enter the Column name: ')
                        Apple_SpecificYear_OneColumn20(colName= column)
        
                    # All Columns for Specific Year
                    if cols == '2':
                        Apple_SpecificYear_AllColumns20()
                    
            # All Years
            if option == '2':               
                print("Columns: Low, High, Adj Close, Volume")
                print('1: Specific Column')
                print('2: All Columns')
                cols = input("Enter the type: ")
                    
                if cols == '1':
                    column = input('Enter the Column name: ')
                    Apple_AllYears_OneColumn(colName= column)
                
                if cols == '2':
                    Apple_AllYears_AllColumns()
            
            # Specific Month
            if option == '3':
                print ("Year options: 2019, 2020")
                year = input("Enter the Year: ")
                if year == '2020':
                    print(' Months for which data is available: \n 1: January \n 2: February \n 3: March \n 4: April \n 5: May \n 6: June \n 7: July \n 8: August \n 9: September \n 10: October \n 11: November \n 12: December')
                    month = input('Enter the Month Name: ')
                    
                    print("Columns: Low, High, Adj Close, Volume")
                    print('1: Specific Column')
                    print('2: All Columns')
                    cols = input("Enter the type: ")
                    
                    if cols == '1':
                        column = input('Enter the Column name: ')
                        Apple_SpecificMonth_OneColumn20(monthName=month, colName=column)
                
                    if cols == '2':
                        Apple_SpecificMonth_AllColumns20(monthName=month)
                
                if year == '2019':
                    print(' Months for which data is available: \n 1: January \n 2: February \n 3: March \n 4: April \n 5: May \n 6: June \n 7: July \n 8: August \n 9: September \n 10: October \n 11: November \n 12: December')
                    month = input('Enter the Month Name: ')
                    
                    print("Columns: Low, High, Adj Close, Volume")
                    print('1: Specific Column')
                    print('2: All Columns')
                    cols = input("Enter the type: ")
                    
                    if cols == '1':
                        column = input('Enter the Column name: ')
                        Apple_SpecificMonth_OneColumn19(monthName=month, colName=column)
                
                    if cols == '2':
                        Apple_SpecificMonth_AllColumns19(monthName=month)

            # Half Yearly
            if option == '4':
                print ("Year options: 2019, 2020")
                year = input("Enter the Year: ")
                if year == '2019':
                    print("Columns: Low, High, Adj Close, Volume")
                    print('1: Specific Column')
                    print('2: All Columns')
                    cols = input("Enter the type: ")
                    
                    if cols == '1':
                        print('Jan - May : 1 \n June - Dec : 2')
                        half = input('Enter the Half of the Year: ')
                        if half == '1':
                            column = input('Enter the Column name: ')
                            Apple_HalfYearly_1_OneColumn19(colName=column)
                        if half == '2':
                            column = input('Enter the Column name: ')
                            Apple_HalfYearly_2_OneColumn19(colName=column)                 
                    if cols == '2':
                        print('Jan - May : 1 \n June - Dec : 2')
                        half = input('Enter the Half of the Year: ')
                        if half == '1':
                            Apple_HalfYearly_1_AllColumns19()
                        if half == '2':
                            Apple_HalfYearly_2_AllColumns19() 

                if year == '2020':
                    print("Columns: Low, High, Adj Close, Volume")
                    print('1: Specific Column')
                    print('2: All Columns')
                    cols = input("Enter the type: ")
                    
                    if cols == '1':
                        print('Jan - May : 1 \n June - Dec : 2')
                        half = input('Enter the Half of the Year: ')
                        if half == '1':
                            column = input('Enter the Column name: ')
                            Apple_HalfYearly_1_OneColumn20(colName=column)
                        if half == '2':
                            column = input('Enter the Column name: ')
                            Apple_HalfYearly_2_OneColumn20(colName=column)                 
                    if cols == '2':
                        print('Jan - May : 1 \n June - Dec : 2')
                        half = input('Enter the Half of the Year: ')
                        if half == '1':
                            Apple_HalfYearly_1_AllColumns20()
                        if half == '2':
                            Apple_HalfYearly_2_AllColumns20()

            # Quarterly
            if option == '5':
                print ("Year options: 2019, 2020")
                year = input("Enter the Year: ")
                if year == '2019':
                    print("Columns: Low, High, Adj Close, Volume")
                    print('1: Specific Column')
                    print('2: All Columns')
                    cols = input("Enter the type: ")
                    
                    if cols == '1':
                        print('Jan - Mar : 1 \n Apr - Jun : 2 \n Jul - Sep : 3 \n Oct - Dec : 4')
                        quarter = input('Enter the Quarter of the Year: ')
                        if quarter == '1':
                            column = input('Enter the Column name: ')
                            Apple_Quarterly_1_OneColumn19(colName=column)

                        if quarter == '2':
                            column = input('Enter the Column name: ')
                            Apple_Quarterly_2_OneColumn19(colName=column)                 

                        if quarter == '3':
                            column = input('Enter the Column name: ') 
                            Apple_Quarterly_3_OneColumn19(colName=column)
                        if quarter == '4':
                            column = input('Enter the Column name: ')
                            Apple_Quarterly_4_OneColumn19(colName=column)
                    if cols == '2':
                        print('Jan - Mar : 1 \n Apr - Jun : 2 \n Jul - Sep : 3 \n Oct - Dec : 4')
                        quarter = input('Enter the Quarter of the Year: ')
                        if quarter == '1':
                            Apple_Quarterly_1_AllColumns19()
                        if quarter == '2':
                            Apple_Quarterly_2_AllColumns19() 
                        if quarter == '3':
                            Apple_Quarterly_3_AllColumns19()
                        if quarter == '4':
                            Apple_Quarterly_4_AllColumns19() 

                if year == '2020':
                    print("Columns: Low, High, Adj Close, Volume")
                    print('1: Specific Column')
                    print('2: All Columns')
                    cols = input("Enter the type: ")
                    
                    if cols == '1':
                        print('Jan - Mar : 1 \n Apr - Jun : 2 \n Jul - Sep : 3 \n Oct - Dec : 4')
                        quarter = input('Enter the Quarter of the Year: ')
                        if quarter == '1':
                            column = input('Enter the Column name: ')
                            Apple_Quarterly_1_OneColumn20(colName=column)
                        if quarter == '2':
                            column = input('Enter the Column name: ')
                            Apple_Quarterly_2_OneColumn20(colName=column)
                        if quarter == '3':
                            column = input('Enter the Column name: ')
                            Apple_Quarterly_3_OneColumn20(colName=column)
                        if quarter == '4':
                            column = input('Enter the Column name: ')
                            Apple_Quarterly_4_OneColumn20(colName=column)                  
                    if cols == '2':
                        print('Jan - Mar : 1 \n Apr - Jun : 2 \n Jul - Sep : 3 \n Oct - Dec : 4')
                        quarter = input('Enter the Quarter of the Year: ')
                        if quarter == '1':
                            Apple_Quarterly_1_AllColumns20()
                        if quarter == '2':
                            Apple_Quarterly_2_AllColumns20()
                        if quarter == '1':
                            Apple_Quarterly_1_AllColumns20()
                        if quarter == '2':
                            Apple_Quarterly_2_AllColumns20()
                
            if option == '6':
                break

    if stock == '2':
        print('Google')
        while True:
            print('*******************************')
            print("Plot Options")
            print("1. Specific Year")
            print("2. All Years")
            print("3. Specific Month")
            print("4. Half Yearly")
            print("5. Quarterly")
            print("6: Exit")
            print('*******************************')
            
            print()
            option = input("Option: ") # User Input for Plot Option
            print()

            # Specific Year
            if option == '1':
                print ("Year options: 2019, 2020")
                year = input('Enter the year: ') # User Input for Year Option
                if year == '2019':
                    print("Columns: Low, High, Adj Close, Volume")
                    print('1: Specific Column')
                    print('2: All Columns')
                    cols = input("Enter the type: ") # User Input for Column type
                        
                    # Specific Column for Specific Year
                    if cols == '1':
                        column = input('Enter the Column name: ')
                        Google_SpecificYear_OneColumn19(colName= column)
        
                    # All Columns for Specific Year
                    if cols == '2':
                        Google_SpecificYear_AllColumns19()
                if year == '2020':
                    print("Columns: Low, High, Adj Close, Volume")
                    print('1: Specific Column')
                    print('2: All Columns')
                    cols = input("Enter the type: ") # User Input for Column type
                        
                    # Specific Column for Specific Year
                    if cols == '1':
                        column = input('Enter the Column name: ')
                        Google_SpecificYear_OneColumn20(colName= column)
        
                    # All Columns for Specific Year
                    if cols == '2':
                        Google_SpecificYear_AllColumns20()
                    
            # All Years
            if option == '2':               
                print("Columns: Low, High, Adj Close, Volume")
                print('1: Specific Column')
                print('2: All Columns')
                cols = input("Enter the type: ")
                    
                if cols == '1':
                    column = input('Enter the Column name: ')
                    Google_AllYears_OneColumn(colName= column)
                
                if cols == '2':
                    Google_AllYears_AllColumns()
            
            # Specific Month
            if option == '3':
                print ("Year options: 2019, 2020")
                year = input("Enter the Year: ")
                if year == '2020':
                    print(' Months for which data is available: \n 1: January \n 2: February \n 3: March \n 4: April \n 5: May \n 6: June \n 7: July \n 8: August \n 9: September \n 10: October \n 11: November \n 12: December')
                    month = input('Enter the Month Name: ')
                    
                    print("Columns: Low, High, Adj Close, Volume")
                    print('1: Specific Column')
                    print('2: All Columns')
                    cols = input("Enter the type: ")
                    
                    if cols == '1':
                        column = input('Enter the Column name: ')
                        Google_SpecificMonth_OneColumn20(monthName=month, colName=column)
                
                    if cols == '2':
                        Google_SpecificMonth_AllColumns20(monthName=month)
                
                if year == '2019':
                    print(' Months for which data is available: \n 1: January \n 2: February \n 3: March \n 4: April \n 5: May \n 6: June \n 7: July \n 8: August \n 9: September \n 10: October \n 11: November \n 12: December')
                    month = input('Enter the Month Name: ')
                    
                    print("Columns: Low, High, Adj Close, Volume")
                    print('1: Specific Column')
                    print('2: All Columns')
                    cols = input("Enter the type: ")
                    
                    if cols == '1':
                        column = input('Enter the Column name: ')
                        Google_SpecificMonth_OneColumn19(monthName=month, colName=column)
                
                    if cols == '2':
                        Google_SpecificMonth_AllColumns19(monthName=month)

            # Half Yearly
            if option == '4':
                print ("Year options: 2019, 2020")
                year = input("Enter the Year: ")
                if year == '2019':
                    print("Columns: Low, High, Adj Close, Volume")
                    print('1: Specific Column')
                    print('2: All Columns')
                    cols = input("Enter the type: ")
                    
                    if cols == '1':
                        print('Jan - May : 1 \n June - Dec : 2')
                        half = input('Enter the Half of the Year: ')
                        if half == '1':
                            column = input('Enter the Column name: ')
                            Google_HalfYearly_1_OneColumn19(colName=column)
                        if half == '2':
                            column = input('Enter the Column name: ')
                            Google_HalfYearly_2_OneColumn19(colName=column)                 
                    if cols == '2':
                        print('Jan - May : 1 \n June - Dec : 2')
                        half = input('Enter the Half of the Year: ')
                        if half == '1':
                            Google_HalfYearly_1_AllColumns19()
                        if half == '2':
                            Google_HalfYearly_2_AllColumns19() 

                if year == '2020':
                    print("Columns: Low, High, Adj Close, Volume")
                    print('1: Specific Column')
                    print('2: All Columns')
                    cols = input("Enter the type: ")
                    
                    if cols == '1':
                        print('Jan - May : 1 \n June - Dec : 2')
                        half = input('Enter the Half of the Year: ')
                        if half == '1':
                            column = input('Enter the Column name: ')
                            Google_HalfYearly_1_OneColumn20(colName=column)
                        if half == '2':
                            column = input('Enter the Column name: ')
                            Google_HalfYearly_2_OneColumn20(colName=column)                 
                    if cols == '2':
                        print('Jan - May : 1 \n June - Dec : 2')
                        half = input('Enter the Half of the Year: ')
                        if half == '1':
                            Google_HalfYearly_1_AllColumns20()
                        if half == '2':
                            Google_HalfYearly_2_AllColumns20()

            # Quarterly  
            if option == '5':
                print ("Year options: 2019, 2020")
                year = input("Enter the Year: ")
                if year == '2019':
                    print("Columns: Low, High, Adj Close, Volume")
                    print('1: Specific Column')
                    print('2: All Columns')
                    cols = input("Enter the type: ")
                    
                    if cols == '1':
                        print('Jan - Mar : 1 \n Apr - Jun : 2 \n Jul - Sep : 3 \n Oct - Dec : 4')
                        quarter = input('Enter the Quarter of the Year: ')
                        if quarter == '1':
                            column = input('Enter the Column name: ')
                            Google_Quarterly_1_OneColumn19(colName=column)

                        if quarter == '2':
                            column = input('Enter the Column name: ')
                            Google_Quarterly_2_OneColumn19(colName=column)                 

                        if quarter == '3':
                            column = input('Enter the Column name: ') 
                            Google_Quarterly_3_OneColumn19(colName=column)
                        if quarter == '4':
                            column = input('Enter the Column name: ')
                            Google_Quarterly_4_OneColumn19(colName=column)
                    if cols == '2':
                        print('Jan - Mar : 1 \n Apr - Jun : 2 \n Jul - Sep : 3 \n Oct - Dec : 4')
                        quarter = input('Enter the Quarter of the Year: ')
                        if quarter == '1':
                            Google_Quarterly_1_AllColumns19()
                        if quarter == '2':
                            Google_Quarterly_2_AllColumns19() 
                        if quarter == '3':
                            Google_Quarterly_3_AllColumns19()
                        if quarter == '4':
                            Google_Quarterly_4_AllColumns19() 

                if year == '2020':
                    print("Columns: Low, High, Adj Close, Volume")
                    print('1: Specific Column')
                    print('2: All Columns')
                    cols = input("Enter the type: ")
                    
                    if cols == '1':
                        print('Jan - Mar : 1 \n Apr - Jun : 2 \n Jul - Sep : 3 \n Oct - Dec : 4')
                        quarter = input('Enter the Quarter of the Year: ')
                        if quarter == '1':
                            column = input('Enter the Column name: ')
                            Google_Quarterly_1_OneColumn20(colName=column)
                        if quarter == '2':
                            column = input('Enter the Column name: ')
                            Google_Quarterly_2_OneColumn20(colName=column)
                        if quarter == '3':
                            column = input('Enter the Column name: ')
                            Google_Quarterly_3_OneColumn20(colName=column)
                        if quarter == '4':
                            column = input('Enter the Column name: ')
                            Google_Quarterly_4_OneColumn20(colName=column)                  
                    if cols == '2':
                        print('Jan - Mar : 1 \n Apr - Jun : 2 \n Jul - Sep : 3 \n Oct - Dec : 4')
                        quarter = input('Enter the Quarter of the Year: ')
                        if quarter == '1':
                            Google_Quarterly_1_AllColumns20()
                        if quarter == '2':
                            Google_Quarterly_2_AllColumns20()
                        if quarter == '1':
                            Google_Quarterly_1_AllColumns20()
                        if quarter == '2':
                            Google_Quarterly_2_AllColumns20()
                
            if option == '6':
                break
    
    if stock == '3':
        print('Bye')
        break