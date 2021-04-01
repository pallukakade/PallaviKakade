'''
Description:
   Calculate the distance to Dublin office from the
   given co-ordinates(latitude, longitude) of the customer
   provided in the customer.txt file and list the names and
   user_ids customers of the customers living within 100km(sorted list
   User ID (ascending).

Haversine formula::
        compute1 = sin(latitide_diff / 2)**2 + cos(dub_off_latitude) * \
                           cos(latitide1) * sin(longitude_diff / 2)**2
        compute2 = 2 * asin(sqrt(compute1))
        distance_in_kms = round(compute2 * radius_in_kms, 2)
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
    def calculate_distance_haversine_formulae(self):
        """
           @tms_test_steps:
              @step: Create an empty customer list to store the user_id and name
                     of customers whose distance is <=100.
              @result: An empty customer list is created.
              @step: open the file in read mode.
              @result: File is opened in read mode
              @step: Obtain the coordinates (latitude and longitude)
                      from the customer.txt file
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
        # empty customer dictionary is created
        customer_dict = {}

        # retrieve  line of the customer.txt file
        with input_file as file1:
            for line in file1:
                line1 = ast.literal_eval(line)

                latitide1 = radians(float(line1.get('latitude')))
                longitude1 = radians(float(line1.get('longitude')))

                longitude_diff = longitude1 - dub_off_longitude
                latitude_diff = latitide1 - dub_off_latitude

                compute1 = sin(latitude_diff / 2)**2 + cos(dub_off_latitude) * cos(latitide1) * sin(longitude_diff / 2)**2
                compute2 = 2 * asin(sqrt(compute1))
                distance_in_kms = round(compute2 * radius_in_kms, 2)

                if distance_in_kms <= 100:
                    customer_dict[line1['user_id']] = str(line1['name'])

        print('The full list of customers with their names and '
              'user_ids(sorted in ascending order) of matching customers '
              '(within 100km from Dublin office) are :: - ')
        pprint(dict(sorted(customer_dict.items())))
        

if __name__ == "__main__":
    """
       @tms_test_steps:
           @step: Convert the coordinates of Dublin office to radians.
           @result: The coordinates of Dublin office are converted to radians.
           @step: Open the customer.txt file in read mode.
           @result: The customer.txt file is opened in read mode
       @tms_pre-condition: Save the customer.txt file on local machine and
                            update the path of the file in code(input_file)
    """
    # dublin office latitude and longitude co-ordinates.
    dub_off_latitude, dub_off_longitude = radians(53.339428), radians(-6.257664)

    # Please provide the path  of the customer data.txt file stored on your local machine
    # input_file = open("/path/to/customers.txt", "r")
    input_file = open("customers.txt", "r")

    # Radius of earth in kilometers.
    radius_in_kms = 6371

    # Initiate the object and call the method
    customers = Customer_data_retrieval()
    customers.calculate_distance_haversine_formulae()
