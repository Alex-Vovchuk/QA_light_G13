user_data = {
    'name': "Alex",
    'age': 60,
    'phone': 354536787,
}


class TestCreation:

    def test_add_(self, get_connection, delete_user):
        # Creating player by API
        player_service = PlayerService()
        request = player_service.post_player()
        assert request.status_code == 200

        # DB checking
        conn = get_connection
        cursor = conn.cursor()
        my_results = cursor.execute('SELECT * FROM users').fetchall()
        my_result = cursor.execute('SELECT * FROM users WHERE phone = ').fetchall()

        assert any(user_data['phone'] in tup for tup in my_results)









        # conn = get_connection
        # cursor = conn.cursor()
        # cursor.execute('INSERT INTO users (name, age, phone) VALUES (?, ? ,?)',
        #                (user_data['name'], user_data['age'], user_data['phone'])
        #                )
        # conn.commit()
        #
        # my_results = cursor.execute('SELECT * FROM users').fetchall()
        # my_result = cursor.execute('SELECT * FROM users WHERE phone = ').fetchall()
        #
        # assert any(user_data['phone'] in tup for tup in my_results)

