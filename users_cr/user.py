from mysqlconnection import connectToMySQL

class User:
    db = 'users_cr'
    def __init__( self , data ) -> None:
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
            
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        print("These are the results", results)
        for user in results:
            users.append(cls(user))
        return users
    
    @classmethod
    def create_user(cls,data):
        query = """INSERT INTO users (first_name, last_name, email, created_at, updated_at)
        VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"""
        return connectToMySQL('users_cr').query_db(query, data)