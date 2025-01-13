import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

gas = pd.read_csv('gas_prices.csv')

gas

plt.title('PRICE IN US$')

colors = {'Canada': 'red', 'Australia': 'blue', 'Italy': 'yellow'}

plt.plot(gas['Year'], gas['Australia'], label = 'Australia', color = colors['Australia'])
plt.plot(gas['Year'], gas['Italy'], label = 'Italy', color = colors['Italy'])
plt.plot(gas['Year'], gas['Canada'], label = 'Canada', color = colors['Canada'])

plt.xticks(gas['Year'][::2])

plt.xlabel('Years')
plt.ylabel('US DOLAR')

plt.savefig('PRICE IN US$.jpeg')

plt.legend()
plt.show()
