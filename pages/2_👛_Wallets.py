import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config( page_title="NEAR Megadashboard",page_icon="🔍",layout="wide")

st.title('👛 Wallets')

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
t9 = st.container()
t10 = st.container()
t11 = st.container()
t12 = st.container()
t13 = st.container()
t14 = st.container()
t15 = st.container()
t16 = st.container()
t17 = st.container()
t18 = st.container()
t19 = st.container()
t20 = st.container()
t21 = st.container()
t22 = st.container()
t23 = st.container()
t24 = st.container()
t25 = st.container()
t26 = st.container()
t27 = st.container()
t28 = st.container()
t29 = st.container()
t30 = st.container()
t31 = st.container()
t32 = st.container()


with t1:
     st.subheader('Overall Statistics')  

     c1, c2, c3= st.columns(3)       
     total_url="https://node-api.flipsidecrypto.com/api/v2/queries/5d721e1a-ad9d-465b-a354-52b38dff904a/data/latest"
     total_data= pd.read_json(total_url)
     c1.metric(label='Total Number of Users', value=str(total_data['Total Number of Users'].map('{:,.0f}'.format).values[0]))
     c2.metric(label='Average Number of Users per Week', value=str(total_data['Average Number of Users per Week'].map('{:,.0f}'.format).values[0]))

     total_url="https://node-api.flipsidecrypto.com/api/v2/queries/17983c83-e94e-44ea-97eb-4e43dc311052/data/latest"
     total_data= pd.read_json(total_url)
     c3.metric(label='Average New Users per Week', value=str(total_data['Average New Users per Week'].map('{:,.0f}'.format).values[0]))

with t2:
        st.subheader('Statistics Over Time')
        st.subheader('Users')
        col1, col2 = st.columns(2)
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/4ba9d727-3a9c-4d41-830f-9fb20bb00e9f/data/latest"
        transaction_data= pd.read_json(transaction_url)
        
        data= transaction_data; x='DATE'; y=['Number of Users','Cumulative Number of Users'];  tit= 'Number of Users per Week' 
        xtit='Date'; ytit = 'Number of Users' ; w=700; h=450 ; logy = True ; a=col1
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy)   

    
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/a452cecc-e376-49db-bed9-7b0fa4590550/data/latest"
        transaction_data= pd.read_json(transaction_url)
        
        data= transaction_data; x='MINDATE'; y=['New Users','Total Users'];  tit= 'Weekly New and Cumulative Users' 
        xtit='Date'; ytit = 'Users' ; w=700; h=450 ; logy = True ; a=col2
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy) 
              

with t3:
        st.subheader('NEAR Balance')
        col1, col2= st.columns(2)
        time_url="https://node-api.flipsidecrypto.com/api/v2/queries/abc3ba62-0f12-432b-a1ba-b99dd40d1686/data/latest"
        time_data= pd.read_json(time_url)
        data= time_data; x='DATES'; y='Number of Users'; 
        a=col1; tit= 'Weekly Distribution of NEAR Holders by NEAR Balance'; xtit='Date'; ytit = 'Number of Users' ; w=700; h=500 ; 
        logy = False  ; color='Balance Type' ;barmode='relative'   
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
        
        data= time_data; x='DATES'; y='Number of Users'; 
        a=col2; tit= 'Weekly Normalized Distribution of NEAR Holders by NEAR Balance'; xtit='Date'; ytit = 'percent of Users' ; w=700; h=500 ; 
        logy = False  ; color='Balance Type' ;barmode='relative'  
        bar_plot2(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
        
with t4:
        col1, col2, col3= st.columns([2,1,1])
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/43356aff-fbf9-4b83-9bd7-67f0f0e3ae92/data/latest"
        transaction_data= pd.read_json(transaction_url)
        fig8=px.pie(transaction_data, values='Number of Users', names='Balance Type' , 
                    title='NEAR Balance by NEAR Holders Balance' , hole=0.25)
        fig8.update_traces(textposition='outside', textinfo='percent')
        col1.plotly_chart(fig8)
        
        col3.text(" ")
        col3.text(" ")
        col3.text(" ")
        col3.text(" ")
        col3.text(" ")
        total_url="https://node-api.flipsidecrypto.com/api/v2/queries/44696e7a-2565-480e-a4aa-288f1b00f68e/data/latest"
        total_data= pd.read_json(total_url)
        col3.metric(label='Average NEAR Balance of Holders', value=str(total_data['Average NEAR Balance of Holders'].map('{:,.0f}'.format).values[0]))
        

    

        
