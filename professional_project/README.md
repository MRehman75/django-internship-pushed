# Professional Python Project

## Create the project

```cmd
mkdir professional_project
cd professional_project
```

## Create a virtual environment

```cmd
python -m venv venv
```

## Activate the virtual environment

```cmd
venv\Scripts\activate
```

## Install dependencies

```cmd
pip install requests python-dotenv rich
```

## Save dependencies

```cmd
pip freeze > requirements.txt
```

## Run the project

```cmd
python main.py
```

## Rebuild the environment

### Delete the virtual environment

```cmd
rmdir /s /q venv
```

### Create a new virtual environment

```cmd
python -m venv venv
```

### Activate it

```cmd
venv\Scripts\activate
```

### Install dependencies from requirements.txt

```cmd
pip install -r requirements.txt
```

### Run the project

```cmd
python main.py
```

## Git Commands

```cmd
git status
git add .
git commit -m "Set up professional Python project"
git push origin main
```