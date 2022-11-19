import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
Column 2 --> Country Name
Column 12 --> Population as of July 1
Column 15 --> Pop Density as of July 1
Column 21 --> Growth Rate
Column 38 --> Net migration Rate
Column 10 --> Year
'''

# Find greatest population (july 2021) + least density(july 2021)
req_cols = [2, 12, 15, 21, 38, 10]
dataframe = pd.read_excel('assets/data_set.xlsx', usecols=req_cols, skiprows= 16)

# Population
dataframe = dataframe[dataframe['Year'] == 2021]
block_list = ['WORLD', 'AFRICA', 'ASIA', 'EUROPE', 'LATIN AMERICA AND THE CARIBBEAN', 'NORTHERN AMERICA', 'OCEANIA',
            'Eastern and South-Eastern Asia', 'Central and Southern Asia', 'Latin America and the Caribbean',
            'Less developed regions', 'Middle-income countries', 'Less developed regions, excluding least developed countries',
            'Less developed regions, excluding China', 'Lower-middle-income countries', 'Upper-middle-income countries',
            'Southern Asia', 'Eastern Asia', 'More developed regions', 'High-income countries',
            'Sub-Saharan Africa', 'Europe and Northern America', 'Least developed countries',
            'Low-income countries', 'South-Eastern Asia', 'Land-locked Developing Countries (LLDC)',
            'Northern Africa and Western Asia', 'Eastern Africa', 'South America', 'Western Africa',
            'Eastern Europe', 'Western Asia', 'Western Europe',
            'Middle Africa', 'Central America', 'Southern Europe', 'Northern Europe', 'Northern Africa',
            'Central Asia', 'Small Island Developing States (SIDS)', 'Southern Africa', 'South Africa'] 
for i in range (len(block_list)):
    dataframe = dataframe[dataframe["Region, subregion, country or area *"].str.contains(block_list[i]) == False]

countries = dataframe['Region, subregion, country or area *'].tolist()
countries_density = dataframe['Region, subregion, country or area *'].tolist()
pop_data_str = dataframe['Total Population, as of 1 July (thousands)'].tolist()
pop_densities_str = dataframe['Population Density, as of 1 July (persons per square km)'].tolist()
growth_rate_str = dataframe['Population Growth Rate (percentage)'].tolist()
countries2 = dataframe['Region, subregion, country or area *'].tolist()

pop_data = [int(i) for i in pop_data_str]
pop_densities = [int(i) for i in pop_densities_str]
growth_rate = [float(i) for i in growth_rate_str]

max25Population = []
max25Country = []
densities_of_max25 = []
countries

for i in range (27):
    # Finds max population and index of val, removes for new max and index
    x = max(pop_data)
    x_index = pop_data.index(x)

    max25Population.append(x)    
    max25Country.append(countries[x_index])
    densities_of_max25.append(pop_densities[x_index])

    pop_data.pop(x_index)
    countries.pop(x_index)
    pop_densities.pop(x_index)

max25Population.pop(2)
max25Population.pop(19)
max25Country.pop(2)
max25Country.pop(19)
densities_of_max25.pop(2)
densities_of_max25.pop(19)

#print(max25Country, '\n', max25Population, '\n', densities_of_max25)

print('--------------------------------\n', countries)

ratios = []

for i in range(len(max25Country)):
    ratio = max25Population[i] / densities_of_max25[i]
    ratios.append(ratio)

sorted_ratios = []
sorted_population = []
sorted_countries = []

for i in range (10):
    x = max(ratios)
    x_index = ratios.index(x)

    sorted_ratios.append(x)
    sorted_population.append(max25Population[x_index])
    sorted_countries.append(max25Country[x_index])
    
    ratios.pop(x_index)
    max25Country.pop(x_index)
    max25Population.pop(x_index)

growth_factors = []
# Check top 10 coutnries index, then grab growth rate
for i in range (len(sorted_countries)):
    growth_index = countries2.index(sorted_countries[i])
    print(growth_index)
    growth_factors.append(growth_rate[growth_index])

print(countries2, '\n')
print('Sorted Countries: ' , sorted_countries, '\n', 'Sorted Ratios: ' , sorted_ratios)
print(growth_factors)

growth_data = np.empty(shape=(10, 10))

for i in range(10):
    growth_data[0][i] = sorted_population[i]

sorted_population_plot = []
sorted_population_plot.append(sorted_population[1])

for i in range(1, 10, 1):
    sorted_population_plot.append(sorted_population_plot[i-1] * (growth_rate[1] + 1) )

data_dict = {
    'Year': [2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030],
    'Population': sorted_population_plot
}

df = pd.DataFrame(data_dict)
df.head()

df.plot(kind='line',
        x = 'Year',
        y= 'Population',
        color = 'red')

plt.title("China Projection")

plt.show()