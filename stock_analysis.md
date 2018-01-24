Get and analysis data 
=====================
<font color='87cefa'>1. Steps
-------------

+ <font size='3'>Step 1 get the stock data
+ <font size='3'>Step 2 clean and filter the data
+ <font size='3'>step 3 make chart
+ <font size='3'>step 4 correlation analysis



<font color='6495ed' size='5' >2. Here are the codes</font>

    import tushare as ts
    import pandas as pd
    import matplotlib.pyplot as plt
    from pandas.plotting import scatter_matrix


    def find_all_code():
        print 'input the number of the place:'
        place = input()
        while True:
           try:
             all_place_data = ts.get_area_classified()
             all_place_data = all_place_data[all_place_data.area == all_place_data['area'][place]]
             print all_place_data
             return all_place_data
            
            except:
             continue

            
    def get_stock_data():
        print 'input the number of the stock:'
        stock = raw_input()
        while True:
           try:
             stock_data = ts.get_hist_data(stock, ktype='5')
             stock_data.head(10)
             print stock_data
             return stock_data
            except:
             continue

            

    def show_place_gragh(dataframe):
       plt.title("The Graph of the Data")
       x = range(len(dataframe))
       y1=dataframe['ma5']
       y2=dataframe['ma10']
       y3=dataframe['ma20']
       plt.plot(x,y1, label='ma5', color='red')
       plt.plot(x,y2, label='ma10', color='blue')
       plt.plot(x,y3, label='ma20', color='green')
       plt.show()


    def show_mat(dataframe):
      dataframe.hist()
      plt.show()


    def show_scatter(dataframe):
      scatter_matrix(data.head(10),figsize=(10,10))  
      plt.show()


    #find_all_code()
    #data = get_stock_data()
    #show_place_gragh(data)
    #show_mat(data)
    #show_scatter(data)

<font color='00008b' size='5' >3. Something to change</font>
- 改变获取文件的方式
- 函数功能和借口的进一步完善
- argparse的完善