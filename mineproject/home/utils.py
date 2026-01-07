from home.models import Shishir
import time

# we cant run this file here directly because it uses Django models
# so to test this file, we need to run the Django shell or create a Django view
def function_test():
    print("This is a test function.")
    time.sleep(2)
    print("Function test completed.")
