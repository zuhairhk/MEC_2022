import pandas as pd

'''
Column 2 --> Country Name
Column 12 --> Population as of July 1
Column 15 --> Pop Density as of July 1
Column 21 --> Growth Rate
Column 38 --> Net migration Rate
Column 10 --> Year
'''

def data_sorter():
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

    pop_data = [int(i) for i in pop_data_str]
    pop_densities = [int(i) for i in pop_densities_str]

    max25Population = []
    max25Country = []
    min25Densities = []
    min25DensityCountries = []

    for i in range (27):
        # Finds max population and index of val, removes for new max and index
        x = max(pop_data)
        x_index = pop_data.index(x)

        y = min(pop_densities)
        y_index = pop_densities.index(y)

        max25Population.append(x)    
        max25Country.append(countries[x_index])
        min25Densities.append(y)
        min25DensityCountries.append(countries[y_index])

        pop_data.pop(x_index)
        countries.pop(x_index)
        pop_densities.pop(y_index)
        countries_density.pop(y_index)


    print(max25Population, '\n', max25Country, '\n', min25Densities, '\n', min25DensityCountries)
    print(dataframe)