import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config( page_title="NEAR Megadashboard",page_icon="🔍",layout="wide")

st.title('📊 Transactions')

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
t7 = st.container()
t8 = st.container()
    
    
with t1:
     total_url="https://node-api.flipsidecrypto.com/api/v2/queries/c2743cef-fe3c-4cdb-8806-f10d24cbcb03/data/latest"
     total_data= pd.read_json(total_url)
     st.subheader('Overall Statistics')   

     c1, c2= st.columns(2) 
        
     c1.metric(label='Total Number of Transactions', value=str(total_data['Total Number of Transactions'].map('{:,.0f}'.format).values[0]))
     c1.metric(label='Total Transaction Fees', value=str(total_data['Total Transaction Fees'].map('{:,.0f}'.format).values[0]))
     c1.metric(label='Total Number of Blocks', value=str(total_data['Total Number of Blocks'].map('{:,.0f}'.format).values[0]))
     c2.metric(label='Median TPS per Week', value=str(total_data['Median TPS per Week'].map('{:,.0f}'.format).values[0]))
     c2.metric(label='Average Number of Transactions per Week', value=str(total_data['Average Number of Transactions per Week'].map('{:,.0f}'.format).values[0]))
     c2.metric(label='Average Transction Fees per Week', value=str(total_data['Average Transction Fees per Week'].map('{:,.0f}'.format).values[0]))


with t2:
        st.subheader('Statistics Over Time')
        st.subheader('Price, Transactions, Fees and Blocks')
        # col1, col2 = st.columns(2)
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/98b96218-7dae-477a-afb5-2327d576bc24/data/latest"
        transaction_data= pd.read_json(transaction_url)
        
        data= transaction_data; x='DATE'; y='NEAR USD Price';  tit= 'NEAR Price USD' 
        xtit='Date'; ytit = 'Price USD' ; w=1400; h=450 ; logy = False ; a=st
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy)
       

        # data= transaction_data; x='DATE'; y=['FEES','TPS']; a=col2; 
        # tit= 'Weekly Luna Fees'; xtit='Date'; ytit = 'FEES & TPS' ; w=700; h=450 ; logy = True 
        # fig=scatter_plot(data,x,y,a,tit,xtit,ytit,w,h,logy)    
      
    
with t3:
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/4ba9d727-3a9c-4d41-830f-9fb20bb00e9f/data/latest"
        transaction_data= pd.read_json(transaction_url)
        col1, col2= st.columns(2) 

        data= transaction_data; x='DATE'; y=['Number of Transactions','Cumulative Number of Transactions'];  tit= 'Number of Transactions per Week' 
        xtit='Date'; ytit = '' ; w=700; h=450 ; logy = True ; a=col1
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy)
        
        data= transaction_data; x='DATE'; y=['Transaction Fees','Cumulative Transaction Fees'];  tit= 'Amount of Transaction Fees per Week' 
        xtit='Date'; ytit = 'Transaction Fees' ; w=700; h=450 ; logy = True ; a=col2
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy) 
        
with t4:
        col1, col2= st.columns(2)
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/4ba9d727-3a9c-4d41-830f-9fb20bb00e9f/data/latest"
        transaction_data= pd.read_json(transaction_url)
        
        data= transaction_data; x='DATE'; y=['Number of Transactions','TPS'];  tit= 'Number of Transactions and TPS' 
        xtit='Date'; ytit = 'Number of Transactions' ; w=700; h=450 ; logy = True ; a=col1
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy) 
        
        data= transaction_data; x='DATE'; y='Number of Blocks';  tit= 'Number of Blocks per Week' 
        xtit='Date'; ytit = 'Number of Blocks' ; w=700; h=450 ; logy = True ; a=col2
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy) 

with t5:  
        col1, col2 ,col3 = st.columns([2,1,1])
        time_url="https://node-api.flipsidecrypto.com/api/v2/queries/39345768-0040-4bd5-b234-ffcdec5d3826/data/latest"
        transaction_data= pd.read_json(time_url)  
        data= transaction_data; x='DATE'; y='Average Block Time';  tit= 'Average Block Time per Week' 
        xtit='Date'; ytit = 'Average Block Time' ; w=1000; h=450 ; logy = False ; a=col1
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy) 
        
        col3.text(" ")
        col3.text(" ")
        col3.text(" ")
        col3.text(" ")
        col3.text(" ")
        col3.text(" ")     
        total_url="https://node-api.flipsidecrypto.com/api/v2/queries/4b000504-a0f5-4888-b95c-bd654dd0430a/data/latest"
        total_data= pd.read_json(total_url)
        col3.metric(label='Average Block Time per Week', value=str(total_data['Average Block Time per Week'].map('{:,.2f}'.format).values[0]))

with t6:
        st.subheader('Success Rate')   
        col1, col2, col3= st.columns(3) 
        total_url="https://node-api.flipsidecrypto.com/api/v2/queries/58064af6-5b88-4fa2-815a-6ed6d55a1ccf/data/latest"
        total_data= pd.read_json(total_url)
        col1.metric(label='Average Number of Failed Transactions per Week', value=str(total_data['Average Number of Failed Transactions per Week'].map('{:,.0f}'.format).values[0]))
        col2.metric(label='Average Number of Succeeded Transactions per Week', value=str(total_data['Average Number of Succeeded Transactions per Week'].map('{:,.0f}'.format).values[0]))
        col3.metric(label='Average Success Rate per Week', value=str(total_data['Average Success Rate per Week'].map('{:,.0f}'.format).values[0]))
                    
   
with t7:
        col1, col2= st.columns(2)
        time_url="https://node-api.flipsidecrypto.com/api/v2/queries/94b61780-6323-42c4-b3a0-5c3dd4f2157a/data/latest"
        time_data= pd.read_json(time_url)
        data= time_data; x='DATE'; y=['Failed Transactions','Succeeded Transactions']; 
        a=col1; tit= 'Weekly Ratio of Failed and Succeeded Transactions'; xtit='Date'; ytit = 'Ratio %' ;
        w=700; h=450 ; logy = False  ; color=None ; barmode='relative'   
        bar_plot2(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)  
        
        data= time_data; x='DATE'; y=['Failed Transactions','Succeeded Transactions']; 
        a=col2; tit= 'Weekly Number of Failed and Succeeded Transactions'; xtit='Date'; ytit = 'Transaction numbers' ; w=700; h=450 ; logy = False  ; color=None ;barmode='group'   
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode) 
        
with t8:
        col1, col2= st.columns(2)
        time_url="https://node-api.flipsidecrypto.com/api/v2/queries/94b61780-6323-42c4-b3a0-5c3dd4f2157a/data/latest"
        transaction_data= pd.read_json(time_url)  
        data= transaction_data; x='DATE'; y='Success Rate';  tit= 'Weekly Success Rate' 
        xtit='Date'; ytit = 'Ratio %' ; w=1400; h=450 ; logy = False ; a=st
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy) 
        

        
  