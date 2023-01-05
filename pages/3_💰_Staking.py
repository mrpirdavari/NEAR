import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config( page_title="NEAR Megadashboard",page_icon="🔍",layout="wide")

st.title('💰 Staking')

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
t6 = st.container()


with t1: 
        st.subheader('Overall Statistics')  
        col1, col2= st.columns(2)       
        total_url="https://node-api.flipsidecrypto.com/api/v2/queries/7012becc-f865-4cb3-a5f7-eafbe82f0c12/data/latest"
        total_data= pd.read_json(total_url)
        data= total_data; x='ACTION'; y=['Total Number of Transations','Total Number of Users','Total Volume of Transctions']; 
        a=col1; tit= 'Total Staking/Unstaking Statistics'; xtit='Action'; ytit = 'Statistics' ; w=700; h=450 ; logy = True  ; color=None ;barmode='group'   
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode) 
        
        total_url="https://node-api.flipsidecrypto.com/api/v2/queries/75aa1652-6fe2-48ca-9239-f6ee943d998a/data/latest"
        total_data= pd.read_json(total_url)
        data= total_data; x='ACTION'; y=['Average Number of Transations','Average Number of Users','Average Volume of Transctions']; 
        a=col2; tit= 'Average Staking/Unstaking Statistics'; xtit='Action'; ytit = 'Statistics' ; w=700; h=450 ; logy = True  ; color=None ;barmode='group'   
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode) 

with t2:
        st.subheader('Statistics Over Time')
        col1, col2= st.columns(2)
        time_url="https://node-api.flipsidecrypto.com/api/v2/queries/d3999b43-dc3b-48c7-90c3-4a1375e8420f/data/latest"
        time_data= pd.read_json(time_url)
        data= time_data; x='DATE'; y='Number of Transations'; 
        a=col1; tit= 'Weekly Number of Staking/Unstaking Actions'; xtit='Date'; ytit = 'Transaction Number' ; w=700; h=450 ; 
        logy = False  ; color='ACTION' ;barmode='group'   
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode) 


        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/d3999b43-dc3b-48c7-90c3-4a1375e8420f/data/latest"
        transaction_data= pd.read_json(transaction_url)
        fig8=px.pie(transaction_data, values='Number of Transations', names='ACTION' , title='Distribution of Actions on NEAR by Transactions' , hole=0.5)
        fig8.update_traces(textposition='inside', textinfo='percent+label')
        col2.plotly_chart(fig8)
              
with t3:
        col1, col2= st.columns(2)
       
        data= time_data; x='DATE'; y='Volume of Transctions'; 
        a=col1; tit= 'Weekly Volume of Staking/Unstaking Actions'; xtit='Date'; ytit = 'Volume' ; w=700; h=450 ; 
        logy = False  ; color='ACTION' ;barmode='group'   
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode) 

 
        fig8=px.pie(transaction_data, values='Volume of Transctions', names='ACTION' , title='Distribution of Actions on NEAR by Volume' , hole=0.5)
        fig8.update_traces(textposition='inside', textinfo='percent+label')
        col2.plotly_chart(fig8)
        
with t4:
        col1, col2= st.columns(2)
        data= time_data; x='DATE'; y='Number of Users'; 
        a=col1; tit= 'Weekly Number of Staking/Unstaking Users'; xtit='Date'; ytit = 'User Number' ; w=700; h=450 ; 
        logy = False  ; color='ACTION' ;barmode='group'   
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode) 


        fig8=px.pie(transaction_data, values='Number of Users', names='ACTION' , title='Distribution of Actions on NEAR by Users' , hole=0.5)
        fig8.update_traces(textposition='inside', textinfo='percent+label')
        col2.plotly_chart(fig8) 


with t5:
        col1, col2= st.columns(2)
        time_url="https://node-api.flipsidecrypto.com/api/v2/queries/1b1622ce-b723-4fd7-8b5c-96b786f817c1/data/latest"
        time_data= pd.read_json(time_url)
        data= time_data; x='DATE'; y='Number of Active Validators'; 
        a=col1; tit= 'Weekly Number of Active Validators'; xtit='Date'; ytit = 'Number of Validators' ; w=700; h=500 ; 
        logy = False  ; color=None ;barmode='relative'   
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        time_url="https://node-api.flipsidecrypto.com/api/v2/queries/b3a2b392-ed32-4b59-99e6-ee9e3923d0b5/data/latest"
        time_data= pd.read_json(time_url)
        data= time_data; x='WEEKS'; y='POWER_SHARE'; 
        a=col2; tit= 'Normalised Power Distribution of NEAR Validators Over Time'; xtit='Weeks'; ytit = 'POWER SHARE %' ; w=700; h=500 ; 
        logy = False  ; color='RANKS' ;barmode='relative'   
        bar_plot2(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        

        
with t6:
        col1, col2= st.columns(2)
        time_url="https://node-api.flipsidecrypto.com/api/v2/queries/063e4a4a-92e9-48f8-9326-947ce4550144/data/latest"
        time_data= pd.read_json(time_url)
        data= time_data; x='USER'; y='Staking Transctions'; 
        a=col1; tit= 'Top NEAR Stakers by Transactions'; xtit=''; ytit = 'Transaction Number' ; w=700; h=700 ; 
        logy = False  ; color='Staking Transctions' ;barmode='relative'   
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        time_url="https://node-api.flipsidecrypto.com/api/v2/queries/d81026fb-e819-4990-8c63-9d1b809b1a66/data/latest"
        time_data= pd.read_json(time_url)
        data= time_data; x='USER'; y='Staking Volume'; 
        a=col2; tit= 'Top NEAR Stakers by Volume'; xtit=''; ytit = 'Staking Volume' ; w=700; h=700 ; 
        logy = False  ; color='Staking Volume' ;barmode='relative'   
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode) 
               
  