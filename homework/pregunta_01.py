def pregunta_01():
    """
    El archivo `files/input/shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:
    ...
    """
    import pandas as pd
    import matplotlib.pyplot as plt
    import os

    output_dir = 'docs'
    os.makedirs(output_dir, exist_ok=True)

    def load_data():
        return pd.read_csv('files/input/shipping-data.csv')

   
    def create_visual_for_shipments_per_warehouse(df, output_dir):
        df_copy = df.copy()
        plt.figure()
        counts = df_copy['Warehouse_block'].value_counts()
        counts.plot(
            kind='bar',
            title='Shipments per Warehouse',
            xlabel='Warehouse Block',
            ylabel='Record Count',
            color='tab:blue',
            fontsize=8,
        )
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.tight_layout()
     
        plt.savefig(os.path.join(output_dir, 'shipping_per_warehouse.png')) 
        plt.close()

    def create_visual_for_mode_of_shipment(df, output_dir):
        df_copy = df.copy()
        plt.figure()
        counts = df_copy['Mode_of_Shipment'].value_counts()
        counts.plot(
            kind='pie',
            title='Mode of Shipment',
            ylabel='',
            colors=['tab:blue', 'tab:orange', 'tab:green'],
            wedgeprops={'width': 0.35},
            autopct='%1.1f%%',
        )
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'mode_of_shipment.png'))
        plt.close()

    def create_visual_for_average_customer_rating(df, output_dir):
        df_copy = df.copy()
        plt.figure()
        subset = df_copy[['Mode_of_Shipment', 'Customer_rating']]
        stats = subset.groupby('Mode_of_Shipment')['Customer_rating'].describe()
        
        plt.barh(
            y=stats.index,
            width=stats['max'] - stats['min'],
            left=stats['min'],
            color='lightgray',
            height=0.9,
            alpha=0.8
        )
        colors = ['tab:green' if x >= 3 else 'tab:orange' for x in stats['mean']]
        plt.barh(
            y=stats.index,
            width=stats['mean'] - 1,
            left=1,
            color=colors,
            height=0.5,
            alpha=1.0
        )
        plt.title('Average Customer Rating')
        ax = plt.gca()
        ax.spines['left'].set_color('gray')
        ax.spines['bottom'].set_color('gray')
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'average_customer_rating.png'))
        plt.close()

    def create_visual_for_weight_distribution(df, output_dir):
        df_copy = df.copy()
        plt.figure()
        plt.hist(
            df_copy['Weight_in_gms'],
            bins=50,
            color='tab:blue',
            edgecolor='white'
        )
        plt.title('Weight (gms) Distribution')
        ax = plt.gca()
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        plt.tight_layout()
        plt.savefig(os.path.join(output_dir, 'weight_distribution.png'))
        plt.close()
    
    df_data = load_data()
    
    create_visual_for_shipments_per_warehouse(df_data, output_dir)
    create_visual_for_mode_of_shipment(df_data, output_dir)
    create_visual_for_average_customer_rating(df_data, output_dir)
    create_visual_for_weight_distribution(df_data, output_dir)


   
    html_content = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>Shipping Dashboard Example</title>
        <style>
            body { font-family: Arial, sans-serif; }
            h1 { text-align: center; }
            .column { float: left; width: 48%; padding: 1%; }
            .plot-container { margin-bottom: 20px; }
            img { max-width: 100%; height: auto; border: 1px solid #ccc; }
        </style>
    </head>
    <body>
        <h1>Shipping Dashboard Example</h1>
        <div class="column">
            <div class="plot-container">
                <img src="shipping_per_warehouse.png" alt="Shipments per Warehouse">
            </div>
            <div class="plot-container">
                <img src="mode_of_shipment.png" alt="Mode of Shipment">
            </div>
        </div>
        <div class="column">
            <div class="plot-container">
                <img src="average_customer_rating.png" alt="Average Customer Rating">
            </div>
            <div class="plot-container">
                <img src="weight_distribution.png" alt="Weight Distribution">
            </div>
        </div>
    </body>
    </html>
    """
    
    with open(os.path.join(output_dir, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(html_content)
if __name__ == "__main__":
    pregunta_01()