# Linguado
Linguado is a tool which compares the abstract syntax trees (AST) of two or more scripts to measure the similarity. The 
main goal intended for this tool is to detect two variants of the same malware.

## Background
This tool was developed by Guzmán Cernadas Pérez (@DonCaralludo) working for BE:SEC (@BESEC_byEmetel). It was shown by 
Marcos Carro Fernández and Guzmán Cernadas Pérez at the [VICON](https://vicon.gal/) in april 2023.

## Installation

From pypi:

```
pip3 install linguado
```

From repo:

```
git clone https://github.com/caralludo/linguado.git
cd linguado
pip3 install .
```

## Usage
In order to execute this tool, you have to have two or more source codes in different files, and you have to know in 
which language they are made.

The help is as follows:
```
usage: main.py [-h] [-p PAR] [-o OUTPUT] Files [Files ...] Language

Linguado is a tool which compares the AST of two or more files. Created by Guzmán Cernadas Pérez (@DonCaralludo)
working for BE:SEC (@BESEC_byEmetel)

positional arguments:
  Files                 Files to analyze
  Language              Language of the files. Options: c, javascript, nasm, php, python2, python3, vba

options:
  -h, --help            show this help message and exit
  -p PAR, --par PAR     Changes the number of iterations of the Weisfeiler-Lehman algorithm (default: 3)
  -o OUTPUT, --output OUTPUT
                        Changes the base name of the output files (default: result.csv)
```

### Examples
Compare two source codes made in python3:
```
linguado source1.py source2.py python3
```

Compare two or more files made in python3:
```
linguado source* python3
```

Compare two or more files made in python3 and change the number of iterations of the Weisfeiler-Lehman algorithm:
```
linguado source* python3 -p 10
```

Compare two source codes made in python3 and changing the output name:
```
linguado source1.py source2.py python3 -o output.csv
```

### Available languages
For the moment, the tool can compare the following programming languages:
* C
* JavaScript
* NASM
* PHP
* Python2
* Python3
* VBA

### Adding new languages
To add a new language you have to do the following steps:
1. [Install ANTLR](https://www.antlr.org/download.html)
2. Create or obtain a grammar in ANTLR4 format.
3. Generate the files with the following command:
```
antlr4 -Dlanguage=Python3 *.g4
```
4. Save the files in a new folder in the path ./linguado/\[language name\]
5. Import the Lexer and Parser in the file linguado/main.py
```python
from mygrammar.MyGrammarLexer import MyGrammarLexer
from mygrammar.MyGrammarParser import MyGrammarParser
from linguado.c.CLexer import CLexer
from linguado.c.CParser import CParser
from javascript.JavaScriptLexer import JavaScriptLexer
from javascript.JavaScriptParser import JavaScriptParser
from php.PhpLexer import PhpLexer
from php.PhpParser import PhpParser
from python2.Python2Lexer import Python2Lexer
from python2.Python2Parser import Python2Parser
from python3.Python3Lexer import Python3Lexer
from python3.Python3Parser import Python3Parser
from vba.vbaLexer import vbaLexer
from vba.vbaParser import vbaParser
```
6. Modify the dictionary in the file linguado/main.py putting the lerxer, the parser and the first rule of the grammar
```python
    language_functions = {
        "c": [CLexer, CParser, "translationUnit"],
        "javascript": [JavaScriptLexer, JavaScriptParser, "program"],
        "mygrammar": [MyGrammarLexer, MyGrammarParser, "first_rule"],
        "php": [PhpLexer, PhpParser, "htmlDocument"],
        "python2": [Python2Lexer, Python2Parser, "file_input"],
        "python3": [Python3Lexer, Python3Parser, "file_input"],
        "vba": [vbaLexer, vbaParser, "startRule"]
    }
```

## Output
A possible output example could be:
```
Generating AST's
100%|██████████| 4/4 [00:03<00:00,  1.16it/s]
Calculating Weisfeiler-Lehman matrix
100%|██████████| 3/3 [00:00<00:00, 28.09it/s]
Checking isomorphism (igraph)
100%|██████████| 4/4 [00:02<00:00,  1.98it/s]
Weisfeiler-Lehman:
[[58162880. 58162880. 58162880. 58162880.]
 [58162880. 58162880. 58162880. 58162880.]
 [58162880. 58162880. 58162880. 58162880.]
 [58162880. 58162880. 58162880. 58162880.]]
Weisfeiler-Lehman (%):
[[100. 100. 100. 100.]
 [100. 100. 100. 100.]
 [100. 100. 100. 100.]
 [100. 100. 100. 100.]]
Mean: 58162880.0 , Standard deviation: +- 0.0 ,  0.0
Isomorphism test (igraph):
[[ True  True  True  True]
 [ True  True  True  True]
 [ True  True  True  True]
 [ True  True  True  True]]
```

In each matrix, the columns represents each source code file ordered by name, and each row represents the source code 
file ordered by name. So, in each intersection is represented the comparation between the two files.

```
             source1.py  source2.py  source3.py  source4.py
source1.py [[ 58162880.   58162880.   58162880.   58162880.]
source2.py  [ 58162880.   58162880.   58162880.   58162880.]
source3.py  [ 58162880.   58162880.   58162880.   58162880.]
source4.py  [ 58162880.   58162880.   58162880.   58162880.]]
```

```
           source1.py  source2.py  source3.py  source4.py
source1.py [[ True        True        True        True]
source2.py  [ True        True        True        True]
source3.py  [ True        True        True        True]
source4.py  [ True        True        True        True]]
```

Also, the tool creates two csv files with the same information in the terminal.

### Measuring similarity
Two codes will have the same abstract syntax tree if:
* The isomorphism test matrix has a True in the intersection of the two sources.

Two codes will not have the same abstract syntax tree if:
* The Weisfeiler-Lehman matrix has different values.

If the sources do not have the same abstract syntax tree, we can use the standard deviation to know if they are similar:
* If the standard deviation is close to zero (less than 5%), then the sources will be very similar.
* If the standard deviation is around the 20%, then could be a chance that the sources are sharing some code.
* If the standard deviation is more than 50%, then the sources will not be the same.

## Behavior
1. Generates the abstract syntax tree with ANTLR4.
2. From the abstract syntax tree generates a graph which we can work with.
3. Calculates the Weisfeiler-Lehman matrix.
4. Performs the isomorphism test (igraph).
5. Prints on the screen and writes in a CSV the results of the Weisfeiler-Lehman algorithm and the isomorphism test.

## Other uses
This tool can be used to look for plagiarism in academic environments.


## Links of interest
[ANTLR](https://www.antlr.org/)

[Grammars for ANTLR](https://github.com/antlr/grammars-v4)

[VX-Underground Malware Repository](https://github.com/vxunderground/MalwareSourceCode)

[JavaScript Malware Repository](https://github.com/HynekPetrak/javascript-malware-collection)

[SPTH Repository](https://github.com/SPTHvx/SPTH)
