# Where's my daylight?

[Map of something we want](https://www.timeanddate.com/time/map/)

## Notes:
* Make a long 3 column array where each line is a city name, it's longitude, and it's local time.
* Local time if UTC is at noon June 1 for example.  Because there are probably a bunch of different results depending what calendar day you use because of varying daylight savings times.
* Then it's just a matter of scatter plotting longitude against local time and seeing which places fall close to the trend line and which are way off.
* Animated scatter plot to show daylight savings changing in different places.
* Plenty of details could be different.  Decimal time, x axis could go from 0 to 360.  And I'm not sure how I'd incorporate the calendar day as a variable.  That definitely matters but it would basically necessitate then having like 52 of those arrays for each week of the year.
* The cities with the most "correct" time have an absolute value of 0.
* You want different days to see how daylight savings affects it? Can't we just have a "see before daylight savings" and "after" functions?
* It gets complicated when many countries use different dates.  We don't all change clocks forward and back together, and some places change by a fraction of an hour.  But anyways there should be a way to pick one winter date and one summer date to encompass all the changes and avoid the complicated part in spring and fall

## Future: assign colors to data based on distance from middle of timezone
EXAMPLE
* Green: within 100 miles
* Yellow: within 200 miles
* Red: within 300 miles

## Resources
* [Customizing Plots with Python Matplotlib](https://towardsdatascience.com/customizing-plots-with-python-matplotlib-bcf02691931f)