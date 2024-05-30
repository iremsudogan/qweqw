import streamlit as st

def main():

    # Giving a title
    st.title('Bank Marketing Prediction Web App')
    
    # Getting input from the user
    age = st.number_input('Age')
    job = st.selectbox('Job', ['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 
                               'retired', 'self-employed', 'services', 'student', 'technician', 
                               'unemployed', 'unknown'])
    marital = st.selectbox('Marital Status', ['divorced', 'married', 'single', 'unknown'])
    education = st.selectbox('Education Level', ['basic.4y', 'basic.6y', 'basic.9y', 'high.school', 
                                                 'illiterate', 'professional.course', 'university.degree', 'unknown'])
    default = st.selectbox('Credit in Default', ['no', 'yes', 'unknown'])
    housing = st.selectbox('Housing Loan', ['no', 'yes', 'unknown'])
    loan = st.selectbox('Personal Loan', ['no', 'yes', 'unknown'])
    contact = st.selectbox('Contact Communication Type', ['cellular', 'telephone'])
    month = st.selectbox('Last Contact Month', ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 
                                                'aug', 'sep', 'oct', 'nov', 'dec'])
    day_of_week = st.selectbox('Last Contact Day of Week', ['mon', 'tue', 'wed', 'thu', 'fri'])
    campaign = st.number_input('Number of Contacts Performed During this Campaign')
    pdays = st.number_input('Number of Days that Passed by After the Client was Last Contacted from a Previous Campaign')
    previous = st.number_input('Number of Contacts Performed Before this Campaign')
    poutcome = st.selectbox('Outcome of the Previous Marketing Campaign', ['failure', 'nonexistent', 'success'])
    emp_var_rate = st.number_input('Employment Variation Rate')
    cons_price_idx = st.number_input('Consumer Price Index')
    cons_conf_idx = st.number_input('Consumer Confidence Index')
    euribor3m = st.number_input('Euribor 3 Month Rate')
    nr_employed = st.number_input('Number of Employees')
    prediction = ''
    
    # Getting the input data from the user
    if st.button('Bank Marketing Prediction'):
        prediction = bank_marketing_prediction([age, job, marital, education, default, housing, loan,
                                                contact, month, day_of_week, campaign, pdays, previous, 
                                                poutcome, emp_var_rate, cons_price_idx, cons_conf_idx, 
                                                euribor3m, nr_employed])
        
    st.success(prediction)
    
if __name__ == '__main__':
    main()
