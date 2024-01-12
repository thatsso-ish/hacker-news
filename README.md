# hacker-news
- Introduction
- Setup
- Project Structure
- Database Handling
- Task Execution
- Testing

Introduction
The goal of this and the following exercise is to implement each one of the `CRUD` operations and build a copycat of [Hacker News] (https://news.ycombinator.com). For those who don't know, HackerNews is a _very minimal_ social news website (with a focus on computer science & technology), where users can submit links to articles and other users can choose to "upvote" those article links.

Setup
1. Requirements:
   - Python 3.x
   - SQLite3
   - Invoke (for task automation)
2. Installation:
   pip install invoke
3. Database Setup:
Create a SQLite database file
Update the database connection strings in ‘db_handler.py’ to point to your database file.

Project Structure
The project follows a modular structure for better organization and separation of concerns.
-db_handler.py:
Contains the ‘Post’ class for handling posts and related database operations.
Defines methods for finding posts by ID, retrieving all posts, and building Post instances from database records.
-tasks.py:
Defines Invoke tasks for running tests ‘spec’, checking style offenses ‘rubocop’, and a default task ‘default’ that runs both.
-main.py:
The main script for executing tasks and showcasing example usage of the ‘Post’ class.
-test_post.py:
Contains test cases for the ‘Post’ class using the ‘pytest’ framework.

Database Handling
Post Class Methods
-	‘find(cls, post_id)’
Retrieves a post by ID from the database.
Uses the ‘build_record’ method to construct a ‘Post’ instance from the database record.
-	‘all(cls)’
Retrieves all posts from the database.
Uses the ‘build_record’ method to construct a list of ‘Post’ instances from the database records.
-	‘build_record(cls, row)’
Helper method to construct a ‘Post’ instance from a database record.

Database Operations
-	‘create_table()’
Placeholder for creating the 'posts' table if needed.
-	‘insert_post(post)’
Placeholder for inserting a new post into the 'posts' table.

Task Execution
Invoke tasks are used for common project tasks:
-	‘invoke spec’
Runs tests using ‘pytest’
-	‘invoke rubocop’
Checks style offenses using ‘flake8’
-	‘invoke’ (Default)
Runs both ‘rubocop’ and ‘spec tasks’

Execute tasks by running commands like:
python main.py spec  # To run tests
python main.py rubocop  # To check style offenses
python main.py  # To run the default task (rubocop and spec)

Testing
Test cases for the ‘Post’ class are defined in ‘test_post.py’ using the ‘pytest’ framework.
Execute tests with:
pytest test_post.py


