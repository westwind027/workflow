import streamlit as st
from blocks import event_block,noop_block
from barfi import st_barfi, barfi_schemas

base_blocks = [event_block,noop_block]

#load_schema = st.selectbox('Select a saved schema:', barfi_schemas())

compute_engine = st.checkbox('Activate barfi compute engine', value=False)

barfi_result = st_barfi(base_blocks=base_blocks, compute_engine=compute_engine)
#, load_schema=load_schema)

def getnext(retjson, ckkey):
  d = retjson[ckkey]['interfaces']['Output']['to']
  return list(d)[0]
   
def getkeys(retjson):
  return list(retjson)

def fixid(text):
  return 0

if barfi_result:
  st.write(barfi_result)
  arr = barfi_result['Noop-1']['block'].get_interface(name='Output')
  st.write(arr)
  #toshow = "{0}{1}\n{2}\n{3}".format(arr[0],getnext(barfi_result, '消息监听器-1'),arr[1],arr[2])
  st.write(getkeys(barfi_result))
  #st.code( toshow, language='yaml')