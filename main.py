import os
import sys
from pizzeria.dataset import Order

if __name__ == '__main__':
    mpu_input_file = os.environ.get('MPU_INPUT_FILE', None)
    if not mpu_input_file:
        print("Please set env variable MPU_INPUT_FILE")
        sys.exit(1)

    print("* load order from file")
    order = Order.load_from_file(mpu_input_file)

    print("* order loaded")

    print("* waiting the Mex algorithm before proceeding")
    