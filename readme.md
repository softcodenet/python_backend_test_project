# FastAPI Web Application

This is a FastAPI web application following the MVC design pattern with SQLAlchemy for ORM and Pydantic for validation.

## Endpoints

- **Signup Endpoint**: `/auth/signup`
  - Accepts `email` and `password`.
  - Returns a token (JWT or randomly generated string).

- **Login Endpoint**: `/auth/login`
  - Accepts `email` and `password`.
  - Returns a token upon successful login; error response if login fails.

- **AddPost Endpoint**: `/posts/`
  - Accepts `text` and a `token` for authentication.
  - Validates payload size (limit to 1 MB), saves the post in memory, returning `postID`.
  - Returns an error for invalid or missing token.
  - Dependency injection for token authentication.

- **GetPosts Endpoint**: `/posts/`
  - Requires a token for authentication.
  - Returns all user's posts.
  - Implements response caching for up to 5 minutes for the same user.
  - Returns an error for invalid or missing token.
  - Dependency injection for token authentication.

- **DeletePost Endpoint**: `/posts/{post_id}`
  - Accepts `postID` and a `token` for authentication.
  - Deletes the corresponding post from memory.
  - Returns an error for invalid or missing token.
  - Dependency injection for token authentication.

## Installation

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the required dependencies using `pip install -r requirements.txt`.
4. Set up your MySQL database and update the `SQLALCHEMY_DATABASE_URL` in `database.py`.
5. Run the application using `uvicorn main:app --reload`.

## Usage

- Use the `/auth/signup` endpoint to create a new user.
- Use the `/auth/login` endpoint to log in and obtain a token.
- Use the token to authenticate requests to the `/posts/` endpoints.

## Contributing

Contributions are welcome. Please create a pull request or open an issue for any changes or enhancements.
