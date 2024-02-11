# This function. It goes through every row (event) of the dataframe, and it calculates the expected 
# threat of that action by subtracting the threat of the final zone of the action by the threat of the initial zone 
# of the action (based on the xT heat map provided by The Athletic)

def xT(row):
    initial_threat = 0
    final_threat = 0
# If any of the columns (Initial X, Initial Y, Final X, Final Y) is NaN, we return NaN
    if pd.isnull(row['Initial_X']) or pd.isnull(row['Initial_Y']) or pd.isnull(row['Final_X']) or pd.isnull(row['Final_Y']):
        return pd.NA  # or you can use: return float('nan')
    if 0 <= row['Initial_X']<= (120/16) and 0 <= row['Initial_Y']<= (80/12):
        initial_threat = 0.001
    elif 0 <= row['Initial_X']<= (120/16) and 0 <= row['Initial_Y']<= 2*(80/12):
        initial_threat = 0.002
    elif 0 <= row['Initial_X']<= (120/16) and 0 <= row['Initial_Y']<= 3*(80/12):
        initial_threat = 0.002
    elif 0 <= row['Initial_X']<= (120/16) and 0 <= row['Initial_Y']<= 4*(80/12):
        initial_threat = 0.002
    elif 0 <= row['Initial_X']<= (120/16) and 0 <= row['Initial_Y']<= 5*(80/12):
        initial_threat = 0.003
    elif 0 <= row['Initial_X']<= (120/16) and 0 <= row['Initial_Y']<= 6*(80/12):
        initial_threat = 0.004
    elif 0 <= row['Initial_X']<= (120/16) and 0 <= row['Initial_Y']<= 7*(80/12):
        initial_threat = 0.004
    elif 0 <= row['Initial_X']<= (120/16) and 0 <= row['Initial_Y']<= 8*(80/12):
        initial_threat = 0.004
    elif 0 <= row['Initial_X']<= (120/16) and 0 <= row['Initial_Y']<= 9*(80/12):
        initial_threat = 0.002
    elif 0 <= row['Initial_X']<= (120/16) and 0 <= row['Initial_Y']<= 10*(80/12):
        initial_threat = 0.002
    elif 0 <= row['Initial_X']<= (120/16) and 0 <= row['Initial_Y']<= 11*(80/12):
        initial_threat = 0.002
    elif 0 <= row['Initial_X']<= (120/16) and 0 <= row['Initial_Y']<= 12*(80/12):
        initial_threat = 0.001
    
    if (120/16) <= row['Initial_X']<= 2*(120/16) and 0 <= row['Initial_Y']<= (80/12):
        initial_threat = 0.002
    elif (120/16) <= row['Initial_X']<= 2*(120/16) and 0 <= row['Initial_Y']<= 2*(80/12):
        initial_threat = 0.002
    elif (120/16) <= row['Initial_X']<= 2*(120/16) and 0 <= row['Initial_Y']<= 3*(80/12):
        initial_threat = 0.003
    elif (120/16) <= row['Initial_X']<= 2*(120/16) and 0 <= row['Initial_Y']<= 4*(80/12):
        initial_threat = 0.003
    elif (120/16) <= row['Initial_X']<= 2*(120/16) and 0 <= row['Initial_Y']<= 5*(80/12):
        initial_threat = 0.003
    elif (120/16) <= row['Initial_X']<= 2*(120/16) and 0 <= row['Initial_Y']<= 6*(80/12):
        initial_threat = 0.004
    elif (120/16) <= row['Initial_X']<= 2*(120/16) and 0 <= row['Initial_Y']<= 7*(80/12):
        initial_threat = 0.004
    elif (120/16) <= row['Initial_X']<= 2*(120/16) and 0 <= row['Initial_Y']<= 8*(80/12):
        initial_threat = 0.003
    elif (120/16) <= row['Initial_X']<= 2*(120/16) and 0 <= row['Initial_Y']<= 9*(80/12):
        initial_threat = 0.003
    elif (120/16) <= row['Initial_X']<= 2*(120/16) and 0 <= row['Initial_Y']<= 10*(80/12):
        initial_threat = 0.003
    elif (120/16) <= row['Initial_X']<= 2*(120/16) and 0 <= row['Initial_Y']<= 11*(80/12):
        initial_threat = 0.002
    elif (120/16) <= row['Initial_X']<= 2*(120/16) and 0 <= row['Initial_Y']<= 12*(80/12):
        initial_threat = 0.002
    
    if 2*(120/16) <= row['Initial_X']<= 3*(120/16) and 0 <= row['Initial_Y']<= (80/12):
        initial_threat = 0.002
    elif 2*(120/16) <= row['Initial_X']<= 3*(120/16) and 0 <= row['Initial_Y']<= 2*(80/12):
        initial_threat = 0.003
    elif 2*(120/16) <= row['Initial_X']<= 3*(120/16) and 0 <= row['Initial_Y']<= 3*(80/12):
        initial_threat = 0.003
    elif 2*(120/16) <= row['Initial_X']<= 3*(120/16) and 0 <= row['Initial_Y']<= 4*(80/12):
        initial_threat = 0.003
    elif 2*(120/16) <= row['Initial_X']<= 3*(120/16) and 0 <= row['Initial_Y']<= 5*(80/12):
        initial_threat = 0.004
    elif 2*(120/16) <= row['Initial_X']<= 3*(120/16) and 0 <= row['Initial_Y']<= 6*(80/12):
        initial_threat = 0.004
    elif 2*(120/16) <= row['Initial_X']<= 3*(120/16) and 0 <= row['Initial_Y']<= 7*(80/12):
        initial_threat = 0.004
    elif 2*(120/16) <= row['Initial_X']<= 3*(120/16) and 0 <= row['Initial_Y']<= 8*(80/12):
        initial_threat = 0.004
    elif 2*(120/16) <= row['Initial_X']<= 3*(120/16) and 0 <= row['Initial_Y']<= 9*(80/12):
        initial_threat = 0.004
    elif 2*(120/16) <= row['Initial_X']<= 3*(120/16) and 0 <= row['Initial_Y']<= 10*(80/12):
        initial_threat = 0.003
    elif 2*(120/16) <= row['Initial_X']<= 3*(120/16) and 0 <= row['Initial_Y']<= 11*(80/12):
        initial_threat = 0.003
    elif 2*(120/16) <= row['Initial_X']<= 3*(120/16) and 0 <= row['Initial_Y']<= 12*(80/12):
        initial_threat = 0.002
    
    if 3*(120/16) <= row['Initial_X']<= 4*(120/16) and 0 <= row['Initial_Y']<= (80/12):
        initial_threat = 0.003
    elif 3*(120/16) <= row['Initial_X']<= 4*(120/16) and 0 <= row['Initial_Y']<= 2*(80/12):
        initial_threat = 0.003
    elif 3*(120/16) <= row['Initial_X']<= 4*(120/16) and 0 <= row['Initial_Y']<= 3*(80/12):
        initial_threat = 0.004
    elif 3*(120/16) <= row['Initial_X']<= 4*(120/16) and 0 <= row['Initial_Y']<= 4*(80/12):
        initial_threat = 0.004
    elif 3*(120/16) <= row['Initial_X']<= 4*(120/16) and 0 <= row['Initial_Y']<= 5*(80/12):
        initial_threat = 0.004
    elif 3*(120/16) <= row['Initial_X']<= 4*(120/16) and 0 <= row['Initial_Y']<= 6*(80/12):
        initial_threat = 0.004
    elif 3*(120/16) <= row['Initial_X']<= 4*(120/16) and 0 <= row['Initial_Y']<= 7*(80/12):
        initial_threat = 0.004
    elif 3*(120/16) <= row['Initial_X']<= 4*(120/16) and 0 <= row['Initial_Y']<= 8*(80/12):
        initial_threat = 0.004
    elif 3*(120/16) <= row['Initial_X']<= 4*(120/16) and 0 <= row['Initial_Y']<= 9*(80/12):
        initial_threat = 0.004
    elif 3*(120/16) <= row['Initial_X']<= 4*(120/16) and 0 <= row['Initial_Y']<= 10*(80/12):
        initial_threat = 0.004
    elif 3*(120/16) <= row['Initial_X']<= 4*(120/16) and 0 <= row['Initial_Y']<= 11*(80/12):
        initial_threat = 0.003
    elif 3*(120/16) <= row['Initial_X']<= 4*(120/16) and 0 <= row['Initial_Y']<= 12*(80/12):
        initial_threat = 0.003
    
    if 4*(120/16) <= row['Initial_X']<= 5*(120/16) and 0 <= row['Initial_Y']<= (80/12):
        initial_threat = 0.003
    elif 4*(120/16) <= row['Initial_X']<= 5*(120/16) and 0 <= row['Initial_Y']<= 2*(80/12):
        initial_threat = 0.004
    elif 4*(120/16) <= row['Initial_X']<= 5*(120/16) and 0 <= row['Initial_Y']<= 3*(80/12):
        initial_threat = 0.004
    elif 4*(120/16) <= row['Initial_X']<= 5*(120/16) and 0 <= row['Initial_Y']<= 4*(80/12):
        initial_threat = 0.005
    elif 4*(120/16) <= row['Initial_X']<= 5*(120/16) and 0 <= row['Initial_Y']<= 5*(80/12):
        initial_threat = 0.005
    elif 4*(120/16) <= row['Initial_X']<= 5*(120/16) and 0 <= row['Initial_Y']<= 6*(80/12):
        initial_threat = 0.005
    elif 4*(120/16) <= row['Initial_X']<= 5*(120/16) and 0 <= row['Initial_Y']<= 7*(80/12):
        initial_threat = 0.005
    elif 4*(120/16) <= row['Initial_X']<= 5*(120/16) and 0 <= row['Initial_Y']<= 8*(80/12):
        initial_threat = 0.005
    elif 4*(120/16) <= row['Initial_X']<= 5*(120/16) and 0 <= row['Initial_Y']<= 9*(80/12):
        initial_threat = 0.005
    elif 4*(120/16) <= row['Initial_X']<= 5*(120/16) and 0 <= row['Initial_Y']<= 10*(80/12):
        initial_threat = 0.005
    elif 4*(120/16) <= row['Initial_X']<= 5*(120/16) and 0 <= row['Initial_Y']<= 11*(80/12):
        initial_threat = 0.004
    elif 4*(120/16) <= row['Initial_X']<= 5*(120/16) and 0 <= row['Initial_Y']<= 12*(80/12):
        initial_threat = 0.004
    
    if 5*(120/16) <= row['Initial_X']<= 6*(120/16) and 0 <= row['Initial_Y']<= (80/12):
        initial_threat = 0.004
    elif 5*(120/16) <= row['Initial_X']<= 6*(120/16) and 0 <= row['Initial_Y']<= 2*(80/12):
        initial_threat = 0.005
    elif 5*(120/16) <= row['Initial_X']<= 6*(120/16) and 0 <= row['Initial_Y']<= 3*(80/12):
        initial_threat = 0.005
    elif 5*(120/16) <= row['Initial_X']<= 6*(120/16) and 0 <= row['Initial_Y']<= 4*(80/12):
        initial_threat = 0.006
    elif 5*(120/16) <= row['Initial_X']<= 6*(120/16) and 0 <= row['Initial_Y']<= 5*(80/12):
        initial_threat = 0.006
    elif 5*(120/16) <= row['Initial_X']<= 6*(120/16) and 0 <= row['Initial_Y']<= 6*(80/12):
        initial_threat = 0.006
    elif 5*(120/16) <= row['Initial_X']<= 6*(120/16) and 0 <= row['Initial_Y']<= 7*(80/12):
        initial_threat = 0.006
    elif 5*(120/16) <= row['Initial_X']<= 6*(120/16) and 0 <= row['Initial_Y']<= 8*(80/12):
        initial_threat = 0.006
    elif 5*(120/16) <= row['Initial_X']<= 6*(120/16) and 0 <= row['Initial_Y']<= 9*(80/12):
        initial_threat = 0.006
    elif 5*(120/16) <= row['Initial_X']<= 6*(120/16) and 0 <= row['Initial_Y']<= 10*(80/12):
        initial_threat = 0.006
    elif 5*(120/16) <= row['Initial_X']<= 6*(120/16) and 0 <= row['Initial_Y']<= 11*(80/12):
        initial_threat = 0.005
    elif 5*(120/16) <= row['Initial_X']<= 6*(120/16) and 0 <= row['Initial_Y']<= 12*(80/12):
        initial_threat = 0.004
    
    if 6*(120/16) <= row['Initial_X']<= 7*(120/16) and 0 <= row['Initial_Y']<= (80/12):
        initial_threat = 0.005
    elif 6*(120/16) <= row['Initial_X']<= 7*(120/16) and 0 <= row['Initial_Y']<= 2*(80/12):
        initial_threat = 0.006
    elif 6*(120/16) <= row['Initial_X']<= 7*(120/16) and 0 <= row['Initial_Y']<= 3*(80/12):
        initial_threat = 0.006
    elif 6*(120/16) <= row['Initial_X']<= 7*(120/16) and 0 <= row['Initial_Y']<= 4*(80/12):
        initial_threat = 0.007
    elif 6*(120/16) <= row['Initial_X']<= 7*(120/16) and 0 <= row['Initial_Y']<= 5*(80/12):
        initial_threat = 0.007
    elif 6*(120/16) <= row['Initial_X']<= 7*(120/16) and 0 <= row['Initial_Y']<= 6*(80/12):
        initial_threat = 0.007
    elif 6*(120/16) <= row['Initial_X']<= 7*(120/16) and 0 <= row['Initial_Y']<= 7*(80/12):
        initial_threat = 0.007
    elif 6*(120/16) <= row['Initial_X']<= 7*(120/16) and 0 <= row['Initial_Y']<= 8*(80/12):
        initial_threat = 0.007
    elif 6*(120/16) <= row['Initial_X']<= 7*(120/16) and 0 <= row['Initial_Y']<= 9*(80/12):
        initial_threat = 0.007
    elif 6*(120/16) <= row['Initial_X']<= 7*(120/16) and 0 <= row['Initial_Y']<= 10*(80/12):
        initial_threat = 0.007
    elif 6*(120/16) <= row['Initial_X']<= 7*(120/16) and 0 <= row['Initial_Y']<= 11*(80/12):
        initial_threat = 0.006
    elif 6*(120/16) <= row['Initial_X']<= 7*(120/16) and 0 <= row['Initial_Y']<= 12*(80/12):
        initial_threat = 0.005
    
    if 7*(120/16) <= row['Initial_X']<= 8*(120/16) and 0 <= row['Initial_Y']<= (80/12):
        initial_threat = 0.006
    elif 7*(120/16) <= row['Initial_X']<= 8*(120/16) and 0 <= row['Initial_Y']<= 2*(80/12):
        initial_threat = 0.007
    elif 7*(120/16) <= row['Initial_X']<= 8*(120/16) and 0 <= row['Initial_Y']<= 3*(80/12):
        initial_threat = 0.007
    elif 7*(120/16) <= row['Initial_X']<= 8*(120/16) and 0 <= row['Initial_Y']<= 4*(80/12):
        initial_threat = 0.008
    elif 7*(120/16) <= row['Initial_X']<= 8*(120/16) and 0 <= row['Initial_Y']<= 5*(80/12):
        initial_threat = 0.008
    elif 7*(120/16) <= row['Initial_X']<= 8*(120/16) and 0 <= row['Initial_Y']<= 6*(80/12):
        initial_threat = 0.008
    elif 7*(120/16) <= row['Initial_X']<= 8*(120/16) and 0 <= row['Initial_Y']<= 7*(80/12):
        initial_threat = 0.008
    elif 7*(120/16) <= row['Initial_X']<= 8*(120/16) and 0 <= row['Initial_Y']<= 8*(80/12):
        initial_threat = 0.008
    elif 7*(120/16) <= row['Initial_X']<= 8*(120/16) and 0 <= row['Initial_Y']<= 9*(80/12):
        initial_threat = 0.008
    elif 7*(120/16) <= row['Initial_X']<= 8*(120/16) and 0 <= row['Initial_Y']<= 10*(80/12):
        initial_threat = 0.008
    elif 7*(120/16) <= row['Initial_X']<= 8*(120/16) and 0 <= row['Initial_Y']<= 11*(80/12):
        initial_threat = 0.007
    elif 7*(120/16) <= row['Initial_X']<= 8*(120/16) and 0 <= row['Initial_Y']<= 12*(80/12):
        initial_threat = 0.007
    
    if 8*(120/16) <= row['Initial_X']<= 9*(120/16) and 0 <= row['Initial_Y']<= (80/12):
        initial_threat = 0.007
    elif 8*(120/16) <= row['Initial_X']<= 9*(120/16) and 0 <= row['Initial_Y']<= 2*(80/12):
        initial_threat = 0.008
    elif 8*(120/16) <= row['Initial_X']<= 9*(120/16) and 0 <= row['Initial_Y']<= 3*(80/12):
        initial_threat = 0.009
    elif 8*(120/16) <= row['Initial_X']<= 9*(120/16) and 0 <= row['Initial_Y']<= 4*(80/12):
        initial_threat = 0.009
    elif 8*(120/16) <= row['Initial_X']<= 9*(120/16) and 0 <= row['Initial_Y']<= 5*(80/12):
        initial_threat = 0.01
    elif 8*(120/16) <= row['Initial_X']<= 9*(120/16) and 0 <= row['Initial_Y']<= 6*(80/12):
        initial_threat = 0.01
    elif 8*(120/16) <= row['Initial_X']<= 9*(120/16) and 0 <= row['Initial_Y']<= 7*(80/12):
        initial_threat = 0.009
    elif 8*(120/16) <= row['Initial_X']<= 9*(120/16) and 0 <= row['Initial_Y']<= 8*(80/12):
        initial_threat = 0.01
    elif 8*(120/16) <= row['Initial_X']<= 9*(120/16) and 0 <= row['Initial_Y']<= 9*(80/12):
        initial_threat = 0.009
    elif 8*(120/16) <= row['Initial_X']<= 9*(120/16) and 0 <= row['Initial_Y']<= 10*(80/12):
        initial_threat = 0.009
    elif 8*(120/16) <= row['Initial_X']<= 9*(120/16) and 0 <= row['Initial_Y']<= 11*(80/12):
        initial_threat = 0.009
    elif 8*(120/16) <= row['Initial_X']<= 9*(120/16) and 0 <= row['Initial_Y']<= 12*(80/12):
        initial_threat = 0.008
    
    if 9*(120/16) <= row['Initial_X']<= 10*(120/16) and 0 <= row['Initial_Y']<= (80/12):
        initial_threat = 0.009
    elif 9*(120/16) <= row['Initial_X']<= 10*(120/16) and 0 <= row['Initial_Y']<= 2*(80/12):
        initial_threat = 0.01
    elif 9*(120/16) <= row['Initial_X']<= 10*(120/16) and 0 <= row['Initial_Y']<= 3*(80/12):
        initial_threat = 0.01
    elif 9*(120/16) <= row['Initial_X']<= 10*(120/16) and 0 <= row['Initial_Y']<= 4*(80/12):
        initial_threat = 0.011
    elif 9*(120/16) <= row['Initial_X']<= 10*(120/16) and 0 <= row['Initial_Y']<= 5*(80/12):
        initial_threat = 0.011
    elif 9*(120/16) <= row['Initial_X']<= 10*(120/16) and 0 <= row['Initial_Y']<= 6*(80/12):
        initial_threat = 0.012
    elif 9*(120/16) <= row['Initial_X']<= 10*(120/16) and 0 <= row['Initial_Y']<= 7*(80/12):
        initial_threat = 0.012
    elif 9*(120/16) <= row['Initial_X']<= 10*(120/16) and 0 <= row['Initial_Y']<= 8*(80/12):
        initial_threat = 0.012
    elif 9*(120/16) <= row['Initial_X']<= 10*(120/16) and 0 <= row['Initial_Y']<= 9*(80/12):
        initial_threat = 0.011
    elif 9*(120/16) <= row['Initial_X']<= 10*(120/16) and 0 <= row['Initial_Y']<= 10*(80/12):
        initial_threat = 0.011
    elif 9*(120/16) <= row['Initial_X']<= 10*(120/16) and 0 <= row['Initial_Y']<= 11*(80/12):
        initial_threat = 0.01
    elif 9*(120/16) <= row['Initial_X']<= 10*(120/16) and 0 <= row['Initial_Y']<= 12*(80/12):
        initial_threat = 0.009
    
    if 10*(120/16) <= row['Initial_X']<= 11*(120/16) and 0 <= row['Initial_Y']<= (80/12):
        initial_threat = 0.011
    elif 10*(120/16) <= row['Initial_X']<= 11*(120/16) and 0 <= row['Initial_Y']<= 2*(80/12):
        initial_threat = 0.012
    elif 10*(120/16) <= row['Initial_X']<= 11*(120/16) and 0 <= row['Initial_Y']<= 3*(80/12):
        initial_threat = 0.013
    elif 10*(120/16) <= row['Initial_X']<= 11*(120/16) and 0 <= row['Initial_Y']<= 4*(80/12):
        initial_threat = 0.014
    elif 10*(120/16) <= row['Initial_X']<= 11*(120/16) and 0 <= row['Initial_Y']<= 5*(80/12):
        initial_threat = 0.014
    elif 10*(120/16) <= row['Initial_X']<= 11*(120/16) and 0 <= row['Initial_Y']<= 6*(80/12):
        initial_threat = 0.014
    elif 10*(120/16) <= row['Initial_X']<= 11*(120/16) and 0 <= row['Initial_Y']<= 7*(80/12):
        initial_threat = 0.014
    elif 10*(120/16) <= row['Initial_X']<= 11*(120/16) and 0 <= row['Initial_Y']<= 8*(80/12):
        initial_threat = 0.014
    elif 10*(120/16) <= row['Initial_X']<= 11*(120/16) and 0 <= row['Initial_Y']<= 9*(80/12):
        initial_threat = 0.014
    elif 10*(120/16) <= row['Initial_X']<= 11*(120/16) and 0 <= row['Initial_Y']<= 10*(80/12):
        initial_threat = 0.013
    elif 10*(120/16) <= row['Initial_X']<= 11*(120/16) and 0 <= row['Initial_Y']<= 11*(80/12):
        initial_threat = 0.013
    elif 10*(120/16) <= row['Initial_X']<= 11*(120/16) and 0 <= row['Initial_Y']<= 12*(80/12):
        initial_threat = 0.012
    
    if 11*(120/16) <= row['Initial_X']<= 12*(120/16) and 0 <= row['Initial_Y']<= (80/12):
        initial_threat = 0.013
    elif 11*(120/16) <= row['Initial_X']<= 12*(120/16) and 0 <= row['Initial_Y']<= 2*(80/12):
        initial_threat = 0.015
    elif 11*(120/16) <= row['Initial_X']<= 12*(120/16) and 0 <= row['Initial_Y']<= 3*(80/12):
        initial_threat = 0.016
    elif 11*(120/16) <= row['Initial_X']<= 12*(120/16) and 0 <= row['Initial_Y']<= 4*(80/12):
        initial_threat = 0.018
    elif 11*(120/16) <= row['Initial_X']<= 12*(120/16) and 0 <= row['Initial_Y']<= 5*(80/12):
        initial_threat = 0.019
    elif 11*(120/16) <= row['Initial_X']<= 12*(120/16) and 0 <= row['Initial_Y']<= 6*(80/12):
        initial_threat = 0.019
    elif 11*(120/16) <= row['Initial_X']<= 12*(120/16) and 0 <= row['Initial_Y']<= 7*(80/12):
        initial_threat = 0.02
    elif 11*(120/16) <= row['Initial_X']<= 12*(120/16) and 0 <= row['Initial_Y']<= 8*(80/12):
        initial_threat = 0.02
    elif 11*(120/16) <= row['Initial_X']<= 12*(120/16) and 0 <= row['Initial_Y']<= 9*(80/12):
        initial_threat = 0.018
    elif 11*(120/16) <= row['Initial_X']<= 12*(120/16) and 0 <= row['Initial_Y']<= 10*(80/12):
        initial_threat = 0.017
    elif 11*(120/16) <= row['Initial_X']<= 12*(120/16) and 0 <= row['Initial_Y']<= 11*(80/12):
        initial_threat = 0.016
    elif 11*(120/16) <= row['Initial_X']<= 12*(120/16) and 0 <= row['Initial_Y']<= 12*(80/12):
        initial_threat = 0.014
    
    if 12*(120/16) <= row['Initial_X']<= 13*(120/16) and 0 <= row['Initial_Y']<= (80/12):
        initial_threat = 0.016
    elif 12*(120/16) <= row['Initial_X']<= 13*(120/16) and 0 <= row['Initial_Y']<= 2*(80/12):
        initial_threat = 0.018
    elif 12*(120/16) <= row['Initial_X']<= 13*(120/16) and 0 <= row['Initial_Y']<= 3*(80/12):
        initial_threat = 0.021
    elif 12*(120/16) <= row['Initial_X']<= 13*(120/16) and 0 <= row['Initial_Y']<= 4*(80/12):
        initial_threat = 0.024
    elif 12*(120/16) <= row['Initial_X']<= 13*(120/16) and 0 <= row['Initial_Y']<= 5*(80/12):
        initial_threat = 0.027
    elif 12*(120/16) <= row['Initial_X']<= 13*(120/16) and 0 <= row['Initial_Y']<= 6*(80/12):
        initial_threat = 0.033
    elif 12*(120/16) <= row['Initial_X']<= 13*(120/16) and 0 <= row['Initial_Y']<= 7*(80/12):
        initial_threat = 0.034
    elif 12*(120/16) <= row['Initial_X']<= 13*(120/16) and 0 <= row['Initial_Y']<= 8*(80/12):
        initial_threat = 0.028
    elif 12*(120/16) <= row['Initial_X']<= 13*(120/16) and 0 <= row['Initial_Y']<= 9*(80/12):
        initial_threat = 0.025
    elif 12*(120/16) <= row['Initial_X']<= 13*(120/16) and 0 <= row['Initial_Y']<= 10*(80/12):
        initial_threat = 0.021
    elif 12*(120/16) <= row['Initial_X']<= 13*(120/16) and 0 <= row['Initial_Y']<= 11*(80/12):
        initial_threat = 0.019
    elif 12*(120/16) <= row['Initial_X']<= 13*(120/16) and 0 <= row['Initial_Y']<= 12*(80/12):
        initial_threat = 0.016
    
    if 13*(120/16) <= row['Initial_X']<= 14*(120/16) and 0 <= row['Initial_Y']<= (80/12):
        initial_threat = 0.017
    elif 13*(120/16) <= row['Initial_X']<= 14*(120/16) and 0 <= row['Initial_Y']<= 2*(80/12):
        initial_threat = 0.021
    elif 13*(120/16) <= row['Initial_X']<= 14*(120/16) and 0 <= row['Initial_Y']<= 3*(80/12):
        initial_threat = 0.025
    elif 13*(120/16) <= row['Initial_X']<= 14*(120/16) and 0 <= row['Initial_Y']<= 4*(80/12):
        initial_threat = 0.029
    elif 13*(120/16) <= row['Initial_X']<= 14*(120/16) and 0 <= row['Initial_Y']<= 5*(80/12):
        initial_threat = 0.055
    elif 13*(120/16) <= row['Initial_X']<= 14*(120/16) and 0 <= row['Initial_Y']<= 6*(80/12):
        initial_threat = 0.077
    elif 13*(120/16) <= row['Initial_X']<= 14*(120/16) and 0 <= row['Initial_Y']<= 7*(80/12):
        initial_threat = 0.085
    elif 13*(120/16) <= row['Initial_X']<= 14*(120/16) and 0 <= row['Initial_Y']<= 8*(80/12):
        initial_threat = 0.062
    elif 13*(120/16) <= row['Initial_X']<= 14*(120/16) and 0 <= row['Initial_Y']<= 9*(80/12):
        initial_threat = 0.035
    elif 13*(120/16) <= row['Initial_X']<= 14*(120/16) and 0 <= row['Initial_Y']<= 10*(80/12):
        initial_threat = 0.026
    elif 13*(120/16) <= row['Initial_X']<= 14*(120/16) and 0 <= row['Initial_Y']<= 11*(80/12):
        initial_threat = 0.021
    elif 13*(120/16) <= row['Initial_X']<= 14*(120/16) and 0 <= row['Initial_Y']<= 12*(80/12):
        initial_threat = 0.018
    
    if 14*(120/16) <= row['Initial_X']<= 15*(120/16) and 0 <= row['Initial_Y']<= (80/12):
        initial_threat = 0.017
    elif 14*(120/16) <= row['Initial_X']<= 15*(120/16) and 0 <= row['Initial_Y']<= 2*(80/12):
        initial_threat = 0.02
    elif 14*(120/16) <= row['Initial_X']<= 15*(120/16) and 0 <= row['Initial_Y']<= 3*(80/12):
        initial_threat = 0.027
    elif 14*(120/16) <= row['Initial_X']<= 15*(120/16) and 0 <= row['Initial_Y']<= 4*(80/12):
        initial_threat = 0.039
    elif 14*(120/16) <= row['Initial_X']<= 15*(120/16) and 0 <= row['Initial_Y']<= 5*(80/12):
        initial_threat = 0.091
    elif 14*(120/16) <= row['Initial_X']<= 15*(120/16) and 0 <= row['Initial_Y']<= 6*(80/12):
        initial_threat = 0.142
    elif 14*(120/16) <= row['Initial_X']<= 15*(120/16) and 0 <= row['Initial_Y']<= 7*(80/12):
        initial_threat = 0.134
    elif 14*(120/16) <= row['Initial_X']<= 15*(120/16) and 0 <= row['Initial_Y']<= 8*(80/12):
        initial_threat = 0.095
    elif 14*(120/16) <= row['Initial_X']<= 15*(120/16) and 0 <= row['Initial_Y']<= 9*(80/12):
        initial_threat = 0.042
    elif 14*(120/16) <= row['Initial_X']<= 15*(120/16) and 0 <= row['Initial_Y']<= 10*(80/12):
        initial_threat = 0.026
    elif 14*(120/16) <= row['Initial_X']<= 15*(120/16) and 0 <= row['Initial_Y']<= 11*(80/12):
        initial_threat = 0.02
    elif 14*(120/16) <= row['Initial_X']<= 15*(120/16) and 0 <= row['Initial_Y']<= 12*(80/12):
        initial_threat = 0.017
    
    if 15*(120/16) <= row['Initial_X']<= 16*(120/16) and 0 <= row['Initial_Y']<= (80/12):
        initial_threat = 0.016
    elif 15*(120/16) <= row['Initial_X']<= 16*(120/16) and 0 <= row['Initial_Y']<= 2*(80/12):
        initial_threat = 0.021
    elif 15*(120/16) <= row['Initial_X']<= 16*(120/16) and 0 <= row['Initial_Y']<= 3*(80/12):
        initial_threat = 0.024
    elif 15*(120/16) <= row['Initial_X']<= 16*(120/16) and 0 <= row['Initial_Y']<= 4*(80/12):
        initial_threat = 0.031
    elif 15*(120/16) <= row['Initial_X']<= 16*(120/16) and 0 <= row['Initial_Y']<= 5*(80/12):
        initial_threat = 0.071
    elif 15*(120/16) <= row['Initial_X']<= 16*(120/16) and 0 <= row['Initial_Y']<= 6*(80/12):
        initial_threat = 0.332
    elif 15*(120/16) <= row['Initial_X']<= 16*(120/16) and 0 <= row['Initial_Y']<= 7*(80/12):
        initial_threat = 0.32
    elif 15*(120/16) <= row['Initial_X']<= 16*(120/16) and 0 <= row['Initial_Y']<= 8*(80/12):
        initial_threat = 0.085
    elif 15*(120/16) <= row['Initial_X']<= 16*(120/16) and 0 <= row['Initial_Y']<= 9*(80/12):
        initial_threat = 0.033
    elif 15*(120/16) <= row['Initial_X']<= 16*(120/16) and 0 <= row['Initial_Y']<= 10*(80/12):
        initial_threat = 0.022
    elif 15*(120/16) <= row['Initial_X']<= 16*(120/16) and 0 <= row['Initial_Y']<= 11*(80/12):
        initial_threat = 0.02
    elif 15*(120/16) <= row['Initial_X']<= 16*(120/16) and 0 <= row['Initial_Y']<= 12*(80/12):
        initial_threat = 0.017
    
    
    if 0 <= row['Final_X']<= (120/16) and 0 <= row['Final_Y']<= (80/12):
        final_threat= 0.001
    elif 0 <= row['Final_X']<= (120/16) and 0 <= row['Final_Y']<= 2*(80/12):
        final_threat= 0.002
    elif 0 <= row['Final_X']<= (120/16) and 0 <= row['Final_Y']<= 3*(80/12):
        final_threat= 0.002
    elif 0 <= row['Final_X']<= (120/16) and 0 <= row['Final_Y']<= 4*(80/12):
        final_threat= 0.002
    elif 0 <= row['Final_X']<= (120/16) and 0 <= row['Final_Y']<= 5*(80/12):
        final_threat= 0.003
    elif 0 <= row['Final_X']<= (120/16) and 0 <= row['Final_Y']<= 6*(80/12):
        final_threat= 0.004
    elif 0 <= row['Final_X']<= (120/16) and 0 <= row['Final_Y']<= 7*(80/12):
        final_threat= 0.004
    elif 0 <= row['Final_X']<= (120/16) and 0 <= row['Final_Y']<= 8*(80/12):
        final_threat= 0.004
    elif 0 <= row['Final_X']<= (120/16) and 0 <= row['Final_Y']<= 9*(80/12):
        final_threat= 0.002
    elif 0 <= row['Final_X']<= (120/16) and 0 <= row['Final_Y']<= 10*(80/12):
        final_threat= 0.002
    elif 0 <= row['Final_X']<= (120/16) and 0 <= row['Final_Y']<= 11*(80/12):
        final_threat= 0.002
    elif 0 <= row['Final_X']<= (120/16) and 0 <= row['Final_Y']<= 12*(80/12):
        final_threat= 0.001
    
    if (120/16) <= row['Final_X']<= 2*(120/16) and 0 <= row['Final_Y']<= (80/12):
        final_threat= 0.002
    elif (120/16) <= row['Final_X']<= 2*(120/16) and 0 <= row['Final_Y']<= 2*(80/12):
        final_threat= 0.002
    elif (120/16) <= row['Final_X']<= 2*(120/16) and 0 <= row['Final_Y']<= 3*(80/12):
        final_threat= 0.003
    elif (120/16) <= row['Final_X']<= 2*(120/16) and 0 <= row['Final_Y']<= 4*(80/12):
        final_threat= 0.003
    elif (120/16) <= row['Final_X']<= 2*(120/16) and 0 <= row['Final_Y']<= 5*(80/12):
        final_threat= 0.003
    elif (120/16) <= row['Final_X']<= 2*(120/16) and 0 <= row['Final_Y']<= 6*(80/12):
        final_threat= 0.004
    elif (120/16) <= row['Final_X']<= 2*(120/16) and 0 <= row['Final_Y']<= 7*(80/12):
        final_threat= 0.004
    elif (120/16) <= row['Final_X']<= 2*(120/16) and 0 <= row['Final_Y']<= 8*(80/12):
        final_threat= 0.003
    elif (120/16) <= row['Final_X']<= 2*(120/16) and 0 <= row['Final_Y']<= 9*(80/12):
        final_threat= 0.003
    elif (120/16) <= row['Final_X']<= 2*(120/16) and 0 <= row['Final_Y']<= 10*(80/12):
        final_threat= 0.003
    elif (120/16) <= row['Final_X']<= 2*(120/16) and 0 <= row['Final_Y']<= 11*(80/12):
        final_threat= 0.002
    elif (120/16) <= row['Final_X']<= 2*(120/16) and 0 <= row['Final_Y']<= 12*(80/12):
        final_threat= 0.002
    
    if 2*(120/16) <= row['Final_X']<= 3*(120/16) and 0 <= row['Final_Y']<= (80/12):
        final_threat= 0.002
    elif 2*(120/16) <= row['Final_X']<= 3*(120/16) and 0 <= row['Final_Y']<= 2*(80/12):
        final_threat= 0.003
    elif 2*(120/16) <= row['Final_X']<= 3*(120/16) and 0 <= row['Final_Y']<= 3*(80/12):
        final_threat= 0.003
    elif 2*(120/16) <= row['Final_X']<= 3*(120/16) and 0 <= row['Final_Y']<= 4*(80/12):
        final_threat= 0.003
    elif 2*(120/16) <= row['Final_X']<= 3*(120/16) and 0 <= row['Final_Y']<= 5*(80/12):
        final_threat= 0.004
    elif 2*(120/16) <= row['Final_X']<= 3*(120/16) and 0 <= row['Final_Y']<= 6*(80/12):
        final_threat= 0.004
    elif 2*(120/16) <= row['Final_X']<= 3*(120/16) and 0 <= row['Final_Y']<= 7*(80/12):
        final_threat= 0.004
    elif 2*(120/16) <= row['Final_X']<= 3*(120/16) and 0 <= row['Final_Y']<= 8*(80/12):
        final_threat= 0.004
    elif 2*(120/16) <= row['Final_X']<= 3*(120/16) and 0 <= row['Final_Y']<= 9*(80/12):
        final_threat= 0.004
    elif 2*(120/16) <= row['Final_X']<= 3*(120/16) and 0 <= row['Final_Y']<= 10*(80/12):
        final_threat= 0.003
    elif 2*(120/16) <= row['Final_X']<= 3*(120/16) and 0 <= row['Final_Y']<= 11*(80/12):
        final_threat= 0.003
    elif 2*(120/16) <= row['Final_X']<= 3*(120/16) and 0 <= row['Final_Y']<= 12*(80/12):
        final_threat= 0.002
    
    if 3*(120/16) <= row['Final_X']<= 4*(120/16) and 0 <= row['Final_Y']<= (80/12):
        final_threat= 0.003
    elif 3*(120/16) <= row['Final_X']<= 4*(120/16) and 0 <= row['Final_Y']<= 2*(80/12):
        final_threat= 0.003
    elif 3*(120/16) <= row['Final_X']<= 4*(120/16) and 0 <= row['Final_Y']<= 3*(80/12):
        final_threat= 0.004
    elif 3*(120/16) <= row['Final_X']<= 4*(120/16) and 0 <= row['Final_Y']<= 4*(80/12):
        final_threat= 0.004
    elif 3*(120/16) <= row['Final_X']<= 4*(120/16) and 0 <= row['Final_Y']<= 5*(80/12):
        final_threat= 0.004
    elif 3*(120/16) <= row['Final_X']<= 4*(120/16) and 0 <= row['Final_Y']<= 6*(80/12):
        final_threat= 0.004
    elif 3*(120/16) <= row['Final_X']<= 4*(120/16) and 0 <= row['Final_Y']<= 7*(80/12):
        final_threat= 0.004
    elif 3*(120/16) <= row['Final_X']<= 4*(120/16) and 0 <= row['Final_Y']<= 8*(80/12):
        final_threat= 0.004
    elif 3*(120/16) <= row['Final_X']<= 4*(120/16) and 0 <= row['Final_Y']<= 9*(80/12):
        final_threat= 0.004
    elif 3*(120/16) <= row['Final_X']<= 4*(120/16) and 0 <= row['Final_Y']<= 10*(80/12):
        final_threat= 0.004
    elif 3*(120/16) <= row['Final_X']<= 4*(120/16) and 0 <= row['Final_Y']<= 11*(80/12):
        final_threat= 0.003
    elif 3*(120/16) <= row['Final_X']<= 4*(120/16) and 0 <= row['Final_Y']<= 12*(80/12):
        final_threat= 0.003
    
    if 4*(120/16) <= row['Final_X']<= 5*(120/16) and 0 <= row['Final_Y']<= (80/12):
        final_threat= 0.003
    elif 4*(120/16) <= row['Final_X']<= 5*(120/16) and 0 <= row['Final_Y']<= 2*(80/12):
        final_threat= 0.004
    elif 4*(120/16) <= row['Final_X']<= 5*(120/16) and 0 <= row['Final_Y']<= 3*(80/12):
        final_threat= 0.004
    elif 4*(120/16) <= row['Final_X']<= 5*(120/16) and 0 <= row['Final_Y']<= 4*(80/12):
        final_threat= 0.005
    elif 4*(120/16) <= row['Final_X']<= 5*(120/16) and 0 <= row['Final_Y']<= 5*(80/12):
        final_threat= 0.005
    elif 4*(120/16) <= row['Final_X']<= 5*(120/16) and 0 <= row['Final_Y']<= 6*(80/12):
        final_threat= 0.005
    elif 4*(120/16) <= row['Final_X']<= 5*(120/16) and 0 <= row['Final_Y']<= 7*(80/12):
        final_threat= 0.005
    elif 4*(120/16) <= row['Final_X']<= 5*(120/16) and 0 <= row['Final_Y']<= 8*(80/12):
        final_threat= 0.005
    elif 4*(120/16) <= row['Final_X']<= 5*(120/16) and 0 <= row['Final_Y']<= 9*(80/12):
        final_threat= 0.005
    elif 4*(120/16) <= row['Final_X']<= 5*(120/16) and 0 <= row['Final_Y']<= 10*(80/12):
        final_threat= 0.005
    elif 4*(120/16) <= row['Final_X']<= 5*(120/16) and 0 <= row['Final_Y']<= 11*(80/12):
        final_threat= 0.004
    elif 4*(120/16) <= row['Final_X']<= 5*(120/16) and 0 <= row['Final_Y']<= 12*(80/12):
        final_threat= 0.004
    
    if 5*(120/16) <= row['Final_X']<= 6*(120/16) and 0 <= row['Final_Y']<= (80/12):
        final_threat= 0.004
    elif 5*(120/16) <= row['Final_X']<= 6*(120/16) and 0 <= row['Final_Y']<= 2*(80/12):
        final_threat= 0.005
    elif 5*(120/16) <= row['Final_X']<= 6*(120/16) and 0 <= row['Final_Y']<= 3*(80/12):
        final_threat= 0.005
    elif 5*(120/16) <= row['Final_X']<= 6*(120/16) and 0 <= row['Final_Y']<= 4*(80/12):
        final_threat= 0.006
    elif 5*(120/16) <= row['Final_X']<= 6*(120/16) and 0 <= row['Final_Y']<= 5*(80/12):
        final_threat= 0.006
    elif 5*(120/16) <= row['Final_X']<= 6*(120/16) and 0 <= row['Final_Y']<= 6*(80/12):
        final_threat= 0.006
    elif 5*(120/16) <= row['Final_X']<= 6*(120/16) and 0 <= row['Final_Y']<= 7*(80/12):
        final_threat= 0.006
    elif 5*(120/16) <= row['Final_X']<= 6*(120/16) and 0 <= row['Final_Y']<= 8*(80/12):
        final_threat= 0.006
    elif 5*(120/16) <= row['Final_X']<= 6*(120/16) and 0 <= row['Final_Y']<= 9*(80/12):
        final_threat= 0.006
    elif 5*(120/16) <= row['Final_X']<= 6*(120/16) and 0 <= row['Final_Y']<= 10*(80/12):
        final_threat= 0.006
    elif 5*(120/16) <= row['Final_X']<= 6*(120/16) and 0 <= row['Final_Y']<= 11*(80/12):
        final_threat= 0.005
    elif 5*(120/16) <= row['Final_X']<= 6*(120/16) and 0 <= row['Final_Y']<= 12*(80/12):
        final_threat= 0.004
    
    if 6*(120/16) <= row['Final_X']<= 7*(120/16) and 0 <= row['Final_Y']<= (80/12):
        final_threat= 0.005
    elif 6*(120/16) <= row['Final_X']<= 7*(120/16) and 0 <= row['Final_Y']<= 2*(80/12):
        final_threat= 0.006
    elif 6*(120/16) <= row['Final_X']<= 7*(120/16) and 0 <= row['Final_Y']<= 3*(80/12):
        final_threat= 0.006
    elif 6*(120/16) <= row['Final_X']<= 7*(120/16) and 0 <= row['Final_Y']<= 4*(80/12):
        final_threat= 0.007
    elif 6*(120/16) <= row['Final_X']<= 7*(120/16) and 0 <= row['Final_Y']<= 5*(80/12):
        final_threat= 0.007
    elif 6*(120/16) <= row['Final_X']<= 7*(120/16) and 0 <= row['Final_Y']<= 6*(80/12):
        final_threat= 0.007
    elif 6*(120/16) <= row['Final_X']<= 7*(120/16) and 0 <= row['Final_Y']<= 7*(80/12):
        final_threat= 0.007
    elif 6*(120/16) <= row['Final_X']<= 7*(120/16) and 0 <= row['Final_Y']<= 8*(80/12):
        final_threat= 0.007
    elif 6*(120/16) <= row['Final_X']<= 7*(120/16) and 0 <= row['Final_Y']<= 9*(80/12):
        final_threat= 0.007
    elif 6*(120/16) <= row['Final_X']<= 7*(120/16) and 0 <= row['Final_Y']<= 10*(80/12):
        final_threat= 0.007
    elif 6*(120/16) <= row['Final_X']<= 7*(120/16) and 0 <= row['Final_Y']<= 11*(80/12):
        final_threat= 0.006
    elif 6*(120/16) <= row['Final_X']<= 7*(120/16) and 0 <= row['Final_Y']<= 12*(80/12):
        final_threat= 0.005
    
    if 7*(120/16) <= row['Final_X']<= 8*(120/16) and 0 <= row['Final_Y']<= (80/12):
        final_threat= 0.006
    elif 7*(120/16) <= row['Final_X']<= 8*(120/16) and 0 <= row['Final_Y']<= 2*(80/12):
        final_threat= 0.007
    elif 7*(120/16) <= row['Final_X']<= 8*(120/16) and 0 <= row['Final_Y']<= 3*(80/12):
        final_threat= 0.007
    elif 7*(120/16) <= row['Final_X']<= 8*(120/16) and 0 <= row['Final_Y']<= 4*(80/12):
        final_threat= 0.008
    elif 7*(120/16) <= row['Final_X']<= 8*(120/16) and 0 <= row['Final_Y']<= 5*(80/12):
        final_threat= 0.008
    elif 7*(120/16) <= row['Final_X']<= 8*(120/16) and 0 <= row['Final_Y']<= 6*(80/12):
        final_threat= 0.008
    elif 7*(120/16) <= row['Final_X']<= 8*(120/16) and 0 <= row['Final_Y']<= 7*(80/12):
        final_threat= 0.008
    elif 7*(120/16) <= row['Final_X']<= 8*(120/16) and 0 <= row['Final_Y']<= 8*(80/12):
        final_threat= 0.008
    elif 7*(120/16) <= row['Final_X']<= 8*(120/16) and 0 <= row['Final_Y']<= 9*(80/12):
        final_threat= 0.008
    elif 7*(120/16) <= row['Final_X']<= 8*(120/16) and 0 <= row['Final_Y']<= 10*(80/12):
        final_threat= 0.008
    elif 7*(120/16) <= row['Final_X']<= 8*(120/16) and 0 <= row['Final_Y']<= 11*(80/12):
        final_threat= 0.007
    elif 7*(120/16) <= row['Final_X']<= 8*(120/16) and 0 <= row['Final_Y']<= 12*(80/12):
        final_threat= 0.007
    
    if 8*(120/16) <= row['Final_X']<= 9*(120/16) and 0 <= row['Final_Y']<= (80/12):
        final_threat= 0.007
    elif 8*(120/16) <= row['Final_X']<= 9*(120/16) and 0 <= row['Final_Y']<= 2*(80/12):
        final_threat= 0.008
    elif 8*(120/16) <= row['Final_X']<= 9*(120/16) and 0 <= row['Final_Y']<= 3*(80/12):
        final_threat= 0.009
    elif 8*(120/16) <= row['Final_X']<= 9*(120/16) and 0 <= row['Final_Y']<= 4*(80/12):
        final_threat= 0.009
    elif 8*(120/16) <= row['Final_X']<= 9*(120/16) and 0 <= row['Final_Y']<= 5*(80/12):
        final_threat= 0.01
    elif 8*(120/16) <= row['Final_X']<= 9*(120/16) and 0 <= row['Final_Y']<= 6*(80/12):
        final_threat= 0.01
    elif 8*(120/16) <= row['Final_X']<= 9*(120/16) and 0 <= row['Final_Y']<= 7*(80/12):
        final_threat= 0.009
    elif 8*(120/16) <= row['Final_X']<= 9*(120/16) and 0 <= row['Final_Y']<= 8*(80/12):
        final_threat= 0.01
    elif 8*(120/16) <= row['Final_X']<= 9*(120/16) and 0 <= row['Final_Y']<= 9*(80/12):
        final_threat= 0.009
    elif 8*(120/16) <= row['Final_X']<= 9*(120/16) and 0 <= row['Final_Y']<= 10*(80/12):
        final_threat= 0.009
    elif 8*(120/16) <= row['Final_X']<= 9*(120/16) and 0 <= row['Final_Y']<= 11*(80/12):
        final_threat= 0.009
    elif 8*(120/16) <= row['Final_X']<= 9*(120/16) and 0 <= row['Final_Y']<= 12*(80/12):
        final_threat= 0.008
    
    if 9*(120/16) <= row['Final_X']<= 10*(120/16) and 0 <= row['Final_Y']<= (80/12):
        final_threat= 0.009
    elif 9*(120/16) <= row['Final_X']<= 10*(120/16) and 0 <= row['Final_Y']<= 2*(80/12):
        final_threat= 0.01
    elif 9*(120/16) <= row['Final_X']<= 10*(120/16) and 0 <= row['Final_Y']<= 3*(80/12):
        final_threat= 0.01
    elif 9*(120/16) <= row['Final_X']<= 10*(120/16) and 0 <= row['Final_Y']<= 4*(80/12):
        final_threat= 0.011
    elif 9*(120/16) <= row['Final_X']<= 10*(120/16) and 0 <= row['Final_Y']<= 5*(80/12):
        final_threat= 0.011
    elif 9*(120/16) <= row['Final_X']<= 10*(120/16) and 0 <= row['Final_Y']<= 6*(80/12):
        final_threat= 0.012
    elif 9*(120/16) <= row['Final_X']<= 10*(120/16) and 0 <= row['Final_Y']<= 7*(80/12):
        final_threat= 0.012
    elif 9*(120/16) <= row['Final_X']<= 10*(120/16) and 0 <= row['Final_Y']<= 8*(80/12):
        final_threat= 0.012
    elif 9*(120/16) <= row['Final_X']<= 10*(120/16) and 0 <= row['Final_Y']<= 9*(80/12):
        final_threat= 0.011
    elif 9*(120/16) <= row['Final_X']<= 10*(120/16) and 0 <= row['Final_Y']<= 10*(80/12):
        final_threat= 0.011
    elif 9*(120/16) <= row['Final_X']<= 10*(120/16) and 0 <= row['Final_Y']<= 11*(80/12):
        final_threat= 0.01
    elif 9*(120/16) <= row['Final_X']<= 10*(120/16) and 0 <= row['Final_Y']<= 12*(80/12):
        final_threat= 0.009
    
    if 10*(120/16) <= row['Final_X']<= 11*(120/16) and 0 <= row['Final_Y']<= (80/12):
        final_threat= 0.011
    elif 10*(120/16) <= row['Final_X']<= 11*(120/16) and 0 <= row['Final_Y']<= 2*(80/12):
        final_threat= 0.012
    elif 10*(120/16) <= row['Final_X']<= 11*(120/16) and 0 <= row['Final_Y']<= 3*(80/12):
        final_threat= 0.013
    elif 10*(120/16) <= row['Final_X']<= 11*(120/16) and 0 <= row['Final_Y']<= 4*(80/12):
        final_threat= 0.014
    elif 10*(120/16) <= row['Final_X']<= 11*(120/16) and 0 <= row['Final_Y']<= 5*(80/12):
        final_threat= 0.014
    elif 10*(120/16) <= row['Final_X']<= 11*(120/16) and 0 <= row['Final_Y']<= 6*(80/12):
        final_threat= 0.014
    elif 10*(120/16) <= row['Final_X']<= 11*(120/16) and 0 <= row['Final_Y']<= 7*(80/12):
        final_threat= 0.014
    elif 10*(120/16) <= row['Final_X']<= 11*(120/16) and 0 <= row['Final_Y']<= 8*(80/12):
        final_threat= 0.014
    elif 10*(120/16) <= row['Final_X']<= 11*(120/16) and 0 <= row['Final_Y']<= 9*(80/12):
        final_threat= 0.014
    elif 10*(120/16) <= row['Final_X']<= 11*(120/16) and 0 <= row['Final_Y']<= 10*(80/12):
        final_threat= 0.013
    elif 10*(120/16) <= row['Final_X']<= 11*(120/16) and 0 <= row['Final_Y']<= 11*(80/12):
        final_threat= 0.013
    elif 10*(120/16) <= row['Final_X']<= 11*(120/16) and 0 <= row['Final_Y']<= 12*(80/12):
        final_threat= 0.012
    
    if 11*(120/16) <= row['Final_X']<= 12*(120/16) and 0 <= row['Final_Y']<= (80/12):
        final_threat= 0.013
    elif 11*(120/16) <= row['Final_X']<= 12*(120/16) and 0 <= row['Final_Y']<= 2*(80/12):
        final_threat= 0.015
    elif 11*(120/16) <= row['Final_X']<= 12*(120/16) and 0 <= row['Final_Y']<= 3*(80/12):
        final_threat= 0.016
    elif 11*(120/16) <= row['Final_X']<= 12*(120/16) and 0 <= row['Final_Y']<= 4*(80/12):
        final_threat= 0.018
    elif 11*(120/16) <= row['Final_X']<= 12*(120/16) and 0 <= row['Final_Y']<= 5*(80/12):
        final_threat= 0.019
    elif 11*(120/16) <= row['Final_X']<= 12*(120/16) and 0 <= row['Final_Y']<= 6*(80/12):
        final_threat= 0.019
    elif 11*(120/16) <= row['Final_X']<= 12*(120/16) and 0 <= row['Final_Y']<= 7*(80/12):
        final_threat= 0.02
    elif 11*(120/16) <= row['Final_X']<= 12*(120/16) and 0 <= row['Final_Y']<= 8*(80/12):
        final_threat= 0.02
    elif 11*(120/16) <= row['Final_X']<= 12*(120/16) and 0 <= row['Final_Y']<= 9*(80/12):
        final_threat= 0.018
    elif 11*(120/16) <= row['Final_X']<= 12*(120/16) and 0 <= row['Final_Y']<= 10*(80/12):
        final_threat= 0.017
    elif 11*(120/16) <= row['Final_X']<= 12*(120/16) and 0 <= row['Final_Y']<= 11*(80/12):
        final_threat= 0.016
    elif 11*(120/16) <= row['Final_X']<= 12*(120/16) and 0 <= row['Final_Y']<= 12*(80/12):
        final_threat= 0.014
    
    if 12*(120/16) <= row['Final_X']<= 13*(120/16) and 0 <= row['Final_Y']<= (80/12):
        final_threat= 0.016
    elif 12*(120/16) <= row['Final_X']<= 13*(120/16) and 0 <= row['Final_Y']<= 2*(80/12):
        final_threat= 0.018
    elif 12*(120/16) <= row['Final_X']<= 13*(120/16) and 0 <= row['Final_Y']<= 3*(80/12):
        final_threat= 0.021
    elif 12*(120/16) <= row['Final_X']<= 13*(120/16) and 0 <= row['Final_Y']<= 4*(80/12):
        final_threat= 0.024
    elif 12*(120/16) <= row['Final_X']<= 13*(120/16) and 0 <= row['Final_Y']<= 5*(80/12):
        final_threat= 0.027
    elif 12*(120/16) <= row['Final_X']<= 13*(120/16) and 0 <= row['Final_Y']<= 6*(80/12):
        final_threat= 0.033
    elif 12*(120/16) <= row['Final_X']<= 13*(120/16) and 0 <= row['Final_Y']<= 7*(80/12):
        final_threat= 0.034
    elif 12*(120/16) <= row['Final_X']<= 13*(120/16) and 0 <= row['Final_Y']<= 8*(80/12):
        final_threat= 0.028
    elif 12*(120/16) <= row['Final_X']<= 13*(120/16) and 0 <= row['Final_Y']<= 9*(80/12):
        final_threat= 0.025
    elif 12*(120/16) <= row['Final_X']<= 13*(120/16) and 0 <= row['Final_Y']<= 10*(80/12):
        final_threat= 0.021
    elif 12*(120/16) <= row['Final_X']<= 13*(120/16) and 0 <= row['Final_Y']<= 11*(80/12):
        final_threat= 0.019
    elif 12*(120/16) <= row['Final_X']<= 13*(120/16) and 0 <= row['Final_Y']<= 12*(80/12):
        final_threat= 0.016
    
    if 13*(120/16) <= row['Final_X']<= 14*(120/16) and 0 <= row['Final_Y']<= (80/12):
        final_threat= 0.017
    elif 13*(120/16) <= row['Final_X']<= 14*(120/16) and 0 <= row['Final_Y']<= 2*(80/12):
        final_threat= 0.021
    elif 13*(120/16) <= row['Final_X']<= 14*(120/16) and 0 <= row['Final_Y']<= 3*(80/12):
        final_threat= 0.025
    elif 13*(120/16) <= row['Final_X']<= 14*(120/16) and 0 <= row['Final_Y']<= 4*(80/12):
        final_threat= 0.029
    elif 13*(120/16) <= row['Final_X']<= 14*(120/16) and 0 <= row['Final_Y']<= 5*(80/12):
        final_threat= 0.055
    elif 13*(120/16) <= row['Final_X']<= 14*(120/16) and 0 <= row['Final_Y']<= 6*(80/12):
        final_threat= 0.077
    elif 13*(120/16) <= row['Final_X']<= 14*(120/16) and 0 <= row['Final_Y']<= 7*(80/12):
        final_threat= 0.085
    elif 13*(120/16) <= row['Final_X']<= 14*(120/16) and 0 <= row['Final_Y']<= 8*(80/12):
        final_threat= 0.062
    elif 13*(120/16) <= row['Final_X']<= 14*(120/16) and 0 <= row['Final_Y']<= 9*(80/12):
        final_threat= 0.035
    elif 13*(120/16) <= row['Final_X']<= 14*(120/16) and 0 <= row['Final_Y']<= 10*(80/12):
        final_threat= 0.026
    elif 13*(120/16) <= row['Final_X']<= 14*(120/16) and 0 <= row['Final_Y']<= 11*(80/12):
        final_threat= 0.021
    elif 13*(120/16) <= row['Final_X']<= 14*(120/16) and 0 <= row['Final_Y']<= 12*(80/12):
        final_threat= 0.018
    
    if 14*(120/16) <= row['Final_X']<= 15*(120/16) and 0 <= row['Final_Y']<= (80/12):
        final_threat= 0.017
    elif 14*(120/16) <= row['Final_X']<= 15*(120/16) and 0 <= row['Final_Y']<= 2*(80/12):
        final_threat= 0.02
    elif 14*(120/16) <= row['Final_X']<= 15*(120/16) and 0 <= row['Final_Y']<= 3*(80/12):
        final_threat= 0.027
    elif 14*(120/16) <= row['Final_X']<= 15*(120/16) and 0 <= row['Final_Y']<= 4*(80/12):
        final_threat= 0.039
    elif 14*(120/16) <= row['Final_X']<= 15*(120/16) and 0 <= row['Final_Y']<= 5*(80/12):
        final_threat= 0.091
    elif 14*(120/16) <= row['Final_X']<= 15*(120/16) and 0 <= row['Final_Y']<= 6*(80/12):
        final_threat= 0.142
    elif 14*(120/16) <= row['Final_X']<= 15*(120/16) and 0 <= row['Final_Y']<= 7*(80/12):
        final_threat= 0.134
    elif 14*(120/16) <= row['Final_X']<= 15*(120/16) and 0 <= row['Final_Y']<= 8*(80/12):
        final_threat= 0.095
    elif 14*(120/16) <= row['Final_X']<= 15*(120/16) and 0 <= row['Final_Y']<= 9*(80/12):
        final_threat= 0.042
    elif 14*(120/16) <= row['Final_X']<= 15*(120/16) and 0 <= row['Final_Y']<= 10*(80/12):
        final_threat= 0.026
    elif 14*(120/16) <= row['Final_X']<= 15*(120/16) and 0 <= row['Final_Y']<= 11*(80/12):
        final_threat= 0.02
    elif 14*(120/16) <= row['Final_X']<= 15*(120/16) and 0 <= row['Final_Y']<= 12*(80/12):
        final_threat= 0.017
    
    if 15*(120/16) <= row['Final_X']<= 16*(120/16) and 0 <= row['Final_Y']<= (80/12):
        final_threat= 0.016
    elif 15*(120/16) <= row['Final_X']<= 16*(120/16) and 0 <= row['Final_Y']<= 2*(80/12):
        final_threat= 0.021
    elif 15*(120/16) <= row['Final_X']<= 16*(120/16) and 0 <= row['Final_Y']<= 3*(80/12):
        final_threat= 0.024
    elif 15*(120/16) <= row['Final_X']<= 16*(120/16) and 0 <= row['Final_Y']<= 4*(80/12):
        final_threat= 0.031
    elif 15*(120/16) <= row['Final_X']<= 16*(120/16) and 0 <= row['Final_Y']<= 5*(80/12):
        final_threat= 0.071
    elif 15*(120/16) <= row['Final_X']<= 16*(120/16) and 0 <= row['Final_Y']<= 6*(80/12):
        final_threat= 0.332
    elif 15*(120/16) <= row['Final_X']<= 16*(120/16) and 0 <= row['Final_Y']<= 7*(80/12):
        final_threat= 0.32
    elif 15*(120/16) <= row['Final_X']<= 16*(120/16) and 0 <= row['Final_Y']<= 8*(80/12):
        final_threat= 0.085
    elif 15*(120/16) <= row['Final_X']<= 16*(120/16) and 0 <= row['Final_Y']<= 9*(80/12):
        final_threat= 0.033
    elif 15*(120/16) <= row['Final_X']<= 16*(120/16) and 0 <= row['Final_Y']<= 10*(80/12):
        final_threat= 0.022
    elif 15*(120/16) <= row['Final_X']<= 16*(120/16) and 0 <= row['Final_Y']<= 11*(80/12):
        final_threat= 0.02
    elif 15*(120/16) <= row['Final_X']<= 16*(120/16) and 0 <= row['Final_Y']<= 12*(80/12):
        final_threat= 0.017

    xT = final_threat - initial_threat
    return xT

import pandas as pd
from statsbombpy import sb
import numpy as np

def process_match_events(match_id):
    events = sb.events(match_id=match_id)
    events = events[["id", "type", "player", "player_id", "team", "location", "pass_end_location", "carry_end_location", "position", "substitution_replacement", "tactics"]]
    # Splits 'location' into two separate columns for initial coordinates
    events['Initial_X'] = events['location'].apply(lambda loc: loc[0] if isinstance(loc, list) and len(loc) == 2 else None)
    events['Initial_Y'] = events['location'].apply(lambda loc: loc[1] if isinstance(loc, list) and len(loc) == 2 else None)
    
        # Splits 'pass_end_location' and 'carry_end_location' into 'Final X' and 'Final Y'
    def final_x(row):
        if isinstance(row['pass_end_location'], list) and len(row['pass_end_location']) == 2:
            return row['pass_end_location'][0]
        elif isinstance(row['carry_end_location'], list) and len(row['carry_end_location']) == 2:
            return row['carry_end_location'][0]
        return None
    
    def final_y(row):
        if isinstance(row['pass_end_location'], list) and len(row['pass_end_location']) == 2:
            return row['pass_end_location'][1]
        elif isinstance(row['carry_end_location'], list) and len(row['carry_end_location']) == 2:
            return row['carry_end_location'][1]
        return None
    
    events['Final_X'] = events.apply(final_x, axis=1)
    events['Final_Y'] = events.apply(final_y, axis=1)
    
    
    # Identifies substitute players
    substitute_players = events[pd.notna(events['substitution_replacement'])]['substitution_replacement'].tolist()
    
    # Exclude these players from average position calculation
    non_substitute_events = events[~events['player'].isin(substitute_players)]
    
    
    # Calculate average positions
    avg_coordinates = non_substitute_events.groupby(['player', 'team'])[['Initial_X', 'Initial_Y']].mean().reset_index()
    
    # Calculate total positive xT conceded by each team
    events['xT'] = events.apply(xT, axis=1)  # Assuming the xT function is already defined
    events['Positive xT'] = np.where(events['xT'].isna(), 0, np.where(events['xT'] > 0, events['xT'], 0))


        # General Position calculation
    def map_to_general_position(position):
        if pd.isnull(position):
            return "Other"
        if "Goalkeeper" in position:
            return "Goalkeeper"
        elif "Back" in position or "back" in position:
            return "Defender"
        elif "Midfield" in position or "midfield" in position:
            return "Midfielder"
        elif any(x in position for x in ["Forward", "forward", "Striker", "Wing"]):
            return "Attacker"
        else:
            return "Other"

    non_substitute_events['General Position'] = non_substitute_events['position'].apply(map_to_general_position)
    
    # Calculates the total xT conceded by each team
    team_xt_conceded = {}
    for team in events['team'].unique():
        opponent_xt = events[(events['team'] != team)]['xT'].sum()
        team_xt_conceded[team] = opponent_xt

    avg_coordinates_with_positions = non_substitute_events.groupby(['player', 'team', 'position'])[['Initial_X', 'Initial_Y']].mean().reset_index()

    # Constructing the results dictionary
    match_data = {
        'match_id': match_id,
        'data': []
    }
    
    for _, row in avg_coordinates_with_positions.iterrows():
        player_data = {
            'team': row['team'],
            'player': row['player'],
            'position': row['position'],
            'avg_x': row['Initial_X'],
            'avg_y': row['Initial_Y']
        }
        match_data['data'].append(player_data)
        
    for team, xt in team_xt_conceded.items():
        team_data = {
            'team': team,
            'xt_conceded': xt
        }

        match_data['data'].append(team_data)
        
        return match_data

        # Retrieve all the matches for the desired competition and season (2015/2016 Premier League Season)
        competition_id = 2
        season_id = 27
        matches = sb.matches(competition_id=competition_id, season_id=season_id)

        results = []
        for match_id in matches['match_id']:
                result = process_match_events(match_id)
                results.append(result)

import pickle

# Dump dictionary into a .pkl to preserve data
with open("results.pkl", "wb") as f:
    pickle.dump(results, f)

import pickle
with open("results.pkl", "rb") as f:
    results = pickle.load(f)
results


import pandas as pd
data = results 
df_list = []

for match in data:
    match_id = match['match_id']
    for player_data in match['data']:
        if 'player' in player_data:
            df_list.append({
                'match_id': match_id,
                'team': player_data['team'],
                'player': player_data['player'],
                'avg_x': player_data['avg_x'],
                'avg_y': player_data['avg_y'],
                'position': player_data['position'],
                'opposition': [m['team'] for m in match['data'] if 'xt_conceded' in m and m['team'] != player_data['team']][0],
                'xt_conceded': [m['xt_conceded'] for m in match['data'] if 'xt_conceded' in m and m['team'] == player_data['team']][0]
            })

df = pd.DataFrame(df_list)
df


def zone_identification(row):
    zone = 0
    if 0 <= row['avg_x']<= (120/16) and 0 <= row['avg_y']<= (80/12):
        zone =  1
    elif 0 <= row['avg_x']<= (120/16) and 0 <= row['avg_y']<= 2*(80/12):
        zone =  2
    elif 0 <= row['avg_x']<= (120/16) and 0 <= row['avg_y']<= 3*(80/12):
        zone =  3
    elif 0 <= row['avg_x']<= (120/16) and 0 <= row['avg_y']<= 4*(80/12):
        zone = 4 
    elif 0 <= row['avg_x']<= (120/16) and 0 <= row['avg_y']<= 5*(80/12):
        zone = 5
    elif 0 <= row['avg_x']<= (120/16) and 0 <= row['avg_y']<= 6*(80/12):
        zone = 6 
    elif 0 <= row['avg_x']<= (120/16) and 0 <= row['avg_y']<= 7*(80/12):
        zone = 7
    elif 0 <= row['avg_x']<= (120/16) and 0 <= row['avg_y']<= 8*(80/12):
        zone = 8
    elif 0 <= row['avg_x']<= (120/16) and 0 <= row['avg_y']<= 9*(80/12):
        zone = 9
    elif 0 <= row['avg_x']<= (120/16) and 0 <= row['avg_y']<= 10*(80/12):
        zone = 10
    elif 0 <= row['avg_x']<= (120/16) and 0 <= row['avg_y']<= 11*(80/12):
        zone = 11
    elif 0 <= row['avg_x']<= (120/16) and 0 <= row['avg_y']<= 12*(80/12):
        zone = 12
    
    if (120/16) <= row['avg_x']<= 2*(120/16) and 0 <= row['avg_y']<= (80/12):
        zone = 13
    elif (120/16) <= row['avg_x']<= 2*(120/16) and 0 <= row['avg_y']<= 2*(80/12):
        zone = 14
    elif (120/16) <= row['avg_x']<= 2*(120/16) and 0 <= row['avg_y']<= 3*(80/12):
        zone = 15
    elif (120/16) <= row['avg_x']<= 2*(120/16) and 0 <= row['avg_y']<= 4*(80/12):
        zone = 16
    elif (120/16) <= row['avg_x']<= 2*(120/16) and 0 <= row['avg_y']<= 5*(80/12):
        zone = 17
    elif (120/16) <= row['avg_x']<= 2*(120/16) and 0 <= row['avg_y']<= 6*(80/12):
        zone = 18
    elif (120/16) <= row['avg_x']<= 2*(120/16) and 0 <= row['avg_y']<= 7*(80/12):
        zone = 19
    elif (120/16) <= row['avg_x']<= 2*(120/16) and 0 <= row['avg_y']<= 8*(80/12):
        zone = 20
    elif (120/16) <= row['avg_x']<= 2*(120/16) and 0 <= row['avg_y']<= 9*(80/12):
        zone = 21
    elif (120/16) <= row['avg_x']<= 2*(120/16) and 0 <= row['avg_y']<= 10*(80/12):
        zone = 22
    elif (120/16) <= row['avg_x']<= 2*(120/16) and 0 <= row['avg_y']<= 11*(80/12):
        zone = 23
    elif (120/16) <= row['avg_x']<= 2*(120/16) and 0 <= row['avg_y']<= 12*(80/12):
        zone = 24
    
    if 2*(120/16) <= row['avg_x']<= 3*(120/16) and 0 <= row['avg_y']<= (80/12):
        zone = 25
    elif 2*(120/16) <= row['avg_x']<= 3*(120/16) and 0 <= row['avg_y']<= 2*(80/12):
        zone = 26
    elif 2*(120/16) <= row['avg_x']<= 3*(120/16) and 0 <= row['avg_y']<= 3*(80/12):
        zone = 27
    elif 2*(120/16) <= row['avg_x']<= 3*(120/16) and 0 <= row['avg_y']<= 4*(80/12):
        zone = 28
    elif 2*(120/16) <= row['avg_x']<= 3*(120/16) and 0 <= row['avg_y']<= 5*(80/12):
        zone = 29
    elif 2*(120/16) <= row['avg_x']<= 3*(120/16) and 0 <= row['avg_y']<= 6*(80/12):
        zone = 30
    elif 2*(120/16) <= row['avg_x']<= 3*(120/16) and 0 <= row['avg_y']<= 7*(80/12):
        zone = 31
    elif 2*(120/16) <= row['avg_x']<= 3*(120/16) and 0 <= row['avg_y']<= 8*(80/12):
        zone = 32
    elif 2*(120/16) <= row['avg_x']<= 3*(120/16) and 0 <= row['avg_y']<= 9*(80/12):
        zone = 33
    elif 2*(120/16) <= row['avg_x']<= 3*(120/16) and 0 <= row['avg_y']<= 10*(80/12):
        zone = 34
    elif 2*(120/16) <= row['avg_x']<= 3*(120/16) and 0 <= row['avg_y']<= 11*(80/12):
        zone = 35
    elif 2*(120/16) <= row['avg_x']<= 3*(120/16) and 0 <= row['avg_y']<= 12*(80/12):
        zone = 36
    
    if 3*(120/16) <= row['avg_x']<= 4*(120/16) and 0 <= row['avg_y']<= (80/12):
        zone = 37
    elif 3*(120/16) <= row['avg_x']<= 4*(120/16) and 0 <= row['avg_y']<= 2*(80/12):
        zone = 38
    elif 3*(120/16) <= row['avg_x']<= 4*(120/16) and 0 <= row['avg_y']<= 3*(80/12):
        zone = 39
    elif 3*(120/16) <= row['avg_x']<= 4*(120/16) and 0 <= row['avg_y']<= 4*(80/12):
        zone = 40
    elif 3*(120/16) <= row['avg_x']<= 4*(120/16) and 0 <= row['avg_y']<= 5*(80/12):
        zone = 41
    elif 3*(120/16) <= row['avg_x']<= 4*(120/16) and 0 <= row['avg_y']<= 6*(80/12):
        zone = 42
    elif 3*(120/16) <= row['avg_x']<= 4*(120/16) and 0 <= row['avg_y']<= 7*(80/12):
        zone = 43
    elif 3*(120/16) <= row['avg_x']<= 4*(120/16) and 0 <= row['avg_y']<= 8*(80/12):
        zone = 44
    elif 3*(120/16) <= row['avg_x']<= 4*(120/16) and 0 <= row['avg_y']<= 9*(80/12):
        zone = 45
    elif 3*(120/16) <= row['avg_x']<= 4*(120/16) and 0 <= row['avg_y']<= 10*(80/12):
        zone = 46
    elif 3*(120/16) <= row['avg_x']<= 4*(120/16) and 0 <= row['avg_y']<= 11*(80/12):
        zone = 47
    elif 3*(120/16) <= row['avg_x']<= 4*(120/16) and 0 <= row['avg_y']<= 12*(80/12):
        zone = 48
    
    if 4*(120/16) <= row['avg_x']<= 5*(120/16) and 0 <= row['avg_y']<= (80/12):
        zone = 49
    elif 4*(120/16) <= row['avg_x']<= 5*(120/16) and 0 <= row['avg_y']<= 2*(80/12):
        zone = 50
    elif 4*(120/16) <= row['avg_x']<= 5*(120/16) and 0 <= row['avg_y']<= 3*(80/12):
        zone = 51
    elif 4*(120/16) <= row['avg_x']<= 5*(120/16) and 0 <= row['avg_y']<= 4*(80/12):
        zone = 52
    elif 4*(120/16) <= row['avg_x']<= 5*(120/16) and 0 <= row['avg_y']<= 5*(80/12):
        zone = 53
    elif 4*(120/16) <= row['avg_x']<= 5*(120/16) and 0 <= row['avg_y']<= 6*(80/12):
        zone = 54
    elif 4*(120/16) <= row['avg_x']<= 5*(120/16) and 0 <= row['avg_y']<= 7*(80/12):
        zone = 55
    elif 4*(120/16) <= row['avg_x']<= 5*(120/16) and 0 <= row['avg_y']<= 8*(80/12):
        zone = 56
    elif 4*(120/16) <= row['avg_x']<= 5*(120/16) and 0 <= row['avg_y']<= 9*(80/12):
        zone = 57
    elif 4*(120/16) <= row['avg_x']<= 5*(120/16) and 0 <= row['avg_y']<= 10*(80/12):
        zone = 58
    elif 4*(120/16) <= row['avg_x']<= 5*(120/16) and 0 <= row['avg_y']<= 11*(80/12):
        zone = 59
    elif 4*(120/16) <= row['avg_x']<= 5*(120/16) and 0 <= row['avg_y']<= 12*(80/12):
        zone = 60
    
    if 5*(120/16) <= row['avg_x']<= 6*(120/16) and 0 <= row['avg_y']<= (80/12):
        zone = 61
    elif 5*(120/16) <= row['avg_x']<= 6*(120/16) and 0 <= row['avg_y']<= 2*(80/12):
        zone = 62
    elif 5*(120/16) <= row['avg_x']<= 6*(120/16) and 0 <= row['avg_y']<= 3*(80/12):
        zone = 63
    elif 5*(120/16) <= row['avg_x']<= 6*(120/16) and 0 <= row['avg_y']<= 4*(80/12):
        zone = 64
    elif 5*(120/16) <= row['avg_x']<= 6*(120/16) and 0 <= row['avg_y']<= 5*(80/12):
        zone = 65
    elif 5*(120/16) <= row['avg_x']<= 6*(120/16) and 0 <= row['avg_y']<= 6*(80/12):
        zone = 66
    elif 5*(120/16) <= row['avg_x']<= 6*(120/16) and 0 <= row['avg_y']<= 7*(80/12):
        zone = 67
    elif 5*(120/16) <= row['avg_x']<= 6*(120/16) and 0 <= row['avg_y']<= 8*(80/12):
        zone = 68
    elif 5*(120/16) <= row['avg_x']<= 6*(120/16) and 0 <= row['avg_y']<= 9*(80/12):
        zone = 69
    elif 5*(120/16) <= row['avg_x']<= 6*(120/16) and 0 <= row['avg_y']<= 10*(80/12):
        zone = 70
    elif 5*(120/16) <= row['avg_x']<= 6*(120/16) and 0 <= row['avg_y']<= 11*(80/12):
        zone = 71
    elif 5*(120/16) <= row['avg_x']<= 6*(120/16) and 0 <= row['avg_y']<= 12*(80/12):
        zone = 72
    
    if 6*(120/16) <= row['avg_x']<= 7*(120/16) and 0 <= row['avg_y']<= (80/12):
        zone = 73
    elif 6*(120/16) <= row['avg_x']<= 7*(120/16) and 0 <= row['avg_y']<= 2*(80/12):
        zone = 74
    elif 6*(120/16) <= row['avg_x']<= 7*(120/16) and 0 <= row['avg_y']<= 3*(80/12):
        zone = 75
    elif 6*(120/16) <= row['avg_x']<= 7*(120/16) and 0 <= row['avg_y']<= 4*(80/12):
        zone = 76
    elif 6*(120/16) <= row['avg_x']<= 7*(120/16) and 0 <= row['avg_y']<= 5*(80/12):
        zone = 77
    elif 6*(120/16) <= row['avg_x']<= 7*(120/16) and 0 <= row['avg_y']<= 6*(80/12):
        zone = 78
    elif 6*(120/16) <= row['avg_x']<= 7*(120/16) and 0 <= row['avg_y']<= 7*(80/12):
        zone = 79
    elif 6*(120/16) <= row['avg_x']<= 7*(120/16) and 0 <= row['avg_y']<= 8*(80/12):
        zone = 80
    elif 6*(120/16) <= row['avg_x']<= 7*(120/16) and 0 <= row['avg_y']<= 9*(80/12):
        zone = 81
    elif 6*(120/16) <= row['avg_x']<= 7*(120/16) and 0 <= row['avg_y']<= 10*(80/12):
        zone = 82
    elif 6*(120/16) <= row['avg_x']<= 7*(120/16) and 0 <= row['avg_y']<= 11*(80/12):
        zone = 83
    elif 6*(120/16) <= row['avg_x']<= 7*(120/16) and 0 <= row['avg_y']<= 12*(80/12):
        zone = 84
    
    if 7*(120/16) <= row['avg_x']<= 8*(120/16) and 0 <= row['avg_y']<= (80/12):
        zone = 85
    elif 7*(120/16) <= row['avg_x']<= 8*(120/16) and 0 <= row['avg_y']<= 2*(80/12):
        zone = 86
    elif 7*(120/16) <= row['avg_x']<= 8*(120/16) and 0 <= row['avg_y']<= 3*(80/12):
        zone = 87
    elif 7*(120/16) <= row['avg_x']<= 8*(120/16) and 0 <= row['avg_y']<= 4*(80/12):
        zone = 88
    elif 7*(120/16) <= row['avg_x']<= 8*(120/16) and 0 <= row['avg_y']<= 5*(80/12):
        zone = 89
    elif 7*(120/16) <= row['avg_x']<= 8*(120/16) and 0 <= row['avg_y']<= 6*(80/12):
        zone = 90
    elif 7*(120/16) <= row['avg_x']<= 8*(120/16) and 0 <= row['avg_y']<= 7*(80/12):
        zone = 91
    elif 7*(120/16) <= row['avg_x']<= 8*(120/16) and 0 <= row['avg_y']<= 8*(80/12):
        zone = 92
    elif 7*(120/16) <= row['avg_x']<= 8*(120/16) and 0 <= row['avg_y']<= 9*(80/12):
        zone = 93
    elif 7*(120/16) <= row['avg_x']<= 8*(120/16) and 0 <= row['avg_y']<= 10*(80/12):
        zone = 94
    elif 7*(120/16) <= row['avg_x']<= 8*(120/16) and 0 <= row['avg_y']<= 11*(80/12):
        zone = 95
    elif 7*(120/16) <= row['avg_x']<= 8*(120/16) and 0 <= row['avg_y']<= 12*(80/12):
        zone = 96
    
    if 8*(120/16) <= row['avg_x']<= 9*(120/16) and 0 <= row['avg_y']<= (80/12):
        zone = 97
    elif 8*(120/16) <= row['avg_x']<= 9*(120/16) and 0 <= row['avg_y']<= 2*(80/12):
        zone = 98
    elif 8*(120/16) <= row['avg_x']<= 9*(120/16) and 0 <= row['avg_y']<= 3*(80/12):
        zone = 99
    elif 8*(120/16) <= row['avg_x']<= 9*(120/16) and 0 <= row['avg_y']<= 4*(80/12):
        zone = 100
    elif 8*(120/16) <= row['avg_x']<= 9*(120/16) and 0 <= row['avg_y']<= 5*(80/12):
        zone = 101
    elif 8*(120/16) <= row['avg_x']<= 9*(120/16) and 0 <= row['avg_y']<= 6*(80/12):
        zone = 102
    elif 8*(120/16) <= row['avg_x']<= 9*(120/16) and 0 <= row['avg_y']<= 7*(80/12):
        zone = 103
    elif 8*(120/16) <= row['avg_x']<= 9*(120/16) and 0 <= row['avg_y']<= 8*(80/12):
        zone = 104
    elif 8*(120/16) <= row['avg_x']<= 9*(120/16) and 0 <= row['avg_y']<= 9*(80/12):
        zone = 105
    elif 8*(120/16) <= row['avg_x']<= 9*(120/16) and 0 <= row['avg_y']<= 10*(80/12):
        zone = 106
    elif 8*(120/16) <= row['avg_x']<= 9*(120/16) and 0 <= row['avg_y']<= 11*(80/12):
        zone = 107
    elif 8*(120/16) <= row['avg_x']<= 9*(120/16) and 0 <= row['avg_y']<= 12*(80/12):
        zone = 108
    
    if 9*(120/16) <= row['avg_x']<= 10*(120/16) and 0 <= row['avg_y']<= (80/12):
        zone = 109
    elif 9*(120/16) <= row['avg_x']<= 10*(120/16) and 0 <= row['avg_y']<= 2*(80/12):
        zone = 110
    elif 9*(120/16) <= row['avg_x']<= 10*(120/16) and 0 <= row['avg_y']<= 3*(80/12):
        zone = 111
    elif 9*(120/16) <= row['avg_x']<= 10*(120/16) and 0 <= row['avg_y']<= 4*(80/12):
        zone = 112
    elif 9*(120/16) <= row['avg_x']<= 10*(120/16) and 0 <= row['avg_y']<= 5*(80/12):
        zone = 113
    elif 9*(120/16) <= row['avg_x']<= 10*(120/16) and 0 <= row['avg_y']<= 6*(80/12):
        zone = 114
    elif 9*(120/16) <= row['avg_x']<= 10*(120/16) and 0 <= row['avg_y']<= 7*(80/12):
        zone = 115
    elif 9*(120/16) <= row['avg_x']<= 10*(120/16) and 0 <= row['avg_y']<= 8*(80/12):
        zone = 116
    elif 9*(120/16) <= row['avg_x']<= 10*(120/16) and 0 <= row['avg_y']<= 9*(80/12):
        zone = 117
    elif 9*(120/16) <= row['avg_x']<= 10*(120/16) and 0 <= row['avg_y']<= 10*(80/12):
        zone = 118
    elif 9*(120/16) <= row['avg_x']<= 10*(120/16) and 0 <= row['avg_y']<= 11*(80/12):
        zone = 119
    elif 9*(120/16) <= row['avg_x']<= 10*(120/16) and 0 <= row['avg_y']<= 12*(80/12):
        zone = 120
    
    if 10*(120/16) <= row['avg_x']<= 11*(120/16) and 0 <= row['avg_y']<= (80/12):
        zone = 121
    elif 10*(120/16) <= row['avg_x']<= 11*(120/16) and 0 <= row['avg_y']<= 2*(80/12):
        zone = 122
    elif 10*(120/16) <= row['avg_x']<= 11*(120/16) and 0 <= row['avg_y']<= 3*(80/12):
        zone = 123
    elif 10*(120/16) <= row['avg_x']<= 11*(120/16) and 0 <= row['avg_y']<= 4*(80/12):
        zone = 124
    elif 10*(120/16) <= row['avg_x']<= 11*(120/16) and 0 <= row['avg_y']<= 5*(80/12):
        zone = 125
    elif 10*(120/16) <= row['avg_x']<= 11*(120/16) and 0 <= row['avg_y']<= 6*(80/12):
        zone = 126
    elif 10*(120/16) <= row['avg_x']<= 11*(120/16) and 0 <= row['avg_y']<= 7*(80/12):
        zone = 127
    elif 10*(120/16) <= row['avg_x']<= 11*(120/16) and 0 <= row['avg_y']<= 8*(80/12):
        zone = 128
    elif 10*(120/16) <= row['avg_x']<= 11*(120/16) and 0 <= row['avg_y']<= 9*(80/12):
        zone = 129
    elif 10*(120/16) <= row['avg_x']<= 11*(120/16) and 0 <= row['avg_y']<= 10*(80/12):
        zone = 130
    elif 10*(120/16) <= row['avg_x']<= 11*(120/16) and 0 <= row['avg_y']<= 11*(80/12):
        zone = 131
    elif 10*(120/16) <= row['avg_x']<= 11*(120/16) and 0 <= row['avg_y']<= 12*(80/12):
        zone = 132
    
    if 11*(120/16) <= row['avg_x']<= 12*(120/16) and 0 <= row['avg_y']<= (80/12):
        zone = 133
    elif 11*(120/16) <= row['avg_x']<= 12*(120/16) and 0 <= row['avg_y']<= 2*(80/12):
        zone = 134
    elif 11*(120/16) <= row['avg_x']<= 12*(120/16) and 0 <= row['avg_y']<= 3*(80/12):
        zone = 135
    elif 11*(120/16) <= row['avg_x']<= 12*(120/16) and 0 <= row['avg_y']<= 4*(80/12):
        zone = 136
    elif 11*(120/16) <= row['avg_x']<= 12*(120/16) and 0 <= row['avg_y']<= 5*(80/12):
        zone = 137
    elif 11*(120/16) <= row['avg_x']<= 12*(120/16) and 0 <= row['avg_y']<= 6*(80/12):
        zone = 138
    elif 11*(120/16) <= row['avg_x']<= 12*(120/16) and 0 <= row['avg_y']<= 7*(80/12):
        zone = 139
    elif 11*(120/16) <= row['avg_x']<= 12*(120/16) and 0 <= row['avg_y']<= 8*(80/12):
        zone = 140
    elif 11*(120/16) <= row['avg_x']<= 12*(120/16) and 0 <= row['avg_y']<= 9*(80/12):
        zone = 141
    elif 11*(120/16) <= row['avg_x']<= 12*(120/16) and 0 <= row['avg_y']<= 10*(80/12):
        zone = 142
    elif 11*(120/16) <= row['avg_x']<= 12*(120/16) and 0 <= row['avg_y']<= 11*(80/12):
        zone = 143
    elif 11*(120/16) <= row['avg_x']<= 12*(120/16) and 0 <= row['avg_y']<= 12*(80/12):
        zone = 144
    
    if 12*(120/16) <= row['avg_x']<= 13*(120/16) and 0 <= row['avg_y']<= (80/12):
        zone = 145
    elif 12*(120/16) <= row['avg_x']<= 13*(120/16) and 0 <= row['avg_y']<= 2*(80/12):
        zone = 146
    elif 12*(120/16) <= row['avg_x']<= 13*(120/16) and 0 <= row['avg_y']<= 3*(80/12):
        zone = 147
    elif 12*(120/16) <= row['avg_x']<= 13*(120/16) and 0 <= row['avg_y']<= 4*(80/12):
        zone = 148
    elif 12*(120/16) <= row['avg_x']<= 13*(120/16) and 0 <= row['avg_y']<= 5*(80/12):
        zone = 149
    elif 12*(120/16) <= row['avg_x']<= 13*(120/16) and 0 <= row['avg_y']<= 6*(80/12):
        zone = 150
    elif 12*(120/16) <= row['avg_x']<= 13*(120/16) and 0 <= row['avg_y']<= 7*(80/12):
        zone = 151
    elif 12*(120/16) <= row['avg_x']<= 13*(120/16) and 0 <= row['avg_y']<= 8*(80/12):
        zone = 152
    elif 12*(120/16) <= row['avg_x']<= 13*(120/16) and 0 <= row['avg_y']<= 9*(80/12):
        zone = 153
    elif 12*(120/16) <= row['avg_x']<= 13*(120/16) and 0 <= row['avg_y']<= 10*(80/12):
        zone = 154
    elif 12*(120/16) <= row['avg_x']<= 13*(120/16) and 0 <= row['avg_y']<= 11*(80/12):
        zone = 155
    elif 12*(120/16) <= row['avg_x']<= 13*(120/16) and 0 <= row['avg_y']<= 12*(80/12):
        zone = 156
    
    if 13*(120/16) <= row['avg_x']<= 14*(120/16) and 0 <= row['avg_y']<= (80/12):
        zone = 157
    elif 13*(120/16) <= row['avg_x']<= 14*(120/16) and 0 <= row['avg_y']<= 2*(80/12):
        zone = 158
    elif 13*(120/16) <= row['avg_x']<= 14*(120/16) and 0 <= row['avg_y']<= 3*(80/12):
        zone = 159
    elif 13*(120/16) <= row['avg_x']<= 14*(120/16) and 0 <= row['avg_y']<= 4*(80/12):
        zone = 160
    elif 13*(120/16) <= row['avg_x']<= 14*(120/16) and 0 <= row['avg_y']<= 5*(80/12):
        zone = 161
    elif 13*(120/16) <= row['avg_x']<= 14*(120/16) and 0 <= row['avg_y']<= 6*(80/12):
        zone = 162
    elif 13*(120/16) <= row['avg_x']<= 14*(120/16) and 0 <= row['avg_y']<= 7*(80/12):
        zone = 163
    elif 13*(120/16) <= row['avg_x']<= 14*(120/16) and 0 <= row['avg_y']<= 8*(80/12):
        zone = 164
    elif 13*(120/16) <= row['avg_x']<= 14*(120/16) and 0 <= row['avg_y']<= 9*(80/12):
        zone = 165
    elif 13*(120/16) <= row['avg_x']<= 14*(120/16) and 0 <= row['avg_y']<= 10*(80/12):
        zone = 166
    elif 13*(120/16) <= row['avg_x']<= 14*(120/16) and 0 <= row['avg_y']<= 11*(80/12):
        zone = 167
    elif 13*(120/16) <= row['avg_x']<= 14*(120/16) and 0 <= row['avg_y']<= 12*(80/12):
        zone = 168
    
    if 14*(120/16) <= row['avg_x']<= 15*(120/16) and 0 <= row['avg_y']<= (80/12):
        zone = 169
    elif 14*(120/16) <= row['avg_x']<= 15*(120/16) and 0 <= row['avg_y']<= 2*(80/12):
        zone = 170
    elif 14*(120/16) <= row['avg_x']<= 15*(120/16) and 0 <= row['avg_y']<= 3*(80/12):
        zone = 171
    elif 14*(120/16) <= row['avg_x']<= 15*(120/16) and 0 <= row['avg_y']<= 4*(80/12):
        zone = 172
    elif 14*(120/16) <= row['avg_x']<= 15*(120/16) and 0 <= row['avg_y']<= 5*(80/12):
        zone = 173
    elif 14*(120/16) <= row['avg_x']<= 15*(120/16) and 0 <= row['avg_y']<= 6*(80/12):
        zone = 174
    elif 14*(120/16) <= row['avg_x']<= 15*(120/16) and 0 <= row['avg_y']<= 7*(80/12):
        zone = 175
    elif 14*(120/16) <= row['avg_x']<= 15*(120/16) and 0 <= row['avg_y']<= 8*(80/12):
        zone = 176
    elif 14*(120/16) <= row['avg_x']<= 15*(120/16) and 0 <= row['avg_y']<= 9*(80/12):
        zone = 177
    elif 14*(120/16) <= row['avg_x']<= 15*(120/16) and 0 <= row['avg_y']<= 10*(80/12):
        zone = 178
    elif 14*(120/16) <= row['avg_x']<= 15*(120/16) and 0 <= row['avg_y']<= 11*(80/12):
        zone = 179
    elif 14*(120/16) <= row['avg_x']<= 15*(120/16) and 0 <= row['avg_y']<= 12*(80/12):
        zone = 180
    
    if 15*(120/16) <= row['avg_x']<= 16*(120/16) and 0 <= row['avg_y']<= (80/12):
        zone = 181
    elif 15*(120/16) <= row['avg_x']<= 16*(120/16) and 0 <= row['avg_y']<= 2*(80/12):
        zone = 182
    elif 15*(120/16) <= row['avg_x']<= 16*(120/16) and 0 <= row['avg_y']<= 3*(80/12):
        zone = 183
    elif 15*(120/16) <= row['avg_x']<= 16*(120/16) and 0 <= row['avg_y']<= 4*(80/12):
        zone = 184
    elif 15*(120/16) <= row['avg_x']<= 16*(120/16) and 0 <= row['avg_y']<= 5*(80/12):
        zone = 185
    elif 15*(120/16) <= row['avg_x']<= 16*(120/16) and 0 <= row['avg_y']<= 6*(80/12):
        zone = 186
    elif 15*(120/16) <= row['avg_x']<= 16*(120/16) and 0 <= row['avg_y']<= 7*(80/12):
        zone = 187
    elif 15*(120/16) <= row['avg_x']<= 16*(120/16) and 0 <= row['avg_y']<= 8*(80/12):
        zone = 188
    elif 15*(120/16) <= row['avg_x']<= 16*(120/16) and 0 <= row['avg_y']<= 9*(80/12):
        zone = 189
    elif 15*(120/16) <= row['avg_x']<= 16*(120/16) and 0 <= row['avg_y']<= 10*(80/12):
        zone = 190
    elif 15*(120/16) <= row['avg_x']<= 16*(120/16) and 0 <= row['avg_y']<= 11*(80/12):
        zone = 191
    elif 15*(120/16) <= row['avg_x' ]<= 16*(120/16) and 0 <= row['avg_y']<= 12*(80/12):
        zone = 192

df['zone_number'] = df.apply(zone_identification, axis=1)
df = df.drop(columns=['position', 'avg_x', 'avg_y', 'player'])

# Create a dictionary with match_id and team as keys and zone numbers as values
zones_dict = df.groupby(['match_id', 'team', 'opposition', 'xt_conceded'])['zone_number'].apply(list).to_dict()
zones_dict

specific_opposition = 'Newcastle United' 

# Filter the dictionary to only include entries for the specific opposition team
filtered_zones_dict = {(match_id, team, opposition, xt_conceded): zones 
                       for (match_id, team, opposition, xt_conceded), zones in zones_dict.items()
                       if opposition == specific_opposition}

# Show the resulting filtered dictionary
filtered_zones_dict

# Initialize the list to collect the dictionary rows
data_rows = []

# Define the columns for the zones
zone_columns = ['zone_' + str(i) for i in range(1, 193)]

# Loop over each entry in filtered_zones_dict to create the binary zone variables
for (match_id, team, opposition, xt_conceded), zones in filtered_zones_dict.items():
    # Initialize the dictionary for the current row with all zones set to 0
    row_data = {f'zone_{zone}': 0 for zone in range(1, 193)}
    
    # Set the binary variables for zones present in the list
    for zone in zones:
        if 1 <= zone <= 192:  # Ensure the zone number is within the valid range
            row_data[f'zone_{zone}'] = 1
    
    # Add the non-zone data
    row_data.update({
        'xt_conceded': xt_conceded,
    })
    
    # Append the row data to the list
    data_rows.append(row_data)

# Create the DataFrame from the list of dictionaries
ml_df = pd.DataFrame(data_rows)


# Output the prepared DataFrame
display(ml_df)

