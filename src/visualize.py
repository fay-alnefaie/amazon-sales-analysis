import matplotlib.pyplot as plt
import seaborn as sns

def set_theme():
    """Sets a consistent visual theme for all plots."""
    sns.set_style('whitegrid')
    sns.set_palette('Set2')

def visualize_top_categories(result3):
    """Horizontal bar chart of top-selling categories by order count."""
    plt.figure(figsize=(10, 6))
    sns.barplot(x='total_orders', y='category', hue='category', data=result3, palette='viridis')
    plt.title('Top Selling Categories', fontsize=15)
    plt.xlabel('Number of Orders')
    plt.ylabel('Category')
    plt.tight_layout()
    plt.show()

def visualize_monthly_revenue(result11):
    """Line plot showing monthly revenue trend across 2022."""
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='month', y='total_revenue', data=result11, marker='o', color='b', linewidth=2.5)
    plt.title('Monthly Revenue Trend (2022)', fontsize=15)
    plt.xlabel('Month')
    plt.ylabel('Total Revenue (INR)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def visualize_cancellation_rate(result6):
    """Horizontal bar chart of cancellation rate percentage per category."""
    plt.figure(figsize=(10, 6))
    sns.barplot(x='cancel_rate', y='category', hue='category', data=result6, palette='magma')
    plt.title('Cancellation Rate (%) per Category', fontsize=15)
    plt.xlabel('Cancellation Rate Percentage')
    plt.ylabel('Category')
    plt.tight_layout()
    plt.show()
    
    


