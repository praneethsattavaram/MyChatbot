README FILE FOR FIRSTCHATBOT

# Django Chatbot Project

This project is a simple web application built with Django, featuring a chatbot functionality using the OpenAI GPT-3.5 model. Users can interact with the chatbot, register, and log in to the system.

## Getting Started

To run this project locally, follow these steps:

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/django-chatbot-project.git
   ```

2. Navigate to the project directory:
   ```bash
   cd django-chatbot-project
   ```

3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/Mac
   .\venv\Scripts\activate   # For Windows
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Access the application in your web browser at `http://127.0.0.1:8000/`

## Features

- **Chatbot:** Interact with the OpenAI GPT-3.5 powered chatbot.
- **Login and Registration:** Users can register for an account and log in to access the chatbot functionality.
- **User Authentication:** Built-in user authentication system using Django's authentication framework.

## Project Structure

- `chatbot_app/`: Django app containing the chatbot functionality.
- `templates/`: HTML templates for rendering the frontend.
- `static/`: Static files such as CSS stylesheets and JavaScript files.
- `openai_api_key.py`: Store your OpenAI API key in this file (not included in the repository for security reasons).

## Technologies Used

- Python (Django)
- HTML/CSS
- OpenAI API


## Contributing

Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---
