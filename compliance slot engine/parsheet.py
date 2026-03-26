import pandas as pd

def export(metrics, path="par_sheet.xlsx"):
    pd.DataFrame([metrics]).to_excel(path, index=False)