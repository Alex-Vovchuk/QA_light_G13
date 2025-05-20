from src.services.base import ApiService


class UsersService(ApiService):

    def get_users_list(self):
        return self.get('/users', )

    def get_user(self, user_id):
        return self.get(path=f'/users/{user_id}', headers=self.headers)

    def create_user(self, json):
        return self.post('/users', json=json)
