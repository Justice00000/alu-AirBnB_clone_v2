from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Define a route
@app.route('/', strict_slashes=False)
def hello():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'

# Run the Flask application
if __name__ == '__main__':
    # Start the server
    print("Starting server...")
    app.run(host='0.0.0.0', port=5000)

    # Stop the server
    print("Stopping server...")
