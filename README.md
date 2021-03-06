# ghk_filter
1D implementation of g/gh/ghk filter (0/1st/2nd order), or alfa-beta-gamma filter.
Used for some testing on Teensy 4.0 uC. 
Use one class for each filter to keep naming clarity.

This filter is "nothing special", it uses static g/h/k values. 
g/h/k values should be chosen depending on the system and sensors, 
e.g. bigger g if we "trust" sensors more than our system, 
bigger h if we want our system to respond to the changes in "velocity"
more quickly...

For "more advanced" filter implementation check filterpy by rlabbe
(https://github.com/rlabbe/filterpy) and for the theory behind the basic check
his great interactive book
(https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python)
and (https://www.kalmanfilter.net/alphabeta.html).
Boilerplate of filter implementation can be found in examples.

There is too, a python script implementation (g/gh filter) on some data set
that I have had. There can be seen a couple of big spikes at some points, 
this is due to errors in measurements, and this data should be treated as 
an outlier and removed. But it was left to see how g_filter will react to this
data, and "half acceptable" if we use a low g value (we give more weight to 
the static model).
*/
