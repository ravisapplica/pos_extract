# This repo holds ETL scripts which takes clients APIs to extract data for ML models.

# Data download from Winston API

#### RUN cmd: python data_download.py -a <api_key> -s <start_date> -e <end_date> -t <table_name>

#### Arguments:
    api_key = For APIKEY, Please contact Paul
    start_date = Date should be ISO format eg: "2024-07-01" 
    end_date = Date should be ISO format eg: "2024-07-01" 
    table_name = one of the in the below list. Only download daily data for bills and orders.
      
    Total Tables List: ['bills', 'categories', 'courses', 'logged_hours', 'order_courses', 'option_groups', 'options', 'orders', 'products', 'tableplans', 'tables', 'reservations', 'reservationTypes', 'revenueGroups', 'tenant_paymentmethods']

Note: This code runs in USA due to geograhic restrictions on API


## Use this command format to upload local files from your machine to S3 folder.

#### Arguments:
    LocalFolder = LocalFolder till file directory
    bucketName = S3 bucket name
    S3Folder = S3Folder till before table path

#### RUN cmd: python parquetfileupload.py -a <Local_Folder> -s <bucket_Name> -e <S3_Folder>



