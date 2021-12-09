import pandas as pd

friends = {
    'name' : ['kim', 'lee', 'choi'],
    'age' : [26, 30, 45],
    'job' : ['student', 'employee', 'teacher']
}

df = pd.DataFrame(friends)
print(df)