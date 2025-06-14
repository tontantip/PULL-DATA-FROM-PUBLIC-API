# PULL DATA FROM PUBLIC API.
Hi!👋🏼 welcome to my side project to pull data from a public API, transform it into a Pandas Data Frame, and prepare it for further analysis.
## 5 Pulblic API.
1. Accident information, car crash statistics, accident and car crash statistics on expressways🚗 (EXAT).  [EXAT_API](https://data.go.th/dataset/exat-api-document)
2. Holiday information for each country.🗓️ [Holiday_API](https://date.nager.at/)
3. Open API data for artesian wells nationwide.🚿 [Wells_API](https://data.go.th/dataset/open-api)
4. Summary of import-export value.🪙 [ImportExport_API](https://dataservices.mof.go.th/menu6?id=6&page=&freq=year&yf=2567&search_text=)
5. Reports on earthquakes data.🚨 [earthquakes](https://data.tmd.go.th/api/index1.php)
## Method.
1. Requests API. Choose the interesting data from public API and use library requests in pyrhon for Data exrtraction and retrieved the raw data (JSON).
2. Data Processing. Collect row data into list of data ready to tranformation to Data Frame
3. Transforming to Data Frame. Use pandas such as DataFrame or json_normalize for converted the raw API response into a flat DataFrame.
## Codeing
1. [EXAT_API_code](code/get_api_EXAT.py)
2. [Holiday_API_code](code/get_api_holiday.py)
3. [Wells_API_code](code/get_api_wells.py)
4. [ImportExport_API_code](code/get_api_importexport.py)
5. [Earthquakes_API_code](code/get_api_earthquakes.py)
## Data Frame
1. [EXAT_API_df](DataFrame/EXAT_API.csv)
2. [Holiday_API_df](DataFrame/Holiday_API.csv)
3. [Wells_API_df](DataFrame/Wells_API.csv)
4. [ImEx_API_df](DataFrame/ImEx_API.csv)
5. [Earthquakes_API_df](DataFrame/Earthquakes_API.csv)

