import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config( page_title="NEAR Megadashboard",page_icon="🔍",layout="wide")

st.title('🖼️ NFT Sales')

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

with t1:
        st.subheader('Overall Statistics')          
        total_url="https://node-api.flipsidecrypto.com/api/v2/queries/bbe784bf-3153-480c-a85b-e4c839381eb4/data/latest"
        total_data= pd.read_json(total_url)
        c1, c2, c3, c4= st.columns(4)       
        total_data= pd.read_json(total_url)
        c1.metric(label='Total Number of NFT Sales', value=str(total_data['Total Number of NFT Sales'].map('{:,.0f}'.format).values[0]))
        c2.metric(label='Total Number of NFT Buyers', value=str(total_data['Total Number of NFT Buyers'].map('{:,.0f}'.format).values[0]))
        c3.metric(label='Total Number of NFT Sellers', value=str(total_data['Total Number of NFT Sellers'].map('{:,.0f}'.format).values[0]))
        c4.metric(label='Total Volume of NFT Sales', value=str(total_data['Total Volume of NFT Sales'].map('{:,.0f}'.format).values[0]))
        
        total_url="https://node-api.flipsidecrypto.com/api/v2/queries/7f30c889-13eb-4b87-b46a-2aeb5d8d220a/data/latest"
        total_data= pd.read_json(total_url)
        c1.metric(label='Average Number of NFT Sales', value=str(total_data['Average Number of NFT Sales'].map('{:,.0f}'.format).values[0]))
        c2.metric(label='Average Number of NFT Buyers', value=str(total_data['Average Number of NFT Buyers'].map('{:,.0f}'.format).values[0]))
        c3.metric(label='Average Number of NFT Sellers', value=str(total_data['Average Number of NFT Sellers'].map('{:,.0f}'.format).values[0]))
        c4.metric(label='Average Volume of NFT Sales', value=str(total_data['Average Volume of NFT Sales'].map('{:,.0f}'.format).values[0]))  

with t2:
        st.subheader('Statistics Over Time')
        col1, col2= st.columns(2)
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/1ce61183-7c95-4461-a2fd-89fdb117788f/data/latest"
        transaction_data= pd.read_json(transaction_url)
        
        data= transaction_data; x='DATE'; y=['Sales Count','Cumulative Sales Count'];  tit= 'Weekly Number of NFT Sales' 
        xtit='Date'; ytit = 'Sales Count' ; w=700; h=450 ; logy = True ; a=col1
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy) 
        
        data= transaction_data; x='DATE'; y=['Volume','Cumulative Volume'];  tit= 'Weekly Volume of NFT Sales' 
        xtit='Date'; ytit = 'Volume' ; w=700; h=450 ; logy = True ; a=col2
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy) 
   
with t3:
        
        time_url="https://node-api.flipsidecrypto.com/api/v2/queries/1ce61183-7c95-4461-a2fd-89fdb117788f/data/latest"
        time_data= pd.read_json(time_url)
        data= time_data; x='DATE'; y=['Buyers','Sellers']; 
        a=st; tit= 'Weekly Number of NFT Buyers and Sellers'; xtit='Date'; ytit = '' ; w=700; h=450 ; 
        logy = False  ; color=None ;barmode='group'   
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)         
        
