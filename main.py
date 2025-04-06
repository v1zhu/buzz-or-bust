from flask import Flask, render_template, jsonify
import pandas as pd
import matplotlib.pyplot as plt

app = Flask(__name__, template_folder='docs')

# Load the dataset
df = pd.read_csv('new_cleaned_tracks.csv')

# Create energy histogram
plt.hist(df['energy'], bins=30, edgecolor='black', color='#1DB954')
plt.title('Distribution of Energy in Songs')
plt.xlabel('Energy')
plt.ylabel('Frequency')
plt.savefig('static/energy_plot.png')
plt.close()


# Create duration histogram
plt.hist(df['duration_ms'], bins=30, edgecolor='black', color='#1DB954')
plt.title('Distribution of Duration in Songs')
plt.xlabel('Duration (ms)')
plt.ylabel('Frequency')
plt.savefig('static/duration_plot.png')
plt.close()

# Create acousticness histogram
plt.hist(df['acousticness'], bins=30, edgecolor='black', color='#1DB954') 
plt.title('Distribution of Acousticness in Songs')
plt.xlabel('Acousticness')
plt.ylabel('Frequency')
plt.savefig('static/acousticness_plot.png')
plt.close()


@app.route('/')
def start():
    return render_template('index.html')

@app.route('/energy_page')
def energy():
    return render_template('energy_page.html')

@app.route('/duration_page')
def duration():
    return render_template('duration_page.html')

@app.route('/acousticness_page')
def acousticness():
    return render_template('acousticness_page.html')

@app.route('/starting')
def index():
    return render_template('starting.html')


@app.route('/ending')
def ending():
    return render_template('ending.html')


@app.route('/get-songs')
def get_songs():
    song1, song2 = df.sample(2).to_dict(
        orient='records'
    )  #'records' means columns as keys and elements as values from extracted row of dataframe
    print(song1, song2)
    return jsonify([song1, song2])  #list of two songs as dictionaries

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=81)
