# khmer_letters_recognition_on_air

Khmer letters recognition on air is an application that can detect and recognize hand writing on air for khmer letters

- This project requires some dependencies to run so make sure you install the required dependencies
```
$ git clone https://github.com/MuongKimhong/khmer_letters_recognition_on_air.git
$ cd khmer_letters_recognition_on_air
$ npm install
$ pip3 install -r requirements.txt
```
**Important** 
- If you use virtual environment make sure you have it activated

### Run project with welcome interface
This project uses electron to build welcome interface. To start it, run:
```
$ npm start
```

### Run project without welcome interface
You can also run this project directly with python module, To start it, run:
- For data collecting mode:
```
$ python3 src/app.py --data True
```
- For predict mode:
```
$ python3 src/app.py --predict True
```

**This project was tested on MacOS and Ubuntu**
