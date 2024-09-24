import os


def main():
    """Execute the command lines and fill-in the database"""
    os.system('python manage.py create_users')
    os.system('python manage.py create_courses')
    os.system('python manage.py create_lessons')
    os.system('python manage.py fill_payments')
    os.system('python manage.py create_moderators')


main()