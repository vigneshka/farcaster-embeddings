import pyarrow.dataset as ds
from datetime import datetime, timedelta

four_days_ago = datetime.now() - timedelta(days=4)
casts = ds.dataset('raw_data/farcaster-casts-0-1714755600.parquet').to_table(filter=ds.field('timestamp') > four_days_ago)
print(len(casts))