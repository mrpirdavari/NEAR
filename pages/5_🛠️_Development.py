import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config( page_title="NEAR Megadashboard",page_icon="🔍",layout="wide")

st.title('🛠️ Development')

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


with t1:    
        st.subheader('Overall Statistics') 
        total_url="https://node-api.flipsidecrypto.com/api/v2/queries/7b407913-df9c-42d7-913f-097b60834dac/data/latest"
        total_data= pd.read_json(total_url)
        c1, c2= st.columns(2)       
        total_data= pd.read_json(total_url)
        c1.metric(label='Total Deployed Contracts', value=str(total_data['Total Deployed Contracts'].map('{:,.0f}'.format).values[0]))
        c2.metric(label='Average Deployed Contracts', value=str(total_data['Average Deployed Contracts'].map('{:,.0f}'.format).values[0]))

with t2:
        st.subheader('Statistics Over Time')
        col1, col2= st.columns(2)
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/a7fb4216-2d0b-4319-a62b-6d1ab50424b2/data/latest"
        transaction_data= pd.read_json(transaction_url)

        data= transaction_data; x='DATE'; y=['Number of New Contracts','Cumultive Number of New Contracts'];
        tit= 'Weekly Deployed Contracts' 
        xtit='Date'; ytit = 'Number of New Contracts' ; w=550; h=450 ; logy = True ; a=col1
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy) 
        
        
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/0401617a-fbd0-4ddf-b820-bb06f591e51e/data/latest"
        transaction_data= pd.read_json(transaction_url)
        
        data= transaction_data; x='DATE'; y=['Number of Transactions','Cumulative Number of Transactions'];  tit= 'Weekly Number of Transactions on Contracts' 
        xtit='Date'; ytit = 'Transaction Number' ; w=550; h=450 ; logy = True ; a=col2
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy) 
with t3: 
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/0401617a-fbd0-4ddf-b820-bb06f591e51e/data/latest"
        transaction_data= pd.read_json(transaction_url) 
        data= transaction_data; x='DATE'; y=['Number of Users','Cumulative Number of Users'];  tit= 'Weekly Number of Users on Contracts' 
        xtit='Date'; ytit = 'Number of Users' ; w=550; h=450 ; logy = True ; a=st
        line_plot(data,x,y,a,tit,xtit,ytit,w,h,logy)         

with t4:
        col1, col2, col3= st.columns([2,1,1])
        transaction_url="https://node-api.flipsidecrypto.com/api/v2/queries/f091fb19-bef1-4219-ad37-4a63136a6d4c/data/latest"
        transaction_data= pd.read_json(transaction_url)
        fig8=px.pie(transaction_data, values='Number of Transactions', names='Contract ID' , 
        title='Top 10 Most Interacted Contracts' , hole=0.25)
        fig8.update_traces(textposition='outside', textinfo='percent+value')
        col1.plotly_chart(fig8)
        
        data= transaction_data; x='DATE'; y='Number of Transactions'; 
        a=col2; tit= 'Weekly NEAR Interactions om Top 10 Contract'; xtit='Date'; ytit = '' ; w=550; h=450 ; 
        logy = False  ; color='Contract ID' ;barmode='relative'   
        bar_plot(data,x,y,a,tit,xtit,ytit,w,h,logy,color,barmode)
