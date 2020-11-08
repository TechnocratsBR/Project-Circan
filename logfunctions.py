def openxlsx():
    import pandas as pd
    from openpyxl import load_workbook

    writer = pd.ExcelWriter('circanlog.xlsx', engine='xlsxwriter')
    writer.save()

    # dataframe columns
    df = pd.DataFrame({'Days': [],
                    'Sleep': [],
                    'Wake': [],
                    'Naps': [],
                    'Steps': [],
                    'Mood': [],                  
                    })
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('circanlog.xlsx', engine='xlsxwriter')

    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name='Sheet1', index=False)

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()