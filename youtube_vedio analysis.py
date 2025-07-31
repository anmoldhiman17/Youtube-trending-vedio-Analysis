import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set visual style
sns.set(style="whitegrid")

# Simulated YouTube trending data
data = {
    'title': [
        "Logan Paul Vlog", "MrBeast Giveaway", "Music Video", "Science Experiment", "Tech Review",
        "DIY Room Decor", "Fitness Challenge", "Gaming Walkthrough", "Cooking Recipe", "Comedy Skit"
    ],
    'channel_title': [
        "Logan Paul", "MrBeast", "MusicWorld", "SciFun", "TechZone",
        "CreativeCorner", "FitLife", "GamePlayPro", "TastyKitchen", "LaughOutLoud"
    ],
    'views': [1500000, 2500000, 3200000, 1100000, 1400000, 900000, 1200000, 1800000, 1300000, 1600000],
    'likes': [120000, 300000, 400000, 100000, 110000, 80000, 95000, 150000, 115000, 130000],
    'dislikes': [5000, 4000, 3500, 2000, 1500, 1000, 1200, 1800, 1700, 1600],
    'comment_count': [25000, 35000, 40000, 12000, 14000, 8000, 9500, 15000, 13500, 16000]
}

# Convert to DataFrame
df = pd.DataFrame(data)


# Top 5 by views
top5_views = df.sort_values(by="views", ascending=False).head(5)

# Bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x='views', y='title', data=top5_views, palette='viridis')
plt.title('Top 5 Trending YouTube Videos by Views', fontsize=16)
plt.xlabel('Views')
plt.ylabel('Video Title')
plt.tight_layout()
plt.show()
