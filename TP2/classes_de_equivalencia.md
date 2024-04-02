# Classes de equivalência
### Função ```validarForma(self)```

| Variáveis de Entrada |          Classes Válidas      |          Classes Inválidas        |
|----------------------|-------------------------------|-----------------------------------|
| A, B, C              | A < (B + C)                   | A >= (B+C)                        |
|                      | B < (C + A)                   | B >= (A+C)                        |
|                      | C < (A + B)                   | C >= (B+A)                        |
|                      |                               | C >= (B+A)                        |
|                      |                               | Valores negativos                 |


### Função ```ehEquilatero(self)```

| Variáveis de Entrada |          Classes Válidas      |          Classes Inválidas        |
|----------------------|-------------------------------|-----------------------------------|
| A, B, C              | A = B && B = C                | A ≠ C                             |
|                      |                               | A ≠ B                             |
|                      |                               | B ≠ C                             |

### Função ```ehIsosceles(self)```

| Variáveis de Entrada |          Classes Válidas      |          Classes Inválidas        |
|----------------------|-------------------------------|-----------------------------------|
| A, B, C              |  A = B && A ≠ C               | A = B && A = C                    |
|                      |  A = C && A ≠ B               | A ≠ B && B ≠ C                    |
|                      |  B = C && B ≠ A               |                                   |

### Função ```ehEscaleno(self)```

| Variáveis de Entrada |          Classes Válidas      |          Classes Inválidas        |
|----------------------|-------------------------------|-----------------------------------|
| A, B, C              |  A ≠ B && A ≠ C && B ≠ C      | A = B && A ≠ C                    |
|                      |                               | A = C && A ≠ B                    |
|                      |                               | B = C && A ≠ B                    |
|                      |                               | A = B && A = C                    |


