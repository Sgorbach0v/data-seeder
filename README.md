# Data seeder tool
## Description
This tool generates queries that could be used for data seeding for modelling or for testing a dialogue system.
The algorithm outputs all the combinations for a query by iterating over its syntactic structure and synonyms.
Hundreds of thousands of valid queries could be easily created by using this tool

## How to use this tool
1. Pick a query with one intent
Set alarm
2. Come up with various syntactic structures for the query
Set alarm
Set my alarm
Set my alarm now
Set my alarm now please
Please set my alarm
...
3. Fill out a table with the longest query on top where one word takes one cell. Note: I used Google Sheets to enter my data
| First element  | Second element | Third element | Fourth element | Fifth element |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Set  | my  | alarm  | now  | please |
| Please | set  | my  | alarm  | asd |
| Set  | my  | alarm  | now | asd |
| Set  | my  | alarm  | asd | asd |
| Set  | alarm  | asd | asd | asd |

4. Identify the least common multiples for the queries in terms of their syntactic position. It will be the root query
| First element  | Second element |
| Set  | alarm  |
5.a Expand the root query by adding additional elements anywhere in the structure, so that the whole query is still correct
5.b Everything except for the root query should me marked as optional and will be used once and then omitted when generating queries
5.c Rename the column headers to 1, 2, 3, 4, ...
| 1  | 2  | 3 | 4 | 5 | 6 |
| Please  | Set  | my | alarm  | now | please |
| optional |  | optional |  | optional | optional |
6.a Expand the query by adding more elements to the structure
6.b List the synonyms in the column
| 1  | 2  | 3 | 4 | 5 | 6 |
| Could you    | please  | Set  | my | alarm  | now | please |
| Can you    |   |   |  |   |  |  |
| Will you    |   |   |  |   |  |  |
| Would you    |   |   |  |   |  |  |
| optional    | optional |  | optional |  | optional | optional |
7. The input data should be in .csv format. I used downloaded my Google Spreadsheet as csv and used it in the script.
The structure of the spreadsheet should be exactly the same as in my example.
8. The tool will iterate over all the combinations in the example and will output a csv

Note: More documentation will be added later

#### Developed in Fall 2018
