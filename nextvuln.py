import sqlite3

def get_user_by_username(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # WARNING: This line is vulnerable to SQL injection!
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    result = cursor.fetchall()
    conn.close()
    return result

# Example usage (attacker input)
print(get_user_by_username("admin' OR '1'='1"))
