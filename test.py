from pulp import *

meals = ["meal1", "meal2", "meal3", "meal4", "meal5"]

# dictionary for all variables

costs = {
    "meal1" : 6000,
    "meal2" : 2500,
    "meal3" : 9000,
    "meal4" : 7000,
    "meal5" : 8000
}

calories = {
    "meal1" : 572,
    "meal2" : 812,
    "meal3" : 429,
    "meal4" : 357,
    "meal5" : 520
}

carbohydrate = {
    "meal1" : 31,
    "meal2" : 77,
    "meal3" : 61,
    "meal4" : 11,
    "meal5" : 87
}

protein = {
    "meal1" : 40,
    "meal2" : 41,
    "meal3" : 12,
    "meal4" : 27,
    "meal5" : 19
}

lipids = {
    "meal1" : 33,
    "meal2" : 38,
    "meal3" : 15,
    "meal4" : 23,
    "meal5" : 10
}

natrium = {
    "meal1" : 1,
    "meal2" : 2,
    "meal3" : 1,
    "meal4" : 1,
    "meal5" : 1
}

prob = LpProblem("DietProblem", LpMinimize)

nutrition_vars = LpVariable.dicts("meals", meals, 0)

prob += (
    lpSum([costs[i] * nutrition_vars[i] for i in meals]),
    "Total Cost of meals per day",
)

prob += (
    lpSum([calories[i] * nutrition_vars[i] for i in meals]) >= 2350,
    "CaloriesRequirement",
)
prob += (
    lpSum([carbohydrate[i] * nutrition_vars[i] for i in meals]) <= 130,
    "CardsRequirement",
)
prob += (
    lpSum([carbohydrate[i] * nutrition_vars[i] for i in meals]) >= 100,
    "CarbsRequirement",
)
prob += (
    lpSum([protein[i] * nutrition_vars[i] for i in meals]) >= 60,
    "ProteinRequirement",
)
prob += (
    lpSum([lipids[i] * nutrition_vars[i] for i in meals]) <= 51,
    "LipidsRequirement",
)
prob += (
    lpSum([natrium[i] * nutrition_vars[i] for i in meals]) <= 2,
    "NatriumRequirement",
)

prob.writeLP("DietProblem.lp")

prob.solve()

print("Status:", LpStatus[prob.status])

print("Total Cost of meals = ", value(prob.objective))