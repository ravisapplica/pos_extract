# This repo holds ETL scripts which takes clients APIs to extract data for ML models.

# Data download from Winston API

#### RUN cmd: python data_download.py -a <apikey> -s <start_date> -e <end_date> -t <table_name>

#### Arguments:
    apikey = For APIKEY, Please contact Paul
    start_date = Date should be ISO format eg: "2024-07-01" 
    end_date = Date should be ISO format eg: "2024-07-01" 
    table_name = one of the in the below list.
      
    ['bills', 'categories', 'courses', 'logged_hours', 'order_courses', 'option_groups', 'options', 'orders', 'products', 'tableplans', 'tables', 'reservations', 'reservationTypes', 'revenueGroups', 'tenant_paymentmethods']

Note: This code runs in USA due to geograhic restrictions on API


