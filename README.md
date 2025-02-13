# datafun-06-eda
DataFun: Mod 6: Custom Data Analytics Project

## Project Overview
This project is focused on Exploratory Data Analysis (EDA) using Python. The repository is set up with a virtual environment and necessary dependencies for data analysis and visualization.

## Setup Instructions

### 1. Clone the Repository
To get started, clone the repository from GitHub:
```powershell
cd ~/Documents
git clone https://github.com/SchroderJ-pixel/datafun-06-eda
cd datafun-06-eda
code .
```

### 2. Set Up the Virtual Environment
Create and activate a virtual environment for package management:
```powershell
py -m venv .venv
.venv\Scripts\Activate
```

### 3. Install Required Packages
Install the necessary dependencies:
```powershell
py -m pip install jupyterlab numpy pandas pyarrow matplotlib seaborn
```

### 4. Set Python Interpreter in VS Code
- Open **VS Code**.
- Press **Ctrl + Shift + P**.
- Search for **"Python: Select Interpreter"**.
- Choose `.venv` as the interpreter.

### 5. Commit and Push Changes to GitHub
After setting up the environment, commit and push the changes:
```powershell
git add .
git commit -m "Setup virtual environment and installed required packages"
git push
```

## Additional Notes
- The `.gitignore` file includes:
  ```
  .vscode/
  .venv/
  .ipynb_checkpoints/
  ```
- The repository is now ready for further development and analysis.

## Verifying the Setup
Ensure your GitHub repository reflects the latest updates. If needed, take a screenshot for documentation purposes.

