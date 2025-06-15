import sqlite3


def get_user_by_name(username):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # Vulnerable to SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

 

def get_user_by_email(email):
    conn = sqlite3.connect('example.db')
    cursor = conn.cursor()
    # Vulnerable to SQL Injection
    query = f"SELECT * FROM users WHERE email = '{email}'"
    cursor.execute(query)
    result = cursor.fetchall()
    conn.close()
    return result

 

if __name__ == "__main__":
    for ns in namespaces_without_netpol():
        print(ns)
    # Simulated usage of SQL injection vulnerability
    print("\nSimulated SQL Injection Test:")
    malicious_input = "' OR '1'='1"
    #test
    results = get_user_by_name(malicious_input)
    print(f"Results for injected username {malicious_input!r}: {results}")
    email_sqli = get_user_by_email("avi@gmail.com")
    username_sqli = get_user_by_name("testname")

