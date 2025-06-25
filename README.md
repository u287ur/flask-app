# github-actions

This project demonstrates how to containerize a Flask application with Docker, automate image builds and pushes to DockerHub using GitHub Actions.

## Project Structure

- `Dockerfile`: Builds the Docker image for the Flask app.
- `docker-compose.yml`: Manages the Flask app service.
- `.env.example`: Template for your DockerHub username.
- `.github/workflows/main.yml`: GitHub Actions workflow for CI/CD.
- `app/`: Contains the Flask application code.

## Getting Started

### 1. Environment Variables

Copy `.env.example` to `.env` and set your DockerHub username:

```sh
cp .env.example .env
# Edit .env and set:
# DOCKERHUB_USERNAME=your-dockerhub-username
```

### 2. CI/CD with GitHub Actions

On every push to the `main` branch:
- The Docker image is built and pushed to DockerHub with two tags:
  - `latest`
  - A timestamp (`yyyyMMdd-HHmm`)

**Required GitHub Secrets:**
- `DOCKERHUB_USERNAME`
- `DOCKERHUB_TOKEN` (DockerHub access token)

> **Note:**  
> You must push your code to GitHub and wait for the GitHub Actions workflow to build and push the Docker image to DockerHub before running Docker Compose.  
> The image must exist on DockerHub for Docker Compose to work.

### 3. Running with Docker Compose

After the image is available on DockerHub, start the application:

```sh
docker compose up -d
```

The Flask app will be available at [http://localhost:8888](http://localhost:8888).

## Notes

- Do not commit your `.env` file; keep it in your `.gitignore`.
- Make sure your DockerHub credentials are set as GitHub repository secrets.


