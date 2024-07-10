# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Konto(ABC):
    '''
    A class to represent a bank account with some
    basic functionalities
    '''
    # bankname for all accounts
    bankname = 'SPK'
    
    def __init__(self, inhaber: str, kontonr: int, kontostand: float = 0.0):
        '''
        intializing a basic account with private attributes:
            inhaber: account holder name (str)
            kontonr: account number (str)
            kontostand: account balance (float)
            !!!This is an abstract class which acts as a base class for
            other sub-classes!!!
        '''
        
        self.__inhaber = inhaber
        self.__kontonr = kontonr
        self.__kontostand = kontostand
        
    # necessary getter and setter functions   
    @property
    def inhaber(self):
        return self.__inhaber
    
    @property
    def kontonr(self):
        return self.__kontonr
    
    @property
    def kontostand(self):
        return self.__kontostand
    
    @kontostand.setter
    def kontostand(self, value):
        self.__kontostand = value 
    
    def __str__(self):
        '''
        string represatation of a bank account
        '''
        return f'{self.__class__.__name__} (Inhaber {self.inhaber}, Kontonr. {self.kontonr}, Bank {Konto.bankname}) mit Kontostand {self.kontostand}'

    
    def einzahlen(self, betrag):
        '''
        basic deposit method for all accounts
        '''
        self.__kontostand += betrag
        
    def auszahlen(self, betrag, limit=0):
        '''
        basic payment method for all accounts
        works only if it doesn't exceed the lower limit
        '''
        if self.kontostand - betrag >= limit:
            self.__kontostand -= betrag
            return True
        
        return False
    
    @abstractmethod
    def kalkuliere_zinsen(self):
        '''
        must be implemented in all sub-classes
        interest rate calculation: specific for each type of account
        '''
        pass
    
    @classmethod
    def aendere_bankname(cls, neuer_name):
        '''
        changes the bankname for all accounts
        args: neuer_name (str), new name for the bank
        returns: None, sets the bankname to the given name
        '''
        cls.bankname = neuer_name 


class Sparbuch(Konto):
    '''
    A class to represnt a basic savings account
    inherits from class "Konto"
    '''
    # default interest rate
    zinssatz_haben_standard = 0.01
    
    def __init__(self, inhaber: str, kontonr: str,
                 zinssatz_haben: float=zinssatz_haben_standard):
        '''
        initializing a basic savings account with attributes of
        the inherited class "Konto" and another attribute:
            zinssatz: interest rate (float)
            These attributes can be accessed from outside but can't be
            changed from outside
        '''
        # initializng the attributes from the base class
        super().__init__(inhaber, kontonr)
        self.__zinssatz_haben = zinssatz_haben
       
    @property
    def zinssatz_haben(self):
        return self.__zinssatz_haben
    
    
    def kalkuliere_zinsen(self, zinssatz=None, limit=0):
        '''
        calculates the interests for the account
        returns True if possible and updates the balance, False otherwise
        '''
        # if the method is being used by the object of this class and
        # not any sub class
        if not zinssatz: 
            zinssatz = self.zinssatz_haben
        if self.kontostand > limit: # if balnace larger than zero or in case there is a limit,
            # larger than that limit
            # self.kontostand = self.kontostand + self.kontostand * zinssatz
            super().einzahlen(self.kontostand * zinssatz)
            return True
        return False
        
        
class Girokonto(Sparbuch):
    '''
    a class to represent a basic current account
    inherits from class for savings accounts "Sparbuch"
    '''
    
    zinssatz_soll_standard = 0.12
    
    def __init__(self, inhaber: str, kontonr:str, kreditlimit,
                 zinssatz_soll: float=zinssatz_soll_standard,
                 zinssatz_haben: float=Sparbuch.zinssatz_haben_standard):
        '''
        initializing a basic savings account with attributes of
        the inherited class "Sparbuch" and two more attributes:
            kreditlimt: lower limit 
            zinssatz_soll: interest rate (float)
            These attributes can be accessed from outside but can't be
            changed from outside
        '''
        super().__init__(inhaber, kontonr, zinssatz_haben)
        self.__kreditlimit = kreditlimit
        self.__zinssatz_soll = zinssatz_soll
        
    
    @property
    def kreditlimit(self):
        return self.__kreditlimit
    
    @property
    def zinssatz_soll(self):
        return self.__zinssatz_soll
    
    def auszahlen(self, betrag):
        '''
        special payment method for all 'current' accounts
        returns True if balance not under the limit and updates the balance
        returns False if payment not possible with the given limit
        '''
        return super().auszahlen(betrag, self.kreditlimit)
    
    def kalkuliere_zinsen(self):
        '''
        calculates the interests for the account
        returns True if possible, False otherwise
        '''
        # interest rate differs when the balance is positive and when it is negative
        if self.kontostand < 0:
            return super().kalkuliere_zinsen(zinssatz=self.zinssatz_soll,
                                             limit=self.kreditlimit)
        
        return super().kalkuliere_zinsen(limit=self.kreditlimit)
    

class Bausparkonto(Sparbuch):
    '''
    a class to represent a builduing-savings account
    '''
    def __init__(self, inhaber: str, kontonr: str, 
                 zuteilungsbetrag: float,
                 zinssatz_haben: float=Sparbuch.zinssatz_haben_standard):
        '''
        Parameters
        ----------
        inhaber : str
            account holder.
        kontonr : str
            account number.
        zinssatz_haben : float, optional
            interest rate. The default is zinssatz_haben_standard.
        zuteilungsbetrag : float
            limit amount for savings balance.
        -------
        initializes a building-savings account
        '''
        super().__init__(inhaber, kontonr, zinssatz_haben)
        self.__zuteilungsbetrag = zuteilungsbetrag
        self.__sparmodus = True
    
    
    @property
    def zuteilungsbetrag(self):
        return self.__zuteilungsbetrag

    
    def einzahlen(self, betrag):
        '''
        special method for deposits in the building-savings account
        '''
        # if the balance exceeds the set limit then the payments will be activated
        # and the interest rate will be zero
        super().einzahlen(betrag)
        if self.kontostand >= self.zuteilungsbetrag:
            self.__sparmodus = False
            
            
    def auszahlen(self, betrag):
        '''
        special method for payments from the building-savings account
        '''
        if not self.__sparmodus: # only allowed when saving mode is no longer activated
            return super().auszahlen(betrag)
        return False
        
    def kalkuliere_zinsen(self):
        '''
        special method for calculating the interest rate for the building-savings account
        '''
        if self.__sparmodus: # only when in savings mode
            # return super().kalkuliere_zinsen()
            self.einzahlen(self.kontostand * self.zinssatz_haben)
            return True
        
        return False
    
