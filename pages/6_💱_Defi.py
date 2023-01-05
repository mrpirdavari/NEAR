import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config( page_title="NEAR Megadashboard",page_icon="🔍",layout="wide")

st.title('💱 Defi')

st.sidebar.success("Select a metric above.")
st.sidebar.image("https://www.pngall.com/wp-content/uploads/10/NEAR-Protocol-Crypto-Logo-PNG-Photo.png", width=250)

def line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy):
    fig=px.line(data, x, y,log_y=logy)

    fig.update_layout(title=tit,title_font_size=16,#title_xanchor="center",#title_pad_l=30,
                      xaxis_title= xtit, xaxis_title_font_size=16,
                      yaxis_title= ytit, yaxis_title_font_size=16,
                      width=w, height= h, plot_bgcolor="white",
                      showlegend= False, legend_bordercolor="#080808",legend_borderwidth=0.5,
                      legend_font_size=12,legend_title_font_size=14,legend_title_text="",
                      
                      )
    
    a.plotly_chart(fig)
    return

def scatter_plot(data,x,y,a,tit,xtit,ytit,w,h,logy):
    fig=px.scatter(data, x, y, log_y = logy)

    fig.update_layout(title=tit,title_font_size=16,#title_xanchor="center",#title_pad_l=30,
                      xaxis_title= xtit, xaxis_title_font_size=16,
                      yaxis_title= ytit, yaxis_title_font_size=16,
                      width=w, height= h, plot_bgcolor="white",
                      showlegend= False, legend_bordercolor="#080808",legend_borderwidth=0.5,
                      legend_font_size=12,legend_title_font_size=14,legend_title_text="",
                      
                      )
    
    a.plotly_chart(fig)
    return

def bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode):
    fig=px.bar(data, x, y,color, log_y=logy, barmode=barmode)
    
    fig.update_layout(title=tit,title_font_size=16,#title_xanchor="center",#title_pad_l=30,
                      xaxis_title= xtit, xaxis_title_font_size=16,
                      yaxis_title= ytit, yaxis_title_font_size=16,
                      width=w, height= h, plot_bgcolor="white",
                      showlegend= True,
                      legend_font_size=12,legend_title_font_size=14,legend_title_text="",
                      
                      )
    a.plotly_chart(fig)
    return

def bar_plot2(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode):
    fig=px.bar(data, x, y,color, log_y=logy, barmode=barmode)
    
    fig.update_layout(title=tit,title_font_size=16,#title_xanchor="center",#title_pad_l=30,
                      xaxis_title= xtit, xaxis_title_font_size=16,
                      yaxis_title= ytit, yaxis_title_font_size=16,
                      width=w, height= h, plot_bgcolor="white",
                      showlegend= True,
                      legend_font_size=12,legend_title_font_size=14,legend_title_text="",
                      barnorm='percent'
                      )
    a.plotly_chart(fig)
    return

def pie_plot(transaction_data,values,names):#,a,tit,txtpo,txtinf,hole=0.5):
    fig=px.pie(transaction_data, values, names,title='Distribution of wallets by transactions')#, title=tit)
    
    # fig.update_traces(textposition= txtpo,
    #                   textinfo= txtinf)
                   
    st.plotly_chart(fig)
    return



t1 = st.container()
t2 = st.container()
t3 = st.container()
t4 = st.container()
t5 = st.container()
t32 = st.container()

with t1:
        col1, col2= st.columns(2)
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/7992d138-ed15-47cc-b8bf-c045030325fb/data/latest"
        transaction_data= pd.read_json(transaction_url)
        
        data= transaction_data; x='DATE'; y=['Number of Swaps','Number of Swappers'];  tit= 'Weekly Swaps Transactions and Users' 
        xtit='Date'; ytit = 'Transaction Number' ; w=550; h=450 ; logy = True ; a=col1
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy)
        
        data= transaction_data; x='DATE'; y='Volume of Swaps'; 
        a=col2; tit= 'Weekly Swaps Volume'; xtit='Date'; ytit = 'Volume' ; w=550; h=450 ; 
        logy = True  ; color=None;barmode='relative'   
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)

with t2:
        
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/7bb5d8e5-df88-4ffd-ba21-dbab327c7344/data/latest"
        transaction_data= pd.read_json(transaction_url)
        data= transaction_data; x='DATE'; y='Volume of Swaps'; 
        a=st; tit= 'Weekly Swaps Transactions per Platform'; xtit='Date'; ytit = 'Number of Swaps' ; w=1100; h=450 ; 
        logy = True  ; color='PLATFORM'; barmode='relative'   
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
         
    
with t3: 
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/7bb5d8e5-df88-4ffd-ba21-dbab327c7344/data/latest"
        transaction_data= pd.read_json(transaction_url)
        data= transaction_data; x='DATE'; y='Number of Swappers'; 
        a=st; tit= 'Weekly Swaps Users per Platform'; xtit='Date'; ytit = 'Number of Users' ; w=1100; h=450 ; 
        logy = True  ; color='PLATFORM'; barmode='relative'   
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)

with t4: 
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/7bb5d8e5-df88-4ffd-ba21-dbab327c7344/data/latest"
        transaction_data= pd.read_json(transaction_url)
        data= transaction_data; x='DATE'; y='Volume of Swaps'; 
        a=st; tit= 'Weekly Swap Volume per Platform'; xtit='Date'; ytit = '	Volume of Swaps' ; w=1100; h=450 ; 
        logy = True  ; color='PLATFORM'; barmode='relative'   
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)

with t5: 
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/cd4968b9-2a7a-4543-a26b-7a9eb2d511f9/data/latest"
        transaction_data= pd.read_json(transaction_url)
        data= transaction_data; x='PLATFORM'; y='Number of Swaps'; 
        a=st; tit= 'Top 10 Platforms by Swap Transactions'; xtit=''; ytit = '	Number of Swaps' ; w=1100; h=500 ; 
        logy = False  ; color='PLATFORM'; barmode='relative'   
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)    
