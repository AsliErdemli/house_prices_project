import pathlib 
import pandas as pd
import seaborn as sns

project_path = pathlib.Path(__file__).parent.parent
print("My project path is:",project_path)

data_path = project_path /"data"
src_path = project_path / "src"
logs_path = project_path / "logs"

# Import dataset: 
dataset = pd.read_csv(data_path /"test.csv")