
class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
    
    def register(self):
        return "Регистрация пользователя"
    
    
    def auth(self):
        return f"Авторизация пользователя {self.login}"


user1 = User(input("Введите логин: "), input("Введите пароль: "))
print(user1.auth())


