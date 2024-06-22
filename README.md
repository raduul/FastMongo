
# FastMongo

## Description

This project serves as a practical example demonstrating how to:
- Develop a simple route using FastAPI
- Containerize a FastAPI application
- Establish a connection to MongoDB
- Deploy a sample schema using an initialization approach
- Send data to the MongoDB database

## Prerequisites

Ensure you have the following software installed before running this project:

- **Python:** Download and install from the [official Python website](https://www.python.org/downloads/).
- **Docker:** Download and install from the [official Docker website](https://www.docker.com/get-started).
- **MongoDB Compass or Mongosh:** Download and install from the [official MongoDB website](https://www.mongodb.com/try/download/compass).

With these prerequisites installed, you are ready to proceed with setting up and using this project.

## Installation

Follow these steps to set up the project:

1. Create a virtual environment:
    ```bash
    python -m venv venv
    ```

2. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Volume Configuration

It's crucial to configure a virtual volume on Docker Desktop to store sample data:
    ```
    Docker Desktop > Settings > Resources > File Sharing > Select a location on your device
    ```

## Usage

To run the project, execute the following steps:

1. From the root directory, launch the services:
    ```bash
    docker compose -f deployment/docker-compose-fastapi.yaml up --build
    ```

2. Visit `localhost:8000/docs` to access the Swagger UI.

3. Use the `send_data` endpoint to post sample data:
    ```json
    {
      "name": "John Doe",
      "email": "john.doe@example.com"
    }
    ```

4. Verify the stored data using MongoDB Compass or `mongosh`.

## Contributing

Contributions are welcome! Please read through the contribution guidelines before submitting your pull request.

## License

This project is licensed under the [Apache License 2.0](LICENSE).
