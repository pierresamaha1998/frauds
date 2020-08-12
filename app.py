#!/usr/bin/env python
# coding: utf-8

# In[2]:


import flask
import pickle
#now we weill load the saved model
with open(f'model/mysaved_md_pickle.pkl', 'rb') as f:
    loaded_model = pickle.load(f)
    
app = flask.Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        Merchant_id = flask.request.form['Merchant_id']
        AverageAmounttransactionday = flask.request.form['Average Amount/transaction/day']
        Transaction_amount=flask.request.form['Transaction_amount']
        Isdeclined = flask.request.form['Is declined']
        TotalNumberofdeclinesday = flask.request.form['Total Number of declines/day']
        isForeignTransaction = flask.request.form['isForeignTransaction']
        isHighRiskCountry = flask.request.form['isHighRiskCountry']
        Daily_chargeback_avg_amt = flask.request.form['Daily_chargeback_avg_amt']
        month_avg_chbk_amt = flask.request.form['6_month_avg_chbk_amt']
        month_chbk_freq = flask.request.form['6-month_chbk_freq']
        avgs = 1
        input_variables = pd.DataFrame([[AverageAmounttransactionday, Transaction_amount, Isdeclined,TotalNumberofdeclinesday, isForeignTransaction,isHighRiskCountry,Daily_chargeback_avg_amt,month_avg_chbk_amt,month_chbk_freq, avgs]],
                                       columns=['AverageAmount_transaction_day','Transaction_amount', 'IsDeclined', 'TotalNumberOfDeclines_day', 'isForeignTransaction', 'isHighRiskCountry', 'Daily_chargeback_avg_amt', '6_month_avg_chbk_amt','6_month_chbk_freq','avgs'],
                                       dtype=float)
        prediction = loaded_model.predict(input_variables)[0]
        return flask.render_template('main.html', result=prediction,
                                     )
if __name__ == '__main__':
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:




