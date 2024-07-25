if __name__ == '__main__':
    print("Выберите фигуру:", "круг", "треугольник", sep='\n')
    shape = input().lower()
    if shape == 'круг':
        from shapes.circle import Circle
        print("Введите введите радиус круга:")
        radius = float(input())
        circle = Circle(radius)
        print(f"Площадь круга: {circle.area()}")
    elif shape == 'треугольник':
        from shapes.triangle import Triangle
        print("Введите стороны треугольника через пробел:")
        a, b, c = map(float, input().split())
        triangle = Triangle(a, b, c)
        print(f"Площадь треугольника: {triangle.area()}")
        print(f"Треугольник {(triangle.is_right_angled() and 'прямоугольный' or 'непрямоугольный')}")
    else:
        print("Неверная команда")
