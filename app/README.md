# AI Up-Skilling Flask Application Template

A production-ready Flask application framework designed for AI/ML upskilling programs. This starter template provides a solid foundation for building and deploying AI-powered applications.

> **📌 This is a template repository.** See [TEMPLATE_USAGE.md](TEMPLATE_USAGE.md) for instructions on how to use this template for new projects.

## Features

- ✅ **Dockerized** - Ready-to-use Docker setup with corporate certificate support
- ✅ **Makefile** - Common commands simplified (standard in AI/ML projects)
- ✅ **Structured Codebase** - Organized with routes, models, and utilities
- ✅ **Production Ready** - Uses Gunicorn for production deployment
- ✅ **Health Checks** - Built-in health check endpoints
- ✅ **Environment Configuration** - Uses python-decouple for environment variables
- ✅ **Extensible** - Easy to add AI/ML models and endpoints
- ✅ **Security First** - Comprehensive .gitignore and security checks
- ✅ **Well Documented** - Multiple guides for different use cases

## 🚀 Quick Start for New Projects

**Using this template?** See [TEMPLATE_USAGE.md](TEMPLATE_USAGE.md) for detailed instructions.

**Quick steps:**
1. Click "Use this template" on GitHub (if enabled)
2. Or clone and customize: `git clone <repo> my-project`
3. Run `make install` to set up
4. Start building your AI application!

## Project Structure

```
app/
├── app.py                 # Main application entry point
├── routes/                # API route blueprints
│   ├── __init__.py
│   └── api.py            # Example API endpoints
├── models/                # Data models and ML model integration
│   └── __init__.py
├── utils/                 # Utility functions
│   ├── __init__.py
│   └── helpers.py        # Helper functions
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── Makefile              # Common commands (make help to see all)
├── .flaskenv             # Flask environment variables
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## Quick Start

### Prerequisites

- Docker installed
- Certificate file (`Zscaler_Root_CA.cer`) in the parent directory (`ai_upskilling/`)
- Make (optional but recommended - `brew install make` on macOS)

### Using Make (Recommended)

The project includes a `Makefile` with common commands. This is a standard practice in AI/ML projects for simplifying workflows.

**View all available commands:**
```bash
make help
```

**Quick start:**
```bash
# Install dependencies and run locally
make install
make run

# Or use Docker
make docker-build
make docker-run
```

### Building the Docker Image

**Using Make:**
```bash
make docker-build
```

**Manual:**
From the `ai_upskilling` directory:

```bash
docker build -f getting_started/app/Dockerfile -t flask-app .
```

### Running the Container

**Using Make:**
```bash
make docker-run
```

**Manual:**
```bash
docker run -p 5000:5000 flask-app
```

### Accessing the Application

- **Home**: http://localhost:5000
- **Health Check**: http://localhost:5000/api/health
- **Example Endpoint**: http://localhost:5000/api/example

## Development Setup (Local)

### Using Make (Recommended)

```bash
# One command to set up everything
make install

# Run the app
make run

# Or run in development mode with auto-reload
make dev
```

### Manual Setup

#### 1. Create Virtual Environment

```bash
cd app
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 3. Set Environment Variables

Create a `.env` file (optional, defaults are provided):

```env
PORT=5000
```

#### 4. Run the Application

```bash
python app.py
```

Or using Flask:

```bash
flask run
```

## Common Make Commands

The Makefile provides shortcuts for common tasks:

| Command | Description |
|---------|-------------|
| `make install` | Set up virtual environment and install dependencies |
| `make run` | Run Flask app locally |
| `make dev` | Run in development mode with auto-reload |
| `make test` | Run tests |
| `make test-endpoints` | Test API endpoints |
| `make docker-build` | Build Docker image |
| `make docker-run` | Run Docker container |
| `make docker-stop` | Stop Docker container |
| `make docker-logs` | View container logs |
| `make clean` | Remove Python cache files |
| `make status` | Check service status |

**Why Makefiles in AI Projects?**

Makefiles are extremely common in AI/ML projects because they:
- **Standardize commands** across team members
- **Simplify complex workflows** (data prep, training, testing, deployment)
- **Document common tasks** in one place
- **Reduce errors** from typing long commands
- **Enable automation** in CI/CD pipelines

Many popular AI projects (TensorFlow, PyTorch, Hugging Face) use Makefiles for this reason.

## Adding AI/ML Features

### 1. Install AI Libraries

Uncomment the libraries you need in `requirements.txt`:

```txt
numpy>=1.24.0
pandas>=2.0.0
scikit-learn>=1.3.0
# etc.
```

Then rebuild the Docker image or reinstall dependencies locally.

### 2. Create Model Integration

Add your ML models in the `models/` directory:

```python
# models/ml_model.py
import pickle

class MLModel:
    def __init__(self, model_path):
        with open(model_path, 'rb') as f:
            self.model = pickle.load(f)
    
    def predict(self, data):
        return self.model.predict(data)
```

### 3. Create API Endpoints

Add new endpoints in `routes/api.py` or create new route files:

```python
from routes.api import api_bp
from models.ml_model import MLModel

@api_bp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    model = MLModel('path/to/model.pkl')
    prediction = model.predict(data)
    return jsonify({"prediction": prediction}), 200
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `PORT` | 5000 | Port number for the Flask application |

## Docker Configuration

The Dockerfile is configured to:
- Use Python 3.9 slim image
- Install system dependencies (including curl for health checks)
- Handle corporate certificates automatically
- Use Gunicorn for production
- Expose port 5000

### Building with Custom Certificate

If your certificate file has a different name:

```bash
docker build --build-arg CERT_FILE=your-cert.cer -f getting_started/app/Dockerfile -t flask-app .
```

## API Endpoints

### GET `/`
Returns application information and available endpoints.

### GET `/api/health`
Health check endpoint for monitoring.

**Response:**
```json
{
  "status": "healthy",
  "service": "flask-app"
}
```

### GET/POST `/api/example`
Example endpoint demonstrating request/response patterns.

**GET Response:**
```json
{
  "message": "This is an example endpoint",
  "usage": "Add your AI/ML functionality here",
  "methods": ["GET", "POST"]
}
```

**POST Request:**
```json
{
  "data": "your data here"
}
```

## Best Practices

1. **Environment Variables**: Always use environment variables for configuration
2. **Error Handling**: Use try/except blocks and return appropriate HTTP status codes
3. **Logging**: Use the logging module for debugging and monitoring
4. **Validation**: Validate input data before processing
5. **Documentation**: Document your endpoints and functions
6. **Testing**: Write tests for your AI models and endpoints

## Next Steps for AI Integration

1. **Choose Your AI Framework**: TensorFlow, PyTorch, scikit-learn, etc.
2. **Load Models**: Add model loading logic in the `models/` directory
3. **Create Endpoints**: Build API endpoints that use your models
4. **Add Preprocessing**: Create utility functions for data preprocessing
5. **Add Postprocessing**: Format model outputs for API responses
6. **Error Handling**: Handle model errors gracefully
7. **Monitoring**: Add logging and metrics for model performance

## Troubleshooting

### Certificate Issues
If you encounter SSL certificate errors:
- Ensure `Zscaler_Root_CA.cer` is in the `ai_upskilling/` directory
- Check that the certificate file is valid
- Verify the build context is correct

### Port Already in Use
If port 5000 is already in use:
- Change the `PORT` environment variable
- Update the Docker port mapping: `docker run -p 8080:5000 flask-app`

### Import Errors
If you get import errors:
- Ensure you're in the correct directory
- Activate your virtual environment
- Reinstall dependencies: `pip install -r requirements.txt`

## Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Gunicorn Documentation](https://gunicorn.org/)
- [Python Decouple](https://github.com/henriquebastos/python-decouple)

## License

This is a starter template for educational purposes in the AI Up-Skilling program.

