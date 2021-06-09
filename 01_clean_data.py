import pandas as pd 
from mltrace import register, create_component

@register(component_name="clean", input_vars=['input_filepath'], output_vars=['output_filepath'])
def clean(input_filepath: str, output_filepath: str) -> str:
    """
    process raw data by adding column names
    """
    raw = pd.read_csv(input_filepath, header=None)
    print('adding column names')
    raw.columns = ['sex','length','diameter','height','whole_weight','shucked_weight','viscera_weight','shell_weight','rings']
    print('saving data to csv')
    raw.to_csv(output_filepath, index=False)

if __name__=="__main__":
    create_component(
        name="cleaning",
        description="process raw data by adding column names",
        owner="jeanne",
        tags=["etl"],)
    clean('data/abalone.data','data/abalone.csv')

