
class UnknownOperationError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Не знаю операции {self.value}"


class MyValueError(ValueError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value} не является числом"


class Complex:
    real = None
    im = None

    def __init__(self, real=0.0, im=0.0):
        self.set_numb(real, im)

    def set_numb(self, real, im):
        try:
            self.real = float(real)
        except ValueError:
            raise MyValueError(real)

        try:
            self.im = float(im)
        except ValueError:
            raise MyValueError(im)

    def get_real(self):
        return self.real

    def get_im(self):
        return self.im

    def __str__(self):
        if self.im:
            return f"Result = {self.real:g} + {self.im:g}i"
        return f"Result = {self.real:g}"


def add(a: Complex, b: Complex):
    c = Complex(a.get_real() + b.get_real(), a.get_im() + b.get_im())
    print(c)


def substr(a: Complex, b: Complex):
    c = Complex(a.get_real() - b.get_real(), a.get_im() - b.get_im())
    print(c)


def div(a: Complex, b: Complex):
    x1 = a.get_real()
    x2 = b.get_real()
    y1 = a.get_im()
    y2 = b.get_im()
    c = Complex(
        (x1 * x2 + y1 * y2) / (x2 ** 2 + y2 ** 2),
        (x2 * y1 - x1 * y2) / (x2 ** 2 + y2 ** 2),
    )
    if x2 ** 2 + y2 ** 2 == 0:
        raise ZeroDivisionError
    print(c)


def multi(a: Complex, b: Complex):
    x1 = a.get_real()
    x2 = b.get_real()
    y1 = a.get_im()
    y2 = b.get_im()
    c = Complex(x1 * x2 - y1 * y2, x1 * y2 + y1 * x2)
    print(c)


a = Complex()
b = Complex()

while True:
    try:
        a.set_numb(
            input("Введите действительную часть первого числа: "),
            input("Введите мнимую часть первого числа: "),
        )

        while True:
            try:
                s = str(input("Выберете операцию: +, -, *, / : "))
                if s not in ALLOWED_OPERATIONS:
                    raise UnknownOperationError

                b.set_numb(
                    input("Введите действительную часть второго числа: "),
                    input("Введите мнимую часть второго числа: "),
                )

                if s == "+":
                    add(a, b)
                elif s == "-":
                    substr(a, b)
                elif s == "*":
                    multi(a, b)
                elif s == "/":
                    div(a, b)

            except ZeroDivisionError:
                print("Нельзя делить на ноль. Выберите другую операцию")
            except UnknownOperationError as e:
                print(e)
            except MyValueError as e:
                print(e)

            choice = input("Хотите продолжить? (y/n): ")
            if choice.lower() != "y":
                break

    except MyValueError as e:
        print(e)
        choice = input("Хотите продолжить? (y/n): ")
        if choice.lower() != "y":
            break
