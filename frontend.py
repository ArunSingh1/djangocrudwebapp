import streamlit as st
import requests
import pandas as pd
import json 

st.title('Cars Django demo app')


#GET ALL CAR DETAILS
st.header("Display all records")
submit = st.button('Submit',key =1)
if submit:
    response = requests.get("http://127.0.0.1:8000/api/car/")
    print(response.json())
    data_table1 = pd.DataFrame(response.json())
    st.write(data_table1)
else:
    pass


#ADD CAR RECORDS

st.header("Add New Car Records")
carname = st.text_input("enter carname", key=1)
carcompany = st.text_input("enter carcompany ",key=2)
driveline = st.text_input("enter driveline",  key=3)
geartype = st.text_input("enter geartype",  key=4)

submit = st.button('Submit',key=3)
if submit:

    print("code entered")

    url = "http://127.0.0.1:8000/api/car/"

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

else:
    pass


########################################################################
#GET SPECIFIC CAR DETAIL
st.header("Get Specific car records based on id")
user_input = None
user_input = st.text_input("enter car id")
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



#################################################################################
#ALTER SPECIFIC CAR DETAIL
st.header("Edit exsisting car records with car id")
id = st.text_input("enter carid to edit", key=141)
carname = st.text_input("enter carname", key=142)
carcompany = st.text_input("enter carcompany ", key=143)
driveline = st.text_input("enter driveline", key=144)
geartype = st.text_input("enter geartype", key=145)

submit = st.button('Submit',key=146)
if submit:

    print("code entered")

    url = "http://127.0.0.1:8000/api/car/{}/".format(id)

    data = {
    "carname": carname,
    "carcompany": carcompany,
    "driveline": driveline,
    "geartype": geartype
}
    #headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}  headers=headers
    r = requests.put(url, json=data)
    print(r.status_code)
    print(r.json())

    if r.status_code in [200,201,204]:
        st.write('Records edited')
    else:
        pass

else:
    pass



#############################################################################
#DELETE A SPECIFIC CAR DETAIL
st.header("Delete a record car record with car id")
idtodel = None
idtodel = st.text_input("enter id", key=174)
submit = st.button('Submit to delete',key=789)
print("idtodel", idtodel)
if submit and idtodel is not None:
    print("code entered")

    #get the json data from get method

    urltoget ="http://127.0.0.1:8000/api/car/{}/".format(idtodel)
    r = requests.get(urltoget)
    content = r.json()
    print(content)

    req = requests.delete(urltoget, json=content)
    print(req.status_code)

    if req.status_code == 204:
        st.write('Records deleted')

else:
    pass
