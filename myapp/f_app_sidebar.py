###########
# sidebar #
###########
option = st.sidebar.selectbox('Select one symbol', ('AFL', 'PRU', 'MDT'))
import datetime
today = datetime.date.today()
before = today - datetime.timedelta(days=700)
start_date = st.sidebar.date_input('Start date', before)
end_date = st.sidebar.date_input('end date', today)
if start_date < end_date:
    st.sidebar.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))
else:
    st.sidebar.error(''Error: End date must fall after start date.')
