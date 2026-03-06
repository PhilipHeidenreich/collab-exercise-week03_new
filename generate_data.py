data = pd.DataFrame({
    "country": ["Switzerland", "Germany", "France", "Italy", "Spain"],
    "gdp_bn_usd": [800, 4000, 2800, 2100, 1400],
    "population_mn": [8.7, 84.4, 68.2, 59.0, 47.4],
    "gdp_per_capita_usd": [92000, 47000, 41000, 36000, 30000],
    "year": 2023
})
data.to_csv("gdp_data.csv", index=False)