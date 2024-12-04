
# Event Manager Company: Software QA Analyst/Developer Onboarding Assignment

Welcome to the Event Manager Company! As a newly hired Software QA Analyst/Developer and a student in software engineering, you are embarking on an exciting journey to contribute to our project aimed at developing a secure, robust REST API that supports JWT token-based OAuth2 authentication. This API serves as the backbone of our user management system and will eventually expand to include features for event management and registration.

## Assignment Objectives
- **Familiarize with REST API functionality and structure**: Gain hands-on experience working with a REST API, understanding its endpoints, request/response formats, and authentication mechanisms.
- **Implement and refine documentation**: Critically analyze and improve existing documentation based on issues identified in the instructor videos. Ensure that the documentation is up-to-date and accurately reflects the current state of the software.
- **Engage in manual and automated testing**: Develop comprehensive test cases and leverage automated testing tools like `pytest` to push the project's test coverage to over 95%. Gain experience with different types of testing, such as unit testing, integration testing, and end-to-end testing.
- **Explore and debug issues**: Dive deep into the codebase to investigate and resolve issues related to user profile updates and OAuth token generation. Utilize debugging tools, interpret error messages, and trace the flow of execution to identify the root cause of problems.
- **Collaborate effectively**: Experience the power of collaboration using Git for version control and GitHub for code reviews and issue tracking. Work with issues, branches, create pull requests, and merge code while following best practices.

## Setup and Preliminary Steps
1. **Fork the Project Repository**: Fork the project repository to your own GitHub account. This creates a copy of the repository under your account, allowing you to work on the project independently.
2. **Clone the Forked Repository**: Clone the forked repository to your local machine using the `git clone` command. This creates a local copy of the repository on your computer, enabling you to make changes and run the project locally.
3. **Verify the Project Setup**:
   - Follow the steps in the instructor video to set up the project using Docker.
   - Verify that you can access the API documentation at `http://localhost/docs` and the database using PGAdmin at `http://localhost:5050`.

## Testing and Database Management
1. **Explore the API**: Use the Swagger UI at `http://localhost/docs` to familiarize yourself with the API endpoints, request/response formats, and authentication mechanisms.
2. **Run Tests**: Execute the provided test suite using `pytest`. Note that running tests will drop the database tables, so you may need to manually drop the Alembic version table using PGAdmin and re-run migrations to ensure a clean state.
3. **Increase Test Coverage**: Test coverage has been pushed beyond **95%** by writing additional tests for various scenarios and edge cases to ensure the API handles different situations correctly.

## Collaborative Development Using Git
1. **Enable Issue Tracking**: Enabled GitHub issues in the repository settings to track bugs, enhancements, and other tasks.
2. **Create Branches**: Created branches for each issue/task using descriptive names: 
   - [Username Validation Enhancement](https://github.com/Roman-sv966/wsdhomework10-2024/issues/10)
   - [Token-Based Authentication Enhancement](https://github.com/Roman-sv966/wsdhomework10-2024/issues/9)
   - [Password Validation Enhancement](https://github.com/Roman-sv966/wsdhomework10-2024/issues/8)
   - [Nickname Validation Issue](https://github.com/Roman-sv966/wsdhomework10-2024/issues/7)
   - [Refactor Test Fixtures for User Schemas](https://github.com/Roman-sv966/wsdhomework10-2024/issues/6)
   - [Email Validation Issue](https://github.com/Roman-sv966/wsdhomework10-2024/issues/5)
3. **Pull Requests and Code Reviews**: Created pull requests for each branch and reviewed code to ensure high-quality contributions.

## ISSUES are attached
   - [Username Validation Enhancement](https://github.com/Roman-sv966/wsdhomework10-2024/issues/10)
   - [Token-Based Authentication Enhancement](https://github.com/Roman-sv966/wsdhomework10-2024/issues/9)
   - [Password Validation Enhancement](https://github.com/Roman-sv966/wsdhomework10-2024/issues/8)
   - [Nickname Validation Issue](https://github.com/Roman-sv966/wsdhomework10-2024/issues/7)
   - [Refactor Test Fixtures for User Schemas](https://github.com/Roman-sv966/wsdhomework10-2024/issues/6)
   - [Email Validation Issue](https://github.com/Roman-sv966/wsdhomework10-2024/issues/5)
     
## Docker Image
The project is available as a Docker image for deployment: [Dockerhub Project Image](https://hub.docker.com/repository/docker/sv966/event-manager-api/general).

## Submission Requirements
- **GitHub Repository Link**: Ensure the repository includes:
  - Links to closed issues with accompanying test code and application code modifications.
  - An updated README.md file (this file) with:
    - Links to the closed issues.
    - Link to the Docker image on Dockerhub.
    - A reflection on the challenges faced and insights gained during the assignment.

## Reflection
This assignment was an excellent opportunity to gain hands-on experience in API development, debugging, and testing. It provided insights into collaborative development using Git and GitHub, as well as the importance of thorough documentation and clear communication within a team. By resolving issues and improving the existing codebase, I enhanced my technical skills and learned the significance of maintaining high code quality through automated testing and structured development practices.
