205IQ
===

Time:       2 weeks

Team:       2

Language:   Python


The project
----
Most of the reference curves, such as weight and height cruves, are created using **Gaussian distributions**.These curves appear to correctly describe “normality”, and that is why the **Gaussian distribution** is also called [**normal distribution**](https://en.wikipedia.org/wiki/Normal_distribution).

IQ tests are calibrated so that the results follow a normal distribution. The interpretation of the resulting IQ obviously depends on the calibration of the test. Most of the time, the mean is equal to 100. The **standard deviation** is usually 15 but can vary *(24 in the Cattell test, for example)*. **IQ values are always between 0 and 200**.

Your psychiatrist, **Dr. Von Humleit**, plans to create his own IQ test, which is supposed to be better suited to the current population than the classical tests from previous centuries. To help him calibrate his test, you have to program the following tasks:
* Given ***μ*** and ***σ***, plot the density function of the IQ for every integer between 0 and 200.
* Given ***μ***, ***σ*** and one IQ value, print the percentage of people with an IQ inferior to this value.
* Given ***μ***, ***σ*** and two IQ values, print the percentage of people with an IQ in between those values.


## USAGE:

```
>> ./205IQ u s [IQ1] [IQ2]
```

#### DESCRIPTION
u       mean
s       standard deviation
IQ1     minimum IQ
IQ2     maximum IQ

# BONUS:

> prerequisite: [`Gnuplot`](http://www.gnuplot.info/) graphical library

```
>> ./205IQ *u* *s* > data
>> cat bonus/drawer.gnu | gnuplot
```

The graph related to the `data` output file will be plot in an `image.png file`.

Author [**Corentin COUTRET-ROZET**](https://github.com/sheiiva) and [**PATRICIA MONFA-MATAS**](https://github.com/patumm)
