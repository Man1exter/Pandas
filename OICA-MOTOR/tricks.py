import pandas as pd

df = pd.DataFrame({
    'name': ['Mario','Ann','Kris','Joe'],
    'age': [22 , 46 , 21 , 51],
    'children': [1 , 2 , 3 , 4],
    'bank balance': [570.0 , 460.0 , 210.0 , 510.0]
})

print(df)

def even_nb_bgc(cell_value):
    highlight = 'background-color: lightblue;'
    default = ''
    
    if type(cell_value) in [float,int]:
        if cell_value % 2 == 0:
            return highlight
        return default
    
df.style.applymap(even_nb_bgc)

# .ipynb -> use file