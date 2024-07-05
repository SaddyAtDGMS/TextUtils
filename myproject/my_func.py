import pandas as pd
from dbfread import DBF

def get_minecode_result(minecode):
    dbf = DBF("c:/acc/Master/Minemast.dbf")
    # create master dataframe using the dbf file
    df_mine = pd.DataFrame(iter(dbf))

    print(f"get_minecode_result called with minecode: {minecode}")
    # Search for the minecode
    result = df_mine.loc[df_mine['MINECODE'] == int(minecode)]
    
    if not result.empty:
        minename = result.iloc[0]['MINE']
        owncode = result.iloc[0]['OWNCODE']
        region = result.iloc[0]['RGNCODE']
        print(minename)
        return f"Minecode: {minecode}, Minename: {minename}, Owner: {owncode}, Region:{region}"
    else:
        return "Minecode not found"
