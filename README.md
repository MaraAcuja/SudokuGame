# A Simple Sudoku Game
## Overview over Metrics 

[![Build](https://app.travis-ci.com/MaraAcuja/SudokuGame.svg?branch=main)](https://app.travis-ci.com/MaraAcuja/SudokuGame.svg?branch=main)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=MaraAcuja_SudokuGame&metric=bugs)](https://sonarcloud.io/summary/new_code?id=MaraAcuja_SudokuGame)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=MaraAcuja_SudokuGame&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=MaraAcuja_SudokuGame)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=MaraAcuja_SudokuGame&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=MaraAcuja_SudokuGame)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=MaraAcuja_SudokuGame&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=MaraAcuja_SudokuGame)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=MaraAcuja_SudokuGame&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=MaraAcuja_SudokuGame)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=MaraAcuja_SudokuGame&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=MaraAcuja_SudokuGame)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=MaraAcuja_SudokuGame&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=MaraAcuja_SudokuGame)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=MaraAcuja_SudokuGame&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=MaraAcuja_SudokuGame)

## Exercise A for Advanced Software Engineering
### General

This repository contains a simple Sudoku game. It can be played in a shell like a linux terminal. 
It already comes with one first easy Sudoku. Furthermore, it includes functionality to check if the Sudoku is solved correctly or, for the lazy ones, to let the Sudoku be solved automatically.

### Prerequisites

### Handling
1. Clone the repository
2. Install pybuilder
pip install pybuilder
3. Build the project
pyb publish
4. Type in Play
5. Have fun with the small challenge

## Exercise B for Advanced Software Engineering
### 1 UML
Three UML diagrams have been generated for this project. If there are colors involved,
green means that these features have been implemented already. The yellow colors signals
that this will be done in the future. If there are no colors it also means that is already 
implemented.

- The [activity diagram](https://github.com/MaraAcuja/SudokuGame/blob/main/tasks/activity_diagram.png) shows the flow between different activities, hence the printed console 
output next to the expected user input.
- The [use case diagram](https://github.com/MaraAcuja/SudokuGame/blob/main/tasks/use_case.png) displays the different real world problems the software should fulfill next
to the different users of this software.
- Last I created a [component diagram](https://github.com/MaraAcuja/SudokuGame/blob/main/tasks/component_diagram_actual.png) to show the different components of the 
project. I also created a [component diagram including the funding of Edlich Investments](https://github.com/MaraAcuja/SudokuGame/blob/main/tasks/component_diagram_planned.png).

### 2 DDD
While planning the project I created a [problem space](https://github.com/MaraAcuja/SudokuGame/blob/main/tasks/ddd_problem_space.png) with several different 
subdomains and components which have to be implemented. Some are already implemented,
(green) some have to be implemented in the future (yellow).
Furthermore, I created a [glossary](https://github.com/MaraAcuja/SudokuGame/blob/main/tasks/ubiquitous_language.pdf) to specify the domain specific ubiquitous 
language.

### 3 Metrics
To get good metrics I used SonarQube which analyses the provided source code
automatically on different metrics. SonarQube also offers an online version
which I connected directly with my github repository. Each time I conduct a pull or a push
the code base is analysed again to keep the metrics always up-to-date.

For a better visual identification I used badges to show the results of the 
metrics on one sight. The following metrics were used:

 - Bugs: &emsp; &emsp;&emsp;&emsp; &nbsp;[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=MaraAcuja_SudokuGame&metric=bugs)](https://sonarcloud.io/summary/new_code?id=MaraAcuja_SudokuGame)
 - Code smells:     &emsp;&nbsp;&nbsp;[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=MaraAcuja_SudokuGame&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=MaraAcuja_SudokuGame)
 - Lines of Code:   &emsp;[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=MaraAcuja_SudokuGame&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=MaraAcuja_SudokuGame)
 - Maintainability: &nbsp;&nbsp; [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=MaraAcuja_SudokuGame&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=MaraAcuja_SudokuGame)
 - Security Rating: &nbsp; [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=MaraAcuja_SudokuGame&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=MaraAcuja_SudokuGame)
 - Technical debt: &emsp;[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=MaraAcuja_SudokuGame&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=MaraAcuja_SudokuGame)
 - Vulnerabilities: &emsp; [![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=MaraAcuja_SudokuGame&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=MaraAcuja_SudokuGame)
 - Reliability: &emsp; &emsp;&nbsp;&nbsp; [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=MaraAcuja_SudokuGame&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=MaraAcuja_SudokuGame)

An overview over the whole SonarCloud analysis can be found [here](https://sonarcloud.io/summary/overall?id=MaraAcuja_SudokuGame).


### 4 Clean Code Development
[Here](https://github.com/MaraAcuja/SudokuGame/blob/main/tasks/cheat_sheet.py) is the cheat sheet with my most important code principles. As the whole
project is written completely in Python I decided to write also the cheat sheet in 
Python. This is good for testing my clean code principles as for showing some special
features like the TODO coloring in yellow.

Below are five examples where I used my cheat sheet referring to the numbers in the cheat sheet.

- Using verbs for functions as they do a task (cheat sheet #1): [solve_sudoku()](https://github.com/MaraAcuja/SudokuGame/blob/main/src/main/python/sudoku_logic.py#L32)

- Use comments for complicated structures like the not directly intuitive recursive
solving algorithm (cheat sheet #11): [solve_sudoku()](https://github.com/MaraAcuja/SudokuGame/blob/main/src/main/python/sudoku_logic.py#L47)

- Don't write duplicates if a function is called several times. The test_sudoku() function
is called within the solve_sudoku as also in main function. So it is not written twice. Both calls 
refer to the [test_sudoku()](https://github.com/MaraAcuja/SudokuGame/blob/main/src/main/python/sudoku_logic.py#L5)
(cheat sheet #5)

- Each function should have one task. As the test_sudoku() tests several cases, they were
split into different logic parts and therefore in closures (cheat sheet #3 + #4): [test_sudoku()](https://github.com/MaraAcuja/SudokuGame/blob/main/src/main/python/sudoku_logic.py#L5)

- Use multiline statements, in this specific case I did a new line for each
loop to also have the chance to comment why the loop is necessary (cheat sheet #2): [is_same_element_in_squares()](https://github.com/MaraAcuja/SudokuGame/blob/main/src/main/python/sudoku_logic.py#L17)


### 5 Build Management
The build management is done with pybuilder. It is the first time that I configured a build 
management tool myself. Before of it I was not convinced if the additional work in setting it 
up really benefits. But as I now don't have to build all the necessary files myself or to 
document which files have to be build in which order, I am convinced that the additional effort is 
worth.

[Here](https://github.com/MaraAcuja/SudokuGame/blob/main/build.py) is my build file.

### 6 Unit-Tests

### 7 Continuous Delivery
For the continuous delivery pipeline I used Travis CI. In combination with pybuilder it is very 
convenient to use. Every time I push to my repository a new build is triggered. 

[Here](https://app.travis-ci.com/github/MaraAcuja/SudokuGame) 
is the corresponding website for the CD management.

[![Build](https://app.travis-ci.com/MaraAcuja/SudokuGame.svg?branch=main)](https://app.travis-ci.com/MaraAcuja/SudokuGame.svg?branch=main)

A badge was included to always show the status of the last build process.
Also a [screenshot](https://github.com/MaraAcuja/SudokuGame/blob/main/tasks/travis-ci.png) was added to show the result of the Travis CI-website.

### 8 IDE

I chose PyCharm as IDE. Before, I always used Microsoft Visual Studio as IDE as I knew it 
from my Bachelors. But after I decided to try out Python a bit more and not C, I decided
to also change the IDE this time. Smaller projects in Python I completed in Python IDLE in
the past. But after I heard of PyCharm I wanted to try this one out also for a bigger project.

And I am very happy with my choice as PyCharm includes all features like easy refactoring, 
a clear structured project organisation, an integrated git plugin for pulling, commiting and 
pushing, a terminal and most important auto-completion.

My favorite shortcuts are:

- Ctrl + Shift + F10: For running a single python file. This was very useful before the implementation of pybuilder.
- Hitting TAB: For auto-completion when typing a variable or function name.
- Hitting Shift twice: For searching within the whole project for a variable, a string or a function.

### 9 DSL
DSLs are still missing in the actual version cause we didn't cover the topic in the lectures yet.

### 10 Functional Programming

All over this project I tried to use as much as functional programming as possible. Below, there are some links to examples for the implementation:
1. Final data structures: [user_output.py](https://github.com/MaraAcuja/SudokuGame/blob/main/src/main/python/user_output.py)
2. Side-effect-free functions: [user_output.py](https://github.com/MaraAcuja/SudokuGame/blob/main/src/main/python/user_output.py)
3. Closured / anonymous functions: [sudoku_logic.py](https://github.com/MaraAcuja/SudokuGame/blob/main/src/main/python/sudoku_logic.py)