import numpy as np
from random import randint, shuffle
import math
from .encode import Encode

class Data:
    """ Get train data """

    def __init__(self):
        pass

    def get_train_data(self):
        """ Get train data """

        # Create sample train data for now. Get month, day and hour.
        train_data = []
        # Start with wd = 1 which is monday.
        wd = 1
        # Create a variable to be sure that at least on Saturday, the shops will be closed. 
        # This acts like a momentum for possibility.
        smm = 1000.0
        # Previous days operation. If it is 1, it was not operational.
        nopd = np.zeros(5)
        # How many years to add to the data.
        years = 10
        # How many nodes (e.g. shops) there are. We use diferrent variable from
        # years, because there are closed at the same time.
        nodes = 1
        # Utilization factor. We use this to make analogue values.
        uf = 1
        # Last 72 hours ulilization. Probably, I will not normalize this.
        latest_utilization = np.zeros(72)

        for y in range(0, years): # Add the same thing many times.
            for m in range(1, 13):
                for d in range(1, 31):

                    # An indicator when something is not-operational.
                    no = 0

                    # Get random utilization.
                    utilization = (50 * uf) + randint(0, (6 * uf))

                    # Add to utilization if previous days where closed.
                    if (np.array_equal(nopd[-2:], np.array([0, 1]))):
                        utilization += 10 * uf
                    elif (np.array_equal(nopd[-2:], np.ones(2))):
                        utilization += 30 * uf

                    # If it saturday, add 5 to utilization.
                    if (wd == 6):
                        utilization += 20 * uf
                        # Let's create a random condition where a saturday the shop is closed and
                        # the coming monday we have douple utilization.
                        ri = randint(1, 1001)
                        if (ri < (smm * nodes)):
                            print('SM', y, m, d)
                            no = 1
                        
                        smm = smm/(years * nodes * 2)    
                        # If it becomes to small. Make it 1000.0 again.
                        smm = 1000.0 if smm < 0.000000000000000000000000000000000000000000001 else smm

                    # Let's say,that almost every Sunday the shop is clossed.
                    if (wd == 7):
                        ri = randint(1, 100)
                        if (ri > 3):
                            no = 1
                        else:
                            utilization += 30 * uf

                    # Regardless what day it is, every 100 days the shop is closed.
                    ri = randint(1, 100)
                    if (ri < 2):
                        no = 1

                    for h in range(0, 24):

                        # Only work hours.
                        final_no = -1
                        final_utilization = -1
                        if (no == 1):
                            final_no = 1
                            final_utilization = 0
                        else:
                            if (h >= 8 and h < 21):
                                if (h <= 14):
                                    utilization += 2*uf
                                else:
                                    utilization -= 2*uf
                                final_no = 0
                                final_utilization = utilization
                            elif (h < 8 or h > 21):
                                final_no = 1
                                final_utilization = 0
                        
                        train_data.append([np.concatenate((np.array([m, d, h, wd, final_no]), latest_utilization)), np.array([final_utilization])])
                        
                        # Append utilization.
                        latest_utilization = np.append(latest_utilization, [final_utilization])
                        latest_utilization = latest_utilization[-72:]

                    # Append operation for previous days.
                    if (no == 1):
                        nopd = np.append(nopd, [1])
                    else:
                        nopd = np.append(nopd, [0])
                    nopd = nopd[-5:]

                    # Add one to wd or, if it 7, got back to 1.
                    wd = 1 if (wd == 7) else (wd + 1)
    
        # Keep the first elements mod 72. To later devide by 3 day steps.
        train_data = train_data[-self.round_down(len(train_data)):]

        # Convert to numpy array.
        return Encode().categorize_values(np.asarray([item[0] for item in train_data])), np.asarray([item[1] for item in train_data])
    
    def get_test_data(self):
        """ Get test data """

        # Create sample test data for now. Get month, day and hour.
        test_data = []
        # Start with wd = 1 which is monday.
        wd = 2

        smm = 50

        m = 2

        # Last 72 hours ulilization. Probably, I will not normalize this.
        latest_utilization = np.zeros(72)

        for d in range(1, 8):
            # An indicator when something is not-operational.
            no = 0

            # Get random utilization.
            utilization = 50 + randint(0, 6)

            # If it saturday, add 5 to utilization.
            if (wd == 6):
                # Uncomment the three lines below to set Saturday closed.
                # utilization = 0
                # no = 1
                # pass

                utilization += 20
                ri = randint(1, 1001)
                if (ri < smm):
                    print('SM')
                    no = 1
                    smm = smm/10

            # Let's say,that almost every Sunday the shop is clossed.
            if (wd == 7):
                ri = randint(1, 100)
                if (ri > 3):
                    no = 1
                else:
                    utilization += 30

            # Regardless what day it is, every 100 days the shop is closed.
            ri = randint(1, 100)
            if (ri < 2):
                no = 1

            for h in range(0, 24):
                final_no = -1
                final_utilization = -1
                if (no == 1):
                    final_no = 1
                    final_utilization = 0
                else:
                    if (h >= 8 and h < 21):
                        if (h <= 14):
                            utilization += 2
                        else:
                            utilization -= 2
                        final_no = 0
                        final_utilization = utilization
                    elif (h < 8 or h > 21):
                        final_no = 1
                        final_utilization = 0
                
                test_data.append(np.concatenate((np.array([m, d, h, wd, final_no]), latest_utilization)))

                # Append utilization.
                # @todo: On production, I have to append predicted utilization.
                latest_utilization = np.append(latest_utilization, [final_utilization])
                latest_utilization = latest_utilization[-72:]
            
            # Add one to wd or, if it 7, got back to 1.
            wd = 1 if (wd == 7) else (wd + 1)

        return Encode().categorize_values(test_data)

    def round_down(self, x):
        return (int(math.ceil(x / 72.0)) * 72) - 72
    