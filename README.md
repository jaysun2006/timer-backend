# Productivity and Time Entry Rest API Documentation

### Requirements

    Create a RESTful APIs that makes it possible to create and maintain Time Entries.

### Solution

Here is deployed on aws api url

```sh
   http://13.232.218.162
```

### API Lists:

    - Create Timer Entry and listing these

| Task                       | API ENDPOINT                     | REQUESTS TYPE |
| -------------------------- | -------------------------------- | ------------- |
| For listing Time Entry     | <domain>/api/timer/              | GET           |
| For Creating Time Entry    | <domain>/api/timer/              | POST          |
| For details of Time Entry  | <domain>/api/timer/<id>          | GET           |
| For deleting Time Entry    | <domain>/api/timer/              | DELETE        |
| For updating Time Entry    | <domain>/api/timer/<id>          | PUT           |
| For complet the Time Entry | <domain>/api/timer/<id>/complete | PUT           |

### Database architecture:

![alt text](https://bookmanager.s3.us-east-2.amazonaws.com/foo_bar.png)

### Run Locally

If you clone the project and want to run into your local system environment

Here are the steps to run

- Make virtualenv with python 3 or greater version activate and


    ```sh
    $ pip install -r requirements.txt

    ```

- Run the local server


    ```sh
    $ python manage.py makemigrations && python manage.py migrate && python manage.py runserver
    ```

### Project Structure

![alt text](https://bookmanager.s3.us-east-2.amazonaws.com/structure.png)
