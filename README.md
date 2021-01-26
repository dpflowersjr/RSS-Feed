# RSS-Feed


RSS-Feed is a python function take in RSS feeds and find which companies have had no activity for a certain amount of days.



## Usage

```python
import src.url_parser

get_latest_publish_date(url:string) # returns lastest_publish_date
get_num_days_without_activity(datetime:date) # returns count in days away from days now
find_company_with_inactivity_for_given_num_of_days(company:dict, number of interactive days : int) # returns list of companies that have been inactive for the given amount of days
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

