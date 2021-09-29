import streamlit as st
import requests
import pandas as pd
import json 


st.title('Cars Django demo app')


#GET ALL CAR DETAILS
st.write("Display all records")
submit = st.button('Submit',key =1)
if submit:
    response = requests.get("http://127.0.0.1:8000/api/car/")
    print(response.json())
    data_table1 = pd.DataFrame(response.json())
    st.write(data_table1)
else:
    pass

#GET SPECIFIC CAR DETAIL
st.write("Get Specific car records based on id")
user_input = None
user_input = st.text_input("enter car id", None)
submit = st.button('Submit', key=2)
if submit and user_input is not None:
    url ="http://127.0.0.1:8000/api/car/{}/".format(user_input)
    #print(url)
    response = requests.get(url)
    #print(response.json())
    data_table1 = pd.DataFrame(response.json(), index=[0])
    st.write(data_table1)
else:
    pass

#GET SPECIFIC CAR DETAIL
st.write("Add New Car Records")
carname = st.text_input("enter carname", None, key=1)
carcompany = st.text_input("enter carcompany ", None,key=2)
driveline = st.text_input("enter driveline", None, key=3)
geartype = st.text_input("enter geartype", None, key=4)

submit = st.button('Submit',key=3)
if submit:

    print("code entered")

    url = "http://127.0.0.1:8000/api/car/"
    #data = {'carname': carname , 'carcompany': carcompany, 'driveline': driveline, 'geartype': geartype }
#     data = {
#     "carname": "new",
#     "carcompany": "new1",
#     "driveline": "sdfsdf3",
#     "geartype": "tesdfsd"
# }

    data = {
    "carname": carname,
    "carcompany": carcompany,
    "driveline": driveline,
    "geartype": geartype
}
    #headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}  headers=headers
    r = requests.post(url, json=data)
    print(r.status_code)
    print(r.json())

    if r.status_code == 201:
        st.write('Records added')

else:
    pass



#GET SPECIFIC CAR DETAIL
st.write("delete a record")
submit = st.button('Submit',key=4)
if submit:

    print("code entered")

    url = "http://127.0.0.1:8000/api/car/9/"
    #data = {'carname': carname , 'carcompany': carcompany, 'driveline': driveline, 'geartype': geartype }
#     data = {
#     "carname": "new",
#     "carcompany": "new1",
#     "driveline": "sdfsdf3",
#     "geartype": "tesdfsd"
# }

    data =  {
        "carname": "addedfromui",
        "carcompany": "asdas",
        "driveline": "fghfg",
        "geartype": "werwe"
    }
    #headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}  headers=headers
    r = requests.delete(url)
    print(r.status_code)
    print(r.json())

    if r.status_code == 201:
        st.write('Records deleted')

else:
    pass