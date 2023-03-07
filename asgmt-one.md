# Assignment 1

> Programming Design 2023

## 01. Define a function `calculate_movie_minutes()` which returns the time of a movie in minutes given hours and minutes.

```python
def calculate_movie_minutes(hours: int, mins: int) -> int:
    """
    >>> calculate_movie_minutes(2, 22) # The Shawshank Redemption
    142
    >>> calculate_movie_minutes(2, 55) # The Godfather
    175
    >>> calculate_movie_minutes(2, 32) # The Dark Knight
    152
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 02. Define a function `convert_kilometers_to_miles()` which converts kilometers to miles given a distance in kilometers.

$$
1 \; \text{km} = 0.621371192 \; \text{mile}
$$

```python
def convert_kilometers_to_miles(km: float) -> float:
    """
    >>> convert_kilometers_to_miles(42.195) # a full marathon
    26.21875744644
    >>> convert_kilometers_to_miles(21.095) # a half marathon
    13.10782529524
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 03. Define a function named `calculate_bmi()` which calculates BMI given heights in centimeters and weights in kilograms.

$$
\text{BMI} = \frac{\text{weight}_{\text{kg}}}{\text{height}_{\text{m}}^2}
$$

```python
def calculate_bmi(height: int, weight: int) -> float:
    """
    >>> calculate_bmi(216, 147) # Shaquille O'Neal in his prime
    31.507201646090532
    >>> calculate_bmi(206, 113) # LeBron James
    26.628334433028563
    >>> calculate_bmi(211, 110) # Giannis Antetokounmpo
    24.70744143213315
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 04. Define a function `format_movie_time()` which returns the time of a movie in text format given hours and minutes.

```python
def format_movie_time(hours: int, mins: int) -> str:
    """
    >>> format_movie_time(2, 22) # The Shawshank Redemption
    '2 hours 22 minutes'
    >>> format_movie_time(2, 55) # The Godfather
    '2 hours 55 minutes'
    >>> format_movie_time(2, 32) # The Dark Knight
    '2 hours 32 minutes'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 05. Define a function `format_temperature_degrees()` which returns Fahrenheit degrees in text format given Celsius degrees.

$$
\text{Fahrenheit}^{\circ} \text{F} = \text{Celsius}^{\circ} \text{C} \times \frac{9}{5} + 32
$$

```python
def format_temperature_degrees(celsius: int) -> str:
    """
    >>> format_temperature_degrees(0)
    '0 Degrees Celsius = 32.0 Degrees Fahrenheit'
    >>> format_temperature_degrees(100)
    '100 Degrees Celsius = 212.0 Degrees Fahrenheit'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 06. Define a function `format_integer_with_dollar_sign_and_commas()` which returns a comma format with dollar sign given an integer.

```python
def format_integer_with_dollar_sign_and_commas(x: int) -> str:
    """
    >>> format_integer_with_dollar_sign_and_commas(1000)
    '$1,000'
    >>> format_integer_with_dollar_sign_and_commas(1000000)
    '$1,000,000'
    >>> format_integer_with_dollar_sign_and_commas(1000000000)
    '$1,000,000,000'
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 07. Define a function `is_positive()` which returns whether input is a positive integer or not.

```python
def is_positive(x: int) -> bool:
    """
    >>> is_positive(-1)
    False
    >>> is_positive(0)
    False
    >>> is_positive(1)
    True
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 08. Define a function `is_even()` which returns whether input is an even number or not.

```python
def is_even(x: int) -> bool:
    """
    >>> is_even(0)
    True
    >>> is_even(1)
    False
    >>> is_even(2)
    True
    >>> is_even(3)
    False
    >>> is_even(4)
    True
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 09. Define a function `are_vowels_contained()` which returns whether input text contains one of the vowels: a, e, i, o, u.

```python
def are_vowels_contained(x: str) -> bool:
    """
    >>> are_vowels_contained('pythn')
    False
    >>> are_vowels_contained('ncnd')
    False
    >>> are_vowels_contained('rtclt')
    False
    >>> are_vowels_contained('python')
    True
    >>> are_vowels_contained('anaconda')
    True
    >>> are_vowels_contained('reticulate')
    True
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```

## 10. Define a function `are_all_vowels_contained()` which returns whether input text contains all the vowels: a, e, i, o, u.

```python
def are_all_vowels_contained(x: str) -> bool:
    """
    >>> are_all_vowels_contained('python')
    False
    >>> are_all_vowels_contained('anaconda')
    False
    >>> are_all_vowels_contained('reticulate')
    False
    >>> are_all_vowels_contained('anaconda and reticulate')
    True
    """
    ### BEGIN SOLUTION
    
    ### END SOLUTION
```