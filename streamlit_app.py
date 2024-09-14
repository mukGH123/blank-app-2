import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
df = pd.read_excel('Final_Yoga_Studios_Masterdata.xlsx')

# Format Store IDs (name in your case) to avoid comma separation
df['name'] = df['name'].astype(str)

# Define pages
def store_details():
    st.sidebar.header('Select Store Name')
    store_name = st.sidebar.selectbox('Store Name', df['name'].unique())

    # Filter data for the selected store
    store_data = df[df['name'] == store_name].iloc[0]

    # Display store attributes
    st.header(f'Store: {store_name}')
    st.write('### Store Details')
    st.write(f"Address: {store_data['address']}")
    st.write(f"Phone: {store_data['phone']}")
    st.write(f"Email: {store_data['email']}")
    st.write(f"Geographic Area: {store_data['Geographic Area Name']}")
    st.write(f"Total Population: {store_data['Total population']}")
    st.write(f"Male Population: {store_data['Total population-Male']}")
    st.write(f"Female Population: {store_data['Total population-Female']}")
    st.write(f"Sex Ratio (males per 100 females): {store_data['Sex ratio (males per 100 females)']}")
    st.write(f"TAM in TG Age (20-54 yrs): {store_data['TAM in TG Age(20-54 yrs)']}")
    st.write(f"American Indian and Alaska Native Population: {store_data['Total population-American Indian and Alaska Native']}")
    st.write(f"Median Earnings: ${store_data['Median earnings (dollars)']}")
    st.write(f"Male Median Earnings: ${store_data['Median earnings (dollars)-Male']}")
    st.write(f"Female Median Earnings: ${store_data['Median earnings (dollars)-Female']}")
    st.write(f"Total Below Poverty Line: {store_data['Total(Below Poverty)']}")
    st.write(f"Male Below Poverty: {store_data['Total(Below Poverty)-Male']}")
    st.write(f"Male Below Poverty Line in TG: {store_data['Male Below Poverty Line in TG']}")
    st.write(f"Female Below Poverty: {store_data['Total(Below Poverty)-Female']}")
    st.write(f"Female Below Poverty Line in TG: {store_data['Female Below Poverty Line in TG']}")
    st.write(f"High School Completed in TG: {store_data['High School Completed in TG']}")
    st.write(f"Bachelor's Completed in TG: {store_data['Bachelors Completed in TG']}")
    st.write(f"Population Density: {store_data['Population Density']}")
    st.write(f"Prosperity Score: {store_data['Prosperity Score']}")
    st.write(f"Expansion Score: {store_data['Expansion Score']}")
    st.write(f"Radius: {store_data['Radius']} miles")
    st.write(f"City: {store_data['city']}")

    # Pie chart for Male/Female Population
    st.write('### Population Distribution')
    labels = ['Male Population', 'Female Population']
    sizes = [store_data['Total population-Male'], store_data['Total population-Female']]
    colors = ['#ff9999', '#66b3ff']
    explode = (0.1, 0)  # explode the 1st slice

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    st.pyplot(fig1)

def summary_statistics():
    st.header('Summary Statistics')

    st.write('### All Stores Summary')
    # Include all the requested columns in the summary
    summary = df[['name', 'address', 'phone', 'email', 'Geographic Area Name', 
                  'Total population', 'Total population-Male', 'Total population-Female', 
                  'Sex ratio (males per 100 females)', 'TAM in TG Age(20-54 yrs)', 
                  'Total population-American Indian and Alaska Native', 'Median earnings (dollars)', 
                  'Median earnings (dollars)-Male', 'Median earnings (dollars)-Female', 
                  'Total(Below Poverty)', 'Total(Below Poverty)-Male', 'Male Below Poverty Line in TG', 
                  'Total(Below Poverty)-Female', 'Female Below Poverty Line in TG', 
                  'High School Completed in TG', 'Bachelors Completed in TG', 
                  'Population Density', 'Prosperity Score', 'Expansion Score', 'Radius', 'city']]
    
    # Display the DataFrame in the app
    st.dataframe(summary)

def store_comparison():
    st.sidebar.header('Select Stores to Compare')
    selected_stores = st.sidebar.multiselect('Store Names', df['name'].unique())

    if len(selected_stores) > 1:
        st.header('Store Comparison')
        st.write('### Comparison of Selected Stores')

        store_data_list = []
        for store_name in selected_stores:
            store_data = df[df['name'] == store_name].T
            store_data.columns = [store_name]
            store_data_list.append(store_data)

        # Display the stores' data side by side
        for i, store_data in enumerate(store_data_list):
            if i == 0:
                comparison_df = store_data
            else:
                comparison_df = pd.concat([comparison_df, store_data], axis=1)

        st.dataframe(comparison_df)

# Create a navigation menu
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Store Details', 'Summary Statistics', 'Store Comparison'])

st.markdown(
    """
    <style>
    [data-testid="stElementToolbar"] {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Render the selected page
if page == 'Store Details':
    store_details()
elif page == 'Summary Statistics':
    summary_statistics()
elif page == 'Store Comparison':
    store_comparison()
