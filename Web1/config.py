db = {
    'user'     : 'root',
    'password' : '7148',
    'host'     : 'localhost',
    'port'     : '3306',
    'database' : 'klas'
}


DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8" 