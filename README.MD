# Music Recommendation Engine

This project is an application that offers song suggestions based on users' music preferences. It provides personalized music recommendations based on users' favorite music genres.

## Features

- **Music Suggestions:** Offers song suggestions based on the user's favorite music genres.
- **User Profile:** Saves and updates the user's music preferences and favorite genres.
- **Simple Web Interface:** Allows users to enter user ID to get recommendations.

## Requirements

- Python 3.7+
-Flask
- A music data source (API or database)

## Setup

1. Install requirements:
    ```bash
    pip install flask
    ```

2. Start the server:
    ```bash
    python backend/app.py
    ```

3. Go to the web interface: `http://localhost:5000`

## Use

- Use the `/user-profile/<user_id>` endpoint to get the user profile.
- Use the `/user-profile/<user_id>` endpoint with the `PUT` method to update the user profile.
- Use the `/recommendations` endpoint with the `POST` method to get music recommendations.

## Contributors

- Eymen

## Licence

This project is licensed under the [MIT License](LICENSE).