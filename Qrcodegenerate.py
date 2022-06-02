import pyqrcode
import pandas as pd


def createQrCode():
    df=pd.read_csv("data2.csv")
    for index,values in df.iterrows():

        name=values["Name"]
        rollno=values["Rollno"]
        qrcode=values["Qrcode"]
        data=f'''

        Name:{name}\n
        Qrcode:{qrcode}\n
        RollNo:{rollno}

        '''
        image=pyqrcode.create(data)
        image.svg(f"{name}_{rollno}_{qrcode}.svg",scale="5")

createQrCode()
