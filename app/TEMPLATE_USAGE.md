# Using This Template for New Projects

This repository serves as a **starter template** for AI upskilling program projects. Follow these steps to create a new project from this template.

## 🚀 Quick Start

### Option 1: Use GitHub Template (Recommended)

If this is set up as a GitHub template repository:

1. Go to the repository on GitHub
2. Click **"Use this template"** → **"Create a new repository"**
3. Name your new repository (e.g., `project-2`, `assignment-3`)
4. Choose your organization/account
5. Click **"Create repository"**
6. Clone your new repository:
   ```bash
   git clone <your-new-repo-url>
   cd <your-new-repo-name>
   ```

### Option 2: Clone and Customize

```bash
# Clone the template
git clone <template-repo-url> my-new-project
cd my-new-project

# Remove the old git history and start fresh
rm -rf .git
git init
git add .
git commit -m "Initial commit from template"

# Update project-specific files
# - Edit README.md with your project name
# - Update app.py with your project description
# - Add your specific dependencies to requirements.txt
```

### Option 3: Fork and Rename

```bash
# Fork the repository on GitHub first, then:
git clone <your-fork-url> my-new-project
cd my-new-project

# Update remote to point to your new repo
git remote set-url origin <new-repo-url>
```

## 📋 Setup Checklist for New Projects

After creating your project from the template:

- [ ] **Update README.md**
  - Change project name and description
  - Update any project-specific instructions
  - Remove template-specific sections if needed

- [ ] **Update app.py**
  - Change the welcome message
  - Update version number
  - Customize application name

- [ ] **Review requirements.txt**
  - Uncomment AI/ML libraries you'll need
  - Add project-specific dependencies
  - Remove unused dependencies

- [ ] **Set up environment**
  ```bash
  cd app
  make install
  ```

- [ ] **Configure certificates** (if needed)
  - Copy your corporate certificate to the parent directory
  - Update `CERT_FILE` in Dockerfile if using a different name
  - Or remove certificate setup if not needed

- [ ] **Create .env file** (if needed)
  ```bash
  cp .env.example .env
  # Edit .env with your actual values
  ```

- [ ] **Test the setup**
  ```bash
  make run
  # Or
  make docker-build
  make docker-run
  ```

- [ ] **Update git remote** (if cloned)
  ```bash
  git remote set-url origin <your-new-repo-url>
  ```

- [ ] **Initial commit**
  ```bash
  git add .
  git commit -m "Initial project setup"
  git push -u origin main
  ```

## 🎯 Project-Specific Customization

### Adding Your First AI Feature

1. **Install AI libraries** in `requirements.txt`:
   ```txt
   numpy>=1.24.0
   pandas>=2.0.0
   scikit-learn>=1.3.0
   ```

2. **Create a model** in `models/`:
   ```python
   # models/my_model.py
   import pickle
   
   class MyModel:
       def predict(self, data):
           # Your model logic
           return prediction
   ```

3. **Create an endpoint** in `routes/api.py`:
   ```python
   @api_bp.route('/predict', methods=['POST'])
   def predict():
       data = request.get_json()
       # Use your model
       return jsonify({"prediction": result})
   ```

### Removing Template-Specific Content

If you don't need certain features:

- **Docker**: Keep it for deployment, but you can simplify if not using corporate certificates
- **Makefile**: Keep it - it's useful for all projects
- **Security checks**: Keep them - always important
- **Example endpoints**: Replace with your actual endpoints

## 📚 Template Features

This template includes:

- ✅ Flask application structure
- ✅ Docker setup with corporate certificate support
- ✅ Makefile for common commands
- ✅ Security best practices (.gitignore, SECURITY.md)
- ✅ Health check endpoints
- ✅ Environment variable configuration
- ✅ Project structure (routes, models, utils)
- ✅ Documentation (README, LOCAL_SETUP, SECURITY)

## 🔄 Updating from Template

If the template gets updates you want to pull in:

```bash
# Add template as a remote
git remote add template <template-repo-url>

# Fetch template updates
git fetch template

# Merge specific updates (be careful not to overwrite your work)
git merge template/main --allow-unrelated-histories
```

## 💡 Best Practices

1. **Keep it simple**: Start with the template, add features as needed
2. **Document changes**: Update README as you add features
3. **Use the Makefile**: It makes common tasks easier
4. **Run security checks**: Use `make check-secrets` before committing
5. **Test locally first**: Use `make run` before deploying

## 🆘 Getting Help

- Check `README.md` for general usage
- Check `LOCAL_SETUP.md` for local development
- Check `SECURITY.md` for security best practices
- Check `SECURITY.md` for security guidelines

## 📝 Notes for Course Instructors

If you're setting this up for a course:

1. **Make it a template**: Enable "Template repository" in GitHub settings
2. **Add to organization**: Put it in your organization's template list
3. **Version it**: Tag releases if you make improvements
4. **Document updates**: Keep a CHANGELOG.md for template changes
5. **Provide examples**: Consider creating example projects that use this template

---

**Remember**: This is a starting point. Customize it for your specific project needs!

