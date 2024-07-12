product_Prices = [1200, 500, 650, 800, 3500, 1700]
salaries = [52000, 61500, 1800, 13500, 21700]
team_points = [12, 8, 4, 10, 2]

# Goal : find maximum out of these three

max = product_Prices[0]
for index in range(1, len(product_Prices)):
    if product_Prices[index] > max:
        max = product_Prices[index ]