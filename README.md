## Abstract
Using Genetic Algorithms (GA) with  NEAT-Python library to make Mario learn how to play in Super Mario World.

## Dependencies installation
 | Library | Installation command |
 | ---- | ---- |
 |Gym Retro | ```pip3 install gym-retro``` |
 |NEAT      | ```pip3 install neat-python``` |
 |OpenCV    |````pip3 install opencv-python```|


[IMPORTANT] The ROM of "Super Mario World" must be imported to use it in the Gym Retro enviroment, import it with:

```python3 -m retro.import /path/to/your/ROMs/directory/```

## Update RAM variables in *data.json*
Open the file *data.json* located in Python libraries installation folder:

```../lib/python[3.6|3.7|3.8]/site-packages/retro/data/stable/SuperMarioWorld-Snes/```

and subsitute it with the following RAM addresses for the new variables:
```
{
    "info" : {
     " coins " : {
       " address " : 8261055 ,
       " type " : " |u1 "
     },
    " lives " : {
       " address " : 8261054 ,
       " type " : " |i1 "
     },
     "x" : {
       " address " : 148 ,
       " type " : " <u2 "
     },
     " dead " : {
       " address " : 8257688 ,
       " type " : " <u4 "
    },
     " endOfLevel " : {
       " address " : 8259846 ,
       " type " : " |i1 "
    },
     " score " : {
       " address " : 8261428 ,
       " type " : " <u4 "
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


