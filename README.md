## About bot

This simple bot provides some functionality for automate search apartments on [Booking service](https://www.booking.com) and return result as simple table in console output.

### Prerequestance

Bot works with python and selenium. For correct work of bot must be installed [Chrome webdriver](https://chromedriver.chromium.org/downloads). Bot works with russian version of Booking. With other languages can be issues with some locators.

### Bot Usage

Bot provides functionality for change currency, choose destination (by default chose first element from drop down menu of "Where you going field"), check-in and check-out dates, occupancy field. Also bot supports two filters: sort results from lowest price(used by default) and stars filter. For correctness usage stars filter accept one one or more from next list of values:
- 1 звезда
- 2 звезды
- 3 звезды
- 4 зведы
- 5 звезд

### Bot result

Bot returns three columns table: Hotel Name, Hotel Price, Hotel Score.

[Bot result](/assets/images/expected_result.PNG)