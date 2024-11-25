from flask import Flask, request, jsonify, render_template
import main_mogonet  # Assuming this contains the cancer prediction logic

# Create Flask app
app = Flask(__name__, template_folder="templates/Final")  # Update with your folder structure

# Homepage route
@app.route("/")
def index():
    return render_template("Oncologist.html")  # Ensure 'homepage.html' exists in the templates folder

# Cancer Prediction page route
@app.route("/CancerPrediction")
def cancer_prediction():
    return render_template("CancerPrediction.html")  # Ensure this file exists in 'templates/Final'

# Process data route
@app.route("/process-data", methods=["POST"])
def process_data():
    try:
        # Retrieve form data
        patient_data = request.json  # Receiving JSON payload

        # Process data with the AI model
        result = main_mogonet.run(patient_data)  # Example function call

        # Return prediction results
        return jsonify({
            "status": "success",
            "prediction_list": result["prediction_list"],  # Example key
            "prediction": "Cancer Likely",  # Add additional keys as needed
        })
    except Exception as e:
        # Handle and return errors
        return jsonify({"status": "error", "message": str(e)}), 500

# Run the Flask application
if __name__ == "__main__":
    app.run(debug=True)  # Change debug to False in production
