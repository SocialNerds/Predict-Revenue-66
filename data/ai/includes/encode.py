import numpy as np

class Encode:
    """ Encode data to categorical as one hot array """

    def __init__(self):
        pass

    def categorize_values(self, data):
        """ Categorize values to one hot array """
        encoded_data = []

        # We may have to divide by 0 later on latest_utilization = latest_utilization/max(latest_utilization).
        np.seterr(divide='ignore', invalid='ignore')
        
        for item in data:
            month = np.zeros([12])
            month[int(item[0] - 1)] = 1

            day = np.zeros([31])
            day[int(item[1] - 1)] = 1

            hour = np.zeros([24]) 
            hour[int(item[2])] = 1

            week_day = np.zeros([7])
            week_day[int(item[3] - 1)] = 1
 
            not_operational = np.ones([1]) if item[4] == 1 else np.zeros([1])

            latest_utilization = item[5:76]
            
            latest_utilization = latest_utilization/max(latest_utilization)

            encoded_data.append(np.concatenate((month, day, hour, week_day, not_operational, latest_utilization)))

        return np.asarray(encoded_data)
