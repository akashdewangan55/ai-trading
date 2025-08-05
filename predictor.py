import random

def predict_color_number():
    colors = ['Red', 'Green', 'Violet']
    numbers = list(range(10))
    color = random.choice(colors)
    number = random.choice(numbers)

    if number == 0:
        color = 'Red+Violet'
    elif number == 5:
        color = 'Green+Violet'
    elif number % 2 == 0:
        color = 'Red'
    else:
        color = 'Green'

    return {
        'color': color,
        'number': number,
        'confidence': round(random.uniform(0.6, 0.95), 2)
    }