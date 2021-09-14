import os

def main(port=8000):
    os.system('rm db.sqlite3')
    os.system('python manage.py makemigrations')
    os.system('python manage.py migrate --run-syncdb')
    os.system(f'python manage.py runserver {port}')

if __name__ == '__main__':
    main()
