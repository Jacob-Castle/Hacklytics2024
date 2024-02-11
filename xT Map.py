import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from keras.regularizers import l2
import tkinter as tk
from tkinter import ttk



### GUI Code starts here



# Define the size of the pitch image
pitch_width = 1054
pitch_height = 705

# Number of zones horizontally and vertically
zones_horizontally = 16
zones_vertically = 12

# Size of each zone
zone_width = pitch_width / zones_horizontally
zone_height = pitch_height / zones_vertically

# Placeholder for selected zones
selected_zones = []

# Team names
team_names = ['Liverpool', 'Manchester United', 'Sunderland', 'Southampton', 'Stoke City',
              'Manchester City', 'Chelsea',  'Norwich City', 'Crystal Palace', 
              'West Bromwich Albion', 'Newcastle United', 'Tottenham Hotspur',
              'Aston Villa', 'West Ham United', 'AFC Bournemouth',
              'Leicester City', 'Arsenal', 'Watford', 'Swansea City', 'Everton']

# Function to calculate the zone number based on click coordinates
def calculate_zone(x, y):
    zone_x = int(x // zone_width)
    zone_y = int(y // zone_height)
    # Adjust for column-major order labeling
    return zone_x * zones_vertically + zone_y + 1


# Function to handle pitch clicks
def on_pitch_click(event):
    # Calculate the clicked zone
    clicked_zone = calculate_zone(event.x, event.y)
    select_zone(clicked_zone)

# Function to update highlights on the pitch
def update_highlights():
    # Clear existing highlights
    pitch_canvas.delete("highlight")
    # Draw new highlights
    for zone in selected_zones:
        # Calculate the grid coordinates based on the zone number for column-major order
        zone_x = (zone - 1) // zones_vertically
        zone_y = (zone - 1) % zones_vertically
        x1 = zone_x * zone_width
        y1 = zone_y * zone_height
        x2 = x1 + zone_width
        y2 = y1 + zone_height
        # Create a rectangle on the canvas for the highlighted zone
        pitch_canvas.create_rectangle(x1, y1, x2, y2, outline="red", fill="red", stipple="gray12", tags="highlight")

    # Refresh the canvas to show the new highlights
    pitch_canvas.tag_raise("highlight")  # Ensure highlights are on top of the image
    pitch_canvas.update()


# Function to handle zone selection
def select_zone(zone_number):
    if zone_number in selected_zones:
        selected_zones.remove(zone_number)
    else:
        if len(selected_zones) < 11:  # Limit the number of selectable zones to 11
            selected_zones.append(zone_number)
    # Update the label with selected zones
    zones_selected_label.config(text="Zones selected: " + ', '.join(map(str, selected_zones)))
    # Update the canvas to show the new highlights
    update_highlights()


# Modify the reset_selection function to call update_highlights
def reset_selection():
    global selected_zones
    selected_zones = []
    zones_selected_label.config(text="Zones selected: None")
    opposition_var.set('')  # Reset the opposition dropdown
    predicted_threat_label.config(text="Predicted Expected Threat Conceded: None")  # Reset the predicted threat label
    update_highlights()  # Clear any highlights

# Function to handle prediction 
def predict_threat():
    try:
        df = pd.read_csv('data.csv')
        # Create a dictionary with match_id and team as keys and zone numbers as values
        zones_dict = df.groupby(['match_id', 'team', 'opposition', 'xt_conceded'])['zone_number'].apply(list).to_dict()

        # Retrieve the specific opposition team selected by the user from the GUI dropdown
        specific_opposition = opposition_var.get()
        
        # Filter the dictionary to only include entries for the specific opposition team
        filtered_zones_dict = {(match_id, team, opposition, xt_conceded): zones 
                            for (match_id, team, opposition, xt_conceded), zones in zones_dict.items()
                            if opposition == specific_opposition}
        
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
        

        # Separate the features and the target variable
        X = ml_df.drop(['xt_conceded'], axis=1)  # Predictor variables
        y = ml_df['xt_conceded']  # Response variable

        # Feature scaling
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)


        # Neural network architecture
        nn_model = Sequential([
            Dense(256, activation='relu', input_shape=(X_scaled.shape[1],),kernel_regularizer=l2(0.001)),
            Dense(128, activation='relu', kernel_regularizer=l2(0.001)),
            Dense(64, activation='relu', kernel_regularizer=l2(0.001)),
            Dense(1)  # Output layer for regression; no activation function
        ])

        # Compile the model
        nn_model.compile(optimizer='adam', loss='mse')

        # Train the model
        nn_model.fit(X_scaled, y, epochs=100, batch_size=32, verbose=1)  

        # Predictions
        y_pred = nn_model.predict(X_scaled).flatten()
        
        
        # Ensure that the selected_zones variable is accessed globally
        global selected_zones

        # Retrieve the active zones selected by the user
        active_zones = selected_zones  

        # Create the input vector based on the selected zones
        input_vector = np.zeros(192)  # Initialize a vector of zeros for 192 zones
        input_vector[[zone - 1 for zone in active_zones]] = 1  # Set active zones to 1, adjust for 0 indexing

        # Reshape the input vector to match the model's expected input shape
        input_vector_reshaped = input_vector.reshape(1, -1)  # Reshape for a single sample

        # Predict the expected threat
        predicted_xt_structure = nn_model.predict(input_vector_reshaped)
        predicted_xt = predicted_xt_structure[0]

        # Ensure the label is accessed in the global scope
        global predicted_threat_label

        # Update the GUI with the prediction result
        predicted_threat_label.config(text=f"Predicted Expected Threat Conceded: {predicted_xt}")
    
    except Exception as e:
        print(f"An error occurred: {e}")
        predicted_threat_label.config(text=f"An error occurred: {e}")



    

# Create the main window
window = tk.Tk()
window.title("Predicted Expected Threat App")

# Load the soccer pitch image
pitch_image = tk.PhotoImage(file="zones.png")

# Create the canvas to display the soccer pitch image
pitch_canvas = tk.Canvas(window, width=pitch_width, height=pitch_height)
pitch_canvas.create_image(0, 0, anchor=tk.NW, image=pitch_image)
pitch_canvas.grid(row=0, column=0, columnspan=2)

# Bind the click event to the canvas
pitch_canvas.bind('<Button-1>', on_pitch_click)

# Create the label to display selected zones
zones_selected_label = tk.Label(window, text="Zones selected: None")
zones_selected_label.grid(row=1, column=0, sticky="w")

# Create the opposition team selection dropdown
opposition_var = tk.StringVar(window)
opposition_dropdown = ttk.Combobox(window, textvariable=opposition_var, values=team_names)
opposition_dropdown.grid(row=1, column=1, sticky="e")

# Create the predict button
predict_button = tk.Button(window, text="Predict", command=predict_threat)
predict_button.grid(row=2, column=0, columnspan=2)

# Create the reset button
reset_button = tk.Button(window, text="Reset", command=reset_selection)
reset_button.grid(row=1, column=2, sticky="w")

# Create the label to display the predicted threat
predicted_threat_label = tk.Label(window, text="Predicted Expected Threat Conceded: None")
predicted_threat_label.grid(row=3, column=0, columnspan=2)

# Run the application
window.mainloop()


