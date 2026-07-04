# Ans EValuation question 46:
A virtual environment is an isolated Python environment created for a specific project. It has its own Python interpreter and its own installed packages, separate from the system-wide Python installation and other projects.
Why is it critical for every project?
1.Keeps dependencies isolated: Each project can use its own package versions without affecting other projects.
2.Avoids version conflicts: For example, one project can use requests version 2.31 while another uses a newer version, and they won't interfere with each other.
3.Improves reproducibility: Anyone can recreate the same environment by installing the packages listed in requirements.txt.
4.Protects the global Python installation: Project-specific packages are installed inside the virtual environment instead of globally, keeping your system Python clean.
5.Makes collaboration easier: Team members can create identical environments, reducing "it works on my machine" problems.
# ans e question 47:
requirements.txt is a plain text file used in Python projects to list all the external libraries (dependencies) that your project needs to run.
created by command pip freeze > requirements.txt
used by command pip install -r requirements.txt
#ans e question 48:
A .env file is a plain text configuration file used to store environment variables for a project—especially sensitive or environment-specific values.
The .env file often contains sensitive data, such as:API keys
1.Database passwords
2.Secret tokens
3.Private configuration values

If you push it to GitHub:
1.Anyone can see and steal your secrets
2.Your APIs or databases can be compromised
3.You may get unexpected charges (common with cloud APIs)
4.Security incidents can happen in real projects
# ans question 49:
Here’s the simple difference:
-------pip install package-------
2.Installs one package only
3.You choose what to install each time
------pip install -r requirements.txt-----
1. Installs all packages listed in a file
2. Used to set up a full project environment

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
output ss for prove:
ativated env and then deactivate it 
<img width="1297" height="829" alt="image" src="https://github.com/user-attachments/assets/e160bc81-6d33-4897-98d8-36087a6cca68" />
reactivate it again
<img width="1285" height="755" alt="image" src="https://github.com/user-attachments/assets/eae1e02a-59be-4408-8905-810e843644e3" />


