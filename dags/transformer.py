import pandas as pd

# Custom transformation logic using provided formulas

def calculate_revenue_for_order(input_data, input_rate):
    # Load data from Excel
    df_data = pd.read_excel(input_data)
    df_rate = pd.read_excel(input_rate)

    net_commission = 0
    net_income = 0
    revenue = 0
    print(df_rate.columns)
    print(df_data.columns)

    for index, row in df_data.iterrows():
        airline_rate = df_rate[df_rate['operating_airline'] == row['airline_id']]

        # Ensure that there is a match for the airline_rate
        if not airline_rate.empty:
            # Extract the values from the Series
            commission_percentage = airline_rate['commission_percentage'].iloc[0]
            incentive_percentage = airline_rate['incentive_percentage'].iloc[0]
            tax_percentage = airline_rate['tax_percentage'].iloc[0]
            sales_tax = airline_rate['sales_tax'].iloc[0]

            # Perform the transformations
            gross_commission = row['base_fare'] * commission_percentage
            bf_net_commission = row['base_fare'] - gross_commission
            gross_income = bf_net_commission * incentive_percentage
            wht_commission = gross_commission * tax_percentage
            wht_income = gross_income * sales_tax

            net_commission += (gross_commission - wht_commission)
            net_income += (gross_income - wht_income)
            revenue += (net_commission + net_income)

    # Output the results or save to another file/database
    print('Revenue ', revenue)
    print('Net Income ', net_income)
    print('Net Commission ', net_commission)
