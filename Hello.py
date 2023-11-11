import streamlit as st
from pages import func_page_1
from streamlit_option_menu import option_menu
from datetime import datetime
import psycopg2
import base64
import io
import pandas as pd
import matplotlib.pyplot as fig
import matplotlib.pyplot as vig
import plotly.graph_objs as go
import seaborn as sns

hide_st_style = """
<style>
#MainMenu {visibility :hidden;}
footer {visibility :hidden;}
header {visibility :hidden;}
</style>
"""

# Function to connect to the database
def connect_db():
    # Set up a connection string
    username = st.secrets['user']
    password = st.secrets['pw']
    host = 'risk-analysis.postgres.database.azure.com'
    database = 'riskyDB'
    port = '5432'  # or your specified port number
    sslmode = 'prefer'  # or 'prefer' if you don't want to use SSL encryption
    conn_str = f"postgresql://{username}:{password}@{host}:{port}/{database}?sslmode={sslmode}"
    return conn_str

# Connecting to the database and initializing cursor
conn = psycopg2.connect(connect_db())
#cur = conn.cursor()
connect_db()
#@st.cache_resource
def init_connection():
    return conn

conn = init_connection()

#@st.cache_data(ttl=600)
def insert_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        conn.commit()

st.markdown(hide_st_style,unsafe_allow_html =True)
print(fig.style.available)
def creds_entered():
    if st.session_state["user"].strip() == "MUKAMA" and st.session_state["passwd"].strip() == "MUKAMA":
        st.session_state["authenticated"] = True
    else:
        st.session_state["authenticated"] = False
        if not st.session_state["passwd"]:
            st.warning("please enter password")
        elif not st.session_state["user"]:
            st.warning("please enter username")
        else:
            st.error("Invalid username/password :coffee:")

def authenticate_user():
    if "authenticated" not in st.session_state:
        st.text_input(label="Username :", value ="", key="user", on_change=creds_entered)
        st.text_input(label="Password :", value="", key="passwd", type ="password", on_change=creds_entered)
        return False
    else:
        if st.session_state["authenticated"]:
            return True
        else:
            st.text_input(label="Username :", value ="", key="user", on_change=creds_entered)
            st.text_input(label="Password :", value="", key="passwd", type ="password", on_change=creds_entered)
            return False
#st.title(" :flag-ug: National Risk Assessment Tool For Virtual Asset Providers  by  **:orange[MR. BWIRE IVAN]** ")
def logout():
        st.session_state["authenticated"] = False
        if "authenticated" not in st.session_state:
            st.text_input(label="Username :", value ="", key="user", on_change=creds_entered)
            st.text_input(label="Password :", value="", key="passwd", type ="password", on_change=creds_entered)
            return False
        
        

if authenticate_user():

    # Add a navigation menu to switch between pages
    #page = st.sidebar.selectbox("Select a page", ["Home", "Reports"])
    #if page == "Home":
    st.title(" ML/TF RISK ASSESSMENT SYSTEM FOR VIRTUAL ASSETS ")
    #elif page == "Reports":
     #   def run_page_1():
      #      func_page_1()
    #Expander in sidebar
    #st.sidebar.subheader('Expander')
    #with st.sidebar.expander('Time'):
        #time = datetime.now().strftime("%D %H:%M:%S")
        #st.write('**%s**' % (time))
    
    with st.sidebar.expander('VIRTUAL ASSET SERVICE PROVIDERS'):
        VASPS = {'WALLET SERVICE PROVIDERS':['HOT WALLET', 'COLD WALLET'],'ASSET EXCHANGES':['P2P','P2B','FIAT TO VIRTUAL','VIRTUAL TO FIAT','VIRTUAL TO VIRTUAL'],'BROKING':['ATMS','MERCHANTS','CARDS'],'MANAGEMENT PROVIDERS':['FUND MANAGEMENT','FUND DISTRIBTION','COMPLIANCE AUDIT & RISK MGT'],'INITIAL COIN OFFERING':['FIAT TO VIRTUAL','VIRTUAL TO VIRTUAL','DEVELOPMENT OF PRODUCTS AND SERVICES','SECURITY TOKEN OFFERINGS','INITIAL EXCHANGE OFFERINGS'],'INVESTMENT PROVIDERS':['PLATFROM OPERATORS','CUSTODY OF ASSETS','INVESTMENT INTO VA RELATED COMMERCIAL ACTIVITIES','NON SECURITY TOKENS & HYBRID TRADING ACTIVITIES','STABLECOINS','CRYPTO ESCROW SERVICE','CRYPTO CUSTODIAN SERVICE'],'VALIDATORS':['FEES','NEW ASSETS']}
        
        page_selection = st.sidebar.selectbox('SELECT VASP TYPE:', VASPS.keys())
        VASPS_CATEGORIES =  st.sidebar.selectbox('SELECT SERVICE TYPE:', VASPS[page_selection])



    
    LOGOUT = st.sidebar.button('LOGOUT')
    if LOGOUT:
        logout()



    
        
    selected = option_menu(menu_title=None, options=['PRODUCT DIMENSION','ENTITY DIMENSION','TOTAL RISK'], icons=['boxes','boxes','boxes'], orientation='horizontal',)
    
    
    def Product_Dimension():
        if selected == 'PRODUCT DIMENSION':
            st.subheader(":green[THREAT PRODUCT DIMENSION]")
            col1, col2 = st.columns(2)
            with col1:
                with st.expander('VA Asset Nature and Profile'):
                    #form = st.form("VA Asset Nature and Profile")
                    anonmy_risk = st.selectbox('Anonymity/pseudonymity',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if anonmy_risk == 'VERY HIGH RISK':
                        anonmy_risk = 1
                    elif anonmy_risk == 'HIGH RISK':
                        anonmy_risk = 0.8
                    elif anonmy_risk == 'MEDIUM RISK':
                        anonmy_risk = 0.6
                    elif anonmy_risk == 'LOW RISK':
                        anonmy_risk = 0.4
                    elif anonmy_risk == 'VERY LOW RISK':
                        anonmy_risk = 0.2
                    elif anonmy_risk == 'NOT APPLICABLE':
                        anonmy_risk = 0.0

                    p2p_risk  = st.selectbox('P2P Cross-Border Transfer and Portability',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if p2p_risk == 'VERY HIGH RISK':
                        p2p_risk = 1
                    elif p2p_risk == 'HIGH RISK':
                        p2p_risk = 0.8
                    elif p2p_risk == 'MEDIUM RISK':
                        p2p_risk = 0.6
                    elif p2p_risk == 'LOW RISK':
                        p2p_risk = 0.4
                    elif p2p_risk == 'VERY LOW RISK':
                        p2p_risk = 0.2
                    elif p2p_risk == 'NOT APPLICABLE':
                        p2p_risk = 0.0

                    traceability_risk  = st.selectbox('Traceability',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if traceability_risk == 'VERY HIGH RISK':
                        traceability_risk = 1
                    elif traceability_risk == 'HIGH RISK':
                        traceability_risk = 0.8
                    elif traceability_risk == 'MEDIUM RISK':
                        traceability_risk = 0.6
                    elif traceability_risk == 'LOW RISK':
                        traceability_risk = 0.4
                    elif traceability_risk == 'VERY LOW RISK':
                        traceability_risk = 0.2
                    elif traceability_risk == 'NOT APPLICABLE':
                        traceability_risk = 0.0
                    speed_risk  = st.selectbox('Speed of Transfer',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if speed_risk == 'VERY HIGH RISK':
                        speed_risk = 1
                    elif speed_risk == 'HIGH RISK':
                        speed_risk = 0.8
                    elif speed_risk == 'MEDIUM RISK':
                        speed_risk = 0.6
                    elif speed_risk == 'LOW RISK':
                        speed_risk = 0.4
                    elif speed_risk == 'VERY LOW RISK':
                        speed_risk = 0.2
                    elif speed_risk == 'NOT APPLICABLE':
                        speed_risk = 0.0

                    absence_of_face_risk  = st.selectbox('Absence of face-to-face contact',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if absence_of_face_risk == 'VERY HIGH RISK':
                        absence_of_face_risk = 1
                    elif absence_of_face_risk == 'HIGH RISK':
                        absence_of_face_risk = 0.8
                    elif absence_of_face_risk == 'MEDIUM RISK':
                        absence_of_face_risk = 0.6
                    elif absence_of_face_risk == 'LOW RISK':
                        absence_of_face_risk = 0.4
                    elif absence_of_face_risk == 'VERY LOW RISK':
                        absence_of_face_risk = 0.2
                    elif absence_of_face_risk == 'NOT APPLICABLE':
                        absence_of_face_risk = 0.0

                #if form.form_submit_button("ASSESS VIRTUAL ASSET"):
                    anonmy = 1
                    p2p = 0.5
                    traceability=0.5
                    speed=0.5
                    absence_of_face =1
                    total_variable_weight = 3.5


                    weighted_score_for_anonmy = round((anonmy / total_variable_weight * anonmy_risk)*100)
                    #print(weighted_score_for_anonmy)
                    #st.write('**The weighted score for anonmy** ' + str(weighted_score_for_anonmy))

                    weighted_score_for_p2p = round((p2p / total_variable_weight * p2p_risk)*100)
                    #print(weighted_score_for_p2p)
                    #st.write('**The weighted score for p2p** ' + str(weighted_score_for_p2p))

                    weighted_score_for_traceability = round((traceability / total_variable_weight *  traceability_risk)*100)
                    #print(weighted_score_for_traceability)
                    #st.write('**The weighted score for traceability** ' + str(weighted_score_for_traceability))

                    weighted_score_for_speed = round((speed / total_variable_weight * speed_risk)*100)
                    #print(weighted_score_for_speed)
                    #st.write('**The weighted score for speed** ' + str(weighted_score_for_speed))

                    weighted_score_for_absence_of_face = round((absence_of_face / total_variable_weight *  absence_of_face_risk)*100)
                    #print(weighted_score_for_absence_of_face)
                    #st.write('**The weighted score for absence of face** ' + str(weighted_score_for_absence_of_face))

                    #name = st.number_input('Enter ID of wallet SERVICE')
                    
                    

                    VA_Nature_Profile = weighted_score_for_anonmy + weighted_score_for_p2p + weighted_score_for_traceability + weighted_score_for_speed + weighted_score_for_absence_of_face
                    VA_Nature_Profile =round((VA_Nature_Profile ))
                    st.write('**The virtual nature profile risk is** ' + str(VA_Nature_Profile))

                    if st.button('Save Details'):
                        query = f'''INSERT INTO Virtualassetnature (anonmy_risk, anonmy, p2p_risk, p2p, traceability_risk, traceability, speed_risk, speed, absence_of_face_risk, absence_of_face, VA_Nature_Profile, page_selection,VASPS_CATEGORIES) VALUES ('{anonmy_risk}', '{weighted_score_for_anonmy}', '{p2p_risk}', '{weighted_score_for_p2p}', '{traceability_risk}', '{weighted_score_for_traceability}', '{speed_risk}', '{weighted_score_for_speed}', '{absence_of_face_risk}', '{weighted_score_for_absence_of_face}', '{VA_Nature_Profile}', '{page_selection}','{VASPS_CATEGORIES}')'''
                        insert_query(query)

                    print(round(VA_Nature_Profile))
                    import matplotlib.pyplot as fig
                    fig.style.use('ggplot')
                    df = pd.DataFrame(data={'risk':['anonmy','p2p','traceability','speed','absence of face'],'VA Nature Profile':[weighted_score_for_anonmy,weighted_score_for_p2p,weighted_score_for_traceability,weighted_score_for_speed,weighted_score_for_absence_of_face]})
                    df.set_index('risk').plot(kind='bar',xlabel='risk',ylabel='risk contribution',subplots=True)
                    #st.write(df)
                    st.pyplot(fig)

                    #fig = go.Figure(data=[
                    #   go.Line(name='VA Nature Profile', x=df['risk'], y=df['VA Nature Profile'])])

                    #fig.update_layout(
                    #    xaxis_title='risk',
                    #    yaxis_title='risk contribution',
                    #    legend_title='VA Nature Profile',)
                    #st.plotly_chart(fig)
                        

                with st.expander('Accessibility to Criminal'):
                    #form = st.form("Accessibility to Criminal")
                    Mining_by_criminal_risk = st.selectbox('Mining by criminal',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Mining_by_criminal_risk == 'VERY HIGH RISK':
                        Mining_by_criminal_risk = 1
                    elif Mining_by_criminal_risk == 'HIGH RISK':
                        Mining_by_criminal_risk = 0.8
                    elif Mining_by_criminal_risk == 'MEDIUM RISK':
                        Mining_by_criminal_risk = 0.6
                    elif Mining_by_criminal_risk == 'LOW RISK':
                        Mining_by_criminal_risk = 0.4
                    elif Mining_by_criminal_risk == 'VERY LOW RISK':
                        Mining_by_criminal_risk = 0.2
                    elif Mining_by_criminal_risk == 'NOT APPLICABLE':
                        Mining_by_criminal_risk = 0.0

                    Collection_of_funds_risk  = st.selectbox('Collection of funds',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Collection_of_funds_risk == 'VERY HIGH RISK':
                        Collection_of_funds_risk = 1
                    elif Collection_of_funds_risk == 'HIGH RISK':
                        Collection_of_funds_risk = 0.8
                    elif Collection_of_funds_risk == 'MEDIUM RISK':
                        Collection_of_funds_risk = 0.6
                    elif Collection_of_funds_risk == 'LOW RISK':
                        Collection_of_funds_risk = 0.4
                    elif Collection_of_funds_risk == 'VERY LOW RISK':
                        Collection_of_funds_risk = 0.2
                    elif Collection_of_funds_risk == 'NOT APPLICABLE':
                        Collection_of_funds_risk = 0.0

                    Transfer_of_funds_risk  = st.selectbox('Transfer of funds',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Transfer_of_funds_risk == 'VERY HIGH RISK':
                        Transfer_of_funds_risk = 1
                    elif Transfer_of_funds_risk == 'HIGH RISK':
                        Transfer_of_funds_risk = 0.8
                    elif Transfer_of_funds_risk == 'MEDIUM RISK':
                        Transfer_of_funds_risk = 0.6
                    elif Transfer_of_funds_risk == 'LOW RISK':
                        Transfer_of_funds_risk = 0.4
                    elif Transfer_of_funds_risk == 'VERY LOW RISK':
                        Transfer_of_funds_risk = 0.2
                    elif Transfer_of_funds_risk == 'NOT APPLICABLE':
                        Transfer_of_funds_risk = 0.0
                    Dark_Web_Access_risk  = st.selectbox('Dark Web Access',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Dark_Web_Access_risk == 'VERY HIGH RISK':
                        Dark_Web_Access_risk = 1
                    elif Dark_Web_Access_risk == 'HIGH RISK':
                        Dark_Web_Access_risk = 0.8
                    elif Dark_Web_Access_risk == 'MEDIUM RISK':
                        Dark_Web_Access_risk = 0.6
                    elif Dark_Web_Access_risk == 'LOW RISK':
                        Dark_Web_Access_risk = 0.4
                    elif Dark_Web_Access_risk == 'VERY LOW RISK':
                        Dark_Web_Access_risk = 0.2
                    elif Dark_Web_Access_risk == 'NOT APPLICABLE':
                        Dark_Web_Access_risk = 0.0

                    Expenditure_of_funds_risk  = st.selectbox('Expenditure of funds',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Expenditure_of_funds_risk == 'VERY HIGH RISK':
                        Expenditure_of_funds_risk = 1
                    elif Expenditure_of_funds_risk == 'HIGH RISK':
                        Expenditure_of_funds_risk = 0.8
                    elif Expenditure_of_funds_risk == 'MEDIUM RISK':
                        Expenditure_of_funds_risk = 0.6
                    elif Expenditure_of_funds_risk == 'LOW RISK':
                        Expenditure_of_funds_risk = 0.4
                    elif Expenditure_of_funds_risk == 'VERY LOW RISK':
                        Expenditure_of_funds_risk = 0.2
                    elif Expenditure_of_funds_risk == 'NOT APPLICABLE':
                        Expenditure_of_funds_risk = 0.0

                #if form.form_submit_button("ASSESS VIRTUAL ASSET"):
                    Mining_by_criminal = 1
                    Collection_of_funds = 1
                    Transfer_of_funds =1
                    Dark_Web_Access = 1
                    Expenditure_of_funds = 0.5
                    total_variable_weight_for_criminality_access = 4.5
                    weighted_score_for_Mining_by_criminal= round((Mining_by_criminal / total_variable_weight_for_criminality_access * Mining_by_criminal_risk)*100)
                    #print(weighted_score_for_Mining_by_criminal)
                    #st.write('**The weighted score for Mining by criminal** ' + str(weighted_score_for_Mining_by_criminal))

                    weighted_score_for_Collection_of_funds = round((Collection_of_funds / total_variable_weight_for_criminality_access * Collection_of_funds_risk)*100)
                    #print(weighted_score_for_Collection_of_funds)
                    #st.write('**The weighted score for Collection of funds** ' + str(weighted_score_for_Collection_of_funds))

                    weighted_score_for_Transfer_of_funds = round((Transfer_of_funds / total_variable_weight_for_criminality_access *  Transfer_of_funds_risk)*100)
                    #print(weighted_score_for_Transfer_of_funds)
                    #st.write('**The weighted score for Transfer of funds** ' + str(weighted_score_for_Transfer_of_funds))

                    weighted_score_for_Dark_Web_Access = round((Dark_Web_Access / total_variable_weight_for_criminality_access * Dark_Web_Access_risk)*100)
                    #print(weighted_score_for_Dark_Web_Access)
                    #st.write('**The weighted score for Dark Web Access** ' + str(weighted_score_for_Dark_Web_Access))

                    weighted_score_for_Expenditure_of_funds = round((Expenditure_of_funds / total_variable_weight_for_criminality_access *  Expenditure_of_funds_risk)*100)
                    #print(weighted_score_for_Expenditure_of_funds)
                    #st.write('**The weighted score for Expenditure of funds** ' + str(weighted_score_for_Expenditure_of_funds))

                    
                    Accessibility_to_Criminal = weighted_score_for_Mining_by_criminal + weighted_score_for_Collection_of_funds + weighted_score_for_Transfer_of_funds + weighted_score_for_Dark_Web_Access + weighted_score_for_Expenditure_of_funds
                    Accessibility_to_Criminal =round((Accessibility_to_Criminal))
                    st.write('**The Accessibility to Criminal is** ' + str(Accessibility_to_Criminal))

                    if st.button('Accessibility_to_Criminal'):
                        query = f'''INSERT INTO Accessibility_to_Criminal (Mining_by_criminal_risk, Mining_by_criminal, Collection_of_funds_risk, Collection_of_funds, Transfer_of_funds_risk, Transfer_of_funds, Dark_Web_Access_risk, Dark_Web_Access, Expenditure_of_funds_risk, Expenditure_of_funds, Accessibility_to_Criminal, page_selection, VASPS_CATEGORIES) VALUES ('{Mining_by_criminal_risk}', '{weighted_score_for_Mining_by_criminal}', '{Collection_of_funds_risk}', '{weighted_score_for_Collection_of_funds}', '{Transfer_of_funds_risk}', '{weighted_score_for_Transfer_of_funds}', '{Dark_Web_Access_risk}', '{weighted_score_for_Dark_Web_Access}', '{Expenditure_of_funds_risk}', '{weighted_score_for_Expenditure_of_funds}', '{Accessibility_to_Criminal}', '{page_selection}', '{VASPS_CATEGORIES}')'''
                        insert_query(query)

                    print(round(Accessibility_to_Criminal))
                    import matplotlib.pyplot as fig
                    df = pd.DataFrame(data={'risk':['Mining by criminal','Collection of funds','Transfer of funds','Dark Web Access','Expenditure of funds'],'Accessibility to Criminal':[weighted_score_for_Mining_by_criminal,weighted_score_for_Collection_of_funds,weighted_score_for_Transfer_of_funds,weighted_score_for_Dark_Web_Access,weighted_score_for_Expenditure_of_funds]})
                    df.set_index('risk').plot(kind='bar',xlabel='risk',ylabel='risk contribution',subplots=True)
                    #st.write(df)
                    st.pyplot(fig)

                    #fig = go.Figure(data=[
                    #   go.Line(name='Accessibility to Criminal', x=df['risk'], y=df['Accessibility to Criminal'])])
                    
                    #fig.update_layout(
                    #   xaxis_title='risk',
                    #    yaxis_title='risk contribution',
                    #    legend_title='Accessibility to Criminal',)
                    #st.plotly_chart(fig)

                            
                    
                with st.expander('Source of funding Virtual Asset'):

                    #form = st.form("Source of funding Virtual Asset")
                    Bank_or_Card_as_source_of_funding_VA_risk = st.selectbox('Bank or Card as source of funding VA',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Bank_or_Card_as_source_of_funding_VA_risk == 'VERY HIGH RISK':
                        Bank_or_Card_as_source_of_funding_VA_risk = 1
                    elif Bank_or_Card_as_source_of_funding_VA_risk == 'HIGH RISK':
                        Bank_or_Card_as_source_of_funding_VA_risk = 0.8
                    elif Bank_or_Card_as_source_of_funding_VA_risk == 'MEDIUM RISK':
                        Bank_or_Card_as_source_of_funding_VA_risk = 0.6
                    elif Bank_or_Card_as_source_of_funding_VA_risk == 'LOW RISK':
                        Bank_or_Card_as_source_of_funding_VA_risk = 0.4
                    elif Bank_or_Card_as_source_of_funding_VA_risk == 'VERY LOW RISK':
                        Bank_or_Card_as_source_of_funding_VA_risk = 0.2
                    elif Bank_or_Card_as_source_of_funding_VA_risk == 'NOT APPLICABLE':
                        Bank_or_Card_as_source_of_funding_VA_risk = 0.0

                    Cash_transfers_valuable_in_kind_goods_risk  = st.selectbox('Cash transfers valuable in kind goods',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Cash_transfers_valuable_in_kind_goods_risk == 'VERY HIGH RISK':
                        Cash_transfers_valuable_in_kind_goods_risk = 1
                    elif Cash_transfers_valuable_in_kind_goods_risk == 'HIGH RISK':
                        Cash_transfers_valuable_in_kind_goods_risk = 0.8
                    elif Cash_transfers_valuable_in_kind_goods_risk == 'MEDIUM RISK':
                        Cash_transfers_valuable_in_kind_goods_risk = 0.6
                    elif Cash_transfers_valuable_in_kind_goods_risk == 'LOW RISK':
                        Cash_transfers_valuable_in_kind_goods_risk = 0.4
                    elif Cash_transfers_valuable_in_kind_goods_risk == 'VERY LOW RISK':
                        Cash_transfers_valuable_in_kind_goods_risk = 0.2
                    elif Cash_transfers_valuable_in_kind_goods_risk == 'NOT APPLICABLE':
                        Cash_transfers_valuable_in_kind_goods_risk = 0.0

                    Use_of_virtual_currency_risk  = st.selectbox('Transfer  funds',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Use_of_virtual_currency_risk == 'VERY HIGH RISK':
                        Use_of_virtual_currency_risk = 1
                    elif Use_of_virtual_currency_risk == 'HIGH RISK':
                        Use_of_virtual_currency_risk = 0.8
                    elif Use_of_virtual_currency_risk == 'MEDIUM RISK':
                        Use_of_virtual_currency_risk = 0.6
                    elif Use_of_virtual_currency_risk == 'LOW RISK':
                        Use_of_virtual_currency_risk = 0.4
                    elif Use_of_virtual_currency_risk == 'VERY LOW RISK':
                        Use_of_virtual_currency_risk = 0.2
                    elif Use_of_virtual_currency_risk == 'NOT APPLICABLE':
                        Use_of_virtual_currency_risk = 0.0
                    

                #if form.form_submit_button("ASSESS VIRTUAL ASSET"):
                    Bank_or_Card_as_source_of_funding_VA = 0.2
                    Cash_transfers_valuable_in_kind_goods = 1
                    Use_of_virtual_currency =1
                    total_variable_weight_for_Source_of_funding_Virtual_Asset = 2.2
                    weighted_score_for_Bank_or_Card_as_source_of_funding_VA= round((Bank_or_Card_as_source_of_funding_VA / total_variable_weight_for_Source_of_funding_Virtual_Asset * Bank_or_Card_as_source_of_funding_VA_risk)*100)
                    #print(weighted_score_for_Bank_or_Card_as_source_of_funding_VA)
                    #st.write('**The weighted score for Bank or Card as source of funding VA** ' + str(weighted_score_for_Bank_or_Card_as_source_of_funding_VA))

                    weighted_score_for_Cash_transfers_valuable_in_kind_goods = round((Cash_transfers_valuable_in_kind_goods / total_variable_weight_for_Source_of_funding_Virtual_Asset * Cash_transfers_valuable_in_kind_goods_risk)*100)
                    #print(weighted_score_for_Cash_transfers_valuable_in_kind_goods)
                    #st.write('**The weighted score for Cash transfers valuable in kind goods** ' + str(weighted_score_for_Cash_transfers_valuable_in_kind_goods))

                    weighted_score_for_Use_of_virtual_currency = round((Use_of_virtual_currency / total_variable_weight_for_Source_of_funding_Virtual_Asset *  Use_of_virtual_currency_risk)*100)
                    #print(weighted_score_for_Use_of_virtual_currency)
                    #st.write('**The weighted score for Use of virtual currency** ' + str(weighted_score_for_Use_of_virtual_currency))
                    
                    
                    Source_of_funding_Virtual_Asset = weighted_score_for_Bank_or_Card_as_source_of_funding_VA + weighted_score_for_Cash_transfers_valuable_in_kind_goods + weighted_score_for_Use_of_virtual_currency 
                    Source_of_funding_Virtual_Asset =round((Source_of_funding_Virtual_Asset ))
                    st.write('**The Source of funding Virtual Asset is** ' + str(Source_of_funding_Virtual_Asset))


                    if st.button('Source_of_funding_Virtual_Asset'):
                        query = f'''INSERT INTO Source_of_funding_Virtual_Asset (Bank_or_Card_as_source_of_funding_VA_risk, Bank_or_Card_as_source_of_funding_VA, Cash_transfers_valuable_in_kind_goods_risk, Cash_transfers_valuable_in_kind_goods, Use_of_virtual_currency_risk, Use_of_virtual_currency, Source_of_funding_Virtual_Asset, page_selection, VASPS_CATEGORIES) VALUES ('{Bank_or_Card_as_source_of_funding_VA_risk}', '{weighted_score_for_Bank_or_Card_as_source_of_funding_VA}', '{Cash_transfers_valuable_in_kind_goods_risk}', '{weighted_score_for_Cash_transfers_valuable_in_kind_goods}', '{Use_of_virtual_currency_risk}', '{weighted_score_for_Use_of_virtual_currency}', {Source_of_funding_Virtual_Asset}, '{page_selection}', '{VASPS_CATEGORIES}')'''
                        insert_query(query)

                    print(round(Source_of_funding_Virtual_Asset))
                    import matplotlib.pyplot as fig
                    df = pd.DataFrame(data={'risk':['Bank or Card as source of funding VA','Cash transfers valuable in kind goods','Use of virtual currency'],'Source of funding Virtual Asset':[weighted_score_for_Bank_or_Card_as_source_of_funding_VA,weighted_score_for_Cash_transfers_valuable_in_kind_goods,weighted_score_for_Use_of_virtual_currency]})
                    df.set_index('risk').plot(kind='bar',xlabel='risk',ylabel='risk contribution',subplots=True)
                    #st.write(df)
                    st.pyplot(fig)

                    #fig = go.Figure(data=[
                    #    go.Line(name='Source of funding Virtual Asset', x=df['risk'], y=df['Source of funding Virtual Asset'])])
                    
                    #fig.update_layout(
                    #    xaxis_title='risk',
                    #    yaxis_title='risk contribution',
                    #    legend_title='Accessibility to Criminal',)
                    #st.plotly_chart(fig)   

            with col2:
                with st.expander('Operational features of VA'):
                    #form = st.form("Operational features of VA")
                    Regulated_risk = st.selectbox('Regulated',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Regulated_risk == 'VERY HIGH RISK':
                        Regulated_risk = 1
                    elif Regulated_risk == 'HIGH RISK':
                        Regulated_risk = 0.8
                    elif Regulated_risk == 'MEDIUM RISK':
                        Regulated_risk = 0.6
                    elif Regulated_risk == 'LOW RISK':
                        Regulated_risk = 0.4
                    elif Regulated_risk == 'VERY LOW RISK':
                        Regulated_risk = 0.2
                    elif Regulated_risk == 'NOT APPLICABLE':
                        Regulated_risk = 0.0

                    Unregulated_risk  = st.selectbox('Unregulated',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Unregulated_risk == 'VERY HIGH RISK':
                        Unregulated_risk = 1
                    elif Unregulated_risk == 'HIGH RISK':
                        Unregulated_risk = 0.8
                    elif Unregulated_risk == 'MEDIUM RISK':
                        Unregulated_risk = 0.6
                    elif Unregulated_risk == 'LOW RISK':
                        Unregulated_risk = 0.4
                    elif Unregulated_risk == 'VERY LOW RISK':
                        Unregulated_risk = 0.2
                    elif Unregulated_risk == 'NOT APPLICABLE':
                        Unregulated_risk = 0.0

                    Centralised_Environment_risk  = st.selectbox('Centralised Environment',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Centralised_Environment_risk == 'VERY HIGH RISK':
                        Centralised_Environment_risk = 1
                    elif Centralised_Environment_risk == 'HIGH RISK':
                        Centralised_Environment_risk = 0.8
                    elif Centralised_Environment_risk == 'MEDIUM RISK':
                        Centralised_Environment_risk = 0.6
                    elif Centralised_Environment_risk == 'LOW RISK':
                        Centralised_Environment_risk = 0.4
                    elif Centralised_Environment_risk == 'VERY LOW RISK':
                        Centralised_Environment_risk = 0.2
                    elif Centralised_Environment_risk == 'NOT APPLICABLE':
                        Centralised_Environment_risk = 0.0
                    Decentralised_Environment_risk  = st.selectbox('Decentralised Environment',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Decentralised_Environment_risk == 'VERY HIGH RISK':
                        Decentralised_Environment_risk = 1
                    elif Decentralised_Environment_risk == 'HIGH RISK':
                        Decentralised_Environment_risk = 0.8
                    elif Decentralised_Environment_risk == 'MEDIUM RISK':
                        Decentralised_Environment_risk = 0.6
                    elif Decentralised_Environment_risk == 'LOW RISK':
                        Decentralised_Environment_risk = 0.4
                    elif Decentralised_Environment_risk == 'VERY LOW RISK':
                        Decentralised_Environment_risk = 0.2
                    elif Decentralised_Environment_risk == 'NOT APPLICABLE':
                        Decentralised_Environment_risk = 0.0

                    

                #if form.form_submit_button("ASSESS VIRTUAL ASSET"):
                    Regulated = 0.5
                    Unregulated = 1
                    Centralised_Environment =0.2
                    Decentralised_Environment = 1
                    total_variable_weight_for_Operational_features_of_VA = 2.7
                    weighted_score_for_Regulated= round((Regulated / total_variable_weight_for_Operational_features_of_VA * Regulated_risk)*100)
                    #print(weighted_score_for_Regulated)
                    #st.write('**The weighted score for Regulated** ' + str(weighted_score_for_Regulated))

                    weighted_score_for_Unregulated = round((Unregulated / total_variable_weight_for_Operational_features_of_VA * Unregulated_risk)*100)
                    #print(weighted_score_for_Unregulated)
                    #st.write('**The weighted score for Collection of funds** ' + str(weighted_score_for_Unregulated))

                    weighted_score_for_Centralised_Environment = round((Centralised_Environment / total_variable_weight_for_Operational_features_of_VA *  Centralised_Environment_risk)*100)
                    #print(weighted_score_for_Centralised_Environment)
                    #st.write('**The weighted score for Transfer of funds** ' + str(weighted_score_for_Centralised_Environment))

                    weighted_score_for_Decentralised_Environment = round((Decentralised_Environment / total_variable_weight_for_Operational_features_of_VA * Decentralised_Environment_risk)*100)
                    #print(weighted_score_for_Decentralised_Environment)
                    #st.write('**The weighted score for Decentralised Environment** ' + str(weighted_score_for_Decentralised_Environment))


                    Operational_features_of_VA = weighted_score_for_Regulated + weighted_score_for_Unregulated + weighted_score_for_Centralised_Environment + weighted_score_for_Decentralised_Environment 
                    Operational_features_of_VA =round((Operational_features_of_VA ))
                    st.write('**The Operational features of VA is** ' + str(Operational_features_of_VA))


                    if st.button('Operational_features_of_VA'):
                        query = f'''INSERT INTO operationalfeaturesofva (Regulated_risk, Regulated, Unregulated_risk ,Unregulated, Centralised_Environment_risk, Centralised_Environment, Decentralised_Environment_risk, Decentralised_Environment, Operational_features_of_VA, page_selection, VASPS_CATEGORIES) VALUES ('{Regulated_risk}', '{weighted_score_for_Regulated}', '{Unregulated_risk}', '{weighted_score_for_Unregulated}', '{Centralised_Environment_risk}', '{weighted_score_for_Centralised_Environment}', '{Decentralised_Environment_risk}', '{weighted_score_for_Decentralised_Environment}', '{Operational_features_of_VA}', '{page_selection}','{VASPS_CATEGORIES}')'''
                        insert_query(query)




                    print(round(Operational_features_of_VA))
                    import matplotlib.pyplot as fig
                    df = pd.DataFrame(data={'risk':['Regulated','Unregulated','Centralised Environment','Decentralised Environment'],'Operational features of VA':[weighted_score_for_Regulated,weighted_score_for_Unregulated,weighted_score_for_Centralised_Environment,weighted_score_for_Decentralised_Environment]})
                    df.set_index('risk').plot(kind='bar',xlabel='risk',ylabel='risk contribution',subplots=True)
                    #st.write(df)
                    st.pyplot(fig)

                    #fig = go.Figure(data=[
                    #    go.Line(name='Operational features of VA', x=df['risk'], y=df['Operational features of VA'])])
                    
                    #fig.update_layout(
                    #    xaxis_title='risk',
                    #    yaxis_title='risk contribution',
                    #    legend_title='Operational features of VA',)
                    #st.plotly_chart(fig)
                
                with st.expander('Ease of Criminality'):
                    #form = st.form("Ease of Criminality")
                    Tax_Evasion_risk = st.selectbox('Tax Evasion',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Tax_Evasion_risk == 'VERY HIGH RISK':
                        Tax_Evasion_risk = 1
                    elif Tax_Evasion_risk == 'HIGH RISK':
                        Tax_Evasion_risk = 0.8
                    elif Tax_Evasion_risk == 'MEDIUM RISK':
                        Tax_Evasion_risk = 0.6
                    elif Tax_Evasion_risk == 'LOW RISK':
                        Tax_Evasion_risk = 0.4
                    elif Tax_Evasion_risk == 'VERY LOW RISK':
                        Tax_Evasion_risk = 0.2
                    elif Tax_Evasion_risk == 'NOT APPLICABLE':
                        Tax_Evasion_risk = 0.0

                    Terrorist_Financing_risk  = st.selectbox('Terrorist Financing',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Terrorist_Financing_risk == 'VERY HIGH RISK':
                        Terrorist_Financing_risk = 1
                    elif Terrorist_Financing_risk == 'HIGH RISK':
                        Terrorist_Financing_risk = 0.8
                    elif Terrorist_Financing_risk == 'MEDIUM RISK':
                        Terrorist_Financing_risk = 0.6
                    elif Terrorist_Financing_risk == 'LOW RISK':
                        Terrorist_Financing_risk = 0.4
                    elif Terrorist_Financing_risk == 'VERY LOW RISK':
                        Terrorist_Financing_risk = 0.2
                    elif Terrorist_Financing_risk == 'NOT APPLICABLE':
                        Terrorist_Financing_risk = 0.0

                    Disguising_Criminal_Proceeds_to_VA_not_regulated_risk  = st.selectbox('Disguising Criminal Proceeds to VA not regulated',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Disguising_Criminal_Proceeds_to_VA_not_regulated_risk == 'VERY HIGH RISK':
                        Disguising_Criminal_Proceeds_to_VA_not_regulated_risk = 1
                    elif Disguising_Criminal_Proceeds_to_VA_not_regulated_risk == 'HIGH RISK':
                        Disguising_Criminal_Proceeds_to_VA_not_regulated_risk = 0.8
                    elif Disguising_Criminal_Proceeds_to_VA_not_regulated_risk == 'MEDIUM RISK':
                        Disguising_Criminal_Proceeds_to_VA_not_regulated_risk = 0.6
                    elif Disguising_Criminal_Proceeds_to_VA_not_regulated_risk == 'LOW RISK':
                        Disguising_Criminal_Proceeds_to_VA_not_regulated_risk = 0.4
                    elif Disguising_Criminal_Proceeds_to_VA_not_regulated_risk == 'VERY LOW RISK':
                        Disguising_Criminal_Proceeds_to_VA_not_regulated_risk = 0.2
                    elif Disguising_Criminal_Proceeds_to_VA_not_regulated_risk == 'NOT APPLICABLE':
                        Disguising_Criminal_Proceeds_to_VA_not_regulated_risk = 0.0
                    Trace_and_seize_difficulty_risk  = st.selectbox('Trace and seize difficulty',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Trace_and_seize_difficulty_risk == 'VERY HIGH RISK':
                        Trace_and_seize_difficulty_risk = 1
                    elif Trace_and_seize_difficulty_risk == 'HIGH RISK':
                        Trace_and_seize_difficulty_risk = 0.8
                    elif Trace_and_seize_difficulty_risk == 'MEDIUM RISK':
                        Trace_and_seize_difficulty_risk = 0.6
                    elif Trace_and_seize_difficulty_risk == 'LOW RISK':
                        Trace_and_seize_difficulty_risk = 0.4
                    elif Trace_and_seize_difficulty_risk == 'VERY LOW RISK':
                        Trace_and_seize_difficulty_risk = 0.2
                    elif Trace_and_seize_difficulty_risk == 'NOT APPLICABLE':
                        Trace_and_seize_difficulty_risk = 0.0

                    Circumvent_Exchange_Control_risk  = st.selectbox('Circumvent Exchange Control',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Circumvent_Exchange_Control_risk == 'VERY HIGH RISK':
                        Circumvent_Exchange_Control_risk = 1
                    elif Circumvent_Exchange_Control_risk == 'HIGH RISK':
                        Circumvent_Exchange_Control_risk = 0.8
                    elif Circumvent_Exchange_Control_risk == 'MEDIUM RISK':
                        Circumvent_Exchange_Control_risk = 0.6
                    elif Circumvent_Exchange_Control_risk == 'LOW RISK':
                        Circumvent_Exchange_Control_risk = 0.4
                    elif Circumvent_Exchange_Control_risk == 'VERY LOW RISK':
                        Circumvent_Exchange_Control_risk = 0.2
                    elif Circumvent_Exchange_Control_risk == 'NOT APPLICABLE':
                        Circumvent_Exchange_Control_risk = 0.0

                #if form.form_submit_button("ASSESS VIRTUAL ASSET"):
                    Tax_Evasion = 1
                    Terrorist_Financing = 1
                    Disguising_Criminal_Proceeds_to_VA_not_regulated =1
                    Trace_and_seize_difficulty = 1
                    Circumvent_Exchange_Control= 1
                    total_variable_weight_for_ease_of_criminality = 5
                    weighted_score_for_Tax_Evasion= round((Tax_Evasion / total_variable_weight_for_ease_of_criminality * Tax_Evasion_risk)*100)
                    #print(weighted_score_for_Tax_Evasion)
                    #st.write('**The weighted score for Tax Evasion** ' + str(weighted_score_for_Tax_Evasion))

                    weighted_score_for_Terrorist_Financing = round((Terrorist_Financing / total_variable_weight_for_ease_of_criminality * Terrorist_Financing_risk)*100)
                    #print(weighted_score_for_Terrorist_Financing)
                    #st.write('**The weighted score for Terrorist Financing** ' + str(weighted_score_for_Terrorist_Financing))

                    weighted_score_for_Disguising_Criminal_Proceeds_to_VA_not_regulated = round((Disguising_Criminal_Proceeds_to_VA_not_regulated / total_variable_weight_for_ease_of_criminality *  Disguising_Criminal_Proceeds_to_VA_not_regulated_risk)*100)
                    #print(weighted_score_for_Disguising_Criminal_Proceeds_to_VA_not_regulated)
                    #st.write('**The weighted score for Disguising Criminal Proceeds to VA not regulated** ' + str(weighted_score_for_Disguising_Criminal_Proceeds_to_VA_not_regulated))

                    weighted_score_for_Trace_and_seize_difficulty = round((Trace_and_seize_difficulty / total_variable_weight_for_ease_of_criminality * Trace_and_seize_difficulty_risk)*100)
                    #print(weighted_score_for_Trace_and_seize_difficulty)
                    #st.write('**The weighted score for Trace and seize difficulty** ' + str(weighted_score_for_Trace_and_seize_difficulty))

                    weighted_score_for_Circumvent_Exchange_Control = round((Circumvent_Exchange_Control / total_variable_weight_for_ease_of_criminality *  Circumvent_Exchange_Control_risk)*100)
                    #print(weighted_score_for_Circumvent_Exchange_Control)
                    #st.write('**The weighted score for Circumvent Exchange Control** ' + str(weighted_score_for_Circumvent_Exchange_Control))

                    

                    Ease_of_criminality = weighted_score_for_Tax_Evasion + weighted_score_for_Terrorist_Financing + weighted_score_for_Disguising_Criminal_Proceeds_to_VA_not_regulated + weighted_score_for_Trace_and_seize_difficulty + weighted_score_for_Circumvent_Exchange_Control
                    Ease_of_criminality =round((Ease_of_criminality ))
                    st.write('**The Ease of criminality is** ' + str(Ease_of_criminality))

                    if st.button('Ease_of_criminality'):
                        query = f'''INSERT INTO Ease_of_criminality (Tax_Evasion_risk, Tax_Evasion, Terrorist_Financing_risk, Terrorist_Financing, Disguising_Criminal_Proceeds_to_VA_not_regulated_risk, Disguising_Criminal_Proceeds_to_VA_not_regulated, Trace_and_seize_difficulty_risk, Trace_and_seize_difficulty, Circumvent_Exchange_Control_risk, Circumvent_Exchange_Control, Ease_of_criminality, page_selection, VASPS_CATEGORIES) VALUES ('{Tax_Evasion_risk}', '{weighted_score_for_Tax_Evasion}', '{Terrorist_Financing_risk}', '{weighted_score_for_Terrorist_Financing}', '{Disguising_Criminal_Proceeds_to_VA_not_regulated_risk}', '{weighted_score_for_Disguising_Criminal_Proceeds_to_VA_not_regulated}', '{Trace_and_seize_difficulty_risk}', '{weighted_score_for_Trace_and_seize_difficulty}', '{Circumvent_Exchange_Control_risk}', '{weighted_score_for_Circumvent_Exchange_Control}', '{Ease_of_criminality}', '{page_selection}', '{VASPS_CATEGORIES}')'''
                        insert_query(query)

                    print(round(Ease_of_criminality))
                    import matplotlib.pyplot as fig
                    df = pd.DataFrame(data={'risk':['Tax Evasion','Terrorist Financing','Disguising Criminal Proceeds to VA not regulated','Trace and seize difficulty','Circumvent Exchange Control'],'Ease of criminality':[weighted_score_for_Tax_Evasion,weighted_score_for_Terrorist_Financing,weighted_score_for_Disguising_Criminal_Proceeds_to_VA_not_regulated,weighted_score_for_Trace_and_seize_difficulty,weighted_score_for_Circumvent_Exchange_Control]})
                    df.set_index('risk').plot(kind='bar',xlabel='risk',ylabel='risk contribution',subplots=True)
                    #st.write(df)
                    st.pyplot(fig)

                    #fig = go.Figure(data=[
                    #    go.Line(name='Ease of criminality', x=df['risk'], y=df['Ease of criminality'])])
                    
                    #fig.update_layout(
                    #    xaxis_title='risk',
                    #    yaxis_title='risk contribution',
                    #    legend_title='Ease of criminality',)
                    #st.plotly_chart(fig)


                with st.expander('Economic Impact'):
                    #form = st.form("Economic Impact")
                    Underground_Economy_risk = st.selectbox('Underground Economy',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Underground_Economy_risk == 'VERY HIGH RISK':
                        Underground_Economy_risk = 1
                    elif Underground_Economy_risk == 'HIGH RISK':
                        Underground_Economy_risk = 0.8
                    elif Underground_Economy_risk == 'MEDIUM RISK':
                        Underground_Economy_risk = 0.6
                    elif Underground_Economy_risk == 'LOW RISK':
                        Underground_Economy_risk = 0.4
                    elif Underground_Economy_risk == 'VERY LOW RISK':
                        Underground_Economy_risk = 0.2
                    elif Underground_Economy_risk == 'NOT APPLICABLE':
                        Underground_Economy_risk = 0.0

                    Full_integration_with_financial_services_market_risk  = st.selectbox('Full integration with financial services market',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Full_integration_with_financial_services_market_risk == 'VERY HIGH RISK':
                        Full_integration_with_financial_services_market_risk = 1
                    elif Full_integration_with_financial_services_market_risk == 'HIGH RISK':
                        Full_integration_with_financial_services_market_risk = 0.8
                    elif Full_integration_with_financial_services_market_risk == 'MEDIUM RISK':
                        Full_integration_with_financial_services_market_risk = 0.6
                    elif Full_integration_with_financial_services_market_risk == 'LOW RISK':
                        Full_integration_with_financial_services_market_risk = 0.4
                    elif Full_integration_with_financial_services_market_risk == 'VERY LOW RISK':
                        Full_integration_with_financial_services_market_risk = 0.2
                    elif Full_integration_with_financial_services_market_risk == 'NOT APPLICABLE':
                        Full_integration_with_financial_services_market_risk = 0.0

                    Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market_risk  = st.selectbox('Prohibit any interaction between the financial institutions and the VC market\
            ',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market_risk == 'VERY HIGH RISK':
                        Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market_risk = 1
                    elif Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market_risk == 'HIGH RISK':
                        Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market_risk = 0.8
                    elif Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market_risk == 'MEDIUM RISK':
                        Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market_risk = 0.6
                    elif Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market_risk == 'LOW RISK':
                        Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market_risk = 0.4
                    elif Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market_risk == 'VERY LOW RISK':
                        Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market_risk = 0.2
                    elif Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market_risk == 'NOT APPLICABLE':
                        Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market_risk = 0.0

                    High_level_of_the_accountability_product_provider_risk  = st.selectbox('High level of the accountability product provider\
            ',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if High_level_of_the_accountability_product_provider_risk == 'VERY HIGH RISK':
                        High_level_of_the_accountability_product_provider_risk = 1
                    elif High_level_of_the_accountability_product_provider_risk == 'HIGH RISK':
                        High_level_of_the_accountability_product_provider_risk = 0.8
                    elif High_level_of_the_accountability_product_provider_risk == 'MEDIUM RISK':
                        High_level_of_the_accountability_product_provider_risk = 0.6
                    elif High_level_of_the_accountability_product_provider_risk == 'LOW RISK':
                        High_level_of_the_accountability_product_provider_risk = 0.4
                    elif High_level_of_the_accountability_product_provider_risk == 'VERY LOW RISK':
                        High_level_of_the_accountability_product_provider_risk = 0.2
                    elif High_level_of_the_accountability_product_provider_risk == 'NOT APPLICABLE':
                        High_level_of_the_accountability_product_provider_risk = 0.0


                #if form.form_submit_button("ASSESS VIRTUAL ASSET"):
                    Underground_Economy = 1
                    Full_integration_with_financial_services_market = 0.5
                    Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market = 1
                    High_level_of_the_accountability_product_provider = 0.2
                    total_variable_weight_for_economy_impact = 2.7
                    weighted_score_for_Underground_Economy= round((Underground_Economy / total_variable_weight_for_economy_impact * Underground_Economy_risk)*100)
                    #print(weighted_score_for_Underground_Economy)
                    #st.write('**The weighted score for Mining by criminal** ' + str(weighted_score_for_Underground_Economy))

                    weighted_score_for_Full_integration_with_financial_services_market = round((Full_integration_with_financial_services_market / total_variable_weight_for_economy_impact * Full_integration_with_financial_services_market_risk)*100)
                    #print(weighted_score_for_Full_integration_with_financial_services_market)
                    #st.write('**The weighted score for Full integration with financial services market** ' + str(weighted_score_for_Full_integration_with_financial_services_market))

                    weighted_score_for_Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market = round((Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market / total_variable_weight_for_economy_impact *  Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market_risk)*100)
                    #print(weighted_score_for_Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market)
                    #st.write('**The weighted score for Prohibit any interaction between the financial institutions and the VC market** ' + str(weighted_score_for_Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market))

                    weighted_score_for_High_level_of_the_accountability_product_provider = round((High_level_of_the_accountability_product_provider / total_variable_weight_for_economy_impact * High_level_of_the_accountability_product_provider_risk)*100)
                    #print(weighted_score_for_High_level_of_the_accountability_product_provider)
                    #st.write('**The weighted score for High level of the accountability product provider** ' + str(weighted_score_for_High_level_of_the_accountability_product_provider))


                    Economy_impact = weighted_score_for_Underground_Economy + weighted_score_for_Full_integration_with_financial_services_market + weighted_score_for_Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market + weighted_score_for_High_level_of_the_accountability_product_provider
                    Economy_impact =round((Economy_impact ))
                    st.write('**The Economy impact is** ' + str(Economy_impact))

                    if st.button('Economy_impact'):
                        query = f'''INSERT INTO Economy_impact (Underground_Economy_risk, Underground_Economy, Full_integration_with_financial_services_market_risk, Full_integration_with_financial_services_market, Prohibit_institutions_and_VC_market_risk, Prohibit_institutions_and_VC_market, High_level_of_the_accountability_product_provider_risk, High_level_of_the_accountability_product_provider, Economy_impact, page_selection,VASPS_CATEGORIES) VALUES ('{Underground_Economy_risk}', '{weighted_score_for_Underground_Economy}', '{Full_integration_with_financial_services_market_risk}', '{weighted_score_for_Full_integration_with_financial_services_market}', '{Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market_risk}', '{weighted_score_for_Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market}', '{High_level_of_the_accountability_product_provider_risk}', '{weighted_score_for_High_level_of_the_accountability_product_provider}', '{Economy_impact}', '{page_selection}','{VASPS_CATEGORIES}')'''
                        insert_query(query)

                    print(round(Economy_impact))
                    import matplotlib.pyplot as fig
                    df = pd.DataFrame(data={'risk':['Underground Economy','Full integration with financial services market','Prohibit any interaction between the financial institutions and the VC market','High level of the accountability product provider'],'Economy impact':[weighted_score_for_Underground_Economy,weighted_score_for_Full_integration_with_financial_services_market,weighted_score_for_Prohibit_any_interaction_between_the_financial_institutions_and_the_VC_market,weighted_score_for_High_level_of_the_accountability_product_provider]})
                    df.set_index('risk').plot(kind='bar',xlabel='risk',ylabel='risk contribution',subplots=True)
                    #st.write(df)
                    st.pyplot(fig)

                    #fig = go.Figure(data=[
                    #    go.Line(name='Economy impact', x=df['risk'], y=df['Economy impact'])])
                    
                    #fig.update_layout(
                    #   xaxis_title='risk',
                    #    yaxis_title='risk contribution',
                    #    legend_title='Economy impact',)
                    #st.plotly_chart(fig)

            Total_Product_Dimension = (VA_Nature_Profile + Accessibility_to_Criminal + Source_of_funding_Virtual_Asset + Operational_features_of_VA + Ease_of_criminality + Economy_impact)/6
            PRODUCTDIMENSION = st.button('PRODUCT DIMENSION')
            if PRODUCTDIMENSION:
                Total_Product_Dimension = int((VA_Nature_Profile + Accessibility_to_Criminal + Source_of_funding_Virtual_Asset + Operational_features_of_VA + Ease_of_criminality + Economy_impact)/6)
                query = f'''INSERT INTO Total_Product_Dimension (VA_Nature_Profile,Accessibility_to_Criminal, Source_of_funding_Virtual_Asset, Operational_features_of_VA,Ease_of_criminality, Economy_impact, Total_Product_Dimension, page_selection,VASPS_CATEGORIES) VALUES ('{VA_Nature_Profile}', '{Accessibility_to_Criminal}', '{Source_of_funding_Virtual_Asset}', '{Operational_features_of_VA}', '{Ease_of_criminality}', '{Economy_impact}', '{Total_Product_Dimension}', '{page_selection}', '{VASPS_CATEGORIES}')'''
                insert_query(query)
                st.write(Total_Product_Dimension)

            return Total_Product_Dimension
        


    
    


    #Product_Dimension()
            
    
    def Entity_Dimension():
        if selected =='ENTITY DIMENSION':
            st.subheader(":green[VULNERABILITY ENTITY DIMENSION]")
            with st.expander('Products and services provided, and the types of VA'):
                #with st.form("Products and services provided, and the types of VA"):
                col1, col2 = st.columns(2)
                with col1:
                    Licensed_in_the_country_or_abroad_risk = st.selectbox('Licensed in the country or abroad',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Licensed_in_the_country_or_abroad_risk == 'VERY HIGH RISK':
                        Licensed_in_the_country_or_abroad_risk = 1
                    elif Licensed_in_the_country_or_abroad_risk == 'HIGH RISK':
                        Licensed_in_the_country_or_abroad_risk = 0.8
                    elif Licensed_in_the_country_or_abroad_risk == 'MEDIUM RISK':
                        Licensed_in_the_country_or_abroad_risk = 0.6
                    elif Licensed_in_the_country_or_abroad_risk == 'LOW RISK':
                        Licensed_in_the_country_or_abroad_risk = 0.4
                    elif Licensed_in_the_country_or_abroad_risk == 'VERY LOW RISK':
                        Licensed_in_the_country_or_abroad_risk = 0.2
                    elif Licensed_in_the_country_or_abroad_risk == 'NOT APPLICABLE':
                        Licensed_in_the_country_or_abroad_risk = 0.0

                    Nature_size_and_complexity_of_business_risk  = st.selectbox('Nature size and complexity of business',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Nature_size_and_complexity_of_business_risk == 'VERY HIGH RISK':
                        Nature_size_and_complexity_of_business_risk = 1
                    elif Nature_size_and_complexity_of_business_risk == 'HIGH RISK':
                        Nature_size_and_complexity_of_business_risk = 0.8
                    elif Nature_size_and_complexity_of_business_risk == 'MEDIUM RISK':
                        Nature_size_and_complexity_of_business_risk = 0.6
                    elif Nature_size_and_complexity_of_business_risk == 'LOW RISK':
                        Nature_size_and_complexity_of_business_risk = 0.4
                    elif Nature_size_and_complexity_of_business_risk == 'VERY LOW RISK':
                        Nature_size_and_complexity_of_business_risk = 0.2
                    elif Nature_size_and_complexity_of_business_risk == 'NOT APPLICABLE':
                        Nature_size_and_complexity_of_business_risk = 0.0

                    Products_or_services_risk  = st.selectbox('Products or services ',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Products_or_services_risk == 'VERY HIGH RISK':
                        Products_or_services_risk = 1
                    elif Products_or_services_risk == 'HIGH RISK':
                        Products_or_services_risk = 0.8
                    elif Products_or_services_risk == 'MEDIUM RISK':
                        Products_or_services_risk = 0.6
                    elif Products_or_services_risk == 'LOW RISK':
                        Products_or_services_risk = 0.4
                    elif Products_or_services_risk == 'VERY LOW RISK':
                        Products_or_services_risk = 0.2
                    elif Products_or_services_risk == 'NOT APPLICABLE':
                        Products_or_services_risk = 0.0

                    Methods_of_delivery_of_products_or_services_risk  = st.selectbox('Methods of delivery of products or services ',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Methods_of_delivery_of_products_or_services_risk == 'VERY HIGH RISK':
                        Methods_of_delivery_of_products_or_services_risk = 1
                    elif Methods_of_delivery_of_products_or_services_risk == 'HIGH RISK':
                        Methods_of_delivery_of_products_or_services_risk = 0.8
                    elif Methods_of_delivery_of_products_or_services_risk == 'MEDIUM RISK':
                        Methods_of_delivery_of_products_or_services_risk = 0.6
                    elif Methods_of_delivery_of_products_or_services_risk == 'LOW RISK':
                        Methods_of_delivery_of_products_or_services_risk = 0.4
                    elif Methods_of_delivery_of_products_or_services_risk == 'VERY LOW RISK':
                        Methods_of_delivery_of_products_or_services_risk = 0.2
                    elif Methods_of_delivery_of_products_or_services_risk == 'NOT APPLICABLE':
                        Methods_of_delivery_of_products_or_services_risk = 0.0
                    
                    Customer_types_risk  = st.selectbox('Customer types',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Customer_types_risk == 'VERY HIGH RISK':
                        Customer_types_risk = 1
                    elif Customer_types_risk == 'HIGH RISK':
                        Customer_types_risk = 0.8
                    elif Customer_types_risk == 'MEDIUM RISK':
                        Customer_types_risk = 0.6
                    elif Customer_types_risk == 'LOW RISK':
                        Customer_types_risk = 0.4
                    elif Customer_types_risk == 'VERY LOW RISK':
                        Customer_types_risk = 0.2
                    elif Customer_types_risk == 'NOT APPLICABLE':
                        Customer_types_risk = 0.0
                
                with col2:
                    Country_risk = st.selectbox('Country risk',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Country_risk == 'VERY HIGH RISK':
                        Country_risk = 1
                    elif Country_risk == 'HIGH RISK':
                        Country_risk = 0.8
                    elif Country_risk == 'MEDIUM RISK':
                        Country_risk = 0.6
                    elif Country_risk == 'LOW RISK':
                        Country_risk = 0.4
                    elif Country_risk == 'VERY LOW RISK':
                        Country_risk = 0.2
                    elif Country_risk == 'NOT APPLICABLE':
                        Country_risk = 0.0
                    
                    Institutions_dealing_with_VASP_risk  = st.selectbox('Institutions dealing with VASP',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Institutions_dealing_with_VASP_risk == 'VERY HIGH RISK':
                        Institutions_dealing_with_VASP_risk = 1
                    elif Institutions_dealing_with_VASP_risk == 'HIGH RISK':
                        Institutions_dealing_with_VASP_risk = 0.8
                    elif Institutions_dealing_with_VASP_risk == 'MEDIUM RISK':
                        Institutions_dealing_with_VASP_risk = 0.6
                    elif Institutions_dealing_with_VASP_risk == 'LOW RISK':
                        Institutions_dealing_with_VASP_risk = 0.4
                    elif Institutions_dealing_with_VASP_risk == 'VERY LOW RISK':
                        Institutions_dealing_with_VASP_risk = 0.2
                    elif Institutions_dealing_with_VASP_risk == 'NOT APPLICABLE':
                        Institutions_dealing_with_VASP_risk = 0.0

                    VA_Anonymity_or_pseudonymity_risk  = st.selectbox('VA Anonymity or pseudonymity',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if VA_Anonymity_or_pseudonymity_risk == 'VERY HIGH RISK':
                        VA_Anonymity_or_pseudonymity_risk = 1
                    elif VA_Anonymity_or_pseudonymity_risk == 'HIGH RISK':
                        VA_Anonymity_or_pseudonymity_risk = 0.8
                    elif VA_Anonymity_or_pseudonymity_risk == 'MEDIUM RISK':
                        VA_Anonymity_or_pseudonymity_risk = 0.6
                    elif VA_Anonymity_or_pseudonymity_risk == 'LOW RISK':
                        VA_Anonymity_or_pseudonymity_risk = 0.4
                    elif VA_Anonymity_or_pseudonymity_risk == 'VERY LOW RISK':
                        VA_Anonymity_or_pseudonymity_risk = 0.2
                    elif VA_Anonymity_or_pseudonymity_risk == 'NOT APPLICABLE':
                        VA_Anonymity_or_pseudonymity_risk = 0.0

                    Rapid_transaction_settlement_risk  = st.selectbox('Rapid transaction settlement',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Rapid_transaction_settlement_risk == 'VERY HIGH RISK':
                        Rapid_transaction_settlement_risk = 1
                    elif Rapid_transaction_settlement_risk == 'HIGH RISK':
                        Rapid_transaction_settlement_risk = 0.8
                    elif Rapid_transaction_settlement_risk == 'MEDIUM RISK':
                        Rapid_transaction_settlement_risk = 0.6
                    elif Rapid_transaction_settlement_risk == 'LOW RISK':
                        Rapid_transaction_settlement_risk = 0.4
                    elif Rapid_transaction_settlement_risk == 'VERY LOW RISK':
                        Rapid_transaction_settlement_risk = 0.2
                    elif Rapid_transaction_settlement_risk == 'NOT APPLICABLE':
                        Rapid_transaction_settlement_risk = 0.0


                    Dealing_with_unregistered_VASP_from_overseas_risk  = st.selectbox('Dealing with unregistered VASP from overseas',['NOT APPLICABLE','VERY LOW RISK','LOW RISK','MEDIUM RISK','HIGH RISK','VERY HIGH RISK'])
                    if Dealing_with_unregistered_VASP_from_overseas_risk == 'VERY HIGH RISK':
                        Dealing_with_unregistered_VASP_from_overseas_risk = 1
                    elif Dealing_with_unregistered_VASP_from_overseas_risk == 'HIGH RISK':
                        Dealing_with_unregistered_VASP_from_overseas_risk = 0.8
                    elif Dealing_with_unregistered_VASP_from_overseas_risk == 'MEDIUM RISK':
                        Dealing_with_unregistered_VASP_from_overseas_risk = 0.6
                    elif Dealing_with_unregistered_VASP_from_overseas_risk == 'LOW RISK':
                        Dealing_with_unregistered_VASP_from_overseas_risk = 0.4
                    elif Dealing_with_unregistered_VASP_from_overseas_risk == 'VERY LOW RISK':
                        Dealing_with_unregistered_VASP_from_overseas_risk = 0.2
                    elif Dealing_with_unregistered_VASP_from_overseas_risk == 'NOT APPLICABLE':
                        Dealing_with_unregistered_VASP_from_overseas_risk = 0.0


                #submit_button =  st.form_submit_button("ASSESS VIRTUAL ASSET")       

            #if submit_button:
                Licensed_in_the_country_or_abroad = 0.8
                Nature_size_and_complexity_of_business = 0.8
                Products_or_services =0.8
                Methods_of_delivery_of_products_or_services = 1
                Customer_types = 1
                Country_Risk = 1
                Institutions_dealing_with_VASP = 1
                VA_Anonymity_or_pseudonymity =1
                Rapid_transaction_settlement = 1
                Dealing_with_unregistered_VASP_from_overseas = 1
                total_variable_weight_for_Products_and_services_provided_and_the_types_of_VA = 9.4

                weighted_score_for_Licensed_in_the_country_or_abroad= round((Licensed_in_the_country_or_abroad / total_variable_weight_for_Products_and_services_provided_and_the_types_of_VA * Licensed_in_the_country_or_abroad_risk)*100)
                #print(weighted_score_for_Licensed_in_the_country_or_abroad)
                #st.write('**The weighted score for Licensed in the country or abroad** ' + str(weighted_score_for_Licensed_in_the_country_or_abroad))

                weighted_score_for_Nature_size_and_complexity_of_business = round((Nature_size_and_complexity_of_business / total_variable_weight_for_Products_and_services_provided_and_the_types_of_VA * Nature_size_and_complexity_of_business_risk)*100)
                #print(weighted_score_for_Nature_size_and_complexity_of_business)
                #st.write('**The weighted score for Nature size and complexity of business** ' + str(weighted_score_for_Nature_size_and_complexity_of_business))

                weighted_score_for_Products_or_services = round((Products_or_services / total_variable_weight_for_Products_and_services_provided_and_the_types_of_VA *  Products_or_services_risk)*100)
                #print(weighted_score_for_Products_or_services)
                #st.write('**The weighted score for Products or services** ' + str(weighted_score_for_Products_or_services))

                weighted_score_for_Methods_of_delivery_of_products_or_services = round((Methods_of_delivery_of_products_or_services / total_variable_weight_for_Products_and_services_provided_and_the_types_of_VA * Methods_of_delivery_of_products_or_services_risk)*100)
                #print(weighted_score_for_Methods_of_delivery_of_products_or_services)
                #st.write('**The weighted score for Methods of delivery of products or services** ' + str(weighted_score_for_Methods_of_delivery_of_products_or_services))

                weighted_score_for_Customer_types = round((Customer_types / total_variable_weight_for_Products_and_services_provided_and_the_types_of_VA *  Customer_types_risk)*100)
                #print(weighted_score_for_Customer_types)
                #st.write('**The weighted score for Customer types** ' + str(weighted_score_for_Customer_types))

                weighted_score_for_Country_Risk= round((Country_Risk / total_variable_weight_for_Products_and_services_provided_and_the_types_of_VA * Country_risk)*100)
                #print(weighted_score_for_Country_Risk)
                #st.write('**The weighted score for Country Risk** ' + str(weighted_score_for_Country_Risk))

                weighted_score_for_Institutions_dealing_with_VASP = round((Institutions_dealing_with_VASP / total_variable_weight_for_Products_and_services_provided_and_the_types_of_VA * Institutions_dealing_with_VASP_risk)*100)
                #print(weighted_score_for_Institutions_dealing_with_VASP)
                #st.write('**The weighted score for Institutions dealing with VASP** ' + str(weighted_score_for_Institutions_dealing_with_VASP))

                weighted_score_for_VA_Anonymity_or_pseudonymity = round((VA_Anonymity_or_pseudonymity / total_variable_weight_for_Products_and_services_provided_and_the_types_of_VA *  VA_Anonymity_or_pseudonymity_risk)*100)
                #print(weighted_score_for_VA_Anonymity_or_pseudonymity)
                #st.write('**The weighted score for VA Anonymity or pseudonymity** ' + str(weighted_score_for_VA_Anonymity_or_pseudonymity))

                weighted_score_for_Rapid_transaction_settlement = round((Rapid_transaction_settlement / total_variable_weight_for_Products_and_services_provided_and_the_types_of_VA * Rapid_transaction_settlement_risk)*100)
                #print(weighted_score_for_Rapid_transaction_settlement)
                #st.write('**The weighted score for Rapid transaction settlement** ' + str(weighted_score_for_Rapid_transaction_settlement))

                weighted_score_for_Dealing_with_unregistered_VASP_from_overseas = round((Dealing_with_unregistered_VASP_from_overseas / total_variable_weight_for_Products_and_services_provided_and_the_types_of_VA *  Dealing_with_unregistered_VASP_from_overseas_risk)*100)
                #print(weighted_score_for_Dealing_with_unregistered_VASP_from_overseas)
                #st.write('**The weighted score for Dealing with unregistered VASP from overseas** ' + str(weighted_score_for_Dealing_with_unregistered_VASP_from_overseas))

                Products_and_services_provided_and_the_types_of_VA = weighted_score_for_Licensed_in_the_country_or_abroad + weighted_score_for_Nature_size_and_complexity_of_business + weighted_score_for_Products_or_services + weighted_score_for_Methods_of_delivery_of_products_or_services + weighted_score_for_Customer_types + weighted_score_for_Country_Risk + weighted_score_for_Institutions_dealing_with_VASP + weighted_score_for_VA_Anonymity_or_pseudonymity + weighted_score_for_Rapid_transaction_settlement + weighted_score_for_Dealing_with_unregistered_VASP_from_overseas
                Products_and_services_provided_and_the_types_of_VA =round((Products_and_services_provided_and_the_types_of_VA ))
                st.write('**The Products and services provided and the types of VA is** ' + str(Products_and_services_provided_and_the_types_of_VA))

                if st.button('Products_and_services_provided_and_the_types_of_VA'):
                            query = f'''INSERT INTO Products_and_services_provided_and_the_types_of_VA (Licensed_in_the_country_or_abroad_risk, Licensed_in_the_country_or_abroad, Nature_size_and_complexity_of_business_risk, Nature_size_and_complexity_of_business, Products_or_services_risk, Products_or_services, Methods_of_delivery_of_products_or_services_risk, Methods_of_delivery_of_products_or_services, Customer_types_risk, Customer_types, Country_Risk_risk, Country_Risk,  Institutions_dealing_with_VASP_risk, Institutions_dealing_with_VASP,  VA_Anonymity_or_pseudonymity_risk, VA_Anonymity_or_pseudonymity, Rapid_transaction_settlement_risk, Rapid_transaction_settlement, Dealing_with_unregistered_VASP_from_overseas_risk, Dealing_with_unregistered_VASP_from_overseas, Products_and_services_provided_and_the_types_of_VA, page_selection,VASPS_CATEGORIES) VALUES ('{Licensed_in_the_country_or_abroad_risk}', '{weighted_score_for_Licensed_in_the_country_or_abroad}', '{Nature_size_and_complexity_of_business_risk}', '{weighted_score_for_Nature_size_and_complexity_of_business}', '{Products_or_services_risk}', '{weighted_score_for_Products_or_services}', '{Methods_of_delivery_of_products_or_services_risk}', '{weighted_score_for_Methods_of_delivery_of_products_or_services}', '{Customer_types_risk}', '{weighted_score_for_Customer_types}', '{Country_risk}', '{weighted_score_for_Country_Risk}', '{Institutions_dealing_with_VASP_risk}', '{weighted_score_for_Institutions_dealing_with_VASP}', '{VA_Anonymity_or_pseudonymity_risk}', '{weighted_score_for_VA_Anonymity_or_pseudonymity}', '{Rapid_transaction_settlement_risk}', '{weighted_score_for_Rapid_transaction_settlement}', '{Dealing_with_unregistered_VASP_from_overseas_risk}', '{weighted_score_for_Dealing_with_unregistered_VASP_from_overseas}', '{Products_and_services_provided_and_the_types_of_VA}', '{page_selection}','{VASPS_CATEGORIES}')'''
                            insert_query(query)
                
                print(round(Products_and_services_provided_and_the_types_of_VA))
                import matplotlib.pyplot as fig
                df = pd.DataFrame(data={'risk':['Licensed_in_the_country_or_abroad','Nature size and complexity of business','Products or services','Methods of delivery of products or services','Customer types','Country Risk','Institutions dealing with VASP','VA Anonymity or pseudonymity','Rapid transaction settlement','Dealing with unregistered VASP from overseas'],'Products and services provided and the types of VA':[weighted_score_for_Licensed_in_the_country_or_abroad,weighted_score_for_Nature_size_and_complexity_of_business,weighted_score_for_Products_or_services,weighted_score_for_Methods_of_delivery_of_products_or_services,weighted_score_for_Customer_types,weighted_score_for_Country_Risk,weighted_score_for_Institutions_dealing_with_VASP,weighted_score_for_VA_Anonymity_or_pseudonymity,weighted_score_for_Rapid_transaction_settlement,weighted_score_for_Dealing_with_unregistered_VASP_from_overseas]})
                df.set_index('risk').plot(kind='bar',xlabel='risk',ylabel='risk contribution',subplots=True)
                #st.write(df)
                st.pyplot(fig)

                #fig = go.Figure(data=[
                #    go.Line(name='Products and services provided and the types of VA', x=df['risk'], y=df['Products and services provided and the types of VA'])])
                
                #fig.update_layout(
                #    xaxis_title='risk',
                #    yaxis_title='risk contribution',
                #    legend_title='Products and services provided and the types of VA',)
                #st.plotly_chart(fig) 

            Total_Entity_Dimension = (Products_and_services_provided_and_the_types_of_VA)
            ENTITYDIMENSION = st.button('ENTITY DIMENSION')
            if ENTITYDIMENSION:
                Total_Entity_Dimension = (Products_and_services_provided_and_the_types_of_VA)
                query = f'''INSERT INTO Total_Entity_Dimension (Products_and_services_provided_and_the_types_of_VA, Total_Entity_Dimension, page_selection, VASPS_CATEGORIES) VALUES ('{Products_and_services_provided_and_the_types_of_VA}',  '{Total_Entity_Dimension}', '{page_selection}', '{VASPS_CATEGORIES}')'''
                insert_query(query)
                st.write(Total_Entity_Dimension)

            return Total_Entity_Dimension

        #Entity_Dimension()


    def Mitigating_measures():
        if selected == 'MITIGATING MEASURES':
            st.subheader(":green[MITIGATING MEASURES]")
            with st.expander('Government Measures'):
                #form = st.form("Government measures")
                Comprehensiveness_of_AML_CFT_Legal_Framework_mitigation = st.selectbox('Comprehensiveness of AML or CFT Legal Framework',['NOT APPLICABLE','VERY LOW MITIGATION','LOW MITIGATION','MEDIUM MITIGATION','HIGH MITIGATION','VERY HIGH MITIGATION'])
                if Comprehensiveness_of_AML_CFT_Legal_Framework_mitigation == 'VERY HIGH MITIGATION':
                    Comprehensiveness_of_AML_CFT_Legal_Framework_mitigation = 1
                elif Comprehensiveness_of_AML_CFT_Legal_Framework_mitigation == 'HIGH MITIGATION':
                    Comprehensiveness_of_AML_CFT_Legal_Framework_mitigation = 0.8
                elif Comprehensiveness_of_AML_CFT_Legal_Framework_mitigation == 'MEDIUM MITIGATION':
                    Comprehensiveness_of_AML_CFT_Legal_Framework_mitigation = 0.6
                elif Comprehensiveness_of_AML_CFT_Legal_Framework_mitigation == 'LOW MITIGATION':
                    Comprehensiveness_of_AML_CFT_Legal_Framework_mitigation = 0.4
                elif Comprehensiveness_of_AML_CFT_Legal_Framework_mitigation == 'VERY LOW MITIGATION':
                    Comprehensiveness_of_AML_CFT_Legal_Framework_mitigation = 0.2
                elif Comprehensiveness_of_AML_CFT_Legal_Framework_mitigation == 'NOT APPLICABLE':
                    Comprehensiveness_of_AML_CFT_Legal_Framework_mitigation = 0.0

                Availability_and_Effectiveness_of_Entry_Controls_mitigation  = st.selectbox('Availability and Effectiveness of Entry Controls',['NOT APPLICABLE','VERY LOW MITIGATION','LOW MITIGATION','MEDIUM MITIGATION','HIGH MITIGATION','VERY HIGH MITIGATION'])
                if Availability_and_Effectiveness_of_Entry_Controls_mitigation == 'VERY HIGH MITIGATION':
                    Availability_and_Effectiveness_of_Entry_Controls_mitigation = 1
                elif Availability_and_Effectiveness_of_Entry_Controls_mitigation == 'HIGH MITIGATION':
                    Availability_and_Effectiveness_of_Entry_Controls_mitigation = 0.8
                elif Availability_and_Effectiveness_of_Entry_Controls_mitigation == 'MEDIUM MITIGATION':
                    Availability_and_Effectiveness_of_Entry_Controls_mitigation = 0.6
                elif Availability_and_Effectiveness_of_Entry_Controls_mitigation == 'LOW MITIGATION':
                    Availability_and_Effectiveness_of_Entry_Controls_mitigation = 0.4
                elif Availability_and_Effectiveness_of_Entry_Controls_mitigation == 'VERY LOW MITIGATION':
                    Availability_and_Effectiveness_of_Entry_Controls_mitigation = 0.2
                elif Availability_and_Effectiveness_of_Entry_Controls_mitigation == 'NOT APPLICABLE':
                    Availability_and_Effectiveness_of_Entry_Controls_mitigation = 0.0

                Adequate_Supervision_and_Monitoring_Mechanism_mitigation = st.selectbox('Adequate Supervision and Monitoring Mechanism',['NOT APPLICABLE','VERY LOW MITIGATION','LOW MITIGATION','MEDIUM MITIGATION','HIGH MITIGATION','VERY HIGH MITIGATION'])
                if Adequate_Supervision_and_Monitoring_Mechanism_mitigation == 'VERY HIGH MITIGATION':
                    Adequate_Supervision_and_Monitoring_Mechanism_mitigation = 1
                elif Adequate_Supervision_and_Monitoring_Mechanism_mitigation == 'HIGH MITIGATION':
                    Adequate_Supervision_and_Monitoring_Mechanism_mitigation = 0.8
                elif Adequate_Supervision_and_Monitoring_Mechanism_mitigation == 'MEDIUM MITIGATION':
                    Adequate_Supervision_and_Monitoring_Mechanism_mitigation = 0.6
                elif Adequate_Supervision_and_Monitoring_Mechanism_mitigation == 'LOW MITIGATION':
                    Adequate_Supervision_and_Monitoring_Mechanism_mitigation = 0.4
                elif Adequate_Supervision_and_Monitoring_Mechanism_mitigation == 'VERY LOW MITIGATION':
                    Adequate_Supervision_and_Monitoring_Mechanism_mitigation = 0.2
                elif Adequate_Supervision_and_Monitoring_Mechanism_mitigation == 'NOT APPLICABLE':
                    Adequate_Supervision_and_Monitoring_Mechanism_mitigation = 0.0

                Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure_mitigation  = st.selectbox('Regulation for CDD and source of funds and  Availability of Reliable Identification Infrastructure',['NOT APPLICABLE','VERY LOW MITIGATION','LOW MITIGATION','MEDIUM MITIGATION','HIGH MITIGATION','VERY HIGH MITIGATION'])
                if Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure_mitigation == 'VERY HIGH MITIGATION':
                    Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure_mitigation = 1
                elif Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure_mitigation == 'HIGH MITIGATION':
                    Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure_mitigation = 0.8
                elif Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure_mitigation == 'MEDIUM MITIGATION':
                    Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure_mitigation = 0.6
                elif Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure_mitigation == 'LOW MITIGATION':
                    Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure_mitigation = 0.4
                elif Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure_mitigation == 'VERY LOW MITIGATION':
                    Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure_mitigation = 0.2
                elif Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure_mitigation == 'NOT APPLICABLE':
                    Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure_mitigation = 0.0
                
                Financial_and_human_resource_capacity_of_law_enforcement_authorities_mitigation  = st.selectbox('Financial and human resource capacity of law enforcement authorities',['NOT APPLICABLE','VERY LOW MITIGATION','LOW MITIGATION','MEDIUM MITIGATION','HIGH MITIGATION','VERY HIGH MITIGATION'])
                if Financial_and_human_resource_capacity_of_law_enforcement_authorities_mitigation == 'VERY HIGH MITIGATION':
                    Financial_and_human_resource_capacity_of_law_enforcement_authorities_mitigation = 1
                elif Financial_and_human_resource_capacity_of_law_enforcement_authorities_mitigation == 'HIGH MITIGATION':
                    Financial_and_human_resource_capacity_of_law_enforcement_authorities_mitigation = 0.8
                elif Financial_and_human_resource_capacity_of_law_enforcement_authorities_mitigation == 'MEDIUM MITIGATION':
                    Financial_and_human_resource_capacity_of_law_enforcement_authorities_mitigation = 0.6
                elif Financial_and_human_resource_capacity_of_law_enforcement_authorities_mitigation == 'LOW MITIGATION':
                    Financial_and_human_resource_capacity_of_law_enforcement_authorities_mitigation = 0.4
                elif Financial_and_human_resource_capacity_of_law_enforcement_authorities_mitigation == 'VERY LOW MITIGATION':
                    Financial_and_human_resource_capacity_of_law_enforcement_authorities_mitigation = 0.2
                elif Financial_and_human_resource_capacity_of_law_enforcement_authorities_mitigation == 'NOT APPLICABLE':
                    Financial_and_human_resource_capacity_of_law_enforcement_authorities_mitigation = 0.0
                
                Effectiveness_of_international_cooperation_mitigation = st.selectbox('Effectiveness of international cooperation',['NOT APPLICABLE','VERY LOW MITIGATION','LOW MITIGATION','MEDIUM MITIGATION','HIGH MITIGATION','VERY HIGH MITIGATION'])
                if Effectiveness_of_international_cooperation_mitigation == 'VERY HIGH MITIGATION':
                    Effectiveness_of_international_cooperation_mitigation = 1
                elif Effectiveness_of_international_cooperation_mitigation == 'HIGH MITIGATION':
                    Effectiveness_of_international_cooperation_mitigation = 0.8
                elif Effectiveness_of_international_cooperation_mitigation == 'MEDIUM MITIGATION':
                    Effectiveness_of_international_cooperation_mitigation = 0.6
                elif Effectiveness_of_international_cooperation_mitigation == 'LOW MITIGATION':
                    Effectiveness_of_international_cooperation_mitigation = 0.4
                elif Effectiveness_of_international_cooperation_mitigation == 'VERY LOW MITIGATION':
                    Effectiveness_of_international_cooperation_mitigation = 0.2
                elif Effectiveness_of_international_cooperation_mitigation == 'NOT APPLICABLE':
                    Effectiveness_of_international_cooperation_mitigation = 0.0
                
                Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs_mitigation  = st.selectbox('Quality of guidance issued to VASPs and engagement with VASPs',['NOT APPLICABLE','VERY LOW MITIGATION','LOW MITIGATION','MEDIUM MITIGATION','HIGH MITIGATION','VERY HIGH MITIGATION'])
                if Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs_mitigation == 'VERY HIGH MITIGATION':
                    Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs_mitigation = 1
                elif Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs_mitigation == 'HIGH MITIGATION':
                    Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs_mitigation = 0.8
                elif Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs_mitigation == 'MEDIUM MITIGATION':
                    Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs_mitigation = 0.6
                elif Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs_mitigation == 'LOW MITIGATION':
                    Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs_mitigation = 0.4
                elif Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs_mitigation == 'VERY LOW MITIGATION':
                    Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs_mitigation = 0.2
                elif Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs_mitigation == 'NOT APPLICABLE':
                    Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs_mitigation = 0.0
            
            #if form.form_submit_button("ASSESS VIRTUAL ASSET"):
                Comprehensiveness_of_AML_CFT_Legal_Framework = 1
                Availability_and_Effectiveness_of_Entry_Controls = 1
                Adequate_Supervision_and_Monitoring_Mechanism = 1
                Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure = 1
                Financial_and_human_resource_capacity_of_law_enforcement_authorities = 1
                Effectiveness_of_international_cooperation = 1
                Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs = 1
                
                total_variable_weight_for_Government_measures = 7

                weighted_score_for_Comprehensiveness_of_AML_CFT_Legal_Framework= Comprehensiveness_of_AML_CFT_Legal_Framework / total_variable_weight_for_Government_measures * Comprehensiveness_of_AML_CFT_Legal_Framework_mitigation
                #print(weighted_score_for_Comprehensiveness_of_AML_CFT_Legal_Framework)
                #st.write('**The weighted score for Comprehensiveness of AML CFT Legal Framework** ' + str(weighted_score_for_Comprehensiveness_of_AML_CFT_Legal_Framework))

                weighted_score_for_Availability_and_Effectiveness_of_Entry_Controls = Availability_and_Effectiveness_of_Entry_Controls / total_variable_weight_for_Government_measures * Availability_and_Effectiveness_of_Entry_Controls_mitigation
                #print(weighted_score_for_Availability_and_Effectiveness_of_Entry_Controls)
                #st.write('**The weighted score for Availability and Effectiveness of Entry Controls** ' + str(weighted_score_for_Availability_and_Effectiveness_of_Entry_Controls))

                weighted_score_for_Adequate_Supervision_and_Monitoring_Mechanism = Adequate_Supervision_and_Monitoring_Mechanism / total_variable_weight_for_Government_measures *  Adequate_Supervision_and_Monitoring_Mechanism_mitigation
                #print(weighted_score_for_Adequate_Supervision_and_Monitoring_Mechanism)
                #st.write('**The weighted score for Products or services** ' + str(weighted_score_for_Adequate_Supervision_and_Monitoring_Mechanism))

                weighted_score_for_Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure = Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure / total_variable_weight_for_Government_measures * Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure_mitigation
                #print(weighted_score_for_Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure)
                #st.write('**The weighted score for Regulation for CDD and source of funds and Availability of Reliable Identification Infrastructure** ' + str(weighted_score_for_Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure))

                weighted_score_for_Financial_and_human_resource_capacity_of_law_enforcement_authorities = Financial_and_human_resource_capacity_of_law_enforcement_authorities / total_variable_weight_for_Government_measures *  Financial_and_human_resource_capacity_of_law_enforcement_authorities_mitigation
                #print(weighted_score_for_Financial_and_human_resource_capacity_of_law_enforcement_authorities)
                #st.write('**The weighted score for Financial and human resource capacity of law enforcement authorities** ' + str(weighted_score_for_Financial_and_human_resource_capacity_of_law_enforcement_authorities))

                weighted_score_for_Effectiveness_of_international_cooperation = Effectiveness_of_international_cooperation / total_variable_weight_for_Government_measures * Effectiveness_of_international_cooperation_mitigation
                #print(weighted_score_for_Effectiveness_of_international_cooperation)
                #st.write('**The weighted score for Effectiveness of international cooperation** ' + str(weighted_score_for_Effectiveness_of_international_cooperation))

                weighted_score_for_Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs = Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs / total_variable_weight_for_Government_measures * Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs_mitigation
                #print(weighted_score_for_Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs)
                #st.write('**The weighted score for Quality of guidance issued to VASPs and engagement with VASPs** ' + str(weighted_score_for_Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs))
                
                Government_measures = weighted_score_for_Comprehensiveness_of_AML_CFT_Legal_Framework + weighted_score_for_Availability_and_Effectiveness_of_Entry_Controls + weighted_score_for_Adequate_Supervision_and_Monitoring_Mechanism + weighted_score_for_Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure + weighted_score_for_Financial_and_human_resource_capacity_of_law_enforcement_authorities + weighted_score_for_Effectiveness_of_international_cooperation + weighted_score_for_Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs 
                Government_measures =round((Government_measures * 100))
                st.write('**The Government measures is** ' + str(Government_measures))

                if st.button('Government_measures'):
                            query = f'''INSERT INTO Government_measures (Comprehensiveness_of_AML_CFT_Legal_Framework_mitigation,Comprehensiveness_of_AML_CFT_Legal_Framework, Availability_and_Effectiveness_of_Entry_Controls_mitigation, Availability_and_Effectiveness_of_Entry_Controls, Adequate_Supervision_and_Monitoring_Mechanism_mitigation, Adequate_Supervision_and_Monitoring_Mechanism, Regulation_for_CDD_and_source_of_funds_mitigation, Regulation_for_CDD_and_source_of_funds, Financial_and_human_resource_mitigation, Financial_and_human_resource, Effectiveness_of_international_cooperation_mitigation, Effectiveness_of_international_cooperation, Quality_of_guidance_issued_to_VASPs_mitigation, Quality_of_guidance_issued_to_VASPs, Government_measures, page_selection, VASPS_CATEGORIES) VALUES ('{Comprehensiveness_of_AML_CFT_Legal_Framework_mitigation}' ,'{weighted_score_for_Comprehensiveness_of_AML_CFT_Legal_Framework}', '{Availability_and_Effectiveness_of_Entry_Controls_mitigation}' ,'{weighted_score_for_Availability_and_Effectiveness_of_Entry_Controls}', '{Adequate_Supervision_and_Monitoring_Mechanism_mitigation}' ,'{weighted_score_for_Adequate_Supervision_and_Monitoring_Mechanism}', '{Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure_mitigation}' ,'{weighted_score_for_Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure}', '{Financial_and_human_resource_capacity_of_law_enforcement_authorities_mitigation}' ,'{weighted_score_for_Financial_and_human_resource_capacity_of_law_enforcement_authorities}', '{Effectiveness_of_international_cooperation_mitigation}' ,'{weighted_score_for_Effectiveness_of_international_cooperation}', '{Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs_mitigation}' ,'{weighted_score_for_Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs}', '{Government_measures}' ,'{page_selection}','{VASPS_CATEGORIES}')'''
                            insert_query(query)

                print(round(Government_measures))
                import matplotlib.pyplot as fig
                df = pd.DataFrame(data={'risk':['Comprehensiveness_of_AML_CFT_Legal_Framework','Availability and Effectiveness of Entry Controls','Adequate Supervision and Monitoring Mechanism','Regulation for CDD and source of funds and Availability of Reliable Identification Infrastructure' ,'Financial and human resource capacity of law enforcement authorities' ,'Effectiveness of international_cooperation','Quality of guidance issued to VASPs and engagement with VASPs'],'Government_measures':[weighted_score_for_Comprehensiveness_of_AML_CFT_Legal_Framework,weighted_score_for_Availability_and_Effectiveness_of_Entry_Controls, weighted_score_for_Adequate_Supervision_and_Monitoring_Mechanism,weighted_score_for_Regulation_for_CDD_and_source_of_funds_and_Availability_of_Reliable_Identification_Infrastructure,weighted_score_for_Financial_and_human_resource_capacity_of_law_enforcement_authorities,weighted_score_for_Effectiveness_of_international_cooperation,weighted_score_for_Quality_of_guidance_issued_to_VASPs_and_engagement_with_VASPs]})
                df.set_index('risk').plot(kind='bar',xlabel='risk',ylabel='risk contribution',subplots=True)
                st.write(df)
                st.pyplot(fig)

                fig = go.Figure(data=[
                    go.Line(name='Government_measures', x=df['risk'], y=df['Government_measures'])])
                
                fig.update_layout(
                    xaxis_title='risk',
                    yaxis_title='risk contribution',
                    legend_title='Government_measures',)
                st.plotly_chart(fig)


                    
            with st.expander('VASP Measures'):
                #form = st.form("VASP Measures")
                Transparency_of_shareholder_Structure_of_VASP_mitigation = st.selectbox('Transparency of shareholder Structure of VASP',['NOT APPLICABLE','VERY LOW MITIGATION','LOW MITIGATION','MEDIUM MITIGATION','HIGH MITIGATION','VERY HIGH MITIGATION'])
                if Transparency_of_shareholder_Structure_of_VASP_mitigation == 'VERY HIGH MITIGATION':
                    Transparency_of_shareholder_Structure_of_VASP_mitigation = 1
                elif Transparency_of_shareholder_Structure_of_VASP_mitigation == 'HIGH MITIGATION':
                    Transparency_of_shareholder_Structure_of_VASP_mitigation = 0.8
                elif Transparency_of_shareholder_Structure_of_VASP_mitigation == 'MEDIUM MITIGATION':
                    Transparency_of_shareholder_Structure_of_VASP_mitigation = 0.6
                elif Transparency_of_shareholder_Structure_of_VASP_mitigation == 'LOW MITIGATION':
                    Transparency_of_shareholder_Structure_of_VASP_mitigation = 0.4
                elif Transparency_of_shareholder_Structure_of_VASP_mitigation == 'VERY LOW MITIGATION':
                    Transparency_of_shareholder_Structure_of_VASP_mitigation = 0.2
                elif Transparency_of_shareholder_Structure_of_VASP_mitigation == 'NOT APPLICABLE':
                    Transparency_of_shareholder_Structure_of_VASP_mitigation = 0.0

                Quality_of_Governance_structure_and_Level_of_accountability_of_VASP_mitigation  = st.selectbox('Quality of Governance structure and Level of accountability of VASP',['NOT APPLICABLE','VERY LOW MITIGATION','LOW MITIGATION','MEDIUM MITIGATION','HIGH MITIGATION','VERY HIGH MITIGATION'])
                if Quality_of_Governance_structure_and_Level_of_accountability_of_VASP_mitigation == 'VERY HIGH MITIGATION':
                    Quality_of_Governance_structure_and_Level_of_accountability_of_VASP_mitigation = 1
                elif Quality_of_Governance_structure_and_Level_of_accountability_of_VASP_mitigation == 'HIGH MITIGATION':
                    Quality_of_Governance_structure_and_Level_of_accountability_of_VASP_mitigation = 0.8
                elif Quality_of_Governance_structure_and_Level_of_accountability_of_VASP_mitigation == 'MEDIUM MITIGATION':
                    Quality_of_Governance_structure_and_Level_of_accountability_of_VASP_mitigation = 0.6
                elif Quality_of_Governance_structure_and_Level_of_accountability_of_VASP_mitigation == 'LOW MITIGATION':
                    Quality_of_Governance_structure_and_Level_of_accountability_of_VASP_mitigation = 0.4
                elif Quality_of_Governance_structure_and_Level_of_accountability_of_VASP_mitigation == 'VERY LOW MITIGATION':
                    Quality_of_Governance_structure_and_Level_of_accountability_of_VASP_mitigation = 0.2
                elif Quality_of_Governance_structure_and_Level_of_accountability_of_VASP_mitigation == 'NOT APPLICABLE':
                    Quality_of_Governance_structure_and_Level_of_accountability_of_VASP_mitigation = 0.0

                Effectiveness_of_compliance_function_and_internal_control_mechanism_mitigation = st.selectbox('Effectiveness of compliance function and internal control mechanism',['NOT APPLICABLE','VERY LOW MITIGATION','LOW MITIGATION','MEDIUM MITIGATION','HIGH MITIGATION','VERY HIGH MITIGATION'])
                if Effectiveness_of_compliance_function_and_internal_control_mechanism_mitigation == 'VERY HIGH MITIGATION':
                    Effectiveness_of_compliance_function_and_internal_control_mechanism_mitigation = 1
                elif Effectiveness_of_compliance_function_and_internal_control_mechanism_mitigation == 'HIGH MITIGATION':
                    Effectiveness_of_compliance_function_and_internal_control_mechanism_mitigation = 0.8
                elif Effectiveness_of_compliance_function_and_internal_control_mechanism_mitigation == 'MEDIUM MITIGATION':
                    Effectiveness_of_compliance_function_and_internal_control_mechanism_mitigation = 0.6
                elif Effectiveness_of_compliance_function_and_internal_control_mechanism_mitigation == 'LOW MITIGATION':
                    Effectiveness_of_compliance_function_and_internal_control_mechanism_mitigation = 0.4
                elif Effectiveness_of_compliance_function_and_internal_control_mechanism_mitigation == 'VERY LOW MITIGATION':
                    Effectiveness_of_compliance_function_and_internal_control_mechanism_mitigation = 0.2
                elif Effectiveness_of_compliance_function_and_internal_control_mechanism_mitigation == 'NOT APPLICABLE':
                    Effectiveness_of_compliance_function_and_internal_control_mechanism_mitigation = 0.0

                AML_or_CFT_knowledge_of_VASP_staff_mitigation  = st.selectbox('AML or CFT knowledge of VASP staff',['NOT APPLICABLE','VERY LOW MITIGATION','LOW MITIGATION','MEDIUM MITIGATION','HIGH MITIGATION','VERY HIGH MITIGATION'])
                if AML_or_CFT_knowledge_of_VASP_staff_mitigation == 'VERY HIGH MITIGATION':
                    AML_or_CFT_knowledge_of_VASP_staff_mitigation = 1
                elif AML_or_CFT_knowledge_of_VASP_staff_mitigation == 'HIGH MITIGATION':
                    AML_or_CFT_knowledge_of_VASP_staff_mitigation = 0.8
                elif AML_or_CFT_knowledge_of_VASP_staff_mitigation == 'MEDIUM MITIGATION':
                    AML_or_CFT_knowledge_of_VASP_staff_mitigation = 0.6
                elif AML_or_CFT_knowledge_of_VASP_staff_mitigation == 'LOW MITIGATION':
                    AML_or_CFT_knowledge_of_VASP_staff_mitigation = 0.4
                elif AML_or_CFT_knowledge_of_VASP_staff_mitigation == 'VERY LOW MITIGATION':
                    AML_or_CFT_knowledge_of_VASP_staff_mitigation = 0.2
                elif AML_or_CFT_knowledge_of_VASP_staff_mitigation == 'NOT APPLICABLE':
                    AML_or_CFT_knowledge_of_VASP_staff_mitigation = 0.0
                
            
            #if form.form_submit_button("ASSESS VIRTUAL ASSET"):
                Transparency_of_shareholder_Structure_of_VASP = 1
                Quality_of_Governance_structure_and_Level_of_accountability_of_VASP = 1
                Effectiveness_of_compliance_function_and_internal_control_mechanism = 1
                AML_or_CFT_knowledge_of_VASP_staff = 1

                total_variable_weight_for_VASP_measures = 4

                weighted_score_for_Transparency_of_shareholder_Structure_of_VASP = Transparency_of_shareholder_Structure_of_VASP / total_variable_weight_for_VASP_measures * Transparency_of_shareholder_Structure_of_VASP_mitigation
                #print(weighted_score_for_Transparency_of_shareholder_Structure_of_VASP)
                #st.write('**The weighted score for Transparency of shareholder Structure of VASP** ' + str(weighted_score_for_Transparency_of_shareholder_Structure_of_VASP))

                weighted_score_for_Quality_of_Governance_structure_and_Level_of_accountability_of_VASP = Quality_of_Governance_structure_and_Level_of_accountability_of_VASP / total_variable_weight_for_VASP_measures * Quality_of_Governance_structure_and_Level_of_accountability_of_VASP_mitigation
                #print(weighted_score_for_Quality_of_Governance_structure_and_Level_of_accountability_of_VASP)
                #st.write('**The weighted score for Quality_of_Governance_structure_and_Level_of_accountability_of_VASP** ' + str(weighted_score_for_Quality_of_Governance_structure_and_Level_of_accountability_of_VASP))

                weighted_score_for_Effectiveness_of_compliance_function_and_internal_control_mechanism = Effectiveness_of_compliance_function_and_internal_control_mechanism / total_variable_weight_for_VASP_measures *  Effectiveness_of_compliance_function_and_internal_control_mechanism_mitigation
                #print(weighted_score_for_Effectiveness_of_compliance_function_and_internal_control_mechanism)
                #st.write('**The weighted score for Effectiveness of compliance function and internal control mechanism** ' + str(weighted_score_for_Effectiveness_of_compliance_function_and_internal_control_mechanism))

                weighted_score_for_AML_or_CFT_knowledge_of_VASP_staff = AML_or_CFT_knowledge_of_VASP_staff / total_variable_weight_for_VASP_measures * AML_or_CFT_knowledge_of_VASP_staff_mitigation
                #print(weighted_score_for_AML_or_CFT_knowledge_of_VASP_staff)
                #st.write('**The weighted score for AML or CFT knowledge of VASP staff** ' + str(weighted_score_for_AML_or_CFT_knowledge_of_VASP_staff))

                
                VASP_measures = weighted_score_for_Transparency_of_shareholder_Structure_of_VASP + weighted_score_for_Quality_of_Governance_structure_and_Level_of_accountability_of_VASP + weighted_score_for_Effectiveness_of_compliance_function_and_internal_control_mechanism + weighted_score_for_AML_or_CFT_knowledge_of_VASP_staff 
                VASP_measures =round((VASP_measures * 100))
                st.write('**The VASP measures is** ' + str(VASP_measures))

                if st.button('VASP_measures'):
                            query = f'''INSERT INTO VASP_measures (Transparency_of_shareholder_Structure_of_VASP_mitigation, Transparency_of_shareholder_Structure_of_VASP, Quality_of_Governance_structure_mitigation, Quality_of_Governance_structure, Effectiveness_of_compliance_mitigation, Effectiveness_of_compliance, AML_or_CFT_knowledge_of_VASP_staff_mitigation, AML_or_CFT_knowledge_of_VASP_staff, VASP_measures,  page_selection, VASPS_CATEGORIES) VALUES ('{Transparency_of_shareholder_Structure_of_VASP_mitigation}', '{weighted_score_for_Transparency_of_shareholder_Structure_of_VASP}', '{Quality_of_Governance_structure_and_Level_of_accountability_of_VASP_mitigation}', '{weighted_score_for_Quality_of_Governance_structure_and_Level_of_accountability_of_VASP}', '{Effectiveness_of_compliance_function_and_internal_control_mechanism_mitigation}', '{weighted_score_for_Effectiveness_of_compliance_function_and_internal_control_mechanism}', '{AML_or_CFT_knowledge_of_VASP_staff_mitigation}', '{weighted_score_for_AML_or_CFT_knowledge_of_VASP_staff}', '{VASP_measures}','{page_selection}','{VASPS_CATEGORIES}')'''
                            insert_query(query)

                print(round(VASP_measures))
                import matplotlib.pyplot as fig
                df = pd.DataFrame(data={'risk':['Transparency_of_shareholder_Structure_of_VASP','Quality_of_Governance_structure_and_Level_of_accountability_of_VASP','Effectiveness_of_compliance_function_and_internal_control_mechanism','AML_or_CFT_knowledge_of_VASP_staff'],'VASP measures':[weighted_score_for_Transparency_of_shareholder_Structure_of_VASP,weighted_score_for_Quality_of_Governance_structure_and_Level_of_accountability_of_VASP, weighted_score_for_Effectiveness_of_compliance_function_and_internal_control_mechanism,weighted_score_for_AML_or_CFT_knowledge_of_VASP_staff]})
                df.set_index('risk').plot(kind='bar',xlabel='risk',ylabel='risk contribution',subplots=True)
                st.write(df)
                st.pyplot(fig)

                fig = go.Figure(data=[
                    go.Line(name='VASP measures', x=df['risk'], y=df['VASP measures'])])
                
                fig.update_layout(
                    xaxis_title='risk',
                    yaxis_title='risk contribution',
                    legend_title='VASP_measures',)
                st.plotly_chart(fig)


            with st.expander('Financial Institution (FI) Measures and Designated Non-Financial Businesses and Professions (DNFPs)'):
                #form = st.form("Financial Institution (FI) Measures and DNFPs")
                Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs_mitigation = st.selectbox('Risk assessment and Risk Mitigation measures by FIs and DNFBPs',['NOT APPLICABLE','VERY LOW MITIGATION','LOW MITIGATION','MEDIUM MITIGATION','HIGH MITIGATION','VERY HIGH MITIGATION'])
                if Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs_mitigation == 'VERY HIGH MITIGATION':
                    Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs_mitigation = 1
                elif Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs_mitigation == 'HIGH MITIGATION':
                    Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs_mitigation = 0.8
                elif Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs_mitigation == 'MEDIUM MITIGATION':
                    Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs_mitigation = 0.6
                elif Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs_mitigation == 'LOW MITIGATION':
                    Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs_mitigation = 0.4
                elif Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs_mitigation == 'VERY LOW MITIGATION':
                    Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs_mitigation = 0.2
                elif Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs_mitigation == 'NOT APPLICABLE':
                    Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs_mitigation = 0.0

                Effective_of_compliance_function_and_internal_control_mechanism_mitigation  = st.selectbox('Effective of compliance function and internal control mechanism',['NOT APPLICABLE','VERY LOW MITIGATION','LOW MITIGATION','MEDIUM MITIGATION','HIGH MITIGATION','VERY HIGH MITIGATION'])
                if Effective_of_compliance_function_and_internal_control_mechanism_mitigation == 'VERY HIGH MITIGATION':
                    Effective_of_compliance_function_and_internal_control_mechanism_mitigation = 1
                elif Effective_of_compliance_function_and_internal_control_mechanism_mitigation == 'HIGH MITIGATION':
                    Effective_of_compliance_function_and_internal_control_mechanism_mitigation = 0.8
                elif Effective_of_compliance_function_and_internal_control_mechanism_mitigation == 'MEDIUM MITIGATION':
                    Effective_of_compliance_function_and_internal_control_mechanism_mitigation = 0.6
                elif Effective_of_compliance_function_and_internal_control_mechanism_mitigation == 'LOW MITIGATION':
                    Effective_of_compliance_function_and_internal_control_mechanism_mitigation = 0.4
                elif Effective_of_compliance_function_and_internal_control_mechanism_mitigation == 'VERY LOW MITIGATION':
                    Effective_of_compliance_function_and_internal_control_mechanism_mitigation = 0.2
                elif Effective_of_compliance_function_and_internal_control_mechanism_mitigation == 'NOT APPLICABLE':
                    Effective_of_compliance_function_and_internal_control_mechanism_mitigation = 0.0

            
            
            #if form.form_submit_button("ASSESS VIRTUAL ASSET"):
                Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs = 1
                Effective_of_compliance_function_and_internal_control_mechanism = 1

                total_variable_weight_for_Financial_Institution_Measures_and_DNFPs = 2

                weighted_score_for_Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs = Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs / total_variable_weight_for_Financial_Institution_Measures_and_DNFPs * Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs_mitigation
                #print(weighted_score_for_Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs)
                #st.write('**The weighted score for Risk assessment and Risk Mitigation measures by FIs and DNFBPs** ' + str(weighted_score_for_Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs))

                weighted_score_for_Effective_of_compliance_function_and_internal_control_mechanism = Effective_of_compliance_function_and_internal_control_mechanism / total_variable_weight_for_Financial_Institution_Measures_and_DNFPs * Effective_of_compliance_function_and_internal_control_mechanism_mitigation
                #print(weighted_score_for_Effective_of_compliance_function_and_internal_control_mechanism)
                #st.write('**The weighted score for Effective of compliance function and internal control mechanism** ' + str(weighted_score_for_Effective_of_compliance_function_and_internal_control_mechanism))


                Financial_Institution_Measures_and_DNFPs = weighted_score_for_Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs + weighted_score_for_Effective_of_compliance_function_and_internal_control_mechanism
                Financial_Institution_Measures_and_DNFPs =round((Financial_Institution_Measures_and_DNFPs * 100))
                st.write('**The Financial Institution Measures and DNFPs is** ' + str(Financial_Institution_Measures_and_DNFPs))

                if st.button('Financial_Institution_Measures_and_DNFPs'):
                            query = f'''INSERT INTO Financial_Institution_Measures_and_DNFPs (Risk_assessment_and_Risk_Mitigation_mitigation, Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs, Effective_of_compliance_mitigation, Effective_of_compliance, Financial_Institution_Measures_and_DNFPs, page_selection, VASPS_CATEGORIES) VALUES ('{Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs_mitigation}','{weighted_score_for_Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs}', '{Effective_of_compliance_function_and_internal_control_mechanism_mitigation}', '{weighted_score_for_Effective_of_compliance_function_and_internal_control_mechanism}', '{Financial_Institution_Measures_and_DNFPs}', '{page_selection}'. '{VASPS_CATEGORIES}')'''
                            insert_query(query)

                print(round(Financial_Institution_Measures_and_DNFPs))
                import matplotlib.pyplot as fig
                df = pd.DataFrame(data={'risk':['Risk assessment and Risk Mitigation measures by FIs and DNFBPs','Effective of compliance function and internal control mechanism'],'Financial Institution Measures and DNFPs':[weighted_score_for_Risk_assessment_and_Risk_Mitigation_measures_by_FIs_and_DNFBPs, weighted_score_for_Effective_of_compliance_function_and_internal_control_mechanism]})
                df.set_index('risk').plot(kind='bar',xlabel='risk',ylabel='risk contribution',subplots=True)
                st.write(df)
                st.pyplot(fig)

                fig = go.Figure(data=[
                    go.Line(name='Financial Institution Measures and DNFPs', x=df['risk'], y=df['Financial Institution Measures and DNFPs'])])
                
                fig.update_layout(
                    xaxis_title='risk',
                    yaxis_title='risk contribution',
                    legend_title='Financial Institution Measures and DNFPs',)
                st.plotly_chart(fig)

            Total_Mitigation = (Government_measures + VASP_measures + Financial_Institution_Measures_and_DNFPs)
            MITIGATIONMEASURES = st.button('MITIGATION MEASURES')
            if MITIGATIONMEASURES:
                Total_Mitigation = (Government_measures + VASP_measures + Financial_Institution_Measures_and_DNFPs)/3
                query = f'''INSERT INTO Total_Mitigation (Government_measures,VASP_measures, Financial_Institution_Measures_and_DNFPs,  Total_Mitigation, page_selection) VALUES ('{Government_measures}', '{VASP_measures}', '{Financial_Institution_Measures_and_DNFPs}', '{Total_Mitigation}', '{page_selection}')'''
                insert_query(query)
                st.write(Total_Mitigation)

            #TOTAL_Residual_Risk3 = Total_Mitigation

            


        #Mitigating_measures()
        

    #def totalrisk(Product_Dimension,Entity_Dimension):
    #if selected == 'TOTAL RISK':
    def totalrisk(Total_Product_Dimension,Total_Entity_Dimension):
        if selected == 'TOTAL RISK':
            TOTALRISK = st.button('TOTAL RISK')
            cursor = conn.cursor()
            if TOTALRISK:
                # Execute the SQL query to get the sum of the totals
                    query = """
                    SELECT (SELECT Total_Product_Dimension FROM Total_Product_Dimension ORDER BY id  DESC LIMIT 1) +
                    (SELECT Total_Entity_Dimension FROM Total_Entity_Dimension ORDER BY id  DESC LIMIT 1) AS sum_result
                    """
                    #insert_query(query)
                    cursor.execute(query)
                    sum_result = cursor.fetchone()[0]

                    st.write(f"The sum risk of the {VASPS_CATEGORIES} in {page_selection} totalrisk  is: {sum_result}")
                #a = Product_Dimension()
                #b = Entity_Dimension()
                #Total_RISK = (a* 0.5 + b*0.5)
            #query = f'''INSERT INTO TOTAL_Residual_Risk (Product_Dimension,Entity_Dimension,  Total_RISK, page_selection, VASPS_CATEGORIES) VALUES ('{a}', '{b}', '{Total_RISK}', '{page_selection}')'''
            #insert_query(query)
                #return Total_RISK
                #st.write(TOTALRISK)
                
            
        

    totalrisk(Product_Dimension(),Entity_Dimension())

#elif page == "Reports":
 #   def run_page_1():
   #     func_page_1()
#TOTAL_Residual_Risk = (Tota + Total_Entity_Dimension + Total_Mitigation)/3
                #query = f'''INSERT INTO TOTAL_Residual_Risk (Product_Dimension,Entity_Dimension, Mitigating_measures,  TOTAL_Residual_Risk, page_selection) VALUES ('{Total_Product_Dimension}', '{Total_Entity_Dimension}', '{Total_Mitigation}', '{Total_RISK}', '{page_selection}','{VASPS_CATEGORIES}')'''
                #insert_query(query)
                #st.write(TOTAL_Residual_Risk)
       

    #       '''df = pd.DataFrame(data={'risk':['nature',' criminal','darkweb'],'binance':[77,76,87],'trustwallet':[56,97,95],'coingecko':[87,82,93]})
    #       df.set_index('risk').plot(kind='bar',xlabel='risk',ylabel='Score',subplots=True)
    #       st.pyplot(fig)

    #        fig = go.Figure(data=[
    #            go.Line(name='binance', x=df['risk'], y=df['binance']),
    #          go.Line(name='trustwallet', x=df['risk'], y=df['trustwallet']),
    #            go.Line(name='coingecko', x=df['risk'], y=df['coingecko'])
    #        ])
    #         fig.update_layout(
    #           xaxis_title='risk',
    #            yaxis_title='Score',
    #            legend_title='virtual asset service provider',
    #        )
    #        st.plotly_chart(vig)'''
    #        df = pd.DataFrame(data={'university':['Harvard University','Yale University',
    #       'Princeton University','Columbia University','Brown University',
    #       'Dartmouth University','University of Pennsylvania','Cornell University'],'latitude':[42.3770,41.3163,40.3573,40.8075,41.8268,43.7044,39.9522,42.4534],
    #       'longitude':[-71.1167,-72.9223,-74.6672,-73.9626,-71.4025,-72.2887, -75.1932,-76.4735]})

    #        vig = go.Figure(data=go.Scattergeo(
    #                lon = df['longitude'],
    #                lat = df['latitude'],
    #                text = df['university'],))
    #        vig.update_layout(geo_scope='world',)
    #        st.plotly_chart(vig)
