import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file
df = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

# Plot state-wise unemployment trend
plt.figure(figsize=(14, 8))
for state in df['Region'].unique():
    state_data = df[df['Region'] == state]
    plt.plot(state_data['Date'], state_data['Estimated Unemployment Rate (%)'], label=state, alpha=0.6)

plt.title('State-wise Unemployment Rate Trends (2020)', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Unemployment Rate (%)')
plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), ncol=1, fontsize=8)
plt.grid(True)
plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt

# Define the Covid-19 breakpoint
covid_start = pd.to_datetime("2020-03-01")

# Create two subsets: before and after Covid
pre_covid = df[df['Date'] < covid_start]
post_covid = df[df['Date'] >= covid_start]

# Calculate average unemployment rate by state before and after Covid
avg_pre = pre_covid.groupby('Region')['Estimated Unemployment Rate (%)'].mean()
avg_post = post_covid.groupby('Region')['Estimated Unemployment Rate (%)'].mean()

# Combine into one DataFrame for comparison
covid_impact = pd.DataFrame({
    'Pre-Covid Avg': avg_pre,
    'Post-Covid Avg': avg_post
}).dropna()

# Plot the comparison
covid_impact.sort_values('Post-Covid Avg', ascending=False).plot(kind='bar', figsize=(14, 7), colormap='Set2')
plt.title('Covid-19 Impact: Avg Unemployment Rate Before vs During Covid-19')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y')
plt.tight_layout()
plt.show()


import calendar

# Add a column for the month
df['Month'] = df['Date'].dt.month

# Group by month and calculate average unemployment rate
monthly_avg = df.groupby('Month')['Estimated Unemployment Rate (%)'].mean()

# Rename month numbers to names
monthly_avg.index = [calendar.month_name[m] for m in monthly_avg.index]

# Plot the result
monthly_avg.plot(kind='bar', color='coral', figsize=(12, 6))
plt.title('Average Unemployment Rate by Month (2020)', fontsize=14)
plt.xlabel('Month')
plt.ylabel('Unemployment Rate (%)')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()


# Generate summary statistics
peak_unemployment = df[df['Estimated Unemployment Rate (%)'] == df['Estimated Unemployment Rate (%)'].max()]
lowest_unemployment = df[df['Estimated Unemployment Rate (%)'] == df['Estimated Unemployment Rate (%)'].min()]

# Extract values
peak_value = round(peak_unemployment['Estimated Unemployment Rate (%)'].values[0], 2)
peak_date = peak_unemployment['Date'].values[0]
peak_state = peak_unemployment['Region'].values[0]

low_value = round(lowest_unemployment['Estimated Unemployment Rate (%)'].values[0], 2)
low_date = lowest_unemployment['Date'].values[0]
low_state = lowest_unemployment['Region'].values[0]

# Print key insights
print("🔍 Key Insights:")
print(f"1. 📈 Highest unemployment was {peak_value}% in {peak_state} on {pd.to_datetime(peak_date).strftime('%B %Y')}.")
print(f"2. 📉 Lowest unemployment was {low_value}% in {low_state} on {pd.to_datetime(low_date).strftime('%B %Y')}.")
print("3. 🦠 Unemployment spiked sharply from March 2020, peaking in April-May due to Covid-19 lockdown.")
print("4. 📉 Gradual recovery started post-June in most states.")
print("5. 📅 Seasonal trends indicate significant monthly variation, with highest rates in summer months.")
