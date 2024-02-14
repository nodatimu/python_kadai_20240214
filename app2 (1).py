import streamlit as st
st.title("お買い物計算アプリ")

col1, col2, col3 = st.columns(3)

n=0

item_dict = {}
discount_dict = {}
variety_dict ={}

# input

with col1 :

  def create_blank(num):
    item = st.number_input(f"商品{num}",value=0,step=1)
    return item

  item_dict[n+1] = create_blank(n+1)

with col2 :
  def create_discount(num):
    discount = st.number_input(f"値引き率{num}(%)",value=0,step=1)
    return  discount

  discount_dict[n+1] = create_discount(n+1)

with col3 :
  def create_variety(num):
    variety = st.selectbox(f"品種{num}",["飲食料品(8%)","日用品(10%)"])
    return  variety 

  variety_dict[n+1] = create_variety(n+1)

  price = item_dict[n+1]*(1-discount_dict[n+1]/100)

if variety_dict[n+1] == "飲食料品(8%)":
  intax = price*1.08
elif variety_dict[n+1] =="日用品(10%)":
  intax = price*1.1
else:
  pass

total=0
total+=intax

n+=1

while item_dict[n]>0:
  with col1 :
    item_dict[n+1] = create_blank(n+1)
  with col2 :
    discount_dict[n+1] = create_discount(n+1)
  with col3 :
    variety_dict[n+1] = create_variety(n+1)
  

  price = item_dict[n+1]*(1-discount_dict[n+1]/100)

  if variety_dict[n+1] == "飲食料品(8%)":
    intax = price*1.08
  elif variety_dict[n+1] =="日用品(10%)":
    intax = price*1.1
  else:
    pass
  n+=1

  total+=intax

# output
st.title(f"お支払い金額(税込)")
st.text(f"{int(total)}円")