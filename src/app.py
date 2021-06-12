import argparse

from scripts.data_collecting import start_data_collecting_mode


def main():
    if arguments['predict'] != 'True' and arguments['data'] != 'True':
        exception_error = '''
        module app.py requires 1 command line argument but 0 was given.
        -> run < python3 src/app.py --predict True > to enter predict mode
        -> run < python3 src/app.py --data True > to enter data collecting mode
        '''
        raise Exception(exception_error)
    elif arguments['predict'] == 'True':
        print("[INFO] Entering predict mode...")
    else:
        print("[INFO] Entering data collecting mode...")
        start_data_collecting_mode()


if __name__ == '__main__':
    arg_object = argparse.ArgumentParser()
    arg_object.add_argument("-p", "--predict", help="predict mode", required=False)
    arg_object.add_argument("-d", "--data", help="data collecting mode", required=False)
    arguments  = vars(arg_object.parse_args())
    main()
