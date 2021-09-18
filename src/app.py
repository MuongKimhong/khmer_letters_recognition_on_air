import argparse

from scripts.data_collecting import start_data_collecting_mode
from scripts.predict import start_predict_mode


def main():
    if arguments['predict'] != 'True' and arguments['data'] != 'True':
        exception_error = '''
        module app.py requires 1 command line argument but 0 was given.
        -> run < python3 src/app.py --predict True > to enter predict mode
        -> run < python3 src/app.py --data True > to enter data collecting mode
        '''
        raise Exception(exception_error) 
    elif arguments['predict'] == 'True' and arguments['modelpath'] is None:
        raise Exception('''
        preparing to enter predict mode but missing 1 command line argument:
        Error: Missing --modelpath argument
        -> run < python3 src/app.py --predict True --modelpath [path] > to enter
        IMPORTANT : [path] should be a full path from home directory
        ''')
    elif arguments['data'] == 'True' and arguments['savepath'] is None:
        raise Exception('''
        preparing to enter data collecting mode but missing 1 command line argument:
        Error: Missing --savepath argument
        -> run < python3 src/app.py --data True --savepath [path] > to enter
        IMPORTANT : [path] should be a full path from home directory
        ''')
    elif arguments['data'] == 'True' and arguments['savepath'] is not None:
        print("[INFO] Entering data collecting mode...")
        start_data_collecting_mode(arguments['savepath'])
    elif arguments['predict'] == 'True' and arguments['modelpath'] is not None:
        print("[INFO] Entering predict mode...")
        start_predict_mode(arguments['modelpath'])

if __name__ == '__main__':
    arg_object = argparse.ArgumentParser()
    arg_object.add_argument("--predict", help="predict mode", required=False)
    arg_object.add_argument("--data", help="data collecting mode", required=False)
    arg_object.add_argument("--savepath", help="path for saving image", required=False)
    arg_object.add_argument("--modelpath", help="path for pretrained model", required=False)
    arguments  = vars(arg_object.parse_args())
    main()
