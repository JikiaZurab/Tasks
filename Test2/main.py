import requests
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, DateTime, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists
from datetime import datetime
import tkinter as tk
from tkinter import ttk
import traceback

# Checks existence of the DB
def check_for_DB(db_path):
    try:
        engine = create_engine(db_path)
        engine.connect()
        return True

    except NoSuchModuleError:
        return False

# Creates SQLite DB
db_path = "sqlite+pysqlite:///currencyRates.db"


engine = create_engine(db_path, echo=True)

Session = sessionmaker(engine)
session = Session()

Base = declarative_base()

# Changes label text to current DB dates rate
def change_curr_date_label(label):
    dt = session.query(CurrencyDB.date).first()
    label.config(text="Курс от  " + dt[0].strftime('%Y-%m-%d %H:%M:%S'))


class CurrencyDB(Base):

    __tablename__ = "Currency"

    id = Column(Integer, primary_key=True)
    currency = Column(String)
    rate = Column(Float)
    date = Column(DateTime)

    def __init__(self, currency, rate, date):
        self.currency = currency
        self.rate = rate
        self.date = date

# Creates and rewrites DB
def fill_up_db():
    try:
        # If we have DB it will be dropped and then rewritten
        if database_exists(db_path):
            Base.metadata.drop_all(engine)

        Base.metadata.create_all(engine)

        # Where USD is the base currency you want to use
        url = 'https://v6.exchangerate-api.com/v6/f313562c2676e227979bf963/latest/USD'

        # Making our request
        response = requests.get(url)
        data = response.json()

        if data["result"] == "success":

            for curr, rt in  data["conversion_rates"].items():
                new_data = CurrencyDB(currency = str(curr), rate = float(rt), date = datetime.strptime(data["time_last_update_utc"], '%a, %d %b %Y %H:%M:%S %z'))
                session.add(new_data)
                session.commit()

            results = session.query(CurrencyDB).all()

            change_curr_date_label(label)
            cb_add_curr(cb1)
            cb_add_curr(cb2)

        else:
            print("Something went wrong with query for API")
            label.config(text="Something went wrong with query for API")

    except Exception as e:
        print('Something went wrong with DB creation')
        traceback.print_exc()

def rates_viewer():
    if cb1.get() == "":
        label3.config(text="К сожалению, у нас нету курса валют")
    else:
        rates_window = tk.Toplevel(window)
        rates_window.title("Rates")

        # Table creation
        tree = ttk.Treeview(rates_window)
        tree["columns"] = ('ID','Currency','Rate')

        tree.column("#0", width=0, stretch=tk.NO)
        tree.column('ID', width=50)
        tree.column('Currency', width=150)
        tree.column('Rate', width=150)

        tree.heading('ID', text='ID')
        tree.heading('Currency', text='Currency')
        tree.heading('Rate', text='Rate')

        results = session.query(CurrencyDB).all()

        # Process the retrieved data
        for result in results:
            tree.insert("", tk.END, values=(result.id, result.currency,result.rate))

        tree.pack()

def cb_add_curr(cb):
    results = session.query(CurrencyDB).all()
    lst = list()
    for result in results:
        lst.append(result.currency)
    cb['values'] = lst
    cb.current(0)

def input_validator(line):
    if line.isdigit() or line == "":
        return True
    else:
        return False

def change_currency():
    if entry.get() == "":
        label3.config(text="Вы не ввели сумму для обмена")
    elif cb1.get() == "":
        label3.config(text="Пожалуйста, получите сначала курс валют")
    else:
        results = session.query(CurrencyDB).all()
        for result in results:
            if result.currency == cb1.get():
                r1 = result.rate
            if result.currency == cb2.get():
                r2 = result.rate
        s = "За " + entry.get() + " " + cb1.get() + " Вы получите " +  str("{:.2f}".format(round(float(entry.get())/r1*r2),2)) + " " + cb2.get()
        label3.config(text=s)


if __name__ == "__main__":

    try:
        # GUI starts from here
        # Create a new Tkinter window
        # Add widgets (e.g., buttons, labels, etc.) to the window
        window = tk.Tk()
        window.title('Currency changer')
        # Window size
        w = int(window.winfo_screenwidth() / 4)
        h = int(window.winfo_screenheight() / 4)
        window.geometry(f"{w}x{h}")

        label = tk.Label(window, text="")
        label.pack()

        cb1 = ttk.Combobox(window, state="readonly")
        cb1['values'] = ('')
        cb1.pack()

        label1 = tk.Label(window, text="Меняем в количестве")
        label1.pack()

        # Validate and Key checkes every single pressed botton (%P it's a current inputs)
        validation = window.register(input_validator)
        entry = tk.Entry(window, validate="key", validatecommand=(validation, '%P'))
        entry.pack()

        label2 = tk.Label(window, text="Получим")
        label2.pack()

        cb2 = ttk.Combobox(window, state="readonly")
        cb2['values'] = ('  ')
        cb2.pack()

        label3 = tk.Label(window, text="   ")
        label3.pack()

        # If DB exists we filling up empty fields
        if database_exists(db_path):
            change_curr_date_label(label)
            cb_add_curr(cb1)
            cb_add_curr(cb2)
        else:
            label.config(text="Нет данных о курсах валют")

        b1 = tk.Button(window, text="Обмен Валюты", command = change_currency)
        b1.pack()

        b2 = tk.Button(window, text="Посмотреть курс", command = rates_viewer)
        b2.pack()

        b3 = tk.Button(window, text="Получить актуальный курс", command = fill_up_db)
        b3.pack()

        window.mainloop()

    except Exception as e:
        print('Something went wrong in the main brench')
        traceback.print_exc()
