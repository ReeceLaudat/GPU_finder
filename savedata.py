import sqlite3
import os

def itemData(name, price, links):
    conn = sqlite3.connect("GPUfinderDB.db")

    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS ITEM (NAME PRIMARY KEY, COST , LINK);""")

    
    temp_list = []
    for each_data in range(len(name)):
        temp_list.append([name[each_data],price[each_data], links[each_data]])


    cursor.executemany('''INSERT OR IGNORE INTO ITEM(NAME, COST, LINK) VALUES (?, ?, ?)''', temp_list)
    


    conn.commit()



