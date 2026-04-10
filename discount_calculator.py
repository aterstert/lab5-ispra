def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Рассчитывает итоговую цену товара с учётом скидки.

    Аргументы:
        price (float): Исходная цена товара.
        discount_percent (float): Процент скидки.

    Возвращает:
        float: Итоговая цена после применения скидки.

    Вызывает:
        ValueError: Если цена или процент скидки имеют недопустимые значения.
    """
    # Проверка корректности входных данных
    if price < 0:
        raise ValueError("Цена не может быть отрицательной")
    if discount_percent < 0:
        raise ValueError("Процент скидки не может быть отрицательным")
    if discount_percent > 100:
        raise ValueError("Процент скидки не может превышать 100%")
    
    # Расчёт итоговой цены
    discounted_price = price * (1 - discount_percent / 100)
    return round(discounted_price, 2) # Округление до копеек
