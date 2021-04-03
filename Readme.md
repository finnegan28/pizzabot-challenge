# Pizzabot

Pizzabot is a robot that delivers pizza. Given a grid and a set of delivery co-ordinates
pizzabot will return a set of instructions for getting to those locations and delivering a fresh pizza

Pizzabot always starts at the origin point, (0, 0).

Given the following input string: 5x5 (1, 3) (4, 4) one correct solution would be: ENNNDEEEND.

In other words: move east once and north thrice; drop a pizza; move east thrice and north once; drop a final pizza.

## Installation

Please ensure you have Python3 installed on your device and that python has been added to your OS Path.

## Usage

To use Pizzabot you should use the command below.

A valid grid should be two numbers separated by an 'X'.

Both numbers must be greater than 0.

Valid delivery co-ordinates should be enclosed by brackets '( )' and separated by a comma only ','.

There should be no spaces within the brackets.


```
python pizzabot.py 5x5 (1,3) (4,4)
```

### Possible Issue
When testing Pizzabot on macOS, I noticed you need to surround each set of co-ordinates
with single quotes.
```
python pizzabot.py 5x5 '(1,3)' '(4,4)'
```


## Tests
There is a test suite included with this release of Pizzabot. These tests can be run via the command below.

```
python tests.py
```