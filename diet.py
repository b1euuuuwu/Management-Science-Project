from pulp import *

# Create a linear programming problem
meal_plan = LpProblem("MealPlanning", LpMinimize)

# Define the decision variables
food_items = ["Food1", "Food2", "Food3", "Food4", "Food5"]
restaurants = ["RestaurantA", "RestaurantB", "RestaurantC"]

x = LpVariable.dicts("x", (food_items, restaurants), lowBound=0, upBound=None, cat=LpInteger)
y = LpVariable.dicts("y", (food_items, restaurants), cat=LpBinary)

# Define the meal type decision variables
meal_categories = ["Breakfast", "Lunch", "Dinner"]
m = LpVariable.dicts("m", (meal_categories, restaurants), cat=LpBinary)

# Define the objective function (minimize cost)
meal_plan += lpSum([x[i][r] * 0.50 + x[i][r] * 0.75 + x[i][r] * 1.25 + x[i][r] * 1.00 + x[i][r] * 1.50 for i in food_items for r in restaurants]), "Total Cost"

# Define the nutritional requirements as constraints
meal_plan += lpSum([x["Food1"][r] * 150 + x["Food2"][r] * 125 for r in restaurants]) >= 2350, "Calories"
meal_plan += lpSum([x["Food1"][r] * 10 + x["Food2"][r] * 5 for r in restaurants]) >= 7, "Protein"
meal_plan += lpSum([x["Food1"][r] * 10 + x["Food2"][r] * 5 for r in restaurants]) <= 20, "Protein"
meal_plan += lpSum([x["Food3"][r] * 40 for r in restaurants]) >= 45, "VitaminC"
meal_plan += lpSum([x["Food1"][r] * 0.05 + x["Food2"][r] * 0.10 + x["Food4"][r] * 0.15 + x["Food5"][r] * 0.20 for r in restaurants]) >= 5, "Iron"

# Define the budget constraint
meal_plan += lpSum([x[i][r] * (0.50 + 0.75 + 1.25 + 1.00 + 1.50) for i in food_items for r in restaurants]) <= 20, "Budget"

# Add meal type constraints
for m_category in meal_categories:
    meal_plan += lpSum([m[m_category][r] for r in restaurants]) == 1, f"OneMealPer{m_category}"

# Add constraints to ensure no two different restaurants in the same meal category
for m_category in meal_categories:
    for r1 in restaurants:
        for r2 in restaurants:
            if r1 != r2:
                meal_plan += m[m_category][r1] + m[m_category][r2] <= 1, f"UniqueRestaurant_{r1}_{r2}_{m_category}"

# Solve the problem
meal_plan.solve()

# Print the results
print("Status:", LpStatus[meal_plan.status])
print("Optimal Meal Plan:")
for i in food_items:
    for r in restaurants:
        servings = value(x[i][r])
        if servings > 0:
            print(f"{i} from {r}: {servings} servings")

print("Meal Assignment:")
for m_category in meal_categories:
    for r in restaurants:
        if value(m[m_category][r]) == 1:
            print(f"{r} for {m_category}")

print("Total Cost: $", value(meal_plan.objective))
