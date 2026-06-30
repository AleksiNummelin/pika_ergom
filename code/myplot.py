def myplot( output_name, vmin=None, vmax=None):
    
    import numpy as np
    import matplotlib.pyplot as plt
    import datetime as dt
    
    if vmin==None:
        levels=None
    else:
        levels=np.linspace(vmin, vmax, 101)

    # plot 1d or 2d variables
    input_matrix=eval('output_'+output_name)
    
    if len(input_matrix.shape) == 2: # 2-d matrix
        # transpose it
        input_matrix = np.transpose(input_matrix)
        time_axis=eval('time_axis')
        depths=eval('depths')
    
        datetime_axis = [dt.datetime(1899, 12, 30)+dt.timedelta(days=x) for x in time_axis]
        X, Y = np.meshgrid(datetime_axis,depths)
        fig, ax = plt.subplots(figsize=(6,6))
        cf = ax.contourf(X,Y,input_matrix,levels=levels,vmin=vmin,vmax=vmax)
        fig.colorbar(cf, ax=ax, )
        plt.gca().invert_yaxis()
        plt.gcf().autofmt_xdate()
        plt.show()
    
    else: # 1-d vector
        time_axis=eval('time_axis')
        datetime_axis = [dt.datetime(1899, 12, 30)+dt.timedelta(days=x) for x in time_axis]
        # line plot
        plt.plot(datetime_axis,input_matrix)
        plt.gcf().autofmt_xdate()
        
def ratioplot( output_name1, output_name2, vmin=None, vmax=None):
    
    import numpy as np
    import matplotlib.pyplot as plt
    import datetime as dt
    
    if vmin==None:
        levels=None
    else:
        levels=np.linspace(vmin, vmax, 101)

    # plot 1d or 2d variables
    input_matrix=np.divide(eval('output_'+output_name1),eval('output_'+output_name2))
    
    if len(input_matrix.shape) == 2: # 2-d matrix
        # transpose it
        input_matrix = np.transpose(input_matrix)
        time_axis=eval('time_axis')
        depths=eval('depths')
    
        datetime_axis = [dt.datetime(1899, 12, 30)+dt.timedelta(days=x) for x in time_axis]
        X, Y = np.meshgrid(datetime_axis,depths)
        fig, ax = plt.subplots(figsize=(6,6))
        cf = ax.contourf(X,Y,input_matrix,levels=levels,vmin=vmin,vmax=vmax)
        fig.colorbar(cf, ax=ax )
        plt.gca().invert_yaxis()
        plt.gcf().autofmt_xdate()
        plt.show()
    
    else: # 1-d vector
        time_axis=eval('time_axis')
        datetime_axis = [dt.datetime(1899, 12, 30)+dt.timedelta(days=x) for x in time_axis]
        # line plot
        plt.plot(datetime_axis,input_matrix)
        plt.gcf().autofmt_xdate()