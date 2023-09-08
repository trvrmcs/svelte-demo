# initial setup

Build devcontainer with both Python and Node

Install 'Svelte for VS Code extension' in devcontainer.

# Backend 

```
pipenv --python 3.11 
pipenv install fastapi uvicorn <etc>
pipenv install --dev flake8 black ipykernel pytest mypy ipython
mkdir backend 

```

# Frontend
```
mkdir frontend
cd frontend 

npm create vite@latest --  --template svelte-ts

<provide 'frontend' as project name>

cd frontend 
npm install
npm run build
```

This creates the code we want to deliver to the frontend in `frontend/dist`

# Run 

```
pipenv run python -m backend 

```

and navigate to http://localhost:8000/index.html

