import pandas as pd

student1 = pd.Series({'국어':100,'영어':80,'수학':90})
student2 = pd.Series({'수학':80,'국어':90,'영어':80})

print(student1)
print('\n')
print(student2)
print('\n')

addition = student1 + student2
subtraction = student1 + student2
multiplication = student1 + student2
division = student1 / student2
print(type(division))
print('\n')
print(division.index)
print('\n')
print(division.values)
print('\n')

result = pd.DataFrame([addition, subtraction, multiplication, division], index=['덧셈', '뺄셈', '곱셈', '나눗셈'])
print(result)