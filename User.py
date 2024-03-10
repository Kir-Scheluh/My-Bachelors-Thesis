import datetime

import numpy as np
import pandas as pd

import file_encryption as fe


# DF: login[str(hash)], password[str(hash)], is_admin[bool], ttl[str(yyyy-mm-dd)]]

class User:
    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.key = fe.load_key()
        self.__is_authorized, self.__is_admin = self.check_login_info()
    @property
    def is_authorized(self):
        return self.__is_authorized
    def check_login_info(self, path_to_df="users_info.csv"):
        is_authorized = False
        is_admin = False

        fe.file_decrypt(path_to_df, self.key)
        df = pd.read_csv(path_to_df)
        fe.file_encrypt(path_to_df, self.key)

        for index, row in df.iterrows():
            if row['login'] == self.login:
                if row['password'] == self.password:
                    if datetime.datetime.strptime(row['ttl'], '%Y-%m-%d').date() > datetime.date.today():
                        is_authorized = True
                        is_admin = row['is_admin']
        return is_authorized, is_admin

    def create_user(self, path_to_df="users_info.csv"):
        if not (self.__is_authorized and self.__is_admin):
            return

        fe.file_decrypt(path_to_df, self.key)
        df = pd.read_csv(path_to_df)
        login = input('Введите логин')
        for index, row in df.iterrows():
            if row['login'] == login:
                print("Такой логин уже существует!")
        password = input('Введите пароль')
        roots = input('Права администратора [true/false]')
        ttl = input('Введите срок жизни учетной записи [%Y-%m-%d]')

        df.loc[len(df.index)] = [login, password, roots, ttl]
        df.to_csv(path_to_df)
        fe.file_encrypt(path_to_df, self.key)

    def delete_user(self, path_to_df="users_info.csv"):
        is_deleted = False
        if not (self.__is_authorized and self.__is_admin):
            return
        login = input('Введите логин')
        fe.file_decrypt(path_to_df, self.key)
        df = pd.read_csv(path_to_df)
        for index, row in df.iterrows():
            if row['login'] == self.login:
                df = df.drop(np.where(df['login'] == login)[0])
                is_deleted = True
        df.to_csv(path_to_df)
        fe.file_encrypt(path_to_df, self.key)
        return is_deleted
