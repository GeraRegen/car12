# generate_html.py
import webbrowser
# Определяем содержимое HTML-файла
html_content = """
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Тачки</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f0f0f0;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #e38d2b;
            color: white;
            padding: 10px 0;
            text-align: center;
        }
        main {
            padding: 20px;
        }
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 10px 0;
            position: fixed;
            bottom: 0;
            width: 100%;
        }
        a {
            color: #007BFF; /* Цвет ссылки */
            text-decoration: none; /* Убираем подчеркивание */
        }
        a:hover {
            text-decoration: underline; /* Подчеркивание при наведении */
        }
    </style>
</head>
<body>
    <header>
        <h1>Топ 10 машин</h1>
    </header>
    <main>
        <p style="text-align: center;"><a href="https://www.jetbrains.com/pycharm/">BMW M5 F90</a> - $36 800</p>
        <img src="Z:/image.PyCharm/car.py/BMW M5 F90.jpg" alt="BMW M5 F90">
        
        <p style="text-align: center;"><a href="https://www.jetbrains.com/pycharm/">Mercedes 63 S AMG</a> - $45 000</p>
        <img src="Z:/image.PyCharm/car.py/Mercedes 63 S AMG.jpg" alt="Mercedes 63 S AMG">
        
    </main>
    <footer>
        <p>Gera_Regen</p>
    </footer>
</body>
</html>
"""

# Записываем HTML-код в файл
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML-файл успешно создан!")