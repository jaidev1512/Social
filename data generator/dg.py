import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set random seed for reproducibility
np.random.seed(42)

# Generate an even distribution of dates for 1000 posts over 90 days
end_date = datetime(2025, 1, 5)  # Current date
start_date = end_date - timedelta(days=90)

# Create an array of dates with roughly 11-12 posts per day (1000 posts / 90 days)
all_dates = []
current_date = start_date
while current_date <= end_date:
    # Generate 11-12 posts for each day
    posts_per_day = np.random.randint(10, 13)
    all_dates.extend([current_date] * posts_per_day)
    current_date += timedelta(days=1)

# Trim or pad to exactly 1000 dates
all_dates = all_dates[:1000] if len(all_dates) > 1000 else all_dates + [end_date] * (1000 - len(all_dates))
np.random.shuffle(all_dates)  # Shuffle the dates to avoid sequential patterns

# Create data
data = []
post_types = ['carousel', 'reels', 'static_image']
post_id = 1

# Engagement rate multipliers for different post types
multipliers = {
    'carousel': 1.2,  # 20% higher engagement
    'reels': 1.0,     # Base engagement
    'static_image': 1.0  # Base engagement
}

# Comment multipliers (reels get 2x more comments)
comment_multipliers = {
    'carousel': 1.0,
    'reels': 2.0,
    'static_image': 1.0
}

for date in all_dates:
    post_type = np.random.choice(post_types)
    
    # Base metrics
    base_likes = np.random.randint(100, 1000)
    base_shares = np.random.randint(10, 100)
    base_comments = np.random.randint(5, 50)
    
    # Apply multipliers
    likes = int(base_likes * multipliers[post_type])
    shares = int(base_shares * multipliers[post_type])
    comments = int(base_comments * comment_multipliers[post_type])
    
    data.append({
        'post_id': f'POST_{post_id:04d}',
        'date': date.strftime('%Y-%m-%d'),
        'post_type': post_type,
        'likes': likes,
        'shares': shares,
        'comments': comments,
        'total_engagement': likes + shares + comments
    })
    
    post_id += 1

# Create DataFrame
df = pd.DataFrame(data)

# Sort by date and post_id
df = df.sort_values(['date', 'post_id'])

# Save to CSV
df.to_csv('social_media_engagement.csv', index=False)

# Display first few rows and summary statistics
print("\nFirst few rows of the dataset:")
print(df.head())

print("\nDate range in dataset:")
print(f"Start date: {df['date'].min()}")
print(f"End date: {df['date'].max()}")

print("\nPosts per day statistics:")
posts_per_day = df['date'].value_counts().describe()
print(posts_per_day)

print("\nEngagement statistics by post type:")
print(df.groupby('post_type').agg({
    'likes': 'mean',
    'shares': 'mean',
    'comments': 'mean',
    'total_engagement': 'mean'
}).round(2))
