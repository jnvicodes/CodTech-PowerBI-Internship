import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# This script creates a simulated "Live" dataset
# It uses the current time to show real-time movement
now = datetime.now()

# We generate 20 rows of data ending at the current second
data = {
    'Timestamp': [now - timedelta(seconds=i*5) for i in range(20)],
    'Live_Value': np.random.randint(40, 100, size=20)
}

# Converting to a DataFrame for Power BI to read
df = pd.DataFrame(data)