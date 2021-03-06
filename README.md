## Abstract
Using ***Genetic Algorithms*** (GA) with  *NEAT-Python* library to make Mario learn how to play in *Super Mario World*.

## Dependencies installation
 | Library | Installation command |
 | ---- | ---- |
 |Gym Retro | ```pip3 install gym-retro``` |
 |NEAT      | ```pip3 install neat-python``` |
 |OpenCV    | ```pip3 install opencv-python```|


[IMPORTANT] The ROM of *Super Mario World* must be imported to use it in the Gym Retro enviroment, import it with:

```python3 -m retro.import /path/to/your/ROMs/directory/```

## Update RAM variables in *data.json*
Open the file *data.json* located in Python libraries installation folder:

```../lib/python[3.6|3.7|3.8]/site-packages/retro/data/stable/SuperMarioWorld-Snes/```

and subsitute it with the following RAM addresses for the new variables:
```
{
  "info": {
    "checkpoint": {
      "address": 5070,
      "type": "|i1"
    },
    "coins": {
      "address": 8261055,
      "type": "|u1"
    },
    "endOfLevel": {
      "address": 8259846,
      "type": "|i1"
    },
    "lives": {
      "address": 8261399,
      "type": "|u1"
    },
    "powerups": {
      "address": 25,
      "type": "|i1"
    },
    "score": {
      "address": 8261428,
      "type": "<u4"
    },
    "x": {
      "address": 148,
      "type": "<u2"
    },
    "dead": {
      "address": 8257688,
      "type": "<u4"
    },
    "y": {
      "address": 114,
      "type": "<u4"
    },
    "jump": {
      "address": 8257747,
      "type": "<u4"
    },
    "yoshiCoins": {
      "address": 8262690,
      "type": "<u4"
    }
  }
}
```

## Plots obtained from execution
It has been obtained execution statistics for **4 different size populations**:

 - *10 cromosomes*
 - *30 cromosomes*
 - *50 cromosomes*
 - *100 cromosomes*

[Fitness function mean]

<img src="https://github.com/alrodsa/SMW_GeneticAlgorithms/blob/main/graphics/Medias%20fitness%20function.svg">

[Maximun Fitness function]

<img src="https://github.com/alrodsa/SMW_GeneticAlgorithms/blob/main/graphics/M%C3%A1ximos%20fitness%20function.svg">

[Number of time stage is completed]

<img src="https://github.com/alrodsa/SMW_GeneticAlgorithms/blob/main/graphics/N%C3%BAmero%20de%20veces%20que%20se%20supera%20el%20nivel.svg">

[Execution time]

<img src="https://github.com/alrodsa/SMW_GeneticAlgorithms/blob/main/graphics/Tiempo%20de%20ejecuci%C3%B3n.svg">


