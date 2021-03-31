'''
Description:
   Calculate the distance to Dublin office from the
   given co-ordinates(latitude, longitude) of the customer
   provided in the customer.txt file and list the names and
   user_ids customers of the customers living within 100km(sorted list
   User ID (ascending).
computation1 = sin(latitide_diff / 2)**2 + cos(dub_off_latitude) * \
                           cos(latitide1) * sin(longitude_diff / 2)**2
            computation2 = 2 * asin(sqrt(computation1))
            distance_in_kms = round(computation2 * radius_in_kms, 2)


Haversine formula::
        computation1 = sin(latitide_diff / 2)**2 + cos(dub_off_latitude) * \
                           cos(latitide1) * sin(longitude_diff / 2)**2
        computation2 = 2 * asin(sqrt(computation1))
        distance_in_kms = round(computation2 * radius_in_kms, 2)
   where,
      longitude_diff = longitude1 - dub_off_longitude (difference of latitude)
      latitide_diff = latitide1 - dub_off_latitude  (difference of longitude)
      radius_in_kms is radius of earth i.e 6371 KM or 3961 miles
      and distance_in_kms is the distance computed between two points.

@Since    :  March 2021.
@Author   :  Pallavi Ninad Kakade

'''

import ast
from math import cos, sqrt, sin, radians, asin
from pprint import pprint

class Customer_data_retrieval:
    def customer_details(self):
        """
            @tms_test_steps:
                    @step: Convert the coordinates of Dublin office to radians.
                    @result: The coordinates of Dublin office are converted to radians.
                    @step: Open the customer.txt file in read mode.
                    @result: The customer.txt file is opened in read mode
                    @step: Create an empty customer list to store the user_id and name
                           of customers whose distance is <=100.
                    @result: An empty customer list is created.
                    @step: using with statement open the file and read the data
                    @result: File is opened and read successfully
                    @step: Obtain the cordinates (latitude and longitude) from the file
                    @result: Obtained the latitude and longitude from the file
                    @step: Calculate the Distance using Haversine Formulae
                    @result:The Distance is calculated successfully
                    @step: Check if Distance<=100 then retrieve the name and
                           user_id of the customer
                    @result: The name and user_id of the customer is retrieved.
                    @step: Arrange the list of customers in ascending order of user_ids.
                    @result: The list of customers is arranged in ascending order of user_ids.
                @tms_pre-condition: Save the customer.txt file on local machine and
                                    update the path of the file in code(input_file)
        """
        # dublin office latitude and longitude co-ordinates.
        dub_off_latitude, dub_off_longitude = radians(53.339428), radians(-6.257664)

        # Please provide the path  of the customer data.txt file stored on your local machine
        # input_file = open("/path/to/customers.txt", "r")
        input_file = open("customers.txt", "r")
        customer_dict = {}

        # retrieve  line of the customer.txt file
        with input_file as file1:
            for line in file1:
                line1 = ast.literal_eval(line)
                latitide1 = radians(float(line1.get('latitude')))
                longitude1 = radians(float(line1.get('longitude')))

                dlon = longitude1 - dub_off_longitude
                dlat = latitide1 - dub_off_latitude
                # Radius of earth in kilometers.
                r = 6371
                d1 = sin(dlat / 2)**2 + cos(dub_off_latitude) * cos(latitide1) * sin(dlon / 2)**2
                d2 = 2 * asin(sqrt(d1))
                distance = round(d2 * r, 2)

                if distance <= 100:
                    customer_dict[line1['user_id']] = str(line1['name'])

        pprint(dict(sorted(customer_dict.items())))

def main():
    print('The full list of customers with their names and '
          'user_ids(sorted in ascending order) of matching customers '
          '(within 100km from Dublin office) are :: - ')
    customers = Customer_data_retrieval()
    customers.customer_details()


if __name__ == "__main__":
    main()



