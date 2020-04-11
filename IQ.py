############################################
#                MATHEMATICS               #
############################################
#                                          #
#  MONFA-MATAS Patricica & ROZET Corentin  #
#                                          #
#            Project : 205IQ_2019          #
#                                          #
############################################

from math import sqrt, exp, pi
from sys import argv


class IQ():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._u = int(argv[1])
        self._std = int(argv[2])
        self._iq1 = 0
        self._iq2 = 0
        self._values = []

        if (len(argv) > 3):
            self._iq1 = int(argv[3])
        if (len(argv) > 4):
            self._iq2 = int(argv[4])

    def normalDistribution(self, x):

        """
        Compute the Normal Distribution of x,
            using _u the mean value and _std the standard deviation.
        """

        return (1 / (self._std * sqrt(2 * pi))) * exp(-(pow(x - self._u, 2) / (2 * self._std * self._std)))

    def getBound(self, bmin, bmax):

        """
        Print %percentage of poeple having an IQ between bmin and bmax.
        """

        i = bmin
        result = 0
        while i < bmax:
            result += self.normalDistribution(i)
            i += 0.01

        if (not bmin):
            print("{:.1f}% of people have an IQ inferior to {}".format(result, bmax))
        else:
            print("{:.1f}% of people have an IQ between {} and {}".format(result, bmin, bmax))

    def plotDensityFunction(self):

        """
        Print each value of _values.
        """

        for i in range(201):
            print("{} {:.5f}".format(i, self._values[i]))

    def run(self):

        """
        Run computations and process output printing.
        """

        for i in range(201):
            self._values.append(self.normalDistribution(i))

        if (not self._iq1 and not self._iq2):
            self.plotDensityFunction()
        elif (not self._iq2):
            self.getBound(0, self._iq1)
        else:
            self.getBound(self._iq1, self._iq2)
