def count_cakes(recipe, available):
    """
    Рассчитывает максимальное количество тортов, которое можно приготовить на основе рецепта и доступных ингредиентов.

    Аргументы:
    - рецепт (dict): Словарь, представляющий необходимое количество каждого ингредиента для одного торта.
    - доступно (dict): Словарь, представляющий доступные количества каждого ингредиента.

    Возвращает:
    - int: Максимальное количество тортов, которое можно приготовить на основе имеющихся ингредиентов.
        Если какой-либо из необходимых ингредиентов отсутствует, функция возвращает 0.

    Вызывает исключение:
    - ZeroDivisionError: Если количество любого из ингредиентов в рецепте равно 0, возникает это исключение.

    Пример:
    >>> cakes({'flour': 500, 'sugar': 200, 'eggs': 1}, {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200})
    2

    В приведенном выше примере муки достаточно для приготовления 2 тортов, сахара - 6, яиц - 5, поэтому максимальное количество тортов, которое можно испечь, равно 2.
    """

    # проверяем наличие всех ингредиентов доступных из рецепта
    for ingredient in recipe:
        if ingredient not in available:
            return 0

    # рассчитываем максимальное количество тортов, которое можно приготовить из каждого ингредиента
    num_cakes = []
    for ingredient, amount in recipe.items():
        if amount == 0:
            raise ZeroDivisionError(f"Ошибка: Ингридиент {ingredient} в рецепте имеет нулевое значение.")
        else:
            num_cakes.append(available[ingredient] // amount)

    # возвращает минимальное количество тортов, которые можно приготовить на основе имеющихся ингредиентов
    return min(num_cakes)