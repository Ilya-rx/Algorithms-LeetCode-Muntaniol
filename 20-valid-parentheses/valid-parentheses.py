class Solution:
    def isValid(self, s: str) -> bool:
        stack = []  # создаем пустой стек

        for char in s:
            # если открывающая скобка
            if char == '(' or char == '[' or char == '{':
                stack.append(char)

            else:
                # если стек пуст — ошибка
                if not stack:
                    return False

                top = stack.pop()  # берем последний элемент

                # проверяем соответствие
                if char == ')' and top != '(':
                    return False
                if char == ']' and top != '[':
                    return False
                if char == '}' and top != '{':
                    return False

        # если стек пуст — всё ок
        return len(stack) == 0