books = [
    {"id":1, "title":"Book A", "color":"blue", "year":1901},
    {"id":2, "title":"Book B", "color":"red", "year":1957},
    {"id":3, "title":"Book C", "color":"blue", "year":1988},
    {"id":4, "title":"Book D", "color":"green", "year":1923},
    {"id":5, "title":"Book E", "color":"yellow", "year":2017}
]



# 
# for i in books:
#     if i ["id"] == 4:
#         print(i["title"])
# 
# t = 0
# for c in books:
#     if c ["color"] == "blue":
#         t = t + 1
# print(t)
# 
# y = 0
# for a in books:
#     if a ["year"] > 1950:
#         y = y + 1
# print(y)

id_4 = [i ["title"] for i in books if i ["id"]== 4]
print(id_4)

color_blue = [c for c in books if c ["color"]=="blue"]
print(len(color_blue))

year_after_1950 = [y for y in books if y ["year"]>1950]
print(len(year_after_1950))
#breakpoint()