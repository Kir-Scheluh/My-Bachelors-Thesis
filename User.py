import datetime
import hashlib
import numpy as np
import pandas as pd
import file_encryption as fe


class User:
    def __init__(self, login, password):
        self.login = hashlib.md5(login.encode()).hexdigest()
        self.password = hashlib.md5(password.encode()).hexdigest()
        self.key = fe.load_key()
        self.__is_authorized, self.__is_admin = self.check_login_info()

    @property
    def is_authorized(self):
        return self.__is_authorized

    @property
    def is_admin(self):
        return self.__is_admin

    def check_login_info(self, path_to_df="users_info.csv"):
        is_authorized = False
        is_admin = False

        fe.file_decrypt(path_to_df, self.key)
        df = pd.read_csv(path_to_df)
        fe.file_encrypt(path_to_df, self.key)
        # TODO: добавить разные сообщения об ошибках
        for index, row in df.iterrows():
            if row['login'] == self.login:
                if row['password'] == self.password:
                    if datetime.datetime.strptime(row['ttl'], '%Y-%m-%d').date() > datetime.date.today():
                        is_authorized = True
                        is_admin = row['is_admin']
        return is_authorized, is_admin

    def create_user(self, path_to_df="users_info.csv"):
        # TODO: добавить сообщение об отказе в правах
        if not (self.__is_authorized and self.__is_admin):
            return

        fe.file_decrypt(path_to_df, self.key)
        df = pd.read_csv(path_to_df)
        fe.file_encrypt(path_to_df, self.key)
        login = hashlib.md5(input('Введите логин').encode()).hexdigest()
        for index, row in df.iterrows():
            if row['login'] == login:
                print("Такой логин уже существует!")
                return
        password = hashlib.md5(input('Введите пароль').encode()).hexdigest()
        roots = input('Права администратора [true/false]')
        ttl = input('Введите срок жизни учетной записи [%Y-%m-%d]')

        new_row = pd.DataFrame({'login': [login], 'password': [password], 'is_admin': [roots], 'ttl': [ttl]})
        df = pd.concat([df, new_row], ignore_index=True)

        #df.loc[len(df.index)] = [login, password, roots, ttl]
        fe.file_decrypt(path_to_df, self.key)
        df.to_csv(path_to_df)
        fe.file_encrypt(path_to_df, self.key)

    def delete_user(self, path_to_df="users_info.csv"):
        is_deleted = False
        if not (self.__is_authorized and self.__is_admin):
            return
        login = hashlib.md5(input('Введите логин').encode()).hexdigest()
        fe.file_decrypt(path_to_df, self.key)
        df = pd.read_csv(path_to_df)
        fe.file_encrypt(path_to_df, self.key)
        for index, row in df.iterrows():
            if row['login'] == login:
                df = df.drop(np.where(df['login'] == login)[0])
                is_deleted = True
        df.to_csv(path_to_df)
        fe.file_encrypt(path_to_df, self.key)
        return is_deleted
