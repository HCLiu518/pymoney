import sys
from datetime import date

class Record:
    """ Represent a record."""
    def __init__(self, date, category, description, amount):
        self._date = date
        self._category = category
        self._description = description
        self._amount = amount
    
class Records:
    """Maintain a list of all the 'Record's and the initial amount of money."""

    """
    initailize the money and records
    """
    def __init__(self, contents = []):
        self._money = int(0)
        self._records = list()
        ### handle file record data
        for line in contents:
            
            items = line.split()

            if len(items) == 1:

                ### Check if the first line is integer
                try:
                    self._money = int(items[0])
                except ValueError:
                    sys.stderr.write(f'{items[0]}: Total amount needs to be integer')
                    sys.exit(1)

            elif len(items) == 4:
                
                ### Check if the amount is integer
                try:
                    int(items[-1])
                    self._records.append(Record(*items))
                except ValueError:
                    sys.stderr.write(f'{list(i for i in items)}: Item amount needs to be integer')
                    sys.exit(1)

    """
    set money
    """
    def set_money(self, money):
        try:
            self._money = int(money)
        except ValueError:
            raise ValueError('The money must be integer.')

    """
    get money
    """
    def get_money(self):
        return str(self._money)

    money = property(lambda self: self.get_money(), lambda self, v: self.set_money(v))

    """
    add new record into the records
    """
    def add(self, record, categories):

        ### Check the input data
        if "" in record[1:]:
            raise ValueError('Please follow the format: Date(Optional) Category Description Amount')

        try:
            if record[0] != "":
                date.fromisoformat(record[0])
            else:
                record[0] = date.today().isoformat()
        except ValueError:
            raise ValueError('The format of date should be YYYY-MM-DD.')
        
        ### Check if the category is valid
        if categories.is_category_valid(record[0]) == False and categories.is_category_valid(record[1]) == False:
            raise ValueError('The specified category is not in the category list.\nYou can check the category list by command "view categories".')

        ### Check if the amount is an integer
        try:
            self._money += int(record[-1])
            self._records.append(Record(*record))
        except ValueError:
            raise ValueError('Amount needs to be an integer.')

    """
    View the records list
    """
    def view(self, records = None):
        if records is None:
            records = self._records
        
        records_list = []
        #body
        for record in records:
            records_list.append(f"{record._date:=<10s} {record._category: <15s} {record._description: <15s} {int(record._amount):+d}")
        
        return records_list

    """
    Delete the record with item's name input
    """
    def delete(self, delete_item):
        
        for i, record in enumerate(self._records):
            record_str = f"{record._date:=<10s} {record._category: <15s} {record._description: <15s} {int(record._amount):+d}"
            if delete_item == record_str:
                self._money -= int(record._amount)
                self._records.pop(i)
                break

    """
    Find categories and view the records
    """
    def find(self, categories):

        if categories == []:
            raise ValueError("Can't find this category")

        filter_records = filter(lambda n: n._category in categories, self._records)
        records_list = []
        for record in filter_records:
            records_list.append(f"{record._date:=<10s} {record._category: <15s} {record._description: <15s} {int(record._amount):+d}")
                
        return records_list

    """
    Save
    """
    def save(self):
        with open('records.txt', 'w') as fh:
            fh.write(str(self._money) + '\n')
            for record in self._records:
                fh.write(f'{record._date} {record._category} {record._description} {record._amount}\n')
        return True
