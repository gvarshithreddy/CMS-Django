# CMS-Django Project

Welcome to the CMS-Django project! This is a Django-based content management system that requires Python 3.6 or greater and a MySQL server. Follow the steps below to set up and run the project on your local machine.

## Prerequisites

- **Python 3.6 or greater**
- **MySQL server**

## Getting Started

1. **Clone the Repository**

   First, clone the repository using Git:

   ```bash
   git clone https://github.com/gvarshithreddy/CMS-Django.git
   ```

2. **Navigate to the Project Directory**

   Change directory to the cloned project folder:

   ```bash
   cd CMS-Django
   ```

3. **Install Dependencies**

   Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up the MySQL Database**

   - **Create a Database:**

     Log in to your MySQL server and create a new database. For example:

     ```sql
     CREATE DATABASE cms_db;
     ```

   - **Update Database Settings:**

     Open the `settings.py` file located in the `CMS` folder and configure the `DATABASES` setting with your database name, username, and password. It should look something like this:

     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.mysql',
             'NAME': '<database name>',
             'USER': '<username>',
             'PASSWORD': '<password>',
             'HOST': 'localhost',
             'PORT': '3306',
         }
     }
     ```

5. **Run Migrations**

   Apply the database migrations to set up your database schema:

   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser**

   Create a superuser account to manage the site. Follow the prompts to enter a username, email, and password:

   ```bash
   python manage.py createsuperuser
   ```

7. **Run the Development Server**

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

   Visit the URL provided in the terminal (typically `http://127.0.0.1:8000/`) in your web browser.

8. **Log In to Admin Interface**

   Go to the login page of the site and log in with the superuser credentials you created. You can now manage the database and the CMS features from the admin interface.

## Troubleshooting

- **Database Connection Issues:** Ensure that MySQL is running and that the credentials in `settings.py` are correct.
- **Missing Dependencies:** Verify that all required packages are installed. You can update them using `pip` if needed.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or issues, please reach out to [gvarshithreddy](https://github.com/gvarshithreddy) on GitHub.

---

Happy coding!
