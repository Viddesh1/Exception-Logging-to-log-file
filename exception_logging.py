import logging

try:
    first_num = int(input("Enter First Number: "))
    second_num = int(input("Enter Second Number: "))
    output = first_num / second_num
    print()
    print(output)

except ZeroDivisionError:
    logger = logging.getLogger('mylog.log')
    hdlr = logging.FileHandler('mylog.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr) 
    logger.setLevel(logging.WARNING)
    logger.error("ZeroDivisionError")
    print()
    print("Trying to Divide by Zero see mylog.log")

except ValueError:
    logger = logging.getLogger('mylog.log')
    hdlr = logging.FileHandler('mylog.log')
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    hdlr.setFormatter(formatter)
    logger.addHandler(hdlr) 
    logger.setLevel(logging.WARNING)
    logger.error("ValueError")
    print()
    print("Value Error see mylog.log")