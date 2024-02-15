#!/usr/bin/env python
# coding: utf-8




from fpdf import FPDF

class Bill:
    """
    Object that cointains data about a bill, such as 
    total amount and period of the biil. 
    """
    
    def __init__(self, amount, period):
        
        self.amount = amount 
        self.period = period
    
        
class Flatmate: 
    """
    Creates a flatmate person who lives in the flat 
    and pays a share of the bill. 
    """
    
    def __init__(self, name, days_in_the_house):
    
        self.name = name
        self.days_in_the_house = days_in_the_house
        
        
    
    def pays(self, bill, flatmate2):
        weight = self.days_in_the_house / (self.days_in_the_house + flatmate2.days_in_the_house)
        to_pay = bill.amount * weight
        return to_pay
        

