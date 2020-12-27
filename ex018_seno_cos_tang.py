"""import math
ang = int(input('Digite um ângulo qualquer:'))
print(f'O seno do ângulo é{math.sin(ang)}')
print(f'O coseno do ângulo é {math.cos(ang)}')
print(f'A tangente do ângulo é {math.tan(ang)}')"""

import math
ang = float(input('Digite um ângulo qualquer:'))
seno = math.sin(math.radians(ang))
print(f'O seno do ângulo é{seno :.2f}')
cos = math.cos(math.radians(ang))
print(f'O coseno do ângulo é {cos :.2f}')
tan = math.tan(math.radians(ang))
print(f'A tangente do ângulo é {tan :.2f}')


