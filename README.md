# python-qr-email

Python script to send automated email with embedded QR code generated from user data on the go.

## Philosophy
In this example program, a QR code is generated from user data and the then the QR coded is embedded in the email body as multipart/related. This can be served as a conformation mail from an organization to the end user.

### Dependencies
* [Jinja2==2.11.2](https://github.com/pallets/jinja) 
* [MarkupSafe==1.1.1](https://github.com/pallets/markupsafe)
* [pypng==0.0.20](https://github.com/drj11/pypng)
* [PyQRCode==1.2.1](https://github.com/mnooner256/pyqrcode)
* [python-dotenv==0.14.0](https://github.com/theskumar/python-dotenv)


All dependencies are listed in the [requirments.txt](requirments.txt) file. You can use PIP to install all dependencies directly from the requirments.txt file with following command.

```
pip install requirments.txt
```

### How it works

The actual project directory looks as:
```
proj
    ├── data.csv                    (user data)
    ├── mail_test.py                (python script)
    ├── README.md
    ├── .env                        (Email credentials)
    ├── requirments.txt
    ├── templates
    │    └── temp.html.jinja        (HTML template for email body)
    └── tests.log                   (result logs)


```
Keep your email address and password secret in .env file. Add following lines in .env file

```
TEST-EMAIL=your email address
TEST-EMAIL-PASS=your email password
```

If your directory heirarchey is ready then you are ready to test it yourself

```
python3 mail_test.py
```


## Authors

* **Halder Sudipto Dip** - *Initial work* - [sudipto-003](https://github.com/sudipto-003)


## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE version 3 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Inspiration
* etc
