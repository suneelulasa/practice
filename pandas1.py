

# data = ({"cars" : ["ferari", "toyata", "tata", "suziki"]}
#         )
# df = pd.DataFrame(data,index = [1, 2, 3, 4])
# print(df)


# df1 = pd.DataFrame(
#     {
#         "A": ["A0", "A1", "A2", "A3"],
#         "B": ["B0", "B1", "B2", "B3"],
#         "C": ["C0", "C1", "C2", "C3"],
#         "D": ["D0", "D1", "D2", "D3"],
#     },
#     index=[0, 1, 2, 3],
# )
#
#
# df2 = pd.DataFrame(
#     {
#         "A": ["A4", "A5", "A6", "A7"],
#         "B": ["B4", "B5", "B6", "B7"],
#         "C": ["C4", "C5", "C6", "C7"],
#         "D": ["D4", "D5", "D6", "D7"],
#     },
#     index=[4, 5, 6, 7],
# )
#
#
# df3 = pd.DataFrame(
#     {
#         "A": ["A8", "A9", "A10", "A11"],
#         "B": ["B8", "B9", "B10", "B11"],
#         "C": ["C8", "C9", "C10", "C11"],
#         "D": ["D8", "D9", "D10", "D11"],
#     },
#     index=[8, 9, 10, 11],
# )
#
#
# frames = [df1, df2, df3]
#
# result = pd.concat(frames)

# data1 = {
#         "A": ["a", "b", "c", "d"],
#         "B": ["e", "f", "g", "h"],
#         "C": ["i", "j", "k", "l"],
#         "D": ["m", "n", "o", "p"],
#         }
#
# data2 = {
#         "A": ["a", "b", "c", "d"],
#         "B": ["e", "f", "g", "h"],
#         "C": ["i", "j", "k", "l"],
#         "D": ["m", "n", "o", "p"],
#         }
#
# data3 = {
#         "A": ["a", "b", "c", "d"],
#         "B": ["e", "f", "g", "h"],
#         "C": ["i", "j", "k", "l"],
#         "D": ["m", "n", "o", "p"],
#         }
# df1 = pd.DataFrame(data1)
# df2 = pd.DataFrame(data2)
# df3 = pd.DataFrame(data3)
# y = pd.concat([df1, df2, df3],ignore_index=True)
# print(y)


# import pandas as pd
#
# data1 = pd.DataFrame({
#                  "A1": ["a", "b", "c", "d"],
#                  "B2": ["e", "f", "g", "h"],
#                  "C3": ["i", "j", "k", "l"],
#                  "D4": ["m", "n", "o", "p"]
#          },
#          index=[0, 1, 2, 3]
# )
#
# data2 = pd.DataFrame({
#                  "A1": ["a", "b", "c", "d"],
#                  "B2": ["e", "f", "g", "h"],
#                  "C3": ["i", "j", "k", "l"],
#                  "D4": ["m", "n", "o", "p"]
#          },
#          index=[4, 5, 6, 7])
#
# data3 = pd.DataFrame({
#                  "A1": ["a", "b", "c", "d"],
#                  "B2": ["e", "f", "g", "h"],
#                  "C3": ["i", "j", "k", "l"],
#                  "D4": ["m", "n", "o", "p"]
#          },
#          index=[8, 9, 10, 11])
#
# y = pd.concat([data1, data2, data3], ignore_index=True)
# print(y)
# print(data1)
# print(y.loc[10])
# print(y.loc[[10,4]])


# data = pd.read_csv(r"C:\Users\ulasa\OneDrive\Desktop\New student details2.csv")
# print(data[:5])
#
# print(data.info())

# df = pd.options.display.max_rows=900
# print(pd.options.display.max_rows)



# data = { "duration":{"a":10,"b":15, "c":20},
#          "pulse":{"d":11, "e":12, "f":13},
#          "presure":{"g":50, "h":56, "i":45}
#         }
# print(pd.DataFrame(data))



# data = pd.read_csv(r"C:\Users\ulasa\OneDrive\Desktop\data with wrong formate.csv")
# print(data)
# df = pd.DataFrame(data)
# print(data.dropna())
# print(data.fillna(135))
# x = data["Calories"].mean()
# data["Calories"].fillna(x, inplace=True)
# data["Date"] = pd.to_datetime(data["Date"])
# # print(data["Date"].dropna(inplace=True))
# data.dropna(inplace=True)
# data.loc[7,"Duration"] = 50
# (data.drop_duplicates())


# print(data.loc[0:5])
# print(data.iloc[0:5])



# data["total"] = data["Pulse"] + data["Maxpulse"]
# print(data)

# import openpyxl
# df = data.to_excel("C:\\Users\\ulasa\\OneDrive\\Desktop\\data with wrong formate.xlsx")
# print(df)


# import matplotlib.pyplot as plt
#
# data = pd.read_csv(r"C:\Users\ulasa\OneDrive\Desktop\data with wrong formate.csv")
# data.plot()
# plt.show()


# [
#     ('Ankit', 34, 'Uttar pradesh', 34),
#     ('Riti', 30, 'Delhi', 30),
#     ('Aadi', 16, 'Delhi', 16),
#     ('Riti', 30, 'Delhi', 30),
#     ('Riti', 30, 'Delhi', 30),
#     ('Riti', 30, 'Mumbai', 30),
#     ('Ankita', 40, 'Bihar', 40),
#     ('Sachin', 30, 'Delhi', 30)
# ]


#
# import pandas as pd
# df = pd.DataFrame({ "name":['Ankit','Riti','Aadi','Riti',],
#
#                            "age":[34,30,16,30],
#                            "state":["ap", "tn", "ka", "kr"],
#                            "marks":[34,30,16,30] })


# print(df.T.drop_duplicates().T)
#
# print(df.T.duplicated().T)

# print(df.drop(["state","marks"],axis=1))


# for col in df.columns:
#     if "marks" in col:
#         del df[col]
# print(df)

#
# import pandas as pd
# data2 = pd.DataFrame({
#                  "A1": ["a", "b", "c", "d"],
#                  "B2": ["e", "f", "g", "h"],
#                  "C3": ["i", "j", "k", "l"],
#                  "D4": ["m", "n", "o", "p"]})
# print(data2.replace(to_replace="a", value="suneel" ))
# print(data2)

# data1 = pd.DataFrame({
#                  "A1": ["a", "b", "c", "d"],
#                  "B2": ["e", "f", "g", "h"],
#                  "C3": ["i", "j", "k", "l"],
#                  "D4": ["m", "n", "o", "p"]})
#
# print(pd.concat([data1,data2], ignore_index=True))



import pandas as pd
#
# data1 = pd.Series([1,2,3,4,5,6])
# data2 = pd.Series([11,12,13,14,15,16])
# data = pd.Series(["a", "b", "c", "d", "e", "f"])
# col = {"name":data, "sub1":data1, "sub2":data2}
# d = pd.concat(col,axis=1)
# print(d)


# data1 = pd.Series([1, 2, 3, 4, 1, 6, 1])
# print(data1.unique())


# d = [1,0,5,8,0,9,6,0,]
# sort = [x for x in d if x!= 0] + [x for x in d if x == 0]
# print(sort)

# import pandas as pd
# data = pd.DataFrame({"a":[1,2,3,4,5],
#                      "b":[6,7,8,9,10],
#                      "c":[1,2,3,4,5]}
#                     )
# print(data.T.drop_duplicates().T)

# import pandas as pd
# df1 = pd.DataFrame({
#                  "A1": ["a", "b", "c", "d"],
#                  "B2": ["e", "f", "g", "h"],
#                  "C3": ["i", "j", "k", "l"],
#                  "A2": ["a", "b", "c", "d"],
#                  "C": ["i", "j", "k", "l"],
#                  "D4": ["m", "n", "o", "p"]
#          })

# def get_duplicate(df):
#     dup_colms = set()
#     for x in range(df.shape[1]):
#         col = df.iloc[:,x]
#         for y in range(x+1,df.shape[1]):
#             othcol = df.iloc[:,y]
#             if col.equals(othcol):
#                 dup_colms.add(df.columns.values[y])
#     return list(dup_colms)
#
# duplicate = get_duplicate(df1)
#
# for col in duplicate:
#     print("duplicate columns :",col)

# print(df1)
# # print(df1.T.drop_duplicates().T)
#
# print(df1.shape[0])
# print(df1.shape[1])
# print(df1.shape)




# import pandas as pd
# df = pd.read_csv(r"C:\Users\ulasa\OneDrive\Desktop\data with wrong formate.csv")
# print(df.fillna(999,inplace=True))
