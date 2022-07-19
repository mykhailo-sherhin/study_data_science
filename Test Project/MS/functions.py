import pandas as pd
import numpy as np


def outliers_iqr(data, feature, log_scale=False, left=1.5, right=1.5, log_add=1):
    """
    Функция принимает на вход DataFrame и признак, по которому ищутся выбросы, а затем возвращает потенциальные выбросы,
    найденные с помощью метода Тьюки (межквартильного размаха), и очищенный от них датасет.
    
    Параметры left и right, которые задают число IQR влево и вправо от границ ящика (пусть по умолчанию они равны 1.5).
    В дополнение добавим в функцию возможность работы в логарифмическом масштабе: для этого введём аргумент log_scale.
    Если он равен True, то будем логарифмировать рассматриваемый признак, иначе — оставляем его в исходном виде.
    Метод по умолчанию работает для нормального распределения признака, если распределение другое, параметры left и right могут помочь.
    
    Для использования функции нужна библиотека numpy.
    """
    if log_scale:
        x = np.log(data[feature] + log_add)
    else:
        x = data[feature]
    quartile_1, quartile_3 = x.quantile(0.25), x.quantile(0.75),
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * left)
    upper_bound = quartile_3 + (iqr * right)
    outliers = data[(x<lower_bound) | (x> upper_bound)]
    cleaned = data[(x>lower_bound) & (x < upper_bound)]
    return outliers, cleaned


def outliers_z_score(data, feature, log_scale=False, left=3, right=3, log_add=1):
    """
    Функция на вход она принимает DataFrame и признак, по которому ищутся выбросы. Метод Z-отклонений (метод сигм).
    В дополнение добавим в функцию возможность работы в логарифмическом масштабе: для этого введём аргумент log_scale.
    Если он равен True, то будем логарифмировать рассматриваемый признак, иначе — оставляем его в исходном виде.
    
    Параметры left и right, которые будут задавать число сигм (стандартных отклонений) влево и вправо соответственно, которые определяют границы метода z-отклонения.
    Метод по умолчанию работает для нормального распределения признака, если распределение другое, параметры left и right могут помочь.

    Для использования функции нужна библиотека numpy.
    """
    if log_scale:
        x = np.log(data[feature] + log_add)
    else:
        x = data[feature]
    mu = x.mean()
    sigma = x.std()
    lower_bound = mu - left * sigma
    upper_bound = mu + right * sigma
    outliers = data[(x < lower_bound) | (x > upper_bound)]
    cleaned = data[(x > lower_bound) & (x < upper_bound)]
    return outliers, cleaned


def low_information_columns(data, thresh=0.95):
    """
    Функция принимает на вход DataFrame и порог, по которым ищутся неинформативные признаки (в которых все значения уникальны или одинаковы).
    Результат - список неинформативных колонок
    """
    #список неинформативных признаков
    low_information_cols = []

    #цикл по всем столбцам
    for col in data.columns:
        #наибольшая относительная частота в признаке
        top_freq = data[col].value_counts(normalize=True).max()
        #доля уникальных значений от размера признака
        nunique_ratio = data[col].nunique() / data[col].count()
        # сравниваем наибольшую частоту с порогом
        if top_freq > thresh:
            low_information_cols.append(col)
            #print(f'{col}: {round(top_freq*100, 2)}% одинаковых значений')
        # сравниваем долю уникальных значений с порогом
        if nunique_ratio > thresh:
            low_information_cols.append(col)
            #print(f'{col}: {round(nunique_ratio*100, 2)}% уникальных значений')
    return low_information_cols