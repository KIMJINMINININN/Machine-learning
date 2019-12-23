import pandas as pd

url = './part2/sample.html'

tables =pd.read_html(url)

print(len(tables))
print('\n')

for i in range(len(tables)):
    print('tables[%s]' % i)
    print(tables[i])
    print('\n')

df = tables[1]


    
