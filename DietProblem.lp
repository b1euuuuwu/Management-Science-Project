\* DietProblem *\
Minimize
Total_Cost_of_meals_per_day: 6000 meals_meal1 + 2500 meals_meal2
 + 9000 meals_meal3 + 7000 meals_meal4 + 8000 meals_meal5
Subject To
CaloriesRequirement: 572 meals_meal1 + 812 meals_meal2 + 429 meals_meal3
 + 357 meals_meal4 + 520 meals_meal5 >= 2350
CarbsRequirement: 31 meals_meal1 + 77 meals_meal2 + 61 meals_meal3
 + 11 meals_meal4 + 87 meals_meal5 >= 100
CardsRequirement: 31 meals_meal1 + 77 meals_meal2 + 61 meals_meal3
 + 11 meals_meal4 + 87 meals_meal5 <= 130
LipidsRequirement: 33 meals_meal1 + 38 meals_meal2 + 15 meals_meal3
 + 23 meals_meal4 + 10 meals_meal5 <= 51
NatriumRequirement: meals_meal1 + 2 meals_meal2 + meals_meal3 + meals_meal4
 + meals_meal5 <= 2
ProteinRequirement: 40 meals_meal1 + 41 meals_meal2 + 12 meals_meal3
 + 27 meals_meal4 + 19 meals_meal5 >= 60
End
