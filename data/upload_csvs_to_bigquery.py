from google.cloud import bigquery
import pandas as pd
import os

# ==========================================
# CONFIGURATION
# ==========================================

PROJECT_ID = "workspaceagent-492209"
DATASET_ID = "enterprise_ops"

CSV_TABLE_MAPPING = {
    "departments.csv": "departments",
    "employees.csv": "employees",
    "projects.csv": "projects",
    "project_resources.csv": "project_resources",
    "revenue_metrics.csv": "revenue_metrics",
    "budget_metrics.csv": "budget_metrics",
    "customer_health.csv": "customer_health",
    "support_tickets.csv": "support_tickets",
    "vendors.csv": "vendors"
}

CSV_FOLDER = "/home/madhu_712/enterprise-ops/data"

# ==========================================
# BIGQUERY CLIENT
# ==========================================

client = bigquery.Client(project=PROJECT_ID)

# ==========================================
# CREATE DATASET IF NOT EXISTS
# ==========================================

dataset_ref = bigquery.Dataset(
    f"{PROJECT_ID}.{DATASET_ID}"
)

try:
    client.get_dataset(dataset_ref)
    print(f"Dataset {DATASET_ID} already exists")
except Exception:
    client.create_dataset(dataset_ref)
    print(f"Created dataset {DATASET_ID}")

# ==========================================
# UPLOAD FILES
# ==========================================

for csv_file, table_name in CSV_TABLE_MAPPING.items():

    file_path = os.path.join(CSV_FOLDER, csv_file)

    if not os.path.exists(file_path):
        print(f"Skipping {csv_file} (not found)")
        continue

    print(f"\nUploading {csv_file} → {table_name}")

    df = pd.read_csv(file_path)

    table_id = f"{PROJECT_ID}.{DATASET_ID}.{table_name}"

    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_TRUNCATE",
        autodetect=True,
        source_format=bigquery.SourceFormat.CSV,
    )

    load_job = client.load_table_from_dataframe(
        df,
        table_id,
        job_config=job_config
    )

    load_job.result()

    table = client.get_table(table_id)

    print(
        f"✓ Loaded {table.num_rows} rows "
        f"into {table_id}"
    )

print("\nAll uploads completed successfully.")