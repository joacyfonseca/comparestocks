import pandas as pd
import pandas_datareader as pdr
import datetime

# Allow the full width of the data frame to show.
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)
loop = 1
while loop == 1:
    # Creating the input
    print('************************************************')
    print('Menu')
    print('************************************************')
    print('1. Compare Stocks')
    print('2. Quit')
    print('Please enter your selection')
    answer = int(input())
    if answer == 1:
        print('************************************************')
        print('Enter the first stock')
        firstStock = input()
        print('************************************************')
        print(firstStock)
        print('************************************************')
        print('Enter the second stock')
        secondStock = input()
        print(secondStock)
        print('************************************************')
        print('Enter the total previous days for the analysis')
        numDays = input()
        print('************************************************')
        print(numDays)
        print('\n')
        print('Please wait a few seconds for this request to complete... \n')

        # Set and show dates.
        dt = datetime.date.today()
        dtPast = dt + datetime.timedelta(days=-int(numDays))
        def getStock(stk):
            # Call Yahoo finance to get stock data for the stock provided.
            df = pdr.get_data_yahoo(stk,
                                    start=datetime.datetime(dtPast.year, dtPast.month, dtPast.day),
                                    end=datetime.datetime(dt.year, dt.month, dt.day))
            # Return a dataframe containing stock data to the calling instruction.
            return df
        print('Statistics from ' + str(dtPast) + ' to ' + str(dt))
        dfFirstStock = getStock(firstStock)
        dfSecondStock = getStock(secondStock)
        numRowsFirst = len(dfFirstStock)
        numRowsSecond = len(dfSecondStock)
        # Building a new Data Frame
        df = pd.DataFrame(columns=['Stock Name',  'Start Price', 'End Price', 'Mean Price', 'St. Deviation', 'Percent Change'])
        # Creating Data Dictionaries
        firstStockDic = ({  'Stock Name': firstStock,
                            'Start Price': dfFirstStock.iloc[0]['Open'],
                            'End Price': dfFirstStock.iloc[numRowsFirst-1]['Close'],
                            'Mean Price': dfFirstStock['Close'].mean(),
                            'St. Deviation': dfFirstStock['Close'].std(),
                            'Percent Change': ((dfFirstStock.iloc[numRowsFirst-1]['Close'] - dfFirstStock.iloc[0]['Open'])/dfFirstStock.iloc[0]['Open'])*100
                            })
        secondStockDic = ({ 'Stock Name': secondStock,
                            'Start Price': dfSecondStock.iloc[0]['Open'],
                            'End Price': dfSecondStock.iloc[numRowsSecond-1]['Close'],
                            'Mean Price': dfSecondStock['Close'].mean(),
                            'St. Deviation': dfSecondStock['Close'].std(),
                            'Percent Change': ((dfSecondStock.iloc[numRowsSecond-1]['Close'] - dfSecondStock.iloc[0]['Open'])/dfSecondStock.iloc[0]['Open'])*100
                            })
        df = df.append(firstStockDic, ignore_index= True)
        df = df.append(secondStockDic, ignore_index=True)
        print(df)
    elif answer == 2:
        print('The application has terminated.')
        loop = 0
    else:
        print('Please select one valid option.')