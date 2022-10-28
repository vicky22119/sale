
from distutils.command.config import config
from flask import Flask, jsonify, render_template, request
from models.utils import SealsData



app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome sales Prediction")
    return render_template("index.html")


@app.route('/ItemOutletSales',methods = ["GET","POST"])
def sales_prediction():
    if request.method == "POST":
        
        print("We are using POST Method")
        Item_Weight = eval(request.form.get("Item_Weight"))
        Item_Fat_Content = request.form.get("Item_Fat_Content")
        Item_Visibility = eval(request.form.get("Item_Visibility"))
        Item_Type = request.form.get("Item_Type")
        Item_MRP = eval(request.form.get("Item_MRP"))
        Outlet_Identifier = request.form.get("Outlet_Identifier")
        Outlet_Establishment_Year = eval(request.form.get("Outlet_Establishment_Year")) 
        Outlet_Size = eval(request.form.get("Outlet_Size"))
        Outlet_Location_Type = request.form.get("Outlet_Location_Type")
        Outlet_Type = request.form.get("Outlet_Type")

        print(" Item_Weight, Item_Fat_Content, Item_Visibility, Item_Type, Item_MRP, Outlet_Identifier,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type", Item_Weight,
         Item_Fat_Content, Item_Visibility, Item_Type, Item_MRP, Outlet_Identifier,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type)
        
        sales = SealsData(Item_Weight,Item_Fat_Content, Item_Visibility, Item_Type, Item_MRP,
         Outlet_Identifier,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type)
        charges = sales.get_predicted_price()
        print()
        print(f"Predicted Charges for Medical Insurance is {charges}/- Rs. Only")
            
        return render_template("index.html", prediction = charges)    
    else:
        print("We are using GET Method")
        
        Item_Weight = request.args.get("Item_Weight")
        Item_Fat_Content = request.args.get("Item_Fat_Content")
        Item_Visibility = float(request.args.get("Item_Visibility"))
        Item_Type = request.args.get("Item_Type")
        Item_MRP = float(request.args.get("Item_MRP"))
        Outlet_Identifier = request.args.get("Outlet_Identifier")
        Outlet_Establishment_Year =float(request.args.get("Outlet_Establishment_Year")) 
        Outlet_Size = float(request.args.get("Outlet_Size"))
        Outlet_Location_Type = request.args.get("Outlet_Location_Type")
        Outlet_Type = request.args.get("Outlet_Type")    
       
       
       
        sales = SealsData(Item_Weight,Item_Fat_Content, Item_Visibility, Item_Type, Item_MRP,
         Outlet_Identifier,Outlet_Establishment_Year,Outlet_Size,Outlet_Location_Type,Outlet_Type)
        charges = sales.get_predicted_price()
        print()
        print(f"Predicted Charges for Medical Insurance is {charges}/- Rs. Only")
   
        return render_template("index.html", prediction = charges)

if __name__ == ("__main__"):
    app.run(host='0.0.0.0' , port= 5007, debug=True)
    
