# Sauce Demo Purchase Test

## Требования

Для запуска теста необходимы следующие компоненты:

- Python 3.12
- Google Chrome версии 115 или новее
- Установленные зависимости из `requirements.txt`

## Установка

### 1. Клонирование репозитория

Склонируйте репозиторий компьютер:

```bash
git clone https://github.com/default73/saucedemo_test.git
cd saucedemo_test
```

### 2. Создание и активация виртуального окружения

Для Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
Для macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 4. Запуск теста

```bash
python test.py
```
