# Определяем цвета для каждого номера
colors = {
    0: 'green',
    1: 'red',
    2: 'black',
    3: 'red',
    4: 'black',
    5: 'red',
    6: 'black',
    7: 'red',
    8: 'black',
    9: 'red',
    10: 'black',
    11: 'red',
    12: 'black',
    13: 'red',
    14: 'black',
    15: 'red',
    16: 'black',
    17: 'red',
    18: 'black',
    19: 'red',
    20: 'black',
    21: 'red',
    22: 'black',
    23: 'red',
    24: 'black',
    25: 'red',
    26: 'black',
    27: 'red',
    28: 'black',
    29: 'red',
    30: 'black',
    31: 'red',
    32: 'black',
    33: 'red',
    34: 'black',
    35: 'red',
    36: 'black',
}


def generate_html(num, cols):
    html = '''
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Поле Рулетки 3 на 12</title>
        <style>
            body {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                background-color: #2c3e50;
            }
            .roulette {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                grid-template-rows: repeat(12, 1fr);
                width: 400px;
                height: 600px;
                gap: 5px;
                padding: 10px;
                background-color: #34495e;
                border: 2px solid #e74c3c;
                border-radius: 10px;
            }
            .number {
                display: flex;
                justify-content: center;
                align-items: center;
                font-size: 24px;
                color: white;
                border: 1px solid #fff;
                box-sizing: border-box;
                height: 100%;
            }
        </style>
    </head>
    <body>
        <div class="roulette">
    '''

    # colors[] = 'blue'
    # Добавляем номера и их цвета
    for number in range(0, 37):
        color = cols[number]
        html += f'<div class="number" style="background-color: {color};">{number}</div>'

    html += '''
        </div>
    </body>
    </html>
    '''
    return html
