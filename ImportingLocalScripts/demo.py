#%% Importando script
import other_script

# %% Importando script y ejecutando acción desde archivo principal
import other_script
print(4)

# %% Definiendo una variable e intentando acceder desde archivo principal
import other_script2
print(other_script2.num)

# %% Definiendo una variable y accediendo de forma correcta a variable desde
# %  otro script

import other_script2
print(other_script2.num)

# %% Llamando funciones
import useful_functions

scores = [88, 92, 79, 93, 85]

mean = useful_functions.mean(scores)
curved = useful_functions.add_five(scores)

mean_c = useful_functions.mean(curved)

print('Scores: ', scores)
print('Original Mean: ', mean, ' New mean: ', mean_c)
print('Original Mean: {0} New Mean: {1}'.format(mean, mean_c))

# %% Llamando a módulo que realiza pruebas internas
import useful_functionsv2

scores = [88, 92, 79, 93, 85]

mean = useful_functions.mean(scores)
curved = useful_functions.add_five(scores)

mean_c = useful_functions.mean(curved)

print('Scores: ', scores)
print('Original Mean: {0} New Mean: {1}'.format(mean, mean_c))

# %% Invocando módulo que solo ejecuta sus pruebas sólo si es el archivo
# %  principal
import useful_functionsv3

scores = [88, 92, 79, 93, 85]

mean = useful_functions.mean(scores)
curved = useful_functions.add_five(scores)

mean_c = useful_functions.mean(curved)

print('Scores: ', scores)
print('Original Mean: {0} New Mean: {1}'.format(mean, mean_c))
# %% Ahora invocando  a módulo que contiene un control de su método main
import useful_functionsv4

scores = [88, 92, 79, 93, 85]

mean = useful_functions.mean(scores)
curved = useful_functions.add_five(scores)

mean_c = useful_functions.mean(curved)

print('Scores: ', scores)
print('Original Mean: {0} New Mean: {1}'.format(mean, mean_c))

# %% Visualizando nombre de cada archivo

import useful_functionsv4 as uf

scores = [88, 92, 79, 93, 85]

mean = useful_functions.mean(scores)
curved = useful_functions.add_five(scores)

mean_c = useful_functions.mean(curved)

print('Scores: ', scores)
print('Original Mean: {0} New Mean: {1}'.format(mean, mean_c))

print(__name__)
print(uf.__name__)
# %% [Referencia](https://classroom.udacity.com/courses/ud1110/lessons/01465444-9f86-4b97-b1c5-2365ab00749b/concepts/a3dc7153-8f26-4ac9-b5b5-8631600c3563) 


