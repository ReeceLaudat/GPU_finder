import sys
import sqlite3
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


def graphItemData():
    conn = sqlite3.connect("GPUfinderDB.db")


    cursor = conn.cursor()


    df = pd.read_sql_query("SELECT DATE, MAX(£COST) FROM ITEM GROUP BY DATE ORDER BY £COST", conn)


    costTableMAX = []
    costTableAVG = []
    costTableMIN = []



    for eachItemCost in conn.execute("SELECT MAX(£COST) AS £COST FROM ITEM GROUP BY date"):
        cost = str(eachItemCost).replace(",", "")
        costTableMAX.append(cost)

    for eachItemCost in conn.execute("SELECT AVG(£COST) FROM ITEM GROUP BY date"):
        cost = str(eachItemCost).replace(",", "")
        costTableAVG.append(cost)

    for eachItemCost in conn.execute("SELECT MIN(£COST) AS £COST FROM ITEM GROUP BY date"):
        cost = str(eachItemCost).replace(",", "")
        costTableMIN.append(cost)

    plt.plot(df["DATE"], costTableMIN, color="b", label="Min price")
    plt.plot(df["DATE"], costTableAVG, color="g", label="Average price")
    plt.plot(df["DATE"], costTableMAX, color="r", label="Max price")



    plt.xlabel("Dates")
    plt.ylabel("Cost")
    plt.show()


