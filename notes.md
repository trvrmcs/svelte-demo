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

# JSON Editor 
```
npm install -D svelte-jsoneditor 
```
And then in a component:

```html
<script>
    import { JSONEditor } from "svelte-jsoneditor";

    let content = {
        text: undefined, // can be used to pass a stringified JSON document instead
        json: {},
    };
</script>

<div>
    <JSONEditor bind:content />
</div>

```

Note: this adds about 800kb to the output JS, which is still less than 
shipping the vanilla code.

 