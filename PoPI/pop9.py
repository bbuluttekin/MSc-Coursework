# Bank Account Classes


class Person:
    '''to handle person's details'''

    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln
        self.address = None  # addresses stored by strings

    def set_address(self, adr):
        self.address = adr  # strings


class IndividualBankAccount:
    '''to handle individual bank account data'''

    def __init__(self, sort_code, account_number, owner):
        '''TD implement this; creates a bank account
        with sort code as string, account number as string,
        and owner as Person'''
        self.sort_code = sort_code
        self.account_number = account_number
        self.owner = owner

    def set_sort_code(self, sort_code):
        '''TD implement this; updates sort code'''
        self.sort_code = sort_code

    def get_sort_code(self):
        '''TD implement this; returns sort code'''
        return self.sort_code

    def set_account_number(self, account_number):
        '''TD implement this; updates account number'''
        self.account_number = account_number

    def get_account_number(self):
        '''TD implement this; returns account number'''
        return self.account_number

    def get_account_data(self):
        '''TD implement this; returns string "FN LN SC AN"
        where FN and LN are owner's first and last names,
        SC is sort code, AN is account number'''
        return '{} {} {} {}'.format(self.owner.first_name, self.owner.last_name, self.sort_code, self.account_number)


class SharedBankAccount:
    '''to handle data of an account that has several owners'''

    def __init__(self, sort_code, account_number, owners):
        '''TD implement this; creates a bank account
        with sort code as string, account number as string,
        and owners as a list of Persons'''
        self.sort_code = sort_code
        self.account_number = account_number
        self.owners = owners

    def set_sort_code(self, sort_code):
        '''TD implement this; updates sort code'''
        self.sort_code = sort_code

    def get_sort_code(self):
        '''TD implement this; returns sort code'''
        return self.sort_code

    def set_account_number(self, account_number):
        '''TD implement this; updates account number'''
        self.account_number = account_number

    def get_account_number(self):
        '''TD implement this; returns account number'''
        return self.account_number

    def get_account_data(self):
        '''TD implement this; returns string
        "FN1 LN1, FN2 LN2, ..., FNM LNM, SC AN"
        where FNi LNi is the i-th owner first and last names,
        SC is sort code, AN is account number'''
        owner_str = ''
        for i in self.owners:
            owner_str += (i.first_name + ' ')
            owner_str += (i.last_name + ', ')
        return owner_str + self.sort_code + ' ' + self.account_number


# NO modifications below this line
import sys
complete_input = sys.stdin.readlines()
for line in complete_input:
    exec(line)

# Bank Account Classes with Inheritance


class Person:
    '''to handle person's details'''

    def __init__(self, fn, ln):
        self.first_name = fn
        self.last_name = ln
        self.address = None  # addresses stored by strings

    def set_address(self, adr):
        self.address = adr  # strings


class BankAccount:
    def __init__(self, sort_code, account_number):
        '''TD implement this; creates a bank account
        with sort code as string and account number as string'''
        self.sort_code = sort_code
        self.account_number = account_number

    def set_sort_code(self, sort_code):
        '''TD implement this; updates sort code'''
        self.sort_code = sort_code

    def get_sort_code(self):
        '''TD implement this; returns sort code'''
        return self.sort_code

    def set_account_number(self, account_number):
        '''TD implement this; updates account number'''
        self.account_number = account_number

    def get_account_number(self):
        '''TD implement this; returns account number'''
        return self.account_number

    def get_account_data(self):
        '''TD implement this; returns string "SC AN"
        where SC is sort code, AN is account number'''
        return '{} {}'.format(self.sort_code, self.account_number)


class IndividualBankAccount(BankAccount):
    def __init__(self, sort_code, account_number, owner):
        super().__init__(sort_code, account_number)
        '''line above sets up sc and number
        TD implement setting up an owner as Person'''
        self.owner = owner

    def get_account_data(self):
        '''TD implement this; returns string "FN LN SC AN"
        where FN and LN are owner's first and last names,
        SC is sort code, AN is account number'''
        f_name_str = self.owner.first_name + ' ' + self.owner.last_name
        account_str = self.sort_code + ' ' + self.account_number
        return f_name_str + ' ' + account_str


class SharedBankAccount(BankAccount):
    def __init__(self, sort_code, account_number, owners):
        super().__init__(sort_code, account_number)
        '''line above sets up sc and number
    TD implement setting up an owners as a list of Persons'''
        self.owners = owners

    def get_account_data(self):
        '''TD implement this; returns string
        "FN1 LN1, FN2 LN2, ..., FNM LNM, SC AN"
        where FNi LNi is the i-th owner first and last names,
        SC is sort code, AN is account number'''
        owner_str = ' '
        for owner in self.owners:
            owner_str += (owner.first_name + ' ')
            owner_str += (owner.last_name + ', ')
        acc_str = self.sort_code + ' ' + self.account_number
        return owner_str + ' ' + acc_str


# NO modifications below this line
import sys
complete_input = sys.stdin.readlines()
for line in complete_input:
    exec(line)
