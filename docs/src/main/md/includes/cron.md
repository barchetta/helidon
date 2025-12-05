# Cron expression

<div class="formalpara">

<div class="title">

Cron expression format

</div>

    <seconds> <minutes> <hours> <day-of-month> <month> <day-of-week> <year>

</div>

| Order | Name | Supported values | Supported field format | Optional |
|----|----|----|----|----|
| 1 | seconds | 0-59 | CONST, LIST, RANGE, WILDCARD, INCREMENT | false |
| 2 | minutes | 0-59 | CONST, LIST, RANGE, WILDCARD, INCREMENT | false |
| 3 | hours | 0-23 | CONST, LIST, RANGE, WILDCARD, INCREMENT | false |
| 4 | day-of-month | 1-31 | CONST, LIST, RANGE, WILDCARD, INCREMENT, ANY, LAST, WEEKDAY | false |
| 5 | month | 1-12 or JAN-DEC | CONST, LIST, RANGE, WILDCARD, INCREMENT | false |
| 6 | day-of-week | 1-7 or SUN-SAT | CONST, LIST, RANGE, WILDCARD, INCREMENT, ANY, NTH, LAST | false |
| 7 | year | 1970-2099 | CONST, LIST, RANGE, WILDCARD, INCREMENT | true |

Cron expression fields

| Name | Regex format | Example | Description |
|----|----|----|----|
| CONST | \d+ | 12 | exact value |
| LIST | \d+,\d+(,\d+)\* | 1,2,3,4 | list of constants |
| RANGE | \d+-\d+ | 15-30 | range of values from-to |
| WILDCARD | \\ | \* | all values withing the field |
| INCREMENT | \d+\\\d+ | 0/5 | initial number / increments, 2/5 means 2,7,9,11,16,…​ |
| ANY | \\ | ? | any day(apply only to day-of-week and day-of-month) |
| NTH | \\ | 1#3 | nth day of the month, 2#3 means third monday of the month |
| LAST | \d\*L(+\d+\|\\\d+)? | 3L-3 | last day of the month in day-of-month or last nth day in the day-of-week |
| WEEKDAY | \\ | 1#3 | nearest weekday of the nth day of month, 1W is the first monday of the week |

Field formats

| Cron expression      | Description           |
|----------------------|-----------------------|
| \* \* \* \* \* ?     | Every second          |
| 0/2 \* \* \* \* ? \* | Every 2 seconds       |
| 0 45 9 ? \* \*       | Every day at 9:45     |
| 0 15 8 ? \* MON-FRI  | Every workday at 8:15 |

Examples
