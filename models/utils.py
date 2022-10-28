
import pickle
import json
import pandas as pd
import numpy as np

class SealsData():
    def __init__(self, Item_Weight, Item_Fat_Content, Item_Visibility, Item_Type, Item_MRP, Outlet_Identifier,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type):
        self.Item_Weight = Item_Weight
        self.Item_Fat_Content = Item_Fat_Content
        self.Item_Visibility = Item_Visibility
        self.Item_Type = Item_Type
        self.Item_MRP = Item_MRP
        self.Outlet_Identifier = Outlet_Identifier
        self.Outlet_Establishment_Year = Outlet_Establishment_Year
        self.Outlet_Size = Outlet_Size
        self.Outlet_Location_Type = Outlet_Location_Type
        self.Outlet_Type = Outlet_Type

    def load_model(self):
        with open("models/Linear_regression_seals_data.pkl", "rb") as f:
            self.model = pickle.load(f)

        with open("models/dictionary2.json", "r") as f:
            self.json_data = json.load(f)#instance variable 

    def get_predicted_price(self):

        self.load_model()        # Calling load_model method to get model and json_data

        array = np.zeros(len(self.json_data['columns']))

        array[0] = self.Item_Weight
        array[1] = self.json_data['Item_Fat_Content_values'][self.Item_Fat_Content]
        array[2] = self.Item_Visibility
        array[3] = self.json_data['Item_Type_values'][self.Item_Type]
        array[4] = self.Item_MRP
        array[5] = self.json_data['Outlet_Identifier_values'][self.Outlet_Identifier]
        array[6] = self.Outlet_Establishment_Year
        array[7] = self.Outlet_Size
        array[8] = self.json_data['Outlet_Location_Type_values'][ self.Outlet_Location_Type]
        array[9] = self.json_data['Outlet_Type_values'][self.Outlet_Type]
        
        print("Test Array -->\n",array)
        predicted_charges = self.model.predict([array])[0]
        print("predicted_charges",predicted_charges)
        return np.around(predicted_charges, 2)


if __name__ == "__main__":
    Item_Weight = 9.300000
    Item_Fat_Content = 'Low Fat'
    Item_Visibility = 0.016047
    Item_Type = 'Fruits and Vegetables'
    Item_MRP = 249.809200
    Outlet_Identifier = 'OUT027'
    Outlet_Establishment_Year = 1999.000000
    Outlet_Size = 1.000000
    Outlet_Location_Type = 'Tier 3'
    Outlet_Type = 'Supermarket Type2'

    sales = SealsData(Item_Weight,Item_Fat_Content, Item_Visibility, Item_Type, Item_MRP, Outlet_Identifier,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type)
    charges = sales.get_predicted_price()
    print()
    print(f"Predicted Seals is {charges}/- Rs. Only")
    

    
            