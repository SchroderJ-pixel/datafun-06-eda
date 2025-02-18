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

## 6. Downloading the Diamonds Dataset
- Go to the following URL: [Diamonds Dataset - Seaborn GitHub](https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/diamonds.csv).
- Use Python's `requests` library to download the dataset.
- Save the file locally in the `data` folder within the project directory: `C:\Projects\datafun-06\datafun-06-eda\data\diamonds.csv`.

## 7. Data Analysis

### Data Preparation
- Loaded the diamonds dataset and examined its structure.
- Cleaned data by ensuring that the columns had appropriate types for analysis.

### Exploratory Data Analysis (EDA) Charts
1. **Distribution of Diamond Prices**  
   A histogram of diamond prices was created, showing a right-skewed distribution, which suggests that most diamonds have lower prices, with fewer diamonds priced higher.
   
2. **Distribution of Diamond Cuts**  
   A countplot showed that most diamonds in the dataset are classified as "Ideal," with fewer diamonds classified as "Fair." This suggests a preference for better-cut diamonds.

3. **Scatterplot of Carat vs. Cost**  
   A scatterplot illustrated the relationship between carat weight and cost. It revealed that the cost tends to increase significantly as carat weight increases, particularly between 1 and 3 carats.

4. **Boxplot of Cost Distribution by Cut**  
   A boxplot was created to show the cost distribution across different cuts. The boxplot highlighted the presence of outliers, particularly in the "Fair" cut category, and showed that the cost range is wide across all cuts.

5. **Correlation Heatmap of Diamond Features**  
   A heatmap was plotted to visualize correlations between numeric features like carat, cost, depth, and table. It revealed strong positive correlations between carat and cost, and between carat and other dimensions.

6. **Violin Plot of Cost Distribution by Clarity with Color Gradient**  
   A violin plot was created to show the distribution of costs across different clarity levels, with a color gradient indicating clarity. This plot suggested that clarity alone does not significantly affect the median cost, as other factors like carat and cut are also important drivers of price.

### Observations
- Carat weight, cost, and other diamond attributes such as cut and clarity are interrelated, with carat weight being one of the most significant factors driving price increases.
- Although clarity is a valuable characteristic, it does not have as strong an influence on price as carat weight or cut.
- The presence of high-cost outliers suggests that larger diamonds, regardless of their clarity, can still be priced very highly.

## Next Steps
- Further analysis could include predictive modeling to estimate diamond prices based on various features.
- Consider exploring more visualizations to better understand relationships between features, such as 3D plots or pairplots.
