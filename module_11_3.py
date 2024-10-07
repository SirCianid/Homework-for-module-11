import inspect
import types


def introspection_info(obj):
    info = {}

    # Тип объекта
    info['type'] = type(obj).__name__

    # Атрибуты объекта
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]

    # Методы объекта
    info['methods'] = [attr for attr in dir(obj) if callable(getattr(obj, attr))]

    # Модуль, к которому объект принадлежит
    if hasattr(obj, '__module__'):
        info['module'] = obj.__module__
    else:
        info['module'] = 'built-in'

    # Дополнительные свойства объекта
    if inspect.isclass(obj):
        info['bases'] = [base.__name__ for base in inspect.getmro(obj)[1:]]
    elif inspect.ismodule(obj):
        info['functions'] = [(func[0], func[1]) for func in inspect.getmembers(obj, inspect.isfunction)]

    return info


# Создаем класс
class Introspect:
    def __init__(self, name):
        self.name = name

    def my_method(self):
        print(f'Здравствуй, {self.name}!')


# Создаем объект класса
Introman = Introspect('Братишка')


# Создаем рандомную функцию
def some_function():
    pass


# Создаем динамический модуль
some_module = types.ModuleType('some_module')
some_module.some_variable = 'Дементий, народ требует питонов!'
some_module.some_func = some_function


# Вызываем introspection_info с различными объектами
print(introspection_info(Introman))
print(introspection_info(some_module))
print(introspection_info(42))
print(introspection_info('Я вас категорически приветствую!'))
