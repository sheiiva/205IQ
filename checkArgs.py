############################################
#                MATHEMATICS               #
############################################
#                                          #
#  MONFA-MATAS Patricica & ROZET Corentin  #
#                                          #
#            Project : 205IQ_2019          #
#                                          #
############################################


class ArgumentManager():

    def checkArgs(self, argv):

        """
        Check for arguments validity.
        """

        def isNum(value):

            """
            Return True if value is a digit.
            """

            try:
                int(value)
            except ValueError:
                return False
            else:
                return True

        if (len(argv) > 5 or len(argv) < 3):
            print("Wrong number of arguments. Please run with -h.")
            return 84
        for i in range(1, len(argv)):
            if not isNum(argv[i]):
                print("Arguments should be integers. Please run with -h.")
                return 84
            if (i != 2 and (int(argv[i]) < 0 or int(argv[i]) > 200)):
                print("IQ values must fit between 0 and 200. Please run with -h.")
                return 84
            elif (i == 2 and int(argv[i]) < 0):
                print("Wrong Standard Deviation values. Please run with -h.")
                return 84

        return isNum(0)

    def needHelp(self, argv):

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
