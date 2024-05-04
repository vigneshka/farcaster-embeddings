import pyarrow.parquet as pq

file_path = 'raw_data/farcaster-casts-0-1714755600.parquet'

parquet_file = pq.ParquetFile(file_path)

casts = next(parquet_file.iter_batches(batch_size = 1000)) 
