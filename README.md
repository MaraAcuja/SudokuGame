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
It already comes with one first easy sudoku. Furthermore, it includes functionality to check if the Sudoku is solved correctly or, for the lazy ones, to let the Sudoku be solved automatically.

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

### 2 DDD

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

### 5 Build Management
is made with pyb
### 6 Unit-Tests

### 7 Continuous Delivery
is made with travis - ci
### 8 IDE

### 9 DSL

### 10 Functional Programming

Allover this project I tried to use as much as functional programming as possible. Below, there are some links to examples for the implementation:
1. Final data structures user_output.py
2. Side-effect-free functions user_output.py
3. Higher-order functions
4. Closured / anonymous functions