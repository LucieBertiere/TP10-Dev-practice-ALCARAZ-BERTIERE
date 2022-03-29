import argparse
import logging

parser = argparse.ArgumentParser()
parser.add_argument("--input", type=int,
                    help="type the number of terms you want")

args = parser.parse_args()


def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))



def __main__():
    # logging
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler("myscript.log")
    c_handler.setLevel(logging.DEBUG)
    f_handler.setLevel(logging.DEBUG)
    c_format = logging.Formatter('%(name)s - [%(levelname)s] - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] - %(message)s')
    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
    
    # running the function
    my_input = args.input
    logger.info("The --input term of the fibonnaci suite")
    print(fibonacci(my_input))
    
    
__main__()