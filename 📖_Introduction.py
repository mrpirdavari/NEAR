import streamlit as st

st.set_page_config( page_title="NEAR Megadashboard",page_icon="🔍",layout="wide")


st.write("# NEAR Megadashboard! 🔍")

st.sidebar.success("Select a metric above.")
st.sidebar.image("https://www.pngall.com/wp-content/uploads/10/NEAR-Protocol-Crypto-Logo-PNG-Photo.png", width=250)


i1 = st.container()
i2 = st.container()
i3 = st.container()
i4 = st.container()
i5 = st.container()


with i1: 
    col1, col2= st.columns(2) 
    st.write("""
    #### This Megadashboard offers a holistic view of the NEAR ecosystem, including activity, NFTs, staking, and development using the following metrics:
    """)
   
   
with i2:
    col1, col2 = st.columns(2)
    col1.write("""
    #### Transactions
     * ##### Total and average statistics of transactions
     * ##### Transaction statistics per week
     * ##### Transaction fee per transaction per week
     * ##### TPS per week
     * ##### Number of blocks per week
     * ##### Average block time per week
     * ##### Success rate per week
    
    #### Wallets
     * ##### Total and average statistics of users
     * ##### Active wallet statistics per week
     * ##### Holders

    #### NFT Sales
     * ##### Total and average statistics of NFT sales
     * ##### NFT sales per week
     """)
   
    col2.write("""
    #### Staking
     * ##### Total and average statistics of staking
     * ##### Staked/Unstaked NEAR per week
     * ##### Active validators per week
     * ##### Top Stakers

    #### Development
     * ##### Total and average statistics of contracts
     * ##### New contracts deployed per week
     * ##### Activities on contracts per week
     * ##### Most popular contracts

    #### Defi
     * ##### Total and average statistics of swaps
     * ##### Swap activities per platform per week
     * ##### Most popular platforms
    """)


with i3:
    st.info('##### This dashboard updates daily')


with i4:  
    st.write(""" #### This dashboard was created using the [Flipsidecrypto](https://app.flipsidecrypto.com/velocity) database for the "NEAR - 5. Megadashboard" bounty by [Metricsdao](https://metricsdao.notion.site/Bounty-Programs-d4bac7f1908f412f8bf4ed349198e5fe).""")

with i5:
    
    col1, col2, col3, col4= st.columns(4) 
    col2.image("https://pbs.twimg.com/profile_images/1453392380250443782/UC8erEKz_400x400.png",width=250)
    col3.image("https://cryptocurrencyjobs.co/startups/assets/logos/flipside-crypto.jpg",width=250)  