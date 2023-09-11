* clone repo
* open in vscode
* open devcontainer 
* add 'Svelte for VS Code' extension in dev container


### Frontend
```
cd /workspaces/svelte-demo/frontend
npm install  
npm run build
```

### Backend 
```
cd /workspaces/svelte-demo 
pipenv sync --dev
pipenv run python -m backend
```